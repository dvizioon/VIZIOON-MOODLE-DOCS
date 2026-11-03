# Schema do Banco de Dados — XMLDB

## Visão Geral

O Moodle usa um formato XML chamado **XMLDB** para definir e gerenciar a estrutura do banco de dados. Isso permite criar, alterar e remover tabelas de forma portable entre diferentes SGBDs (MySQL, PostgreSQL, MSSQL, Oracle).

## O que é XMLDB?

XMLDB é uma camada de abstração do banco de dados do Moodle que:
- Define estrutura de tabelas via XML
- Gera SQL compatível com múltiplos SGBDs
- Gerencia migrações (upgrade) entre versões
- Fornece uma API para manipulação de dados

## Estrutura do install.xml

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<XMLDB PATH="mod/meuplugin/db" VERSION="20250622"
    COMMENT="XMLDB file for meuplugin"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:noNamespaceSchemaLocation="../../lib/xmldb/xmldb.xsd"
>
    <TABLES>
        <TABLE NAME="meuplugin" COMMENT="Main plugin table">
            <FIELDS>
                <!-- Campos aqui -->
            </FIELDS>
            <KEYS>
                <!-- Chaves aqui -->
            </KEYS>
            <INDEXES>
                <!-- Índices aqui -->
            </INDEXES>
        </TABLE>
    </TABLES>
</XMLDB>
```

## Tipos de Campo

### Tipos Numéricos

| Tipo | Tamanho | Uso |
|------|---------|-----|
| `int` | 10 | IDs, timestamps, contadores |
| `int` | 1 | Flags booleanas (0/1) |
| `number` | 10,2 | Valores decimais (notas, preços) |

### Tipos de Texto

| Tipo | Tamanho | Uso |
|------|---------|-----|
| `char` | 255 | Nomes, títulos, emails |
| `char` | 50 | Códigos curtos, chaves |
| `text` | - | Descrições, conteúdo HTML |

### Tipos Binários

| Tipo | Uso |
|------|-----|
| `binary` | Dados binários, hashes |

## Propriedades dos Campos

```xml
<FIELD
    NAME="id"
    TYPE="int"
    LENGTH="10"
    NOTNULL="true"
    SEQUENCE="true"
    COMMENT="Primary key"
/>
```

| Propriedade | Descrição | Valores |
|-------------|-----------|---------|
| `NAME` | Nome do campo | snake_case |
| `TYPE` | Tipo do dado | `int`, `char`, `text`, `number`, `binary` |
| `LENGTH` | Tamanho | Numérico |
| `NOTNULL` | Obrigatório | `true` / `false` |
| `SEQUENCE` | Auto-incremento | `true` (apenas `id`) |
| `DEFAULT` | Valor padrão | Qualquer valor |
| `SEQUENCE` | Chave primária | `true` (apenas para PK) |
| `COMMENT` | Comentário | String descritiva |

## Exemplo Completo de Tabela

```xml
<TABLE NAME="meuplugin_registro" COMMENT="Registros do plugin">
    <FIELDS>
        <FIELD NAME="id" TYPE="int" LENGTH="10" NOTNULL="true" SEQUENCE="true"/>
        <FIELD NAME="course" TYPE="int" LENGTH="10" NOTNULL="true" DEFAULT="0" SEQUENCE="false"/>
        <FIELD NAME="name" TYPE="char" LENGTH="255" NOTNULL="true" SEQUENCE="false"/>
        <FIELD NAME="intro" TYPE="text" NOTNULL="false" SEQUENCE="false"/>
        <FIELD NAME="introformat" TYPE="int" LENGTH="4" NOTNULL="true" DEFAULT="0" SEQUENCE="false"/>
        <FIELD NAME="status" TYPE="int" LENGTH="1" NOTNULL="true" DEFAULT="0" SEQUENCE="false"/>
        <FIELD NAME="score" TYPE="number" LENGTH="10" NOTNULL="true" DEFAULT="0" SEQUENCE="false"/>
        <FIELD NAME="configdata" TYPE="text" NOTNULL="false" SEQUENCE="false"/>
        <FIELD NAME="timecreated" TYPE="int" LENGTH="10" NOTNULL="true" DEFAULT="0" SEQUENCE="false"/>
        <FIELD NAME="timemodified" TYPE="int" LENGTH="10" NOTNULL="true" DEFAULT="0" SEQUENCE="false"/>
    </FIELDS>
    <KEYS>
        <KEY NAME="primary" TYPE="primary" FIELDS="id"/>
        <KEY NAME="course" TYPE="foreign" FIELDS="course" REFTABLE="course" REFFIELDS="id"/>
    </KEYS>
    <INDEXES>
        <INDEX NAME="course" UNIQUE="false" FIELDS="course"/>
        <INDEX NAME="name_idx" UNIQUE="false" FIELDS="name"/>
        <INDEX NAME="status_course" UNIQUE="false" FIELDS="status,course"/>
    </INDEXES>
