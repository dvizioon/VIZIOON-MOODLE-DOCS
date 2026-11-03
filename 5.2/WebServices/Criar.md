# Criando Web Services no Moodle 5.2

## Visão Geral

Web Services no Moodle permitem expor funções via API REST/SOAP para integrações externas. Cada web service é um plugin do tipo `webservice_`.

## Estrutura do Plugin

```
webservice/minews/
├── version.php
├── db/
│   ├── services.php      # Definição das funções e serviços
│   └── access.php        # Capacidades (opcional)
├── classes/
│   └── external/
│       └── myfunction.php  # Classe da função externa
├── lang/en/webservice_minews.php
└── settings.php          # Configurações (opcional)
```

## Passo 1: version.php

```php
<?php
defined('MOODLE_INTERNAL') || die();

$plugin->component = 'webservice_minews';
$plugin->version   = 2025062200;
$plugin->requires  = 2022041900;
$plugin->maturity  = MATURITY_STABLE;
$plugin->release   = '1.0';
```

## Passo 2: db/services.php — Definição das Funções

```php
<?php
defined('MOODLE_INTERNAL') || die();

$functions = [
    // Função 1: Obter cursos
    'webservice_minews_get_courses' => [
        'classname'   => 'webservice_minews_external',
        'methodname'  => 'get_courses',
        'classpath'   => 'webservice/minews/externallib.php',
        'description' => 'Obtém a lista de cursos do usuário',
        'type'        => 'read',
        'ajax'        => true,
        'capabilities'=> 'moodle/course:view',
    ],
    
    // Função 2: Criar registro
    'webservice_minews_create_record' => [
        'classname'   => 'webservice_minews_external',
        'methodname'  => 'create_record',
        'classpath'   => 'webservice/minews/externallib.php',
        'description' => 'Cria um novo registro',
        'type'        => 'write',
        'ajax'        => false,
        'capabilities'=> 'mod/minews:create',
    ],
    
    // Função 3: Deletar registro
    'webservice_minews_delete_record' => [
        'classname'   => 'webservice_minews_external',
        'methodname'  => 'delete_record',
        'classpath'   => 'webservice/minews/externallib.php',
        'description' => 'Deleta um registro',
        'type'        => 'write',
        'ajax'        => false,
        'capabilities'=> 'mod/minews:delete',
    ],
];

$services = [
    'Minews Service' => [
        'functions' => [
            'webservice_minews_get_courses',
            'webservice_minews_create_record',
            'webservice_minews_delete_record',
        ],
        'restrictedusers' => 0,    // 0 = todos os usuários autorizados
        'enabled' => 1,
        'requiredcapability' => '', // Capacidade requerida para usar o serviço
    ],
];
```

### Campos de $functions

| Campo | Obrigatório | Descrição |
|-------|-------------|-----------|
| `classname` | Sim | Nome da classe externa |
| `methodname` | Sim | Nome do método |
| `classpath` | Sim | Caminho para o arquivo da classe |
| `description` | Sim | Descrição da função |
| `type` | Sim | `read` ou `write` |
| `ajax` | Não | Se pode ser chamado via AJAX |
| `capabilities` | Não | Capacidades necessárias |
| `loginrequired` | Não | Se requer login (default: true) |
| `deprecated` | Não | Se está deprecado |

### Campos de $services

| Campo | Descrição |
|-------|-----------|
| `functions` | Array de funções do serviço |
| `restrictedusers` | 0 = todos, 1 = apenas usuários autorizados |
| `enabled` | 1 = habilitado |
| `requiredcapability` | Capacidade para usar o serviço |
| `restricteduserscontext` | Contexto para restrição |

## Passo 3: classes/external/ — Classe Externa

