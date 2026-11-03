# Módulo de Relatórios no Moodle 5.2 - Guia Completo

## Visão Geral do Sistema de Relatórios

O Moodle possui um sistema modular de relatórios que permite:
- Criar relatórios padrão (logs, atividade, conclusão)
- Criar relatórios customizados
- Desenvolver plugins de relatório personalizados
- Exportar dados em vários formatos

---

## Estrutura de Arquivos de um Plugin de Relatório

### Diretório Padrão

```
report/meurelatorio/
├── db/
│   ├── install.xml          # Schema do banco de dados
│   ├── access.php           # Permissões (capabilities)
│   ├── upgrade.php          # Scripts de upgrade
│   └── services.php         # Web services (opcional)
├── classes/
│   ├── form/
│   │   └── settings.php     # Formulário de configurações
│   ├── output/
│   │   └── table.php        # Renderizador da tabela
│   └── privacy/
│       └── provider.php     # Privacidade (LGPD/GDPR)
├── lang/
│   └── en/
│       └── report_meurelatorio.php  # Strings de idioma
├── templates/
│   └── report.mustache      # Template HTML
├── amd/
│   └── src/
│       └── report.js        # JavaScript (AMD/RequireJS)
├── pix/
│   └── icon.png             # Ícone do relatório
├── lib.php                  # Funções principais
├── index.php                # Página principal
├── view.php                 # Visualização do relatório
├── export.php               # Exportação de dados
├── settings.php             # Configurações globais
├── version.php              # Informações da versão
└── README.md                # Documentação
```

---

## Arquivo: version.php

```php
<?php
defined('MOODLE_INTERNAL') || die();

$plugin->component = 'report_meurelatorio';
$plugin->version = 2025010100;      // Versão YYYYMMDDXX
$plugin->requires = 2024041500;     // Requer Moodle 4.3+
$plugin->maturity = MATURITY_STABLE;
$plugin->release = '1.0';
$plugin->dependencies = [];          // Plugins dependentes
```

---

## Arquivo: db/access.php

```php
<?php
defined('MOODLE_INTERNAL') || die();

$capabilities = array(

    // Ver relatório no curso
    'report/meurelatorio:view' => array(
        'captype' => 'read',
        'contextlevel' => CONTEXT_COURSE,
        'archetypes' => array(
            'teacher' => CAP_ALLOW,
            'editingteacher' => CAP_ALLOW,
            'manager' => CAP_ALLOW,
        ),
    ),

    // Configurar relatório
    'report/meurelatorio:config' => array(
        'captype' => 'write',
        'contextlevel' => CONTEXT_SYSTEM,
        'archetypes' => array(
            'manager' => CAP_ALLOW,
        ),
    ),

    // Exportar dados
    'report/meurelatorio:export' => array(
        'captype' => 'read',
        'contextlevel' => CONTEXT_COURSE,
        'archetypes' => array(
            'teacher' => CAP_ALLOW,
            'editingteacher' => CAP_ALLOW,
        ),
    ),
);
```

---

## Arquivo: db/install.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<XMLDB VERSION="2.0" VERSIONSQL="2024010100" PROJECT="moodle"
       COMMENT="Tabela para relatório personalizado">

    <TABLE NAME="report_data" COMMENT="Dados do relatório">
        <FIELDS>
            <FIELD NAME="id" TYPE="int" LENGTH="10" NOTNULL="true"
                   SEQUENCE="true"/>
            <FIELD NAME="courseid" TYPE="int" LENGTH="10" NOTNULL="true"
                   DEFAULT="0"/>
            <FIELD NAME="userid" TYPE="int" LENGTH="10" NOTNULL="true"
                   DEFAULT="0"/>
            <FIELD NAME="activityname" TYPE="char" LENGTH="255"
                   NOTNULL="true" DEFAULT=""/>
            <FIELD NAME="activitytype" TYPE="char" LENGTH="50"
                   NOTNULL="true" DEFAULT=""/>
            <FIELD NAME="grade" TYPE="number" LENGTH="10"
                   NOTNULL="true" DEFAULT="0"/>
            <FIELD NAME="timemodified" TYPE="int" LENGTH="10"
                   NOTNULL="true" DEFAULT="0"/>
        </FIELDS>
        <KEYS>
            <KEY NAME="primary" TYPE="primary" FIELDS="id"/>
            <KEY NAME="courseid" TYPE="foreign" FIELDS="courseid"
                 REFTABLE="course" REFFIELDS="id"/>
            <KEY NAME="userid" TYPE="foreign" FIELDS="userid"
                 REFTABLE="user" REFFIELDS="id"/>
        </KEYS>
        <INDEXES>
            <INDEX NAME="courseid" FIELDS="courseid"/>
            <INDEX NAME="userid" FIELDS="userid"/>
        </INDEXES>
    </TABLE>

