# Criar Plugin Moodle 5.2 — Guia Passo a Passo

## Visão Geral

Este guia mostra como criar um módulo de atividade (`mod_`) completo, seguindo as convenções do Moodle 5.2. Usaremos como exemplo um plugin fictício chamado `mod_task`.

## Estrutura Final

```
mod/task/
├── version.php
├── lib.php
├── mod_form.php
├── view.php
├── index.php
├── db/
│   ├── install.xml
│   ├── access.php
│   └── upgrade.php
├── classes/
│   └── event/
│       └── course_module_viewed.php
├── lang/
│   ├── en/task.php
│   └── pt_br/task.php
├── templates/
│   └── view.mustache
├── pix/
│   └── icon.png
└── amd/
    └── src/
        └── example.js
```

## Passo 1: version.php

Define identificação e versão do plugin.

```php
<?php
defined('MOODLE_INTERNAL') || die();

$plugin->component = 'mod_task';
$plugin->version   = 2025062200;
$plugin->requires  = 2022041900;
$plugin->maturity  = MATURITY_STABLE;
$plugin->release   = '1.0';
```

### Campos do version.php

| Campo | Obrigatório | Descrição |
|-------|-------------|-----------|
| `component` | Sim | Nome completo: `mod_xxx`, `block_xxx`, etc. |
| `version` | Sim | Versão no formato `YYYYMMDDXX` |
| `requires` | Sim | Versão mínima do Moodle |
| `maturity` | Não | `MATURITY_ALPHA`, `MATURITY_BETA`, `MATURITY_STABLE`, `MATURITY_RC` |
| `release` | Não | String legível da versão |
| `dependencies` | Não | Array de plugins dependentes |

## Passo 2: db/install.xml — Estrutura do Banco

Define as tabelas do banco de dados usando XMLDB.

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<XMLDB PATH="mod/task/db" VERSION="20250622" COMMENT="XMLDB file for task module"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:noNamespaceSchemaLocation="../../lib/xmldb/xmldb.xsd"
>
  <TABLES>
    <TABLE NAME="task" COMMENT="Table for task module">
      <FIELDS>
        <FIELD NAME="id" TYPE="int" LENGTH="10" NOTNULL="true" SEQUENCE="true"/>
        <FIELD NAME="course" TYPE="int" LENGTH="10" NOTNULL="true" DEFAULT="0" SEQUENCE="false"/>
        <FIELD NAME="name" TYPE="char" LENGTH="255" NOTNULL="true" SEQUENCE="false"/>
        <FIELD NAME="intro" TYPE="text" NOTNULL="false" SEQUENCE="false"/>
        <FIELD NAME="introformat" TYPE="int" LENGTH="4" NOTNULL="true" DEFAULT="0" SEQUENCE="false"/>
        <FIELD NAME="timedue" TYPE="int" LENGTH="10" NOTNULL="true" DEFAULT="0" SEQUENCE="false"/>
        <FIELD NAME="timecreated" TYPE="int" LENGTH="10" NOTNULL="true" DEFAULT="0" SEQUENCE="false"/>
        <FIELD NAME="timemodified" TYPE="int" LENGTH="10" NOTNULL="true" DEFAULT="0" SEQUENCE="false"/>
      </FIELDS>
      <KEYS>
        <KEY NAME="primary" TYPE="primary" FIELDS="id"/>
      </KEYS>
      <INDEXES>
        <INDEX NAME="course" UNIQUE="false" FIELDS="course"/>
      </INDEXES>
    </TABLE>
  </TABLES>
</XMLDB>
```

### Tipos de Campo Disponíveis

| Tipo | Descrição | Uso Comum |
|------|-----------|-----------|
| `int` | Número inteiro | IDs, timestamps, flags |
| `char` | String com limite | Nomes, títulos |
| `text` | Texto longo | Descrições, conteúdo |
| `number` | Número decimal | Notas, preços |
| `binary` | Dados binários | Hashes, tokens |
| `boolean` | Verdadeiro/falso | Flags (0/1) |

### Propriedades dos Campos

- `NOTNULL="true"` — Campo obrigatório
- `SEQUENCE="true"` — Auto-incremento (apenas para `id`)
- `DEFAULT="0"` — Valor padrão
- `LENGTH="255"` — Tamanho máximo
- `PRECISION` e `SCALE` — Para number

## Passo 3: db/access.php — Capacidades

Define as permissões do plugin.

```php
<?php
defined('MOODLE_INTERNAL') || die();

