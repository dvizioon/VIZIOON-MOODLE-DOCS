# Sistema de Eventos — Observer

## Visão Geral

O Moodle 5.2 usa um sistema de eventos baseado no padrão **Observer** (publicador-assinante). Eventos são disparados quando algo acontece no sistema (criação de curso, login, conclusão de atividade, etc.) e plugins podem "escutar" esses eventos para executar ações.

## Como Funciona

1. **Evento é disparado** → Uma ação ocorre no sistema
2. **Observador recebe** → O plugin que está "ouvindo" o evento
3. **Ação é executada** → O observador processa o evento

## Criando uma Classe de Evento

### Estrutura

```
meu_plugin/
├── classes/
│   └── event/
│       ├── meu_evento.php
│       └── outro_evento.php
```

### Exemplo de Evento

```php
<?php
namespace mod_meuplugin\event;

use core\event\course_module_viewed;

defined('MOODLE_INTERNAL') || die();

/**
 * Evento disparado quando alguém visualiza a atividade.
 */
class activity_viewed extends course_module_viewed {

    /**
     * Inicializa o evento.
     */
    protected function init() {
        $this->data['objecttable'] = 'meuplugin';
        $this->data['crud'] = 'r';  // r=read, c=create, u=update, d=delete
        $this->data['edulevel'] = self::LEVEL_PARTICIPATING;
    }

    /**
     * Retorna o mapeamento do objeto para restore.
     */
    public static function get_objectid_mapping() {
        return ['db' => 'meuplugin', 'restore' => 'meuplugin'];
    }

    /**
     * Retorna descrição do evento.
     */
    public function get_description() {
        return "O usuário {$this->userid} visualizou a atividade {$this->objectid}.";
    }

    /**
     * Retorna o nome legível do evento.
     */
    public static function get_name() {
        return get_string('event_activity_viewed', 'mod_meuplugin');
    }
}
```

### Propriedades do Evento

| Propriedade | Descrição |
|-------------|-----------|
| `userid` | ID do usuário que causou o evento |
| `context` | Contexto do evento |
| `objectid` | ID do objeto afetado |
| `objecttable` | Tabela do banco de dados |
| `crud` | Operação: r=read, c=create, u=update, d=delete |
| `edulevel` | Nível educacional |
| `other` | Dados extras |

### Níveis Educacionais

```php
self::LEVEL_TEACHING      // Ensino (professor criou conteúdo)
self::LEVEL_PARTICIPATING // Participação (aluno visualizou)
self::LEVEL_OTHER         // Outro (sistema, admin)
```

## Disparando Eventos

### Em lib.php

```php
function mod_meuplugin_add_instance($data, $mform = null) {
    global $DB;

    $id = $DB->insert_record('meuplugin', $data);

    // Disparar evento de criação
    $event = \mod_meuplugin\event\instance_created::create([
        'objectid' => $id,
        'context' => context_module::instance($data->coursemodule),
        'other' => [
            'name' => $data->name,
            'courseid' => $data->course,
        ],
    ]);
    $event->add_record_snapshot('meuplugin', $id);
    $event->trigger();

    return $id;
}
```

### Em view.php

```php
// Disparar evento de visualização
$event = \mod_meuplugin\event\activity_viewed::create([
    'objectid' => $meuplugin->id,
    'context' => context_module::instance($cm->id),
    'other' => [
        'name' => $meuplugin->name,
    ],
]);
$event->add_record_snapshot('meuplugin', $meuplugin->id);
$event->trigger();
```

### Métodos Úteis

```php
// Criar evento
$event = \mod_meuplugin\event\meu_evento::create([
    'objectid' => $id,
    'context' => $context,
    'other' => ['key' => 'value'],
]);

// Adicionar snapshot (para debug/histórico)
$event->add_record_snapshot('meuplugin', $id);

// Disparar
$event->trigger();

// Ou apenas logar (não dispara observers)
$event->log();
```

## Registrando Observadores

### db/events.php

```php
<?php
defined('MOODLE_INTERNAL') || die();

$observers = [
    // Observar evento de visualização
    [
        'eventname' => '\mod_meuplugin\event\activity_viewed',
        'callback'  => '\mod_meuplugin\observer\activity_viewed::handle',
        'internal'  => false,  // Se é handler interno do plugin
        'priority'  => 100,    // Prioridade (menor = primeiro)
    ],
    
    // Observar criação de curso
    [
        'eventname' => '\core\event\course_created',
        'callback'  => '\mod_meuplugin\observer\course_created::handle',
        'internal'  => false,
    ],
    
    // Observar conclusão de atividade
    [
        'eventname' => '\core\event\course_module_completed',
        'callback'  => '\mod_meuplugin\observer\activity_completed::handle',
        'internal'  => false,
    ],
];
```

### Campos do Observer

| Campo | Descrição |
|-------|-----------|
| `eventname` | Namespace completo do evento |
| `callback` | Classe e método a ser chamado |
| `internal` | Se é handler interno (true) ou de plugin (false) |
| `priority` | Ordem de execução (menor = primeiro) |
| `handler` | Se o plugin é o handler do evento |
| `includefile` | Arquivo a incluir antes de chamar |

## Implementando Observadores

### classes/observer/activity_viewed.php