</TABLE>
```

## Chaves (Keys)

### Tipos de Chave

| Tipo | Descrição |
|------|-----------|
| `primary` | Chave primária (auto-incremento) |
| `foreign` | Chave estrangeira |
| `unique` | Valores únicos |

### Chave Primária

```xml
<KEY NAME="primary" TYPE="primary" FIELDS="id"/>
```

### Chave Estrangeira

```xml
<KEY NAME="course" TYPE="foreign" FIELDS="course" REFTABLE="course" REFFIELDS="id"/>
```

> **Nota:** Chaves estrangeiras são **desabilitadas por padrão** no Moodle. Elas servem apenas como documentação.

## Índices

```xml
<INDEXES>
    <!-- Índice simples -->
    <INDEX NAME="course" UNIQUE="false" FIELDS="course"/>
    
    <!-- Índice único -->
    <INDEX NAME="email_unique" UNIQUE="true" FIELDS="email"/>
    
    <!-- Índice composto -->
    <INDEX NAME="status_course" UNIQUE="false" FIELDS="status,course"/>
    
    <!-- Índice com order -->
    <INDEX NAME="timecreated_idx" UNIQUE="false" FIELDS="timecreated" SORTING="ASC"/>
</INDEXES>
```

### Boas Práticas para Índices

- Criar índices para campos usados em `WHERE` e `JOIN`
- Usar índices compostos para consultas com múltiplos campos
- Evitar índices em tabelas pequenas (< 1000 registros)
- Usar índices únicos para campos que devem ser exclusivos

## O Objeto $DB

`$DB` é o objeto global de manipulação do banco de dados.

### Inicialização

```php
global $DB;
```

### Operações CRUD

#### Inserir

```php
// Insert simples
$id = $DB->insert_record('meuplugin', $data);

// Insert e retornar objeto
$registro = $DB->insert_record('meuplugin', $data, true);

// Insert com retorno de ID
$record = new stdClass();
$record->name = 'Teste';
$record->course = $courseid;
$id = $DB->insert_record('meuplugin', $record);
```

#### Selecionar

```php
// Um registro por ID
$record = $DB->get_record('meuplugin', ['id' => $id]);
$record = $DB->get_record('meuplugin', ['id' => $id], '*', MUST_EXIST);

// Múltiplos registros
$records = $DB->get_records('meuplugin', ['course' => $courseid]);
$records = $DB->get_records('meuplugin', ['status' => 1], 'name ASC', 0, 10);

// Primeiro registro
$record = $DB->get_record_select('meuplugin', "course = $courseid");

// Contar registros
$count = $DB->count_records('meuplugin', ['status' => 1]);

// Verificar existência
$existe = $DB->record_exists('meuplugin', ['name' => 'Teste']);
```

#### Atualizar

```php
// Atualizar registro
$DB->update_record('meuplugin', $data);

// Atualizar campo específico
$DB->set_field('meuplugin', 'status', 2, ['id' => $id]);

// Atualizar múltiplos campos
$DB->set_field('meuplugin', 'status', 2, ['course' => $courseid]);
```

#### Deletar

```php
// Deletar registro
$DB->delete_records('meuplugin', ['id' => $id]);

// Deletar múltiplos
$DB->delete_records('meuplugin', ['course' => $courseid, 'status' => 0]);

// Deletar com condição
$DB->delete_records_select('meuplugin', "timecreated < $timestamp");
```

### Consultas SQL

```php
// SQL simples
$sql = "SELECT * FROM {meuplugin} WHERE course = :courseid AND status = :status";
$records = $DB->get_records_sql($sql, ['courseid' => $courseid, 'status' => 1]);

// SQL com LIMIT
$sql = "SELECT * FROM {meuplugin} WHERE course = :courseid ORDER BY name ASC";
$records = $DB->get_records_sql($sql, ['courseid' => $courseid], 0, 10);