$capabilities = [
    // Ver a atividade
    'mod/task:view' => [
        'captype' => 'read',
        'contextlevel' => CONTEXT_MODULE,
        'archetypes' => [
            'guest' => CAP_ALLOW,
            'user' => CAP_ALLOW,
            'student' => CAP_ALLOW,
            'editingteacher' => CAP_ALLOW,
            'manager' => CAP_ALLOW,
        ],
    ],
    // Criar instâncias da atividade
    'mod/task:addinstance' => [
        'riskbitmask' => RISK_XSS,
        'captype' => 'write',
        'contextlevel' => CONTEXT_COURSE,
        'archetypes' => [
            'editingteacher' => CAP_ALLOW,
            'manager' => CAP_ALLOW,
        ],
        'clonepermissionsfrom' => 'moodle/course:manageactivities',
    ],
    // Submeter tarefa
    'mod/task:submit' => [
        'captype' => 'write',
        'contextlevel' => CONTEXT_MODULE,
        'archetypes' => [
            'student' => CAP_ALLOW,
        ],
    ],
];
```

### Campos da Capacidade

- **captype**: `read` ou `write`
- **contextlevel**: Onde a capacidade se aplica (`CONTEXT_MODULE`, `CONTEXT_COURSE`, `CONTEXT_SYSTEM`)
- **archetypes**: Papéis que têm acesso por padrão
- **riskbitmask**: Risco associado (`RISK_XSS`, `RISK_DATALOSS`)
- **clonepermissionsfrom**: Copiar permissões de outra capacidade

## Passo 4: lib.php — Funções Hook

Implementa as funções que o Moodle chama para gerenciar o plugin.

```php
<?php
defined('MOODLE_INTERNAL') || die();

/**
 * Suporte a features do módulo.
 */
function mod_task_supports($feature) {
    switch ($feature) {
        case FEATURE_MOD_INTRO:
            return true;
        case FEATURE_COMPLETION_TRACKS_VIEWS:
            return true;
        case FEATURE_GRADE_HAS_GRADE:
            return false;
        case FEATURE_BACKUP_MOODLE2:
            return true;
        case FEATURE_SHOW_DESCRIPTION:
            return true;
        default:
            return null;
    }
}

/**
 * Adicionar nova instância.
 */
function mod_task_add_instance($data, $mform = null) {
    global $DB;

    $data->timecreated = time();
    $data->timemodified = time();
    $data->introformat = isset($data->introformat) ? $data->introformat : FORMAT_HTML;

    $id = $DB->insert_record('task', $data);

    return $id;
}

/**
 * Atualizar instância existente.
 */
function mod_task_update_instance($data, $mform = null) {
    global $DB;

    $data->id = $data->instance;
    $data->timemodified = time();
    $data->introformat = isset($data->introformat) ? $data->introformat : FORMAT_HTML;

    $DB->update_record('task', $data);

    return true;
}

/**
 * Deletar instância.
 */
function mod_task_delete_instance($id) {
    global $DB;

    if (!$DB->delete_records('task', ['id' => $id])) {
        return false;
    }

    return true;
}

/**
 * Informações para exibição no curso.
 */
function mod_task_get_coursemodule_info($coursemodule) {
    global $DB;

    $instance = $DB->get_record('task', ['id' => $coursemodule->instance],
        'id, name, intro, introformat, timedue');

    if (!$instance) {
        return null;
    }

    $info = new cached_cm_info();
    $info->name = $instance->name;

    if ($coursemodule->showdescription && $instance->intro) {
        $info->content = format_module_intro('task', $instance, $coursemodule->id, false);
    }

    return $info;
}
```

### Hooks Disponíveis para mod_

| Hook | Descrição |
|------|-----------|
| `mod_TASK_supports()` | Declara features suportadas |
| `mod_TASK_add_instance()` | Cria nova instância |
| `mod_TASK_update_instance()` | Atualiza instância |
| `mod_TASK_delete_instance()` | Remove instância |
| `mod_TASK_get_coursemodule_info()` | Dados para exibição |
| `mod_TASK_cm_info_view()` | Chamado ao exibir no curso |
| `mod_TASK_view()` | Página view.php |
| `mod_TASK_print_overview()` | Visão geral no dashboard |

## Passo 5: mod_form.php — Formulário

```php
<?php
defined('MOODLE_INTERNAL') || die();

require_once($CFG->dirroot . '/course/moodleform_mod.php');

class mod_task_mod_form extends moodleform_mod {

