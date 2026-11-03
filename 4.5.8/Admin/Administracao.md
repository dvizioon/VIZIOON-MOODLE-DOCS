# Administração no Moodle 4.5.8

A pasta `admin/` é o subsistema `admin` (`lib/components.json`: `"admin": "admin"`). A URL pública usa `$CFG->admin`, que por padrão é a string `admin`. Os links do core são `"$CFG->wwwroot/$CFG->admin/index.php"`, não um caminho fixo `/admin/`.

A maior parte das páginas exige `moodle/site:config` no contexto do sistema. Algumas usam `moodle/site:configview` (só leitura) ou a capability do próprio `tool_`.

## Duas entradas diferentes

### `admin/index.php` — notificações e upgrade

Não é um menu. É o script de instalação e upgrade.

1. Sem `config.php`, redireciona para `../install.php`.
2. Antes de carregar o Moodle, exige PHP 8.1 (`moodle_require_minimum_php_version`) e as extensões `iconv`, `xml` e `mbstring`.
3. Define `NO_OUTPUT_BUFFERING`. Na primeira visita (sem `cache` e sem `sesskey`) define `CACHE_DISABLE_ALL` e chama `opcache_reset()`.
4. Inclui `config.php`, invalida o opcache de `version.php` e chama `core_component::get_core_subsystems()` para reconstruir o cache de componentes se a versão mudou.
5. Se o salto de versão for major e houver sessão, `redirect_if_major_upgrade_required()` encerra a sessão e volta para esta página.
6. Inclui `lib/adminlib.php` e `lib/upgradelib.php`.

Parâmetros lidos com `optional_param`: confirmação de upgrade do core, confirmação de release e ambiente, confirmação da checagem de plugins, aceite da GPL, instalação de dependência (`installdep`), cancelar install (`abortinstall`), cancelar upgrade de plugin (`abortupgrade`), instalar update (`installupdate`). `upgradekey` enviado por POST vira `sha1` na query `upgradekeyhash`.

Com `$CFG->disableupdateautodeploy`, os parâmetros de instalar plugin pela interface são ignorados.

`index.php` da raiz, se `moodle_needs_upgrading()` e o usuário tem `moodle/site:config`, redireciona para este arquivo.

### `admin/settings.php` — uma página de configuração

```php
$section = required_param('section', PARAM_SAFEDIR);
```

1. `require_login(0, false)` — sem login automático de visitante.
2. Contexto do sistema, layout `admin`, `navigation_node::require_admin_tree()`.
3. `$adminroot = admin_get_root()` e `$settingspage = $adminroot->locate($section, true)`.
4. O nó precisa ser `admin_settingpage`. Se não for e o site ainda precisa de upgrade, volta para `admin/index.php`. Caso contrário, `moodle_exception('sectionerror')`.
5. `$settingspage->check_access()`.
6. POST com `action=save-settings` e sesskey válido chama `admin_write_settings($data)`. Sem erro e com mudança, redireciona com a string `changessaved`.
7. O HTML sai do Mustache `core_admin/settings`.
8. O AMD `core_form/changechecker` observa o form `adminsettings`. Se a página declara dependência entre campos, `core/showhidesettings` os esconde.

URL típica: `/admin/settings.php?section=sitepolicies`.

## Como a árvore é montada

`admin_get_root()` em `lib/adminlib.php` cria um `admin_root` (subclasse de `admin_category`) e inclui os PHP de `admin/settings/` nesta ordem:

1. `admin/settings/top.php` — cria as categorias. Elas precisam existir antes das páginas.
2. Os outros `admin/settings/*.php`, exceto `plugins.php`.
3. `admin/settings/plugins.php` por último, porque um plugin pode inserir página em qualquer categoria.

Categorias criadas em `top.php`, nesta ordem: usuários, cursos, notas, IA, analytics, competências, insígnias, H5P, licenças, localização, idioma, mensagens, pagamentos, plugins, segurança, aparência, página inicial, servidor, MNet, relatórios, desenvolvimento. Também entram páginas soltas: notificações (`admin/index.php`), registro no moodle.org, upgradesettings (oculta), feedback do usuário e recursos avançados.

Arquivos de settings deste checkout: `ai.php`, `analytics.php`, `appearance.php`, `badges.php`, `competency.php`, `courses.php`, `development.php`, `fileredact.php`, `frontpage.php`, `grades.php`, `h5p.php`, `language.php`, `license.php`, `location.php`, `messaging.php`, `mnet.php`, `moodlenet.php`, `payment.php`, `plugins.php`, `reportbuilder.php`, `security.php`, `server.php`, `subsystems.php`, `top.php`, `userfeedback.php`, `users.php`.

