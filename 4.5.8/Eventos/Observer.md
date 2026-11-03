# Eventos e hooks no 4.5.8

Há dois mecanismos. Evento (`\core\event\base`) grava log e aceita observador. Hook (`\core\hook\manager`) é PSR-14 e não passa pelo log.

O 4.5 já tem os dois. Hook não é novidade do 5.x: `lib/classes/hook/manager.php` implementa `Psr\EventDispatcher\EventDispatcherInterface` desde o código desta branch (copyright 2022, Petr Skoda).

## Evento

Base: `lib/classes/event/base.php`. Um módulo estende uma classe pronta, em geral `\core\event\course_module_viewed`.

```php
namespace mod_page\event;

class course_module_viewed extends \core\event\course_module_viewed {
    protected function init() {
        $this->data['objecttable'] = 'page';
        $this->data['crud'] = 'r';
        $this->data['edulevel'] = self::LEVEL_PARTICIPATING;
    }

    public static function get_objectid_mapping() {
        return ['db' => 'page', 'restore' => 'page'];
    }
}
```

`crud` é `c`, `r`, `u` ou `d`. `edulevel` é `LEVEL_TEACHING`, `LEVEL_PARTICIPATING` ou `LEVEL_OTHER`.

Disparo:

```php
$event = \mod_page\event\course_module_viewed::create([
    'objectid' => $page->id,
    'context' => $context,
]);
$event->add_record_snapshot('page', $page);
$event->trigger();
```

`course/mod.php` dispara `\core\event\course_module_updated::create_from_cm($cm)` em hide, show, stealth e groupmode. O delete passa por `course_delete_module()`, que dispara o evento de módulo removido.

Observador em `db/events.php` do plugin:

```php
$observers = [
    [
        'eventname' => '\core\event\course_module_updated',
        'callback'  => '\local_exemplo\observer::module_updated',
    ],
];
```

O callback é estático e recebe o objeto do evento. `priority` menor roda antes. `internal => true` marca observador do próprio componente.

Eventos de core que mais se observam, todos em `lib/classes/event/`:

| Classe | Quando |
|--------|--------|
| `\core\event\course_created` / `course_updated` / `course_viewed` / `course_deleted` | curso |
| `\core\event\course_module_created` / `updated` / `deleted` / `viewed` | atividade |
| `\core\event\user_created` / `user_updated` / `user_loggedin` / `user_loggedout` | usuário |
| `\core\event\grade_item_updated` e eventos em `lib/classes/event/grade_*` | nota |

A lista completa navegável no site é o relatório `report/eventlist` (Administração → Relatórios → Lista de eventos), se o plugin estiver habilitado. Há dezenas de classes em `lib/classes/event/`; a tabela acima não é o catálogo inteiro.

O log padrão é o `tool_log` (`admin/tool/log`). Sem um store de log ativo, `trigger()` ainda chama os observers, mas a tela de logs fica vazia.

## Hook PSR-14

`\core\hook\manager::dispatch($hook)`.

Callbacks descobertos por:

1. Atributo PHP `#[\core\attribute\label(...)]` / `hook\callback` na classe listener (o agente está em `lib/classes/hook/discovery_agent.php`).
2. `db/hooks.php` do plugin, array `$callbacks`:

```php
$callbacks = [
    [
        'hook' => \core\hook\output\before_footer_html_generation::class,
        'callback' => \local_exemplo\hook_listener::class . '::before_footer',
    ],
];
```

Hooks que já existem em `lib/classes/hook/` neste checkout: `after_config`, `di_configuration`, pasta `output/` (HTML do header e do footer), pasta `navigation/`, pasta `task/`, pasta `access/`. A tela `admin/hooks.php` lista o que foi descoberto.

Diferença prática: observer enxerga o que **já aconteceu** e entra no log. Hook deixa outro plugin alterar um objeto **enquanto** a página ou a task roda. Para “quando uma nota mudar, grave uma linha”, use evento. Para “injete HTML no rodapé”, use hook.

## Referências

- [[4.5.8/Plugins/Criar]]
- [[4.5.8/Admin/Administracao]]
