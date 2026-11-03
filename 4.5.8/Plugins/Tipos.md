# Tipos de plugin no Moodle 4.5.8

A lista oficial está em `lib/components.json`, chave `plugintypes`. `\core\component` lê esse JSON mais cada `db/subplugins.json`. Não há tipo fora dessa lista neste checkout.

Frankenstyle: `<tipo>_<pasta>`. A pasta `mod/forum` é o componente `mod_forum`. A classe PHP vive em `mod/forum/classes/` com namespace `mod_forum\`.

## Tipos e pastas

| Tipo | Pasta neste checkout | Prefixo |
|------|----------------------|---------|
| `mod` | `mod/` | atividade |
| `auth` | `auth/` | autenticação |
| `enrol` | `enrol/` | matrícula |
| `block` | `blocks/` | bloco |
| `filter` | `filter/` | filtro de texto |
| `format` | `course/format/` | formato de curso |
| `qtype` | `question/type/` | tipo de questão |
| `qbehaviour` | `question/behaviour/` | comportamento de questão |
| `qformat` | `question/format/` | import/export de questão |
| `qbank` | `question/bank/` | plugins do banco de questões |
| `editor` | `lib/editor/` | editor (Tiny, Atto) |
| `theme` | `theme/` | tema |
| `local` | `local/` | plugin local (vazio aqui) |
| `tool` | `admin/tool/` | ferramenta admin |
| `report` | `report/` | relatório de site/curso |
| `coursereport` | `course/report/` | relatório antigo ligado ao curso |
| `repository` | `repository/` | repositório de arquivo |
| `portfolio` | `portfolio/` | portfólio |
| `webservice` | `webservice/` | protocolo (REST, SOAP) |
| `message` | `message/output/` | saída de mensagem |
| `plagiarism` | `plagiarism/` | plágio |
| `media` | `media/player/` | player |
| `availability` | `availability/condition/` | restrição |
| `customfield` | `customfield/field/` | campo customizado |
| `profilefield` | `user/profile/field/` | campo de perfil |
| `dataformat` | `dataformat/` | CSV, Excel, JSON, PDF, ODS |
| `calendartype` | `calendar/type/` | calendário |
| `gradeexport` | `grade/export/` | exportar notas |
| `gradeimport` | `grade/import/` | importar notas |
| `gradereport` | `grade/report/` | relatório do livro |
| `gradingform` | `grade/grading/form/` | método avançado de nota |
| `cachestore` | `cache/stores/` | backend de cache |
| `cachelock` | `cache/locks/` | lock de cache |
| `fileconverter` | `files/converter/` | conversor |
| `contenttype` | `contentbank/contenttype/` | tipo no banco de conteúdo |
| `search` | `search/engine/` | motor de busca |
| `mlbackend` | `lib/mlbackend/` | backend de analytics |
| `mnetservice` | `mnet/service/` | serviço MNet |
| `antivirus` | `lib/antivirus/` | antivírus |
| `paygw` | `payment/gateway/` | pagamento |
| `h5plib` | `h5p/h5plib/` | biblioteca H5P |
| `communication` | `communication/provider/` | comunicação |
| `aiplacement` | `ai/placement/` | onde a IA aparece |
| `aiprovider` | `ai/provider/` | provedor de IA |
| `smsgateway` | `sms/gateway/` | SMS |

`aiplacement`, `aiprovider`, `communication` e `smsgateway` já existem no 4.5. Não são exclusivos do 5.x.

## Subsistemas que não são plugin

Em `components.json` → `subsystems`. Têm `version.php` próprio e classes `\core_<nome>\`, mas não se instalam como plugin. Exemplos com pasta: `course`, `grades`, `backup`, `badges`, `cohort`, `competency`, `completion`, `reportbuilder`, `privacy`, `sms`, `xapi` (`lib/xapi`), `adminpresets` (`admin/presets`). Vários são `null` (só classes no core): `access`, `role` aponta para `admin/roles`, `hub`, `countries`.

## O que cada tipo precisa no mínimo

Todo plugin: `version.php` com `$plugin->component`, `$plugin->version`, `$plugin->requires`.

| Tipo | Arquivo que o core procura |
|------|----------------------------|
| `mod` | `lib.php` com `mod_<nome>_add_instance`, `update_instance`, `delete_instance`, `<nome>_supports`. Form `mod_form.php`. Página `view.php` |
| `block` | `block_<nome>.php` com classe `block_<nome> extends block_base` |
| `auth` | `auth.php` com classe `auth_plugin_<nome> extends auth_plugin_base` |
| `enrol` | `lib.php` com classe `enrol_<nome>_plugin extends enrol_plugin` |
| `format` | `lib.php` com a classe do formato |
| `qtype` | `questiontype.php` |
| `filter` | `filter.php` com classe que estende o filtro base |
| `theme` | `config.php` (`$THEME->parents`, sheets, layouts) |
| `tool` | `settings.php` registrando no `$ADMIN`, mais um `index.php` |
| `webservice` | protocolo: classe servidora. Funções externas de um `mod_` ou `local_` ficam no `db/services.php` daquele plugin, não exigem um plugin `webservice_` |
| `report` | `lib.php` pode implementar `report_<nome>_extend_navigation_course` |

Capacidades em `db/access.php`. Tabelas em `db/install.xml`. Upgrade em `db/upgrade.php`, função `xmldb_<componente>_upgrade`. Strings em `lang/en/<componente>.php`. Observadores em `db/events.php`. Tasks em `db/tasks.php`. Hooks em `db/hooks.php`.

## Temas deste checkout

Só `theme/boost` e `theme/classic`. Classic declara Boost como pai. Não há child de marca aqui. SCSS do Boost: `theme/boost/scss/preset/default.scss` e o pipeline em `theme/boost/lib.php` (`theme_boost_get_main_scss_content`: pre, preset, post).

## Referências

- [[4.5.8/Plugins/Criar]]
- [[4.5.8/Plugins/Forms]]
- [[4.5.8/Plugins/Settings]]
- [[4.5.8/Plugins/Exemplos]]
- [[4.5.8/Estrutura/Base]]