Cada plugin com `settings.php` é incluído a partir de `plugins.php`. Um `tool_` faz o mesmo: o `settings.php` dele chama `$ADMIN->add(...)`.

Classes principais em `lib/adminlib.php`:

| Classe | Uso |
|--------|-----|
| `admin_category` | Pasta do menu |
| `admin_settingpage` | Formulário de configs |
| `admin_externalpage` | Link para um PHP solto |
| `admin_setting_configtext` | Texto |
| `admin_setting_configcheckbox` | Checkbox |
| `admin_setting_configselect` | Lista |
| `admin_setting_heading` | Título sem valor gravado |
| `admin_setting_configpasswordunmask` | Senha |

Padrão de uma ferramenta:

```php
$ADMIN->add('accounts', new admin_externalpage(
    'tool_exemplo',
    get_string('pluginname', 'tool_exemplo'),
    new moodle_url('/admin/tool/exemplo/index.php'),
    'tool/exemplo:use'
));
```

A categoria `accounts` é criada em `admin/settings/users.php`, não em `top.php`.

## Páginas soltas em `admin/`

| Arquivo | Função |
|---------|--------|
| `auth.php` | Ordem dos `auth_*` |
| `modules.php` | Ativar atividades |
| `blocks.php` | Blocos |
| `filters.php` | Filtros |
| `editors.php` | Editores |
| `courseformats.php` | Formatos de curso |
| `enrol.php` | Métodos de matrícula |
| `repository.php` / `repositoryinstance.php` | Repositórios |
| `qtypes.php` / `qbehaviours.php` / `qbankplugins.php` | Questões |
| `localplugins.php` | `local_*` |
| `plugins.php` | Visão geral |
| `themeselector.php` | Tema |
| `media.php` | Players |
| `dataformats.php` | Exportação |
| `antiviruses.php` | Antivírus |
| `plagiarism.php` | Plágio |
| `portfolio.php` | Portfólio |
| `message.php` | Saídas de mensagem |
| `communication.php` | Comunicação |
| `ai.php` | IA |
| `contentbank.php` | Banco de conteúdo |
| `customfields.php` | Campos customizados |
| `search.php` | Busca nas telas de admin |
| `searchareas.php` / `searchreindex.php` | Busca global |
| `hooks.php` | Callbacks de hook descobertos |
| `environment.php` | Checagem (`environment.xml`) |
| `phpinfo.php` | phpinfo |
| `purgecaches.php` | Limpar caches |
| `cron.php` | Cron via web |
| `user.php` | Ações de usuário |
| `category.php` | Categorias de curso |
| `reports.php` | Relatórios de site |
| `roles/` | Papéis, atribuição, overrides |
| `tool/` | Plugins `tool_*` |
| `cli/` | Linha de comando |
| `presets/` | Admin presets |
| `registration/` | Registro no moodle.org |
| `webservice/` | Tokens e serviços (o protocolo mora em `/webservice`) |

## CLI em `admin/cli/`

| Script | Função |
|--------|--------|
| `install.php` / `install_database.php` | Instalar |
| `upgrade.php` | Upgrade sem browser |
| `cfg.php` | Ler e gravar config |
| `cron.php` | Cron |
| `scheduled_task.php` / `adhoc_task.php` | Uma task |
| `purge_caches.php` | Caches |
| `maintenance.php` | Modo manutenção |
| `backup.php` / `restore_backup.php` | Backup |
| `uninstall_plugins.php` | Desinstalar |
| `check_database_schema.php` | Schema contra XMLDB |
| `kill_all_sessions.php` | Encerrar sessões |
| `reset_password.php` | Senha de um usuário |
| `build_theme_css.php` | CSS do tema |

## Tools do core

`admin/tool/`: `admin_presets`, `analytics`, `availabilityconditions`, `behat`, `brickfield`, `capability`, `cohortroles`, `componentlibrary`, `customlang`, `dataprivacy`, `dbtransfer`, `filetypes`, `generator`, `httpsreplace`, `installaddon`, `langimport`, `licensemanager`, `log`, `lp`, `lpimportcsv`, `lpmigrate`, `messageinbound`, `mfa`, `mobile`, `monitor`, `moodlenet`, `multilangupgrade`, `oauth2`, `phpunit`, `policy`, `profiling`, `recyclebin`, `replace`, `spamcleaner`, `task`, `templatelibrary`, `unsuproles`, `uploadcourse`, `uploaduser`, `usertours`, `xmldb`.

`tool_xmldb` edita `install.xml`. `tool_task` lista as scheduled tasks. `tool_mfa` é o segundo fator. `tool_log` é o destino padrão dos eventos.

## Referências

- [[4.5.8/Lib/Bibliotecas]]
- [[4.5.8/Plugins/Tipos]]
- [[4.5.8/WebServices/Criar]]