    public function definition() {
        global $CFG;

        $mform = $this->_form;

        // Seção Geral
        $mform->addElement('header', 'general', get_string('general', 'form'));

        // Nome da atividade (obrigatório)
        $mform->addElement('text', 'name', get_string('taskname', 'task'), ['size' => '64']);
        $mform->setType('name', PARAM_TEXT);
        $mform->addRule('name', null, 'required', null, 'client');
        $mform->addRule('name', get_string('maximumchars', '', 255), 'maxlength', 255, 'client');

        // Descrição
        $this->standard_intro_elements();

        // Data de entrega
        $mform->addElement('date_time_selector', 'timedue', get_string('timedue', 'task'), [
            'optional' => true,
        ]);

        // Seção Opções
        $mform->addElement('header', 'options', get_string('options', 'task'));

        // Checkbox
        $mform->addElement('advcheckbox', 'optionvalue', get_string('optionvalue', 'task'));
        $mform->setDefault('optionvalue', 0);

        // Elementos padrão do Moodle
        $this->standard_coursemodule_elements();
        $this->add_action_buttons();
    }

    public function definition_after_data() {
        parent::definition_after_data();
    }

    public function validation($data, $files) {
        $errors = parent::validation($data, $files);

        if (!empty($data['timedue']) && $data['timedue'] < time()) {
            $errors['timedue'] = get_string('invalidtimedue', 'task');
        }

        return $errors;
    }
}
```

### Elementos do Formulário

| Elemento | Uso |
|----------|-----|
| `text` | Campo de texto simples |
| `textarea` | Área de texto |
| `select` | Dropdown |
| `advcheckbox` | Checkbox (0/1) |
| `date_time_selector` | Seletor de data/hora |
| `editor` | Editor de texto rico |
| `filemanager` | Upload de arquivos |
| `hidden` | Campo oculto |
| `static` | Texto estático |

### Métodos do Formulário

```php
// Adicionar regras
$mform->addRule('name', null, 'required', null, 'client');
$mform->addRule('name', get_string('maximumchars', '', 255), 'maxlength', 255, 'client');

// Validação customizada
public function validation($data, $files) {
    $errors = parent::validation($data, $files);
    if ($data['campo'] < 0) {
        $errors['campo'] = 'Deve ser positivo';
    }
    return $errors;
}
```

## Passo 6: view.php — Página Principal

```php
<?php
require_once('../../config.php');
require_once($CFG->dirroot . '/mod/task/lib.php');

global $DB, $OUTPUT, $PAGE;

$id = optional_param('id', 0, PARAM_INT);

if ($id) {
    $cm = get_coursemodule_from_id('task', $id, 0, false, MUST_EXIST);
    $task = $DB->get_record('task', ['id' => $cm->instance], '*', MUST_EXIST);
} else {
    print_error('Missing required parameter');
}

$course = $DB->get_record('course', ['id' => $cm->course], '*', MUST_EXIST);

require_course_login($course, true, $cm);

$context = context_module::instance($cm->id);
require_capability('mod/task:view', $context);

// Configurar página
$PAGE->set_url('/mod/task/view.php', ['id' => $cm->id]);
$PAGE->set_title($course->shortname . ': ' . $task->name);
$PAGE->set_heading($task->name);
$PAGE->set_context($context);

// Exibir cabeçalho
echo $OUTPUT->header();

// Exibir descrição
if ($task->intro) {
    echo $OUTPUT->box(format_module_intro('task', $task, $cm->id), 'generalbox intro');
}

// Conteúdo principal
echo $OUTPUT->box('Conteúdo da atividade task');

// Rodapé
echo $OUTPUT->footer();
```

## Passo 7: index.php — Lista no Curso

```php
<?php
require_once('../../config.php');
require_once($CFG->dirroot . '/mod/task/lib.php');

$id = required_param('id', PARAM_INT);

$course = $DB->get_record('course', ['id' => $id], '*', MUST_EXIST);
require_course_login($course);

$context = context_course::instance($course->id);
require_capability('mod/task:view', $context);

// Configurar tabela
$table = new html_table();
$table->head = [
    get_string('taskname', 'task'),
    get_string('timedue', 'task'),
];
$table->align = ['left', 'center'];

// Buscar instâncias
$instances = $DB->get_records('task', ['course' => $course->id]);

foreach ($instances as $instance) {
    $cm = get_coursemodule_from_instance('task', $instance->id);
    $url = new moodle_url('/mod/task/view.php', ['id' => $cm->id]);
    $table->data[] = [
        html_writer::link($url, $instance->name),
        userdate($instance->timedue),
    ];
}

// Exibir
echo $OUTPUT->header();
echo $OUTPUT->heading(get_string('modulenameplural', 'task'));
echo html_writer::table($table);
echo $OUTPUT->footer();
```

## Passo 8: classes/event/ — Eventos

```php
<?php
namespace mod_task\event;

defined('MOODLE_INTERNAL') || die();

class course_module_viewed extends \core\event\course_module_viewed {

