# Bibliotecas em `lib/`

`lib/` é o core. `lib/setup.php` inclui um conjunto fixo em toda requisição normal. O resto é `require_once` sob demanda ou classe em `lib/classes/` carregada pelo autoload.

## Ordem obrigatória (setup.php)

| Arquivo | Por que entra sempre |
|---------|----------------------|
| `classes/component.php` | Mapa de plugins e autoload, antes do banco |
| `setuplib.php` | Funções que as outras libs já chamam (`debugging`, constantes de memória, `NO_OUTPUT_BUFFERING`) |
| `filterlib.php` | Filtros aplicados na saída de texto |
| `ajax/ajaxlib.php` | Registro de JS (AMD e o que restou de YUI) |
| `weblib.php` | `moodle_url`, `redirect`, `required_param`, `html_writer`, `s()` |
| `outputlib.php` | `$OUTPUT`, Mustache, renderables |
| `navigationlib.php` | Árvore de navegação |
| `dmllib.php` | Fachada `$DB` |
| `datalib.php` | Funções legadas de leitura (usuário, curso, contexto) |
| `accesslib.php` | Contextos, papéis, `has_capability` |
| `deprecatedlib.php` | Funções antigas ainda chamáveis |
| `moodlelib.php` | `require_login`, `fullname`, `format_text`, `sesskey`, cron helpers |
| `enrollib.php` | API de matrícula |
| `pagelib.php` | Classe `moodle_page` (`$PAGE`) |
| `blocklib.php` | Blocos na página |
| `grouplib.php` | Grupos |
| `sessionlib.php` | Sessão e cookie |
| `editorlib.php` | Editores (Tiny é o padrão; Atto ainda existe em `lib/editor`) |
| `messagelib.php` | `message_send` |
| `modinfolib.php` | Cache `course_modinfo` (lista de atividades do curso) |

`ABORT_AFTER_CONFIG` corta antes dessa lista e só carrega `configonlylib.php`.

## Bibliotecas sob demanda

Incluídas pelo script que precisa delas, não pelo bootstrap.

| Arquivo | Uso |
|---------|-----|
| `adminlib.php` | Árvore `$ADMIN`, settings, `admin_get_root()` |
| `upgradelib.php` | Install e upgrade (`upgrade_plugins`, checks) |
| `formslib.php` | `moodleform` (QuickForm) |
| `form/` | Tipos de elemento e `MoodleQuickForm` |
| `gradelib.php` | Itens de nota, `grade_update` |
| `completionlib.php` | Conclusão |
| `filelib.php` | File API, curl, draft area |
| `filestorage/` | `file_storage`, stored_file |
| `uploadlib.php` | Upload legado |
| `tablelib.php` + `table/` | `flexible_table`, `table_sql` |
| `externallib.php` | Aliases `external_api`, `external_value`, … para `core_external\*` |
| `external/` | Implementação nova da API externa |
| `ddllib.php` + `ddl/` | `database_manager` (criar tabela, campo, índice) |
| `dml/` | Drivers: mysqli, pgsql, sqlsrv, oci, aurora |
| `xmldb/` | Leitor do `install.xml` |
| `questionlib.php` | Banco de questões |
| `resourcelib.php` | `resource`, `url`, `folder`, `page`, `imscp` compartilham isso |
| `grouplib.php` | Já no bootstrap |
| `cronlib.php` | Cron legado; o agendador novo está em `lib/classes/task` |
| `phpunit/` e `testing/` | Harness de teste |
| `behat/` | Acceptância |
| `clilib.php` | Scripts CLI (`cli_writeln`, parâmetros) |
| `csvlib.class.php` | `csv_export_writer` / `csv_import_reader` |
| `excellib.class.php` | Excel legado |
| `odslib.class.php` | ODS |
| `pdflib.php` | TCPDF |
| `graphlib.php` | Gráficos antigos |
| `oauthlib.php` | OAuth 1. OAuth 2 do core está em `lib/classes/oauth2` |
| `soaplib.php` | Cliente SOAP |
| `rsslib.php` | RSS |
| `searchlib.php` | Busca global |
| `plagiarismlib.php` | Gancho de plágio |
| `badgeslib.php` | Insígnias (há também `badges/lib/`) |
| `environmentlib.php` | Checagem de ambiente no upgrade |
| `installlib.php` | Passos de instalação |
| `componentlib.class.php` | Download de pacote de idioma |
| `editorlib.php` | Já no bootstrap |
| `outputrenderers.php` | `core_renderer` e renderers de curso, bloco, mensagem |
| `outputrequirementslib.php` | Fila de CSS/JS do `$PAGE` |
| `outputcomponents.php` | `html_writer`, `single_button`, `confirm` |
| `outputactions.php` | Ações de output (popup, etc.) |
| `navigationlib.php` | Já no bootstrap |
| `myprofilelib.php` | Árvore do perfil |
| `listlib.php` | Listas hierárquicas (categorias) |
| `licenselib.php` | Licenças de arquivo |
| `gdlib.php` | Resize de imagem |
| `csslib.php` | Compilação de CSS do tema |
| `jslib.php` | Helpers de JS |
| `requirejs.php` | Servir módulos AMD |
| `javascript.php` | Combo de JS legado |
| `validateurlsyntax.php` | Validação de URL |
| `xmlize.php` | XML → array |
| `wiki_to_markdown.php` | Conversor antigo |
| `xsendfilelib.php` | X-Sendfile / X-Accel-Redirect |
| `webdavlib.php` | WebDAV do repositório |
| `googleapi.php` | Cliente Google legado |
| `flickrlib.php` / `flickrclient.php` | Flickr |
| `recaptchalib_v2.php` | reCAPTCHA |
| `ldaplib.php` | LDAP |
| `mathslib.php` / `evalmath/` | Avaliador de fórmula de nota |
| `statslib.php` | Estatísticas antigas do site |
| `conditionlib.php` | Condições legadas (a API nova é `availability/`) |
| `portfoliolib.php` | Portfólio |
| `dtllib.php` | Database transfer |
| `tokeniserlib.php` | Tokenização de busca |
| `customcheckslib.php` | Checks de ambiente extras |
| `configonlylib.php` | Funções seguras antes do banco |
| `phpminimumversionlib.php` | Trava PHP 8.1 sem depender do resto do Moodle |

