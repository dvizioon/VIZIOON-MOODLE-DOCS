# `core\persistent` no Moodle 4.5.8

Arquivo: `lib/classes/persistent.php`. Namespace `core`. A classe é `abstract class persistent`.

O guia do 5.2 mostra `protected static $table`. **Neste 4.5.8 a tabela é a constante `TABLE`.** Quem copiar `$table` não grava em lugar nenhum.

## Contrato real

```php
namespace mod_task\local;

use core\persistent;

class registro extends persistent {
    const TABLE = 'task_registro';

    protected static function define_properties() {
        return [
            'name' => [
                'type' => PARAM_TEXT,
            ],
            'courseid' => [
                'type' => PARAM_INT,
            ],
            'status' => [
                'type' => PARAM_INT,
                'default' => 0,
            ],
            'description' => [
                'type' => PARAM_RAW,
                'default' => '',
                'null' => NULL_ALLOWED,
            ],
        ];
    }
}
```

`define_properties()` é o método que a classe base chama. Cada propriedade precisa de `type` com uma constante `PARAM_*`. Sem `default`, o campo é obrigatório. `null => NULL_ALLOWED` permite NULL (o padrão interno é `NULL_NOT_ALLOWED`). `choices` restringe o valor. `default` pode ser uma closure quando depende de `$CFG`.

O `id` é injetado por `properties_definition()`: `default 0`, `PARAM_INT`. Não se declara `id` de novo.

Getter e setter customizados têm de ser **protected** (`get_name()`, `set_name()`). Se forem public, `verify_protected_methods()` lança `coding_exception` quando `$CFG->debugdeveloper` está ligado. O setter customizado grava com `raw_set()` / `set_many` não substitui isso: `set()` chama `set_<propriedade>()` se existir.

## CRUD que existe de verdade

| Método | Comportamento |
|--------|----------------|
| `new registro($id)` | `$id > 0` chama `read()` e carrega a linha |
| `new registro(0, $record)` | `from_record()` sem ir ao banco |
| `set($prop, $value)` / `set_many([...])` | altera e marca como não validado |
| `get($prop)` | lê, passando pelo getter protected se houver |
| `create()` | INSERT. Antes `before_create()`, depois `after_create()` |
| `update()` | UPDATE. `before_update()`, `after_update($result)` |
| `save()` | `create()` se id é 0, senão `update()` |
| `delete()` | `before_delete()`, `after_delete($result)` |
| `validate()` / `is_valid()` / `get_errors()` | validação |
| `to_record()` / `from_record()` | `stdClass` cru, sem passar pelos getters |

Estáticos:

```php
registro::get_record(['courseid' => $courseid]);          // IGNORE_MISSING por padrão
registro::get_records(['status' => 1], 'name', 'ASC', 0, 50);
registro::count_records(['courseid' => $courseid]);
registro::record_exists($id);                             // recebe o id, não um array de filtros
registro::record_exists_select('courseid = :c', ['c' => $courseid]);
registro::get_records_select($select, $params, $sort);
```

Não existe `get_record_by_id()` nem `delete_records()` nesta classe. Para apagar em massa use `$DB` ou carregue e chame `delete()`. `record_exists(array)` do guia 5.2 não compila contra esta assinatura: o parâmetro é um id inteiro.

## Hooks de ciclo de vida

Todos `protected`, vazios na base, para o filho sobrescrever:

- `before_validate()`
- `before_create()` / `after_create()`
- `before_update()` / `after_update($result)`
- `before_delete()` / `after_delete($result)`

Não há `before_save()` único. Timestamp fica no `before_create` e no `before_update`, ou num setter.

Validação extra: sobrescrever `validate_name($value)` (por propriedade) ou `before_validate()`. Erro é `lang_string` ou string, acumulado em `get_errors()`.

## Referências

- [[4.5.8/DB/Schema]]
- [[4.5.8/Eventos/Observer]]
