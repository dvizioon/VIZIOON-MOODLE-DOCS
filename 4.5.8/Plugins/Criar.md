# Como uma atividade entra no Moodle 4.5.8

Contrato que `course/modedit.php` e `course/modlib.php` exigem de um `mod_`. Os nomes abaixo são os que o core chama. O exemplo usa `page` como modelo vivo em `mod/page/`, não um plugin inventado de outro projeto.

## Arquivos que o core procura

```text
mod/page/
├── version.php
├── lib.php
├── mod_form.php
├── view.php
├── index.php
├── db/install.xml
├── db/access.php
├── db/upgrade.php
├── db/log.php              # legado; evento novo substitui
├── classes/event/course_module_viewed.php
├── lang/en/page.php
├── pix/icon.svg
└── backup/moodle2/         # backup e restore da atividade
```

`version.php` deste módulo declara `$plugin->component = 'mod_page'`. Sem esse arquivo o plugin não aparece em `admin/index.php`.

## `lib.php` — funções com nome fixo

Para o módulo `page` o prefixo das funções de instância é `page_`, e o de feature é `page_supports`. O core também aceita o prefixo `mod_page_` em callbacks novos. Os quatro que `modlib.php` chama ao salvar:

| Função | Quem chama | Deve devolver |
|--------|------------|----------------|
| `page_add_instance($data, $mform)` | `add_moduleinfo` | id da linha em `{page}` |
| `page_update_instance($data, $mform)` | `update_moduleinfo` | bool |
| `page_delete_instance($id)` | `course_delete_module` | bool |
| `page_supports($feature)` | vários | bool ou null |

`page_supports` responde constantes de `lib/moodlelib.php`: `FEATURE_MOD_INTRO`, `FEATURE_COMPLETION_TRACKS_VIEWS`, `FEATURE_GRADE_HAS_GRADE`, `FEATURE_BACKUP_MOODLE2`, `FEATURE_SHOW_DESCRIPTION`, `FEATURE_MOD_PURPOSE`. `FEATURE_MOD_PURPOSE` no 4.5 classifica a atividade (recurso, colaboração, avaliação, comunicação, administração).

Outros callbacks que existem e são opcionais: `page_get_coursemodule_info` (cache do nome e da descrição na página do curso), `page_cm_info_view`, `page_pluginfile`, `page_reset_userdata`, `page_refresh_events`.

`add_instance` grava a tabela do módulo. Quem grava `course_modules` e a sequência da seção é `add_moduleinfo()` em `course/modlib.php`, não o plugin.

## Formulário

`mod_page_mod_form extends moodleform_mod`. O método `definition()` chama `$this->standard_intro_elements()` e, no fim, `$this->standard_coursemodule_elements()` e `$this->add_action_buttons()`. Esses dois últimos trazem visibilidade, grupo, conclusão e restrição. Pular `standard_coursemodule_elements()` quebra o save do cm.

## Capacidades

`db/access.php`. O nome é `mod/page:view`, `mod/page:addinstance`. `addinstance` no core clona de `moodle/course:manageactivities` (`clonepermissionsfrom`) e leva `RISK_XSS` quando o módulo imprime HTML de professor.

`contextlevel` da view é `CONTEXT_MODULE`. Archetypes: `student`, `teacher`, `editingteacher`, `manager`, `guest`.

## View

`mod/page/view.php` segue o padrão:

1. `require('../../config.php')`.
2. `id` = cm id, ou `p` = instance id.
3. `get_coursemodule_from_id('page', $id, ...)`.
4. `$course = $DB->get_record('course', ...)`.
5. `require_course_login($course, true, $cm)`.
6. `require_capability('mod/page:view', $context)`.
7. Dispara `\mod_page\event\course_module_viewed`.
8. `$OUTPUT->header()` … `footer()`.

A lista de todas as pages do curso é `index.php`, exigida pela UI “atividades” quando o módulo não esconde o índice.

## Install

Copiar a pasta para `mod/page` não basta se ela é nova: abrir Administração → Notificações (`admin/index.php`) ou `php admin/cli/upgrade.php`. O core lê `version.php`, roda `install.xml`, `access.php` e grava em `config_plugins` / tabela `modules`.

Backup: sem `backup/moodle2/backup_page_activity_task.class.php` e o stepslib, duplicar em `course/mod.php?duplicate=` falha, porque duplicate é backup/restore (`moodle/backup:backuptargetimport`).

## Strings

`lang/en/page.php` (o arquivo tem o nome do módulo, não `mod_page.php`). Chaves que o core pede: `modulename`, `modulenameplural`, `pluginname`, `pluginadministration`, `page:addinstance`, `page:view`. Pacote `pt_br` fica em `lang/pt_br/page.php` dentro do plugin ou no language pack do dataroot.

## Referências

- [[4.5.8/Course/Mod]]
- [[4.5.8/DB/Schema]]
- [[4.5.8/Plugins/Exemplos]]