```php
<?php
namespace webservice_minews\external;

use external_api;
use external_function_parameters;
use external_value;
use external_single_structure;
use external_multiple_structure;
use invalid_parameter_exception;

defined('MOODLE_INTERNAL') || die();

require_once($CFG->libdir . '/externallib.php');

class webservice_minews_external extends external_api {

    /**
     * Parâmetros da função get_courses
     */
    public static function get_courses_parameters() {
        return new external_function_parameters([
            'userid' => new external_value(PARAM_INT, 'ID do usuário (0 = atual)', VALUE_DEFAULT, 0),
            'limit' => new external_value(PARAM_INT, 'Limite de resultados', VALUE_DEFAULT, 20),
        ]);
    }

    /**
     * Retorno da função get_courses
     */
    public static function get_courses_returns() {
        return new external_multiple_structure(
            new external_single_structure([
                'id' => new external_value(PARAM_INT, 'ID do curso'),
                'fullname' => new external_value(PARAM_TEXT, 'Nome completo'),
                'shortname' => new external_value(PARAM_TEXT, 'Nome abreviado'),
                'summary' => new external_value(PARAM_RAW, 'Descrição'),
                'startdate' => new external_value(PARAM_INT, 'Data de início'),
                'enddate' => new external_value(PARAM_INT, 'Data de término'),
                'visible' => new external_value(PARAM_BOOL, 'Visível'),
            ])
        );
    }

    /**
     * Executa get_courses
     */
    public static function get_courses($userid = 0, $limit = 20) {
        global $DB, $USER;

        // Validar parâmetros
        $params = self::validate_parameters(self::get_courses_parameters(), [
            'userid' => $userid,
            'limit' => $limit,
        ]);

        // Verificar limites
        if ($params['limit'] < 1 || $params['limit'] > 100) {
            throw new invalid_parameter_exception('Limit must be between 1 and 100');
        }

        // Determinar usuário
        $targetuser = $params['userid'] > 0 ? $params['userid'] : $USER->id;

        // Verificar se o usuário pode ver os cursos
        $context = context_system::instance();
        self::validate_context($context);

        // Buscar cursos
        $sql = "SELECT c.id, c.fullname, c.shortname, c.summary,
                       c.startdate, c.enddate, c.visible
                FROM {course} c
                JOIN {role_assignments} ra ON ra.contextid = c.id
                JOIN {role} r ON r.id = ra.roleid
                WHERE ra.userid = :userid
                AND c.visible = 1
                ORDER BY c.fullname ASC";

        $courses = $DB->get_records_sql($sql, [
            'userid' => $targetuser,
        ], 0, $params['limit']);

        // Formatar retorno
        $result = [];
        foreach ($courses as $course) {
            $result[] = [
                'id' => $course->id,
                'fullname' => $course->fullname,
                'shortname' => $course->shortname,
                'summary' => format_text($course->summary, FORMAT_HTML),
                'startdate' => $course->startdate,
                'enddate' => $course->enddate,
                'visible' => $course->visible,
            ];
        }

        return $result;
    }

    /**
     * Parâmetros da função create_record
     */
    public static function create_record_parameters() {
        return new external_function_parameters([
            'name' => new external_value(PARAM_TEXT, 'Nome do registro'),
            'description' => new external_value(PARAM_RAW, 'Descrição', VALUE_DEFAULT, ''),
            'courseid' => new external_value(PARAM_INT, 'ID do curso'),
        ]);
    }

    /**
     * Retorno da função create_record
     */
    public static function create_record_returns() {
        return new external_single_structure([
            'id' => new external_value(PARAM_INT, 'ID do registro criado'),
            'success' => new external_value(PARAM_BOOL, 'Sucesso'),
            'message' => new external_value(PARAM_TEXT, 'Mensagem'),
        ]);
    }

    /**
     * Executa create_record
     */
    public static function create_record($name, $description = '', $courseid) {
        global $DB, $USER;

        $params = self::validate_parameters(self::create_record_parameters(), [
            'name' => $name,
            'description' => $description,
            'courseid' => $courseid,
        ]);

        // Verificar capacidade
        $context = context_course::instance($params['courseid']);
        self::validate_context($context);
        require_capability('mod/minews:create', $context);

        // Criar registro
        $record = new \stdClass();
        $record->name = $params['name'];
        $record->description = $params['description'];
        $record->courseid = $params['courseid'];
        $record->userid = $USER->id;
        $record->timecreated = time();
        $record->timemodified = time();

        try {
            $id = $DB->insert_record('minews', $record);
            
            return [
                'id' => $id,
                'success' => true,
                'message' => 'Record created successfully',
            ];
        } catch (\Exception $e) {
            return [
                'id' => 0,
                'success' => false,
                'message' => 'Error creating record: ' . $e->getMessage(),
            ];
        }
    }

    /**
     * Parâmetros da função delete_record
     */
    public static function delete_record_parameters() {
        return new external_function_parameters([
            'id' => new external_value(PARAM_INT, 'ID do registro'),
        ]);
    }

    /**
     * Retorno da função delete_record
     */
    public static function delete_record_returns() {
        return new external_single_structure([
            'success' => new external_value(PARAM_BOOL, 'Sucesso'),
            'message' => new external_value(PARAM_TEXT, 'Mensagem'),
        ]);
    }

    /**
     * Executa delete_record
     */
    public static function delete_record($id) {
        global $DB;

        $params = self::validate_parameters(self::delete_record_parameters(), [
            'id' => $id,
        ]);

        // Buscar registro
        $record = $DB->get_record('minews', ['id' => $params['id']]);
        if (!$record) {
            return [
                'success' => false,
                'message' => 'Record not found',
            ];
        }

        // Verificar capacidade
        $context = context_course::instance($record->courseid);
        self::validate_context($context);
        require_capability('mod/minews:delete', $context);

        try {
            $DB->delete_records('minews', ['id' => $params['id']]);
            
            return [
                'success' => true,
                'message' => 'Record deleted successfully',
            ];
        } catch (\Exception $e) {
            return [
                'success' => false,
                'message' => 'Error deleting record: ' . $e->getMessage(),
            ];
        }
    }
}
```