// SQL com COUNT
$sql = "SELECT COUNT(*) FROM {meuplugin} WHERE course = :courseid";
$count = $DB->count_records_sql($sql, ['courseid' => $courseid]);

// SQL com JOIN
$sql = "SELECT m.*, u.firstname, u.lastname 
        FROM {meuplugin} m
        JOIN {user} u ON m.userid = u.id
        WHERE m.course = :courseid";
$records = $DB->get_records_sql($sql, ['courseid' => $courseid]);
```

### Prevenção de SQL Injection

```php
// CORRETO — usar placeholders
$sql = "SELECT * FROM {meuplugin} WHERE name = :name";
$DB->get_records_sql($sql, ['name' => $userinput]);

// ERRADO — NUNCA concatenar
$sql = "SELECT * FROM {meuplugin} WHERE name = '$userinput'"; // INSEGURO!

// Usar sql_like_escape para LIKE
$search = '%' . $DB->sql_like_escape($userinput) . '%';
$sql = "SELECT * FROM {meuplugin} WHERE name LIKE :search";
$DB->get_records_sql($sql, ['search' => $search]);
```

## Scripts de Upgrade

### db/upgrade.php

```php
<?php
defined('MOODLE_INTERNAL') || die();

function xmldb_meuplugin_upgrade($oldversion) {
    global $DB;

    $dbman = $DB->get_manager();

    // Versão 2025062200
    if ($oldversion < 2025062200) {
        // Criar tabela
        $table = new xmldb_table('meuplugin_novatabela');
        $table->add_field('id', XMLDB_TYPE_INTEGER, '10', null, XMLDB_NOTNULL, XMLDB_SEQUENCE, null);
        $table->add_field('name', XMLDB_TYPE_CHAR, '255', null, XMLDB_NOTNULL, null, null);
        $table->add_field('timecreated', XMLDB_TYPE_INTEGER, '10', null, XMLDB_NOTNULL, null, '0');
        
        $table->add_key('primary', XMLDB_KEY_PRIMARY, ['id']);
        $table->add_index('name_idx', XMLDB_INDEX_NOTUNIQUE, ['name']);

        if (!$dbman->table_exists($table)) {
            $dbman->create_table($table);
        }
    }

    // Versão 2025062201
    if ($oldversion < 2025062201) {
        // Adicionar campo
        $table = new xmldb_table('meuplugin');
        $field = new xmldb_field('newfield', XMLDB_TYPE_CHAR, '100', null, XMLDB_NOTNULL, null, 'default_value');
        
        if (!$dbman->field_exists($table, $field)) {
            $dbman->add_field($table, $field);
        }
    }

    // Versão 2025062202
    if ($oldversion < 2025062202) {
        // Renomear campo
        $table = new xmldb_table('meuplugin');
        $field = new xmldb_field('oldname', XMLDB_TYPE_CHAR, '255');
        
        if ($dbman->field_exists($table, $field)) {
            $dbman->rename_field($table, $field, 'newname');
        }
    }

    // Versão 2025062203
    if ($oldversion < 2025062203) {
        // Deletar campo
        $table = new xmldb_table('meuplugin');
        $field = new xmldb_field('oldfield');
        
        if ($dbman->field_exists($table, $field)) {
            $dbman->drop_field($table, $field);
        }
    }

    // Versão 2025062204
    if ($oldversion < 2025062204) {
        // Deletar tabela
        $table = new xmldb_table('meuplugin_antiga');
        
        if ($dbman->table_exists($table)) {
            $dbman->drop_table($table);
        }
    }

    return true;
}
```

### Operações de Upgrade

| Método | Descrição |
|--------|-----------|
| `create_table()` | Criar tabela |
| `drop_table()` | Deletar tabela |
| `add_field()` | Adicionar campo |
| `drop_field()` | Remover campo |
| `rename_field()` | Renomear campo |
| `add_key()` | Adicionar chave |
| `drop_key()` | Remover chave |
| `add_index()` | Adicionar índice |
| `drop_index()` | Remover índice |

### XMLDB Editor

O Moodle fornece um editor XMLDB para criar e modificar estruturas:

```
Administração → Desenvolvimento → XMLDB editor
```

Ou via CLI:
```bash
php admin/tool/xmldb/cli/cli.php
```

## Referências

- [[Base]] — Estrutura geral
- [[Persistent]] — Active Record
- [[5.2/Plugins/Criar]] — Criação de plugins
- [[DB/Schema]] — Schema detalhado