## `lib/classes/` — o core moderno

Autoload `\core\...`. Grupos que mais aparecem no dia a dia:

| Pasta / classe | Função |
|----------------|--------|
| `persistent.php` | Active record. Ver [[4.5.8/Classes/Persistent]] |
| `event/` | Base `\core\event\base` |
| `hook/` | PSR-14, `\core\hook\manager` |
| `task/` | Scheduled tasks e ad-hoc |
| `output/` | Mustache, renderers, requirements |
| `external/` e `lib/external` | Web service |
| `context/` | `context_system`, `context_course`, `context_module`, … |
| `plugin_manager.php` / `plugininfo/` | Install, upgrade, enable de plugin |
| `navigation/` | Nós da navbar e do menu admin |
| `reportbuilder/` | Classes base do construtor (o subsistema em si é `reportbuilder/`) |
| `oauth2/` | Issuers e clients |
| `lock/` | Locks de cron |
| `session/` | Handlers de sessão (arquivo, DB, redis) |
| `router.php` / `route/` | Roteador opcional |
| `check/` | Environment checks |
| `message/` | `\core\message\message` |
| `dml/` | SQL helpers novos |

Alias: a classe física é `\core\component` em `lib/classes/component.php`. Código antigo chama `core_component`.

## Terceiros dentro de `lib/`

Não são API Moodle. Entram via Composer ou cópia vendorizada: `adodb`, `gulp` não — aqui estão `guzzlehttp`, `symfony`, `phpmailer`, `tcpdf`, `phpspreadsheet`, `openspout`, `htmlpurifier`, `mustache`, `scssphp`, `simplepie`, `maxmind`, `lti1p3`, `webauthn`, `slim`, `nikic`, `psr`, `laravel` (alguns componentes), `jquery`, `requirejs`, `yui`, `yuilib`, `amd`. A lista oficial é `lib/thirdpartylibs.xml`. A tela admin que mostra isso é `admin/thirdpartylibs.php`.

`lib/editor/tiny` é o editor padrão. `lib/editor/atto` ainda está na árvore. `lib/mlbackend` é o tipo de plugin `mlbackend` (analytics). `lib/antivirus` é o tipo `antivirus`.

## AMD do core

| Caminho | Papel |
|---------|--------|
| `lib/amd/src/` | Fonte dos módulos `core/*` |
| `lib/amd/build/` | Bundle que o browser carrega |
| `lib/requirejs.php` | Endpoint que entrega o módulo |
| `lib/templates/` | Mustache do core (`core/...`) |

Build: `npx grunt amd` na raiz (há `Gruntfile.js`).

## Referências

- [[4.5.8/Estrutura/Base]]
- [[4.5.8/Admin/Administracao]]
- [[4.5.8/Frontend/AMD]]
