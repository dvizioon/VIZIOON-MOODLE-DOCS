# Exemplos reais deste core 4.5.8

As notas do 5.2 analisam plugins Oxygeni (`mod_oxymsteams`, `tool_oxytemppass`, `webservice_oxywebapi`, `block_oxymylib`) e o tema Ceuma. Nenhum deles está neste diretório. Os exemplos abaixo são plugins que o checkout realmente contém.

## `mod_page` — atividade mínima

Pasta `mod/page/`. Serve de molde porque quase não tem regra além de gravar HTML.

- `version.php` — componente `mod_page`
- `lib.php` — `page_add_instance`, `page_update_instance`, `page_delete_instance`, `page_supports`
- `mod_form.php` — classe `mod_page_mod_form`
- `view.php` — lê o cm, exige `mod/page:view`, dispara `mod_page\event\course_module_viewed`
- `db/install.xml` — uma tabela `{page}`
- `db/access.php` — `mod/page:view` e `mod/page:addinstance`
- `backup/moodle2/` — sem isso, `course/mod.php?duplicate` não consegue clonar a page

O nome das funções é `page_add_instance`, não `mod_page_add_instance`. O core procura o nome curto do módulo.

## `mod_forum` — atividade grande

Pasta `mod/forum/`. O mesmo contrato do `page`, mais:

- `db/services.php` — funções `mod_forum_get_forums_by_courses`, `mod_forum_get_discussion_posts`, etc. Classe legada `mod_forum_external` em `externallib.php`, com `classpath`
- `db/messages.php` — provedor de mensagem `posts`
- `classes/` — entidades, eventos, tarefas, privacidade
- `templates/` e `amd/src/` — UI Mustache + AMD
- várias tabelas no `install.xml` (`forum`, `forum_discussions`, `forum_posts`, …)

Mostra o padrão antigo de web service (classe global + `classpath`) convivendo com classes novas em `classes/`.

## `mod_quiz`

Pasta `mod/quiz/`. Além do contrato de módulo:

- subplugins de relatório em `mod/quiz/report/` (não são `report_` de site)
- settings de admin em `mod/quiz/classes/admin/` (`overdue_handling_setting`, `browser_security_setting`, …)
- banco de questões em `question/`, tipos em `question/type/`

## `block_html`

Pasta `blocks/html/`. Classe `block_html extends block_base` em `block_html.php`. `init()` define o título. `get_content()` devolve `stdClass` com `text` e `footer`. Configuração da instância em `edit_form.php`. É o bloco mais curto que ainda segue o contrato.

## `theme_boost` e `theme_classic`

Só esses dois em `theme/`.

`theme/boost/config.php` define `$THEME`: layouts, `scss` via callback, pais vazio (Boost é base). `theme/boost/lib.php` contém `theme_boost_get_main_scss_content`: lê `scss/pre`, o preset, `scss/post`. A cor da marca no admin entra como variável SCSS do preset, não como um nome inventado no child.

`theme/classic` é filho do Boost (`$THEME->parents`). Não há `theme_ceuma` nem outro child neste checkout.

Ícones de tema e de módulo: SVG em `pix/icon.svg`. O helper Mustache `{{#pix}}` resolve isso.

## `report_log`

Pasta `report/log/`. Entra no menu do curso por três callbacks em `lib.php`:

- `report_log_extend_navigation_course`
- `report_log_extend_navigation_user`
- `report_log_extend_navigation_module`

A capability típica de relatório de curso é `report/log:view`. A página principal é `index.php` com `id` do curso. O dado vem do `tool_log`, não de uma tabela própria do relatório.

## `auth_oauth2` e `auth_manual`

`auth/manual` é o login interno (usuário e senha em `{user}`). `auth/oauth2` usa os issuers de `lib/classes/oauth2` e a tela `admin/tool/oauth2`. Os dois implementam `auth.php` com classe `auth_plugin_<nome>`.

## `enrol_manual`, `enrol_self`, `enrol_cohort`

Classe `enrol_<nome>_plugin extends enrol_plugin` em `lib.php`. Manual é a matrícula feita pelo professor. Self é a automatrícula. Cohort sincroniza coorte com o curso. A UI de instâncias é `enrol/instances.php` e `enrol/editenrolment.php`, não `course/mod.php`.

## O que não documentar a partir deste checkout

IOMAD, Oxygeni, tema Ceuma e a fonte `report_activities` não estão na árvore. Qualquer comportamento deles tem de ser lido no código desses plugins, não no core 4.5.8.

## Referências

- [[4.5.8/Plugins/Criar]]
- [[4.5.8/Plugins/Tipos]]
- [[4.5.8/Estrutura/Report-Plugin]]