## Passo 4: Habilitar Web Services

### No Admin do Moodle

1. **Administração > Serviços web**
2. Habilite **Web services**
3. Habilite **REST protocol**
4. Crie um **Token** para o usuário
5. Ative o serviço em **Serviços web > Serviços externos**

### Via CLI

```bash
# Habilitar web services
php admin/cli/cfg.php --name=enablewebservices --set=1

# Habilitar REST
php admin/cli/cfg.php --name=webserviceprotocols --set=rest
```

## Passo 5: Testando a API

### Requisição REST

```
GET https://moodle.exemplo.com.br/webservice/rest/server.php?wstoken=TOKEN&wsfunction=webservice_minews_get_courses&moodlewsrestformat=json
```

### POST com Dados

```
POST https://moodle.exemplo.com.br/webservice/rest/server.php
Content-Type: application/x-www-form-urlencoded

wstoken=TOKEN
&wsfunction=webservice_minews_create_record
&moodlewsrestformat=json
&name=Meu+Registro
&description=Descrição+do+registro
&courseid=2
```

### Resposta JSON

```json
{
    "id": 1,
    "success": true,
    "message": "Record created successfully"
}
```

## Exemplo Real: webservice_oxywebapi

### db/services.php

```php
$functions = [
    'webservice_oxywebapi_get_courses' => [
        'classname'   => 'webservice_oxywebapi_external',
        'methodname'  => 'get_courses',
        'classpath'   => 'webservice/oxywebapi/externallib.php',
        'description' => 'Get courses with cursor pagination and filters',
        'type'        => 'read',
        'ajax'        => true,
        'capabilities'=> 'moodle/course:view',
    ],
];

$services = [
    'oxyWebAPI Service' => [
        'functions' => [
            'webservice_oxywebapi_get_courses',
        ],
        'restrictedusers' => 0,
        'enabled' => 1,
    ],
];
```

### Paginação com Cursor

```php
// Em classes/external/get_courses.php
public static function execute_parameters() {
    return new external_function_parameters([
        'cursor' => new external_value(PARAM_INT, 'Cursor for pagination', VALUE_DEFAULT, 0),
        'limit' => new external_value(PARAM_INT, 'Items per page', VALUE_DEFAULT, 20),
        'search' => new external_value(PARAM_TEXT, 'Search text', VALUE_DEFAULT, ''),
    ]);
}

public static function execute($cursor = 0, $limit = 20, $search = '') {
    global $DB;

    $sql = "SELECT * FROM {course} WHERE id > :minid";
    $params = ['minid' => max(1, $cursor)];

    if (!empty($search)) {
        $sql .= " AND (fullname LIKE :search OR shortname LIKE :search2)";
        $searchparam = '%' . $DB->sql_like_escape($search) . '%';
        $params['search'] = $searchparam;
        $params['search2'] = $searchparam;
    }

    $sql .= " ORDER BY id ASC";
    $sql .= " LIMIT " . ($limit + 1);

    $courses = $DB->get_records_sql($sql, $params);
    $hasmore = count($courses) > $limit;

    if ($hasmore) {
        array_pop($courses);
    }

    return [
        'courses' => array_values($courses),
        'hasmore' => $hasmore,
        'nextcursor' => $hasmore ? end($courses)->id : 0,
    ];
}
```

## Referências

- [[Base]] — Estrutura geral
- [[5.2/WebServices/Criar]] — Criação de plugins
- [[Plugins/Exemplos]] — Exemplos reais
