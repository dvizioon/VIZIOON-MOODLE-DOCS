# Persistent — Active Record no Moodle 5.2

## Visão Geral

O padrão **Active Record** no Moodle é implementado pela classe `core\persistent`. Ele mapeia uma tabela do banco de dados para uma classe PHP, encapsulando operações CRUD e validação.

## Por que usar Persistent?

- Validação automática de dados
- CRUD padronizado
- Integração com o sistema de eventos
- Melhor organização do código
- Suporte a propriedades calculadas

## Estrutura Básica

```
meu_plugin/
├── classes/
│   └── persistent/
│       └── registro.php
├── db/
│   └── install.xml      # Tabela: meu_plugin_registro
```

## Definindo uma Classe Persistent

```php
<?php
namespace mod_meuplugin\persistent;

use core\persistent;

defined('MOODLE_INTERNAL') || die();

class registro extends persistent {

    /** Nome da tabela (sem prefixo) */
    protected static $table = 'meuplugin_registro';

    /** Campo primary key */
    protected static $primary = 'id';

    /**
     * Retorna os tipos das propriedades.
     */
    protected static function define_properties() {
        return [
            'name' => [
                'type' => PARAM_TEXT,
                'description' => 'Nome do registro',
            ],
            'description' => [
                'type' => PARAM_RAW,
                'default' => '',
                'description' => 'Descrição',
            ],
            'courseid' => [
                'type' => PARAM_INT,
                'default' => 0,
                'description' => 'ID do curso',
            ],
            'status' => [
                'type' => PARAM_INT,
                'default' => 0,
                'description' => 'Status: 0=pendente, 1=ativo, 2=inativo',
            ],
            'timecreated' => [
                'type' => PARAM_INT,
                'default' => 0,
            ],
            'timemodified' => [
                'type' => PARAM_INT,
                'default' => 0,
            ],
        ];
    }
}
```

## Operações CRUD

### Criar (Create)

```php
// Criar novo registro
$registro = new registro(0, (object) [
    'name' => 'Meu Registro',
    'description' => 'Uma descrição',
    'courseid' => $courseid,
    'status' => 1,
]);
$registro->save();

// Criar com dados do formulário
$registro = registro::create_from_request($formdata);
$registro->save();

// Obter ID criado
$id = $registro->get('id');
```

### Ler (Read)

```php
// Buscar por ID
$registro = registro::get_record_by_id($id);

// Buscar por condições
$registro = registro::get_record(['courseid' => $courseid, 'status' => 1]);

// Buscar múltiplos registros
$registros = registro::get_records(['courseid' => $courseid]);
$registros = registro::get_records(['status' => 1], 'name ASC');

// Verificar se existe
$existe = registro::record_exists(['name' => 'Teste']);

// Contar registros
$total = registro::count_records(['courseid' => $courseid]);
```

### Atualizar (Update)

```php
// Buscar e atualizar
$registro = registro::get_record_by_id($id);
$registro->set('name', 'Novo Nome');
$registro->set('status', 2);
$registro->update();

// Atualizar múltiplos
registro::update_records(
    ['courseid' => $courseid],
    ['status' => 2]
);
```

### Deletar (Delete)

```php
// Deletar registro
$registro = registro::get_record_by_id($id);
$registro->delete();

// Deletar por condições
registro::delete_records(['status' => 2]);
registro::delete_records(['courseid' => $courseid, 'status' => 0]);
```

## Getters e Setters

### Getters

```php
// Getters são gerados automaticamente para cada propriedade
$name = $registro->get('name');
$courseid = $registro->get('courseid');
$description = $registro->get('description');

// Getter para raw (sem formatação)
$raw = $registro->get_raw('description');

// Getter com valor padrão se não existir
$status = $registro->get('status', 0);
```

### Setters

```php
// Setter básico
$registro->set('name', 'Novo Nome');

// Setter com validação automática
$registro->set('courseid', $courseid); // Validado como PARAM_INT

// Setter múltiplo
$registro->from_record((object) [
    'name' => 'Outro Nome',
    'description' => 'Outra descrição',
]);
```

## Métodos Mágicos

```php
// Verificar se a propriedade existe
$existe = $registro->has_property('name');

// Listar todas as propriedades
$propriedades = $registro->get_properties();

// Converter para objeto
$obj = $registro->to_record();

// Converter para array
$array = $registro->to_array();
```

## Validação Customizada