</XMLDB>
```

---

## Arquivo: lib.php (Funções Principais)

### Registrar o Relatório no Menu

```php
<?php
defined('MOODLE_INTERNAL') || die();

/**
 * Adiciona item ao menu de relatórios do curso
 */
function report_meurelatorio_extend_navigation($navigation) {
    global $CFG, $PAGE, $USER;

    if (empty($PAGE->course)) {
        return;
    }

    $course = $PAGE->course;

    // Verificar permissão
    if (!has_capability('report/meurelatorio:view',
        context_course::instance($course->id))) {
        return;
    }

    // Adicionar link ao menu
    $url = new moodle_url('/report/meurelatorio/index.php',
        array('id' => $course->id));

    $navigation->add('Meu Relatório', $url);
}
```

### Funções de Callback

```php
/**
 * Callback para adicionar colunas ao relatório de notas
 */
function report_meurelatorio_grades_report_column($courseid) {
    return array(
        ' Meu Relatório' => 'report_meurelatorio_get_grade_column',
    );
}

/**
 * Retorna dados para a coluna
 */
function report_meurelatorio_get_grade_column($courseid, $userid) {
    global $DB;

    $record = $DB->get_record('report_data',
        array('courseid' => $courseid, 'userid' => $userid));

    return $record ? $record->grade : '-';
}
```

---

## Arquivo: index.php (Página Principal)

```php
<?php
require_once(__DIR__ . '/../../config.php');
require_once($CFG->libdir . '/gradelib.php');

// Parâmetros
$courseid = required_param('id', PARAM_INT);
$course = $DB->get_record('course', array('id' => $courseid), '*', MUST_EXIST);

// Verificar permissão
require_login($course);
require_capability('report/meurelatorio:view',
    context_course::instance($course->id));

// Configurar página
$PAGE->set_url(new moodle_url('/report/meurelatorio/index.php',
    array('id' => $courseid)));
$PAGE->set_title('Meu Relatório');
$PAGE->set_heading('Meu Relatório - ' . $course->fullname);

// Configurar navegação
$navigation = $PAGE->navbar;
$navigation->add('Relatórios');
$navigation->add('Meu Relatório');

