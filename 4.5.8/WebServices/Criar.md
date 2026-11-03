# Web services no Moodle 4.5.8

Protocolos que existem na pasta `webservice/`: **REST** (`webservice/rest`) e **SOAP** (`webservice/soap`). Não há `webservice/restful` neste checkout. Esse protocolo é posterior.

A classe base nova é `core_external\external_api` em `lib/external/classes/external_api.php`. `lib/externallib.php` publica os aliases antigos:

```php
class_alias(\core_external\external_api::class, 'external_api');
class_alias(\core_external\external_value::class, 'external_value');
class_alias(\core_external\external_function_parameters::class, 'external_function_parameters');
```

Código novo usa `use core_external\external_api`. O alias global ainda funciona porque quase todo `externallib.php` de módulo inclui `lib/externallib.php` por consequência do bootstrap.

## Onde a função é declarada

Não é obrigatório criar um plugin `webservice_`. Qualquer componente registra funções no próprio `db/services.php`. Exemplo real do core: `mod/forum/db/services.php`.

```php
$functions = [
    'mod_forum_get_forums_by_courses' => [
        'classname' => 'mod_forum_external',
        'methodname' => 'get_forums_by_courses',
        'classpath' => 'mod/forum/externallib.php',
        'description' => 'Returns a list of forum instances in a provided set of courses.',
        'type' => 'read',
        'capabilities' => 'mod/forum:viewdiscussion',
        'services' => [MOODLE_OFFICIAL_MOBILE_SERVICE],
    ],
];
```

Essa função do fórum não marca `ajax`. Quem marca `ajax => true` entra no serviço AJAX da sessão, sem token.

Classe com namespace (o estilo atual, sem `classpath`):

```php
$functions = [
    'mod_task_get_item' => [
        'classname'   => \mod_task\external\get_item::class,
        'description' => 'Fetch one item',
        'type'        => 'read',
        'ajax'        => true,
    ],
];
```

Quando `classname` aponta para uma classe namespaced, o método chamado é `execute`. A classe implementa `execute_parameters`, `execute` e `execute_returns`. O estilo antigo (`methodname` = `get_item`) procura `get_item_parameters`, `get_item` e `get_item_returns`.

| Chave | Função |
|-------|--------|
| `classname` | Classe |
| `methodname` | Método, no estilo antigo |
| `classpath` | Arquivo, se a classe não for autoload |
| `type` | `read` ou `write` |
| `ajax` | `true` libera a função no serviço AJAX da página logada |
| `capabilities` | Capability exigida |
| `services` | Serviços em que entra sozinha, por exemplo o app mobile |

Um serviço externo (token de integração) é outro array `$services` no mesmo arquivo, ou um serviço criado na UI. Função `ajax => true` não precisa de token: o browser manda sesskey pelo `core/ajax`.

## Corpo da função

```php
namespace mod_task\external;

use core_external\external_api;
use core_external\external_function_parameters;
use core_external\external_single_structure;
use core_external\external_value;

class get_item extends external_api {
    public static function execute_parameters() {
        return new external_function_parameters([
            'id' => new external_value(PARAM_INT, 'Item id'),
        ]);
    }

    public static function execute(int $id) {
        $params = self::validate_parameters(self::execute_parameters(), ['id' => $id]);
        $context = \context_system::instance();
        self::validate_context($context);
        require_capability('mod/task:view', $context);
        return ['id' => $params['id'], 'name' => 'ok'];
    }

    public static function execute_returns() {
        return new external_single_structure([
            'id' => new external_value(PARAM_INT, 'id'),
            'name' => new external_value(PARAM_TEXT, 'name'),
        ]);
    }
}
```

`validate_context()` confirma que o usuário pode estar naquele contexto. Sem isso a função é recusada na auditoria de web service. `validate_parameters()` aplica os `PARAM_*` e rejeita chave desconhecida.

## Ligar e chamar

Na administração: servidor → web services. Habilitar web services, habilitar o protocolo REST, criar o serviço, adicionar as funções, gerar um token para um usuário.

CLI equivalente ao que o core expõe em `admin/cli/cfg.php`:

```bash
php admin/cli/cfg.php --name=enablewebservices --set=1
```

O protocolo habilitado fica na config `webserviceprotocols` (valor `rest` e/ou `soap`).

Chamada REST:

```text
GET /webservice/rest/server.php?wstoken=TOKEN&wsfunction=mod_task_get_item&moodlewsrestformat=json&id=3
```

O script é `webservice/rest/server.php`. A classe servidora é `webservice_rest_server` em `webservice/rest/locallib.php`. SOAP entra por `webservice/soap/server.php`.

Documentação gerada das funções instaladas: `admin/webservice/documentation.php` e também `webservice/wsdoc.php`.

## Referências

- [[4.5.8/Admin/Administracao]]
- [[4.5.8/Plugins/Tipos]]
