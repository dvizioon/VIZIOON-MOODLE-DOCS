# Plugins `report_` no Moodle 4.5.8

Tipo declarado em `lib/components.json`: `"report": "report"`. Cada pasta em `report/<nome>/` com `version.php` é o componente `report_<nome>`.

Isto é diferente de:

| Caminho | Tipo | O que é |
|---------|------|---------|
| `report/` | `report_` | Relatório de curso ou de site |
| `grade/report/` | `gradereport_` | Relatório do livro de notas (grader, user, overview, singleview, summary) |
| `mod/quiz/report/` | subplugin do quiz | Estatísticas, respostas, notas do questionário |
| `reportbuilder/` | subsistema | Construtor. Ver [[4.5.8/ReportBuilder/Fontes]] |
| `course/report/` | `coursereport` | Neste checkout só há `lib.php`; os relatórios de curso atuais são `report_` |

Não existe `report/activities` nem a fonte “Atividades” das notas do 5.2. Aquele plugin não faz parte deste core.

## Relatórios presentes

| Pasta | Papel |
|-------|--------|
| `report/log` | Logs do curso, do usuário e do módulo. Lê o `tool_log` |
| `report/loglive` | Log ao vivo |
| `report/outline` | Relatório de atividades (outline): último acesso por atividade |
| `report/participation` | Participação |
| `report/progress` | Conclusão |
| `report/completion` | Conclusão do curso |
| `report/stats` | Estatísticas, se o subsistema estiver ligado |
| `report/competency` | Competências no curso |
| `report/insights` | Previsões do analytics |
| `report/courseoverview` | Visão de cursos no site |
| `report/configlog` | Histórico de mudança de config |
| `report/security` | Visão de segurança |
| `report/performance` | Checagens de desempenho |
| `report/status` | Status do site |
| `report/eventlist` | Catálogo de classes de evento |
| `report/backups` | Backups |
| `report/questioninstances` | Onde uma questão é usada |
| `report/infectedfiles` | Arquivos barrados pelo antivírus |
| `report/themeusage` | Uso de temas |
| `report/usersessions` | Sessões do usuário |

`report/view.php` é um encaminhador comum, não um relatório.

## Como entram no menu

O core chama, se a função existir:

```php
function report_log_extend_navigation_course($navigation, $course, $context) {
    if (!has_capability('report/log:view', $context)) {
        return;
    }
    $url = new moodle_url('/report/log/index.php', ['id' => $course->id]);
    $navigation->add(get_string('pluginname', 'report_log'), $url, navigation_node::TYPE_SETTING, null, null, new pix_icon('i/report', ''));
}
```

Assinatura real em `report/log/lib.php`: o primeiro argumento é o nó, o segundo o curso, o terceiro o contexto. Há também `extend_navigation_user` e `extend_navigation_module`.

Capability em `db/access.php`, em geral `report/<nome>:view`, contexto `CONTEXT_COURSE` para relatório de curso e `CONTEXT_SYSTEM` para relatório de site.

A página exige:

```php
require_login($course);
$context = context_course::instance($course->id);
require_capability('report/log:view', $context);
```

Exportação CSV do core usa `csv_export_writer` (`lib/csvlib.class.php`) ou um `dataformat_*` (`dataformat/csv`, `dataformat/excel`, …). Relatório novo no 4.5 deve preferir o Report Builder quando a saída é uma tabela filtrável. `report_` ainda é o lugar certo quando a tela tem fluxo próprio (log ao vivo, outline, participação).

## Settings

`settings.php` do relatório recebe `$settings` (página já criada pelo core) ou, para item de menu, usa `$ADMIN->add` numa categoria de `reports`. Ver [[4.5.8/Admin/Administracao]].

## Referências

- [[4.5.8/ReportBuilder/Fontes]]
- [[4.5.8/Plugins/Tipos]]
- [[4.5.8/Eventos/Observer]]