// Buscar dados
$grades = $DB->get_records_sql("
    SELECT u.id, u.firstname, u.lastname, u.email,
           gi.itemname, g.finalgrade
    FROM {user} u
    JOIN {grade_grades} g ON (u.id = g.userid)
    JOIN {grade_items} gi ON (g.itemid = gi.id)
    WHERE gi.courseid = :courseid
    ORDER BY u.lastname, u.firstname
", array('courseid' => $courseid));

// Criar tabela
$table = new html_table();
$table->head = array('Aluno', 'Email', 'Atividade', 'Nota');
$table->colclasses = array('left', 'left', 'left', 'center');
$table->attributes['class'] = 'generaltable';

foreach ($grades as $grade) {
    $table->data[] = array(
        fullname($grade),
        $grade->email,
        $grade->itemname,
        $grade->finalgrade,
    );
}

// Renderizar
echo $OUTPUT->header();
echo $OUTPUT->heading('Relatório de Notas');
echo $OUTPUT->render($table);

// Botão de exportação
$exporturl = new moodle_url('/report/meurelatorio/export.php',
    array('id' => $courseid));
echo $OUTPUT->single_button($exporturl, 'Exportar CSV');

echo $OUTPUT->footer();
```

---

## Arquivo: view.php (Visualização Detalhada)

```php
<?php
require_once(__DIR__ . '/../../config.php');

$courseid = required_param('id', PARAM_INT);
$userid = required_param('userid', PARAM_INT);

$course = $DB->get_record('course', array('id' => $courseid), '*', MUST_EXIST);
$user = $DB->get_record('user', array('id' => $userid), '*', MUST_EXIST);

require_login($course);
require_capability('report/meurelatorio:view',
    context_course::instance($courseid));

$PAGE->set_url(new moodle_url('/report/meurelatorio/view.php',
    array('id' => $courseid, 'userid' => $userid)));
$PAGE->set_title('Detalhes - ' . fullname($user));

// Buscar dados do usuário
$usergrades = $DB->get_records_sql("
    SELECT gi.itemname, g.finalgrade, g.feedback,
           g.timecreated, g.timemodified
    FROM {grade_grades} g
    JOIN {grade_items} gi ON (g.itemid = gi.id)
    WHERE gi.courseid = :courseid AND g.userid = :userid
    ORDER BY gi.sortorder
", array('courseid' => $courseid, 'userid' => $userid));

echo $OUTPUT->header();
echo $OUTPUT->heading('Detalhes de ' . fullname($user));

// Tabela de notas
$table = new html_table();
$table->head = array('Atividade', 'Nota', 'Feedback', 'Data');
$table->data = array();

foreach ($usergrades as $grade) {
    $table->data[] = array(
        $grade->itemname,
        $grade->finalgrade,
        $grade->feedback,
        userdate($grade->timemodified),
    );
}

echo $OUTPUT->render($table);
echo $OUTPUT->footer();
```

---

## Arquivo: export.php (Exportação CSV)

```php
<?php
require_once(__DIR__ . '/../../config.php');
require_once($CFG->libdir . '/csvlib.class.php');

$courseid = required_param('id', PARAM_INT);
$course = $DB->get_record('course', array('id' => $courseid), '*', MUST_EXIST);

require_login($course);
require_capability('report/meurelatorio:export',
    context_course::instance($courseid));

// Buscar dados
$grades = $DB->get_records_sql("
    SELECT u.firstname, u.lastname, u.email,
           gi.itemname, g.finalgrade
    FROM {user} u
    JOIN {grade_grades} g ON (u.id = g.userid)
    JOIN {grade_items} gi ON (g.itemid = gi.id)
    WHERE gi.courseid = :courseid
    ORDER BY u.lastname, u.firstname
", array('courseid' => $courseid));

// Criar CSV
$csv = new csv_export_writer();
$csv->set_filename('relatorio_' . $course->shortname . '.csv');

// Cabeçalho
$csv->add_data(array('Aluno', 'Email', 'Atividade', 'Nota'));

// Dados
foreach ($grades as $grade) {
    $csv->add_data(array(
        fullname($grade),
        $grade->email,
        $grade->itemname,
        $grade->finalgrade,
    ));
}

// Download
$csv->download_file();
exit;
```

---

## Arquivo: lang/en/report_meurelatorio.php

```php
<?php
defined('MOODLE_INTERNAL') || die();

$string['pluginname'] = 'Meu Relatório';
$string['pluginname_help'] = 'Um relatório personalizado para visualizar notas.';
$string['meurelatorio:view'] = 'Ver meu relatório';
$string['meurelatorio:config'] = 'Configurar meu relatório';
$string['meurelatorio:export'] = 'Exportar dados do relatório';
$string['exportcsv'] = 'Exportar CSV';
$string['noitems'] = 'Nenhum item encontrado.';
```

---

## Arquivo: settings.php (Configurações Globais)

```php
<?php
defined('MOODLE_INTERNAL') || die();

$settings->add(new admin_setting_heading(
    'report_meurelatorio',
    'Configurações do Meu Relatório',
    'Configure as opções do relatório.'
));

$settings->add(new admin_setting_configcheckbox(
    'report_meurelatorio/enableexport',
    'Habilitar exportação',
    'Permite exportar dados em CSV.',
    1
));

$settings->add(new admin_setting_configtext(
    'report_meurelatorio/maxrecords',
    'Máximo de registros',
    'Número máximo de registros exibidos.',
    1000,
    PARAM_INT
));
```

---

## JavaScript (AMD/RequireJS)

### Estrutura AMD

```
amd/
└── src/
    └── report.js
```

### Arquivo: amd/src/report.js

```javascript
define(['core/str', 'core/ajax', 'core/notification'],
    function(str, ajax, notification) {

    /**
     * Inicializa o relatório
     */
    function init() {
        console.log('Relatório inicializado');

        // Buscar dados via AJAX
        loadReportData();

        // Configurar filtros
        setupFilters();

        // Configurar exportação
        setupExport();
    }

    /**
     * Carrega dados do relatório via AJAX
     */
    function loadReportData() {
        var courseid = document.getElementById('courseid').value;

        ajax.call([{
            methodname: 'report_meurelatorio_get_data',
            args: { courseid: courseid },
            done: function(response) {
                updateTable(response.data);
            },
            fail: notification.exception
        }]);
    }

    /**
     * Atualiza a tabela com os dados
     */
    function updateTable(data) {
        var tbody = document.getElementById('report-tbody');
        tbody.innerHTML = '';

        data.forEach(function(row) {
            var tr = document.createElement('tr');
            tr.innerHTML = '<td>' + row.name + '</td>' +
                          '<td>' + row.email + '</td>' +
                          '<td>' + row.grade + '</td>';
            tbody.appendChild(tr);
        });
    }

    /**
     * Configura filtros de busca
     */
    function setupFilters() {
        var searchInput = document.getElementById('search-input');
        if (searchInput) {
            searchInput.addEventListener('keyup', function() {
                filterTable(this.value);
            });
        }
    }

    /**
     * Filtra a tabela
     */
    function filterTable(query) {
        var rows = document.querySelectorAll('#report-tbody tr');
        query = query.toLowerCase();

        rows.forEach(function(row) {
            var text = row.textContent.toLowerCase();
            row.style.display = text.includes(query) ? '' : 'none';
        });
    }

    /**
     * Configura botão de exportação
     */
    function setupExport() {
        var exportBtn = document.getElementById('export-btn');
        if (exportBtn) {
            exportBtn.addEventListener('click', function() {
                exportCSV();
            });
        }
    }

    /**
     * Exporta dados como CSV
     */
    function exportCSV() {
        var table = document.getElementById('report-table');
        var csv = [];
        var rows = table.querySelectorAll('tr');

        rows.forEach(function(row) {
            var cols = row.querySelectorAll('td, th');
            var rowData = [];
            cols.forEach(function(col) {
                rowData.push('"' + col.textContent + '"');
            });
            csv.push(rowData.join(','));
        });

        var csvFile = new Blob([csv.join('\n')], { type: 'text/csv' });
        var downloadLink = document.createElement('a');
        downloadLink.download = 'relatorio.csv';
        downloadLink.href = URL.createObjectURL(csvFile);
        downloadLink.click();
    }

    return {
        init: init
    };
});
```

---

## Template Mustache

### Arquivo: templates/report.mustache

```html
<div class="report-meurelatorio">

    <div class="report-filters">
        <input type="text" id="search-input"
               placeholder="Buscar aluno...">
        <button id="export-btn" class="btn btn-primary">
            Exportar CSV
        </button>
    </div>

    <table id="report-table" class="generaltable">
        <thead>
            <tr>
                <th>Aluno</th>
                <th>Email</th>
                <th>Atividade</th>
                <th>Nota</th>
            </tr>
        </thead>
        <tbody id="report-tbody">
            {{#rows}}
            <tr>
                <td>{{name}}</td>
                <td>{{email}}</td>
                <td>{{activity}}</td>
                <td>{{grade}}</td>
            </tr>
            {{/rows}}
        </tbody>
    </table>

</div>
```

---

## Renderizador de Tabela

### Arquivo: classes/output/table.php

```php
<?php
namespace report_meurelatorio\output;

defined('MOODLE_INTERNAL') || die();

use renderable;
use templatable;
use stdClass;

class table implements renderable, templatable {

    private $courseid;
    private $data;

    public function __construct($courseid) {
        $this->courseid = $courseid;
        $this->load_data();
    }

    private function load_data() {
        global $DB;

        $this->data = $DB->get_records_sql("
            SELECT u.id, u.firstname, u.lastname, u.email,
                   gi.itemname, g.finalgrade
            FROM {user} u
            JOIN {grade_grades} g ON (u.id = g.userid)
            JOIN {grade_items} gi ON (g.itemid = gi.id)
            WHERE gi.courseid = :courseid
            ORDER BY u.lastname, u.firstname
        ", array('courseid' => $this->courseid));
    }

    public function export_for_template($output) {
        $data = new stdClass();
        $data->rows = array();

        foreach ($this->data as $row) {
            $rowdata = new stdClass();
            $rowdata->name = fullname($row);
            $rowdata->email = $row->email;
            $rowdata->activity = $row->itemname;
            $rowdata->grade = $row->finalgrade;
            $data->rows[] = $rowdata;
        }

        return $data;
    }
}
```

---

## Web Services (API)

### Arquivo: db/services.php

```php
<?php
defined('MOODLE_INTERNAL') || die();

$functions = array(

    'report_meurelatorio_get_data' => array(
        'classname' => 'report_meurelatorio\external\get_data',
        'methodname' => 'get_data',
        'classpath' => 'report/meurelatorio/classes/external/get_data.php',
        'description' => 'Obtém dados do relatório',
        'type' => 'read',
        'ajax' => true,
        'loginrequired' => true,
    ),

);

$services = array(
    'report_meurelatorio' => array(
        'functions' => array('report_meurelatorio_get_data'),
        'restrictedusers' => 0,
        'enabled' => 1,
    ),
);
```

### Arquivo: classes/external/get_data.php

```php
<?php
namespace report_meurelatorio\external;

defined('MOODLE_INTERNAL') || die();

use external_api;
use external_function_parameters;
use external_value;
use external_single_structure;
use external_multiple_structure;

class get_data extends external_api {

    public static function execute_parameters() {
        return new external_function_parameters(array(
            'courseid' => new external_value(PARAM_INT, 'ID do curso'),
        ));
    }

    public static function execute($courseid) {
        global $DB;

        // Validação
        $params = self::validate_parameters(self::execute_parameters(),
            array('courseid' => $courseid));

        // Verificar permissão
        $context = \context_course::instance($params['courseid']);
        self::validate_context($context);
        require_capability('report/meurelatorio:view', $context);

        // Buscar dados
        $data = $DB->get_records_sql("
            SELECT u.firstname, u.lastname, u.email,
                   gi.itemname, g.finalgrade
            FROM {user} u
            JOIN {grade_grades} g ON (u.id = g.userid)
            JOIN {grade_items} gi ON (g.itemid = gi.id)
            WHERE gi.courseid = :courseid
            ORDER BY u.lastname
        ", array('courseid' => $params['courseid']));

        // Preparar retorno
        $result = array();
        foreach ($data as $row) {
            $result[] = array(
                'firstname' => $row->firstname,
                'lastname' => $row->lastname,
                'email' => $row->email,
                'itemname' => $row->itemname,
                'grade' => $row->finalgrade,
            );
        }

        return array('data' => $result);
    }

    public static function execute_returns() {
        return new external_single_structure(array(
            'data' => new external_multiple_structure(array(
                'firstname' => new external_value(PARAM_TEXT),
                'lastname' => new external_value(PARAM_TEXT),
                'email' => new external_value(PARAM_TEXT),
                'itemname' => new external_value(PARAM_TEXT),
                'grade' => new external_value(PARAM_RAW),
            )),
        ));
    }
}
```

---

## Instalação do Plugin

### Passo a Passo

1. **Copie o diretório** `report/meurelatorio/` para o Moodle
2. **Acesse:** Administração do Site > Notificações
3. **O Moodle detecta** o novo plugin
4. **Clique em** "Continuar"
5. **Siga** as instruções de instalação
6. **Configure** as permissões

### Verificação

```bash
# No terminal
php admin/cli/upgrade.php
php admin/cli/check_plugins.php
```

---

## Uso do Plugin

### Para Professores

1. Acesse o curso
2. Clique em **"Mais"**
3. Clique em **"Relatórios"**
4. Selecione **"Meu Relatório"**
5. Veja os dados
6. Clique em **"Exportar CSV"**

### Via URL Direta

```
https://seumoodle.com/report/meurelatorio/index.php?id=ID_CURSO
```

---

## Boas Práticas

1. **Permissões sempre** - Use `require_capability()` em todas as páginas
2. **Parâmetros seguros** - Use `required_param()` com tipos corretos
3. **Prevenção de SQL Injection** - Use placeholders `:param`
4. **Performance** - Use índices no banco de dados
5. **Privacidade** - Implemente a API de privacidade
6. **Documentação** - Inclua README.md com instruções
7. **Testes** - Crie testes unitários em `tests/`