    protected function init() {
        $this->data['objecttable'] = 'task';
        $this->data['crud'] = 'r';
        $this->data['edulevel'] = self::LEVEL_PARTICIPATING;
    }

    public static function get_objectid_mapping() {
        return ['db' => 'task', 'restore' => 'task'];
    }
}
```

### Níveis de Educação

- `self::LEVEL_TEACHING` — Professor
- `self::LEVEL_PARTICIPATING` — Participante
- `self::LEVEL_OTHER` — Outro

## Passo 9: lang/ — Strings

### lang/en/task.php

```php
<?php
defined('MOODLE_INTERNAL') || die();

$string['modulename'] = 'Task';
$string['modulenameplural'] = 'Tasks';
$string['taskname'] = 'Task name';
$string['taskname_help'] = 'Enter the name of the task.';
$string['timedue'] = 'Due date';
$string['timedue_help'] = 'When the task is due.';
$string['options'] = 'Options';
$string['optionvalue'] = 'Enable special option';
$string['invalidtimedue'] = 'Due date cannot be in the past';
$string['task:view'] = 'View task';
$string['task:addinstance'] = 'Add a new task';
$string['task:submit'] = 'Submit task';
```

### lang/pt_br/task.php

```php
<?php
defined('MOODLE_INTERNAL') || die();

$string['modulename'] = 'Tarefa';
$string['modulenameplural'] = 'Tarefas';
$string['taskname'] = 'Nome da tarefa';
$string['taskname_help'] = 'Digite o nome da tarefa.';
$string['timedue'] = 'Data de entrega';
$string['timedue_help'] = 'Quando a tarefa deve ser entregue.';
$string['options'] = 'Opções';
$string['optionvalue'] = 'Habilitar opção especial';
$string['invalidtimedue'] = 'A data de entrega não pode estar no passado';
```

### Convenções de Nomenclatura

- `pluginname` — Nome exibido do plugin
- `modulename` — Nome do módulo
- `modulenameplural` — Nome no plural
- `pluginname:addinstance` — Capacidade
- `field_help` — Texto de ajuda
- `field_desc` — Descrição do campo

## Passo 10: templates/ — Mustache

### templates/view.mustache

```mustache
<div class="task-view">
    <div class="task-header">
        <h2>{{name}}</h2>
    </div>
    
    <div class="task-body">
        {{{intro}}}
    </div>
    
    {{#timedue}}
    <div class="task-due">
        {{#str}} timedue, task {{}}: {{#userdate}} {{timedue}}, {{#str}} strftimedate, core {{}} {{/userdate}}
    </div>
    {{/timedue}}
    
    <div class="task-actions">
        <a href="{{actionurl}}" class="btn btn-primary">
            {{#str}} submit, task {{}}
        </a>
    </div>
</div>
```

### Chamando o Template

```php
// Em view.php
$output = $PAGE->get_renderer('mod_task');
echo $output->render_from_template('mod_task/view', [
    'name' => $task->name,
    'intro' => format_text($task->intro, $task->introformat),
    'timedue' => $task->timedue,
    'actionurl' => new moodle_url('/mod/task/submit.php', ['id' => $cm->id]),
]);
```

## Passo 11: pix/ — Ícones

Coloque os ícones em `pix/`:

```
pix/
├── icon.png          # Ícone principal (24x24)
├── icon.svg          # Versão SVG
└── iconlarge.png     # Ícone grande (36x36) — opcional
```

### Usando Ícones

```php
// No template
{{#pix}} icon, mod_task {{/pix}}

// No PHP
$icon = $OUTPUT->pix_icon('icon', get_string('pluginname', 'task'), 'mod_task');
```

## Passo 12: amd/src/ — JavaScript

### amd/src/example.js

```javascript
define(['core/str', 'core/notification'], function(Str, Notification) {
    
    const init = function() {
        document.addEventListener('DOMContentLoaded', function() {
            const button = document.querySelector('#task-action-btn');
            if (button) {
                button.addEventListener('click', handleAction);
            }
        });
    };
    
    const handleAction = function(e) {
        e.preventDefault();
        Notification.alert('Atenção', 'Ação realizada com sucesso!');
    };
    
    return { init: init };
});
```

### Build do AMD

```bash
cd /path/to/moodle
node_modules/.bin/grunt amd --fix
```

### Chamando no PHP

```php
$PAGE->requires->js_call_amd('mod_task/example', 'init');
```

## Referências

- [[Base]] — Estrutura geral
- [[DB/Schema]] — Banco de dados
- [[Templates/Mustache]] — Templates
- [[Classes/Persistent]] — Active Record
- [[Plugins/Exemplos]] — Exemplos reais