```php
protected function validate_instance() {
    $errors = parent::validate_instance();

    // Validação customizada
    if (empty($this->get('name'))) {
        $errors['name'] = get_string('error_noname', 'mod_meuplugin');
    }

    if ($this->get('courseid') <= 0) {
        $errors['courseid'] = get_string('error_nocourse', 'mod_meuplugin');
    }

    // Validação condicional
    if ($this->get('status') == 1 && empty($this->get('description'))) {
        $errors['description'] = get_string('error_nodescwhenactive', 'mod_meuplugin');
    }

    return $errors;
}
```

### Validação de Propriedade Específica

```php
protected function validate_property($name, $value) {
    switch ($name) {
        case 'name':
            if (strlen($value) < 3) {
                return get_string('error_nameshort', 'mod_meuplugin');
            }
            if (strlen($value) > 255) {
                return get_string('error_namelong', 'mod_meuplugin');
            }
            break;
    }
    return parent::validate_property($name, $value);
}
```

## Hook Before/After Save

```php
/**
 * Chamado antes de salvar (INSERT ou UPDATE).
 */
protected function before_save() {
    // Atualizar timestamp
    $this->set('timemodified', time());

    // Se for novo, definir timecreated
    if ($this->get('id') == 0) {
        $this->set('timecreated', time());
    }

    // Validação adicional antes de salvar
    $this->validate_custom();
}

/**
 * Chamado depois de salvar.
 */
protected function after_save() {
    // Disparar evento customizado
    $event = \mod_meuplugin\event\registro_salvo::create([
        'objectid' => $this->get('id'),
        'context' => context_course::instance($this->get('courseid')),
    ]);
    $event->trigger();
}
```

## Exemplo Completo com Factory

```php
<?php
namespace mod_meuplugin\persistent;

use core\persistent;

defined('MOODLE_INTERNAL') || die();

class registro extends persistent {

    protected static $table = 'meuplugin_registro';
    protected static $primary = 'id';

    protected static function define_properties() {
        return [
            'name' => [
                'type' => PARAM_TEXT,
            ],
            'courseid' => [
                'type' => PARAM_INT,
                'default' => 0,
            ],
            'typeid' => [
                'type' => PARAM_INT,
                'default' => 0,
            ],
            'status' => [
                'type' => PARAM_INT,
                'default' => 0,
            ],
            'configdata' => [
                'type' => PARAM_RAW,
                'default' => '',
            ],
            'timecreated' => [
                'type' => PARAM_INT,
                'default' => 0,
            ],
            'timemodified' => [
                'type' => PARAM_INT,
                'default' => 0,
            ],
        ];
    }

    /**
     * Retorna registro ativo para um curso.
     */
    public static function get_active_for_course($courseid) {
        return static::get_records([
            'courseid' => $courseid,
            'status' => 1,
        ], 'name ASC');
    }

    /**
     * Retorna config decodificada.
     */
    public function get_config() {
        $data = $this->get('configdata');
        if (empty($data)) {
            return [];
        }
        $decoded = json_decode($data, true);
        return is_array($decoded) ? $decoded : [];
    }

    /**
     * Salva config como JSON.
     */
    public function set_config($config) {
        $this->set('configdata', json_encode($config));
    }

    /**
     * Validação customizada.
     */
    protected function validate_instance() {
        $errors = parent::validate_instance();

        if (strlen($this->get('name')) < 3) {
            $errors['name'] = get_string('error_nameshort', 'mod_meuplugin');
        }

        return $errors;
    }

    /**
     * Antes de salvar.
     */
    protected function before_save() {
        $this->set('timemodified', time());
        if ($this->get('id') == 0) {
            $this->set('timecreated', time());
        }
    }
}
```

## Uso no Controller

```php
// Em um arquivo de ação (ex: save.php)
require_once('../../config.php');
require_once($CFG->dirroot . '/mod/meuplugin/lib.php');

$id = required_param('id', PARAM_INT);
$context = context_module::instance($id);
require_capability('mod/meuplugin:edit', $context);

$registro = \mod_meuplugin\persistent\registro::get_record_by_id($id);

if (!$registro) {
    print_error('notfound');
}

// Atualizar
$registro->set('name', required_param('name', PARAM_TEXT));
$registro->set('status', required_param('status', PARAM_INT));

if ($error = $registro->validate()) {
    print_error('validationerror');
}

$registro->update();
redirect(new moodle_url('/mod/meuplugin/view.php', ['id' => $id]));
```

## Referências

- [[5.2/Plugins/Criar]] — Criação de plugins
- [[DB/Schema]] — Schema do banco
- [[Eventos/Observer]] — Sistema de eventos