```php
<?php
namespace mod_meuplugin\observer;

use core\event\course_module_viewed;

defined('MOODLE_INTERNAL') || die();

class activity_viewed {

    /**
     * Processa o evento de visualização.
     */
    public static function handle(course_module_viewed $event) {
        global $DB, $USER;

        // Verificar se é do nosso plugin
        if ($event->component !== 'mod_meuplugin') {
            return;
        }

        // Buscar dados do evento
        $instanceid = $event->objectid;
        $userid = $event->userid;
        $courseid = $event->courseid;

        // Registrar no log
        $data = [
            'userid' => $userid,
            'instanceid' => $instanceid,
            'courseid' => $courseid,
            'timeviewed' => $event->timecreated,
        ];

        $DB->insert_record('meuplugin_log', $data);

        // Enviar notificação se necessário
        self::check_notification($userid, $instanceid, $courseid);
    }

    /**
     * Verifica se deve enviar notificação.
     */
    private static function check_notification($userid, $instanceid, $courseid) {
        global $DB;

        $instance = $DB->get_record('meuplugin', ['id' => $instanceid]);
        if (!$instance) {
            return;
        }

        // Lógica de notificação...
    }
}
```

### classes/observer/course_created.php

```php
<?php
namespace mod_meuplugin\observer;

use core\event\course_created;

defined('MOODLE_INTERNAL') || die();

class course_created {

    public static function handle(course_created $event) {
        global $DB;

        $courseid = $event->objectid;

        // Criar dados iniciais para o curso
        $data = new \stdClass();
        $data->courseid = $courseid;
        $data->config = json_encode(['default' => true]);
        $data->timecreated = time();

        $DB->insert_record('meuplugin_course_config', $data);
    }
}
```

## Eventos Disponíveis no Core

### Eventos de Curso

| Evento | Descrição |
|--------|-----------|
| `\core\event\course_created` | Curso criado |
| `\core\event\course_deleted` | Curso deletado |
| `\core\event\course_updated` | Curso atualizado |
| `\core\event\course_viewed` | Curso visualizado |

### Eventos de Módulo

| Evento | Descrição |
|--------|-----------|
| `\core\event\course_module_created` | Módulo criado |
| `\core\event\course_module_updated` | Módulo atualizado |
| `\core\event\course_module_deleted` | Módulo deletado |
| `\core\event\course_module_viewed` | Módulo visualizado |
| `\core\event\course_module_completion_updated` | Conclusão atualizada |

### Eventos de Usuário

| Evento | Descrição |
|--------|-----------|
| `\core\event\user_created` | Usuário criado |
| `\core\event\user_deleted` | Usuário deletado |
| `\core\event\user_updated` | Usuário atualizado |
| `\core\event\user_loggedin` | Login realizado |
| `\core\event\user_loggedout` | Logout realizado |

### Eventos de Nota

| Evento | Descrição |
|--------|-----------|
| `\core\event\grade_created` | Nota criada |
| `\core\event\grade_updated` | Nota atualizada |
| `\core\event\grade_deleted` | Nota deletada |

## Hook System (PSR-14) no Moodle 5.x

O Moodle 5.x introduziu suporte a hooks PSR-14 para extensibilidade.

### Definindo um Hook

```php
<?php
namespace mod_meuplugin\hook;

defined('MOODLE_INTERNAL') || die();

class after_save {
    public $record;
    public $context;

    public function __construct($record, $context) {
        $this->record = $record;
        $this->context = $context;
    }
}
```

### Disparando o Hook

```php
use core\hook\manager as hook_manager;

$hook = new \mod_meuplugin\hook\after_save($record, $context);
hook_manager::dispatch($hook);
```

### Escutando o Hook

```php
<?php
namespace mod_meuplugin\hook_listener;

defined('MOODLE_INTERNAL') || die();

class after_save_listener {
    public function handle(\mod_meuplugin\hook\after_save $hook) {
        // Processar hook
    }
}
```

### Registrando o Listener

```php
// classes/hook_listener.php ou db/hooks.php
$listeners = [
    '\mod_meuplugin\hook\after_save' => [
        '\mod_meuplugin\hook_listener\after_save_listener::handle',
    ],
];
```

## Exemplo Completo: Observer com Notificação

```php
<?php
namespace mod_meuplugin\observer;

defined('MOODLE_INTERNAL') || die();

class instance_created {

    public static function handle(\mod_meuplugin\event\instance_created $event) {
        global $DB, $USER;

        // Buscar curso
        $course = $DB->get_record('course', ['id' => $event->courseid]);
        if (!$course) {
            return;
        }

        // Enviar notificação para o professor
        $teacher = $DB->get_record('user', ['id' => $event->userid]);
        if ($teacher) {
            $message = new \core\message\message();
            $message->component = 'mod_meuplugin';
            $message->name = 'instance_created';
            $message->userfrom = \core_user::get_noreply_user();
            $message->userto = $teacher;
            $message->subject = 'Nova atividade criada';
            $message->fullmessage = "Você criou a atividade: {$event->other['name']}";
            $message->fullmessageformat = FORMAT_HTML;
            $message->fullmessagehtml = "<p>Você criou a atividade: <strong>{$event->other['name']}</strong></p>";
            $message->smallmessage = 'Atividade criada';

            \core\message\api::send_message($message);
        }
    }
}
```

## Referências

- [[5.2/Plugins/Criar]] — Criação de plugins
- [[Base]] — Estrutura geral
- [[Plugins/Exemplos]] — Exemplos reais
