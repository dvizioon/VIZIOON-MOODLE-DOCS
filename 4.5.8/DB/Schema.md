# XMLDB e o objeto `$DB` no 4.5.8

O Moodle não deixa o plugin mandar `CREATE TABLE` cru. A estrutura nasce em `db/install.xml` (XMLDB). No upgrade, `lib/xmldb` compara o XML com o banco e o driver em `lib/dml/` gera o SQL de MySQL/MariaDB, PostgreSQL, SQL Server ou Oracle.

Editor visual: Administração → Desenvolvimento → Editor XMLDB, implementado em `admin/tool/xmldb`. Conferência sem browser: `php admin/cli/check_database_schema.php`.

## Forma do install.xml

O XSD está em `lib/xmldb/xmldb.xsd`. Um módulo real (por exemplo `mod/page/db/install.xml`) segue este formato:

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<XMLDB PATH="mod/page/db" VERSION="20120122" COMMENT="XMLDB file for Moodle mod/page"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:noNamespaceSchemaLocation="../../../lib/xmldb/xmldb.xsd"
>
  <TABLES>
    <TABLE NAME="page" COMMENT="Each record is one page and its config data">
      <FIELDS>
        <FIELD NAME="id" TYPE="int" LENGTH="10" NOTNULL="true" SEQUENCE="true"/>
        <FIELD NAME="course" TYPE="int" LENGTH="10" NOTNULL="true" DEFAULT="0" SEQUENCE="false"/>
        <FIELD NAME="name" TYPE="char" LENGTH="255" NOTNULL="true" SEQUENCE="false"/>
        <FIELD NAME="intro" TYPE="text" NOTNULL="false" SEQUENCE="false"/>
        <FIELD NAME="introformat" TYPE="int" LENGTH="4" NOTNULL="true" DEFAULT="0" SEQUENCE="false"/>
        <FIELD NAME="content" TYPE="text" NOTNULL="false" SEQUENCE="false"/>
        <FIELD NAME="contentformat" TYPE="int" LENGTH="4" NOTNULL="true" DEFAULT="0" SEQUENCE="false"/>
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

O nome da tabela do módulo principal é o nome do módulo (`page`, `forum`, `quiz`), sem prefixo. `$CFG->prefix` (padrão `mdl_`) é aplicado pelo `$DB`. No SQL escrito à mão usa-se `{page}`.

## Tipos de campo

| TYPE | Uso no 4.5 |
|------|------------|
| `int` | ids, timestamps, flags. `LENGTH="10"` é o tamanho lógico |
| `char` | até 1333 caracteres; nome e shortname usam 255 |
| `text` | HTML, intro, JSON |
| `number` | notas (`LENGTH` + `DECIMALS`) |
| `binary` | raro |
| `float` | desencorajado; nota usa `number` |

`SEQUENCE="true"` só no `id`. Chave estrangeira (`TYPE="foreign"`) é documentação: o Moodle **não cria** FK física por padrão. Integridade é do PHP. Índice único é `<INDEX UNIQUE="true">` ou `<KEY TYPE="unique">`.

## Upgrade

`db/upgrade.php`:

```php
function xmldb_page_upgrade($oldversion) {
    global $DB;
    $dbman = $DB->get_manager();

    if ($oldversion < 2024100701) {
        $table = new xmldb_table('page');
        $field = new xmldb_field('extra', XMLDB_TYPE_CHAR, '100', null, null, null, null);
        if (!$dbman->field_exists($table, $field)) {
            $dbman->add_field($table, $field);
        }
        upgrade_mod_savepoint(true, 2024100701, 'page');
    }
    return true;
}
```

O `savepoint` é obrigatório dentro do `if`. O nome da função de savepoint depende do tipo: `upgrade_mod_savepoint`, `upgrade_block_savepoint`, `upgrade_plugin_savepoint`. A versão nova tem de ser maior que `$plugin->version` anterior e igual à versão declarada no `version.php` quando o passo entra.

Operações do `database_manager`: `create_table`, `drop_table`, `add_field`, `change_field_type`, `rename_field`, `drop_field`, `add_index`, `drop_index`, `add_key`, `rename_table`.

## `$DB`

Driver carregado por `lib/dmllib.php` conforme `$CFG->dbtype` (`mysqli`, `pgsql`, `sqlsrv`, `oci`, `auroramysql`).

```php
$record = $DB->get_record('page', ['id' => $id], '*', MUST_EXIST);
$pages  = $DB->get_records('page', ['course' => $courseid], 'name ASC');
$id     = $DB->insert_record('page', $obj);
$DB->update_record('page', $obj);          // exige $obj->id
$DB->set_field('page', 'name', $name, ['id' => $id]);
$DB->delete_records('page', ['id' => $id]);
$n      = $DB->count_records('page', ['course' => $courseid]);
$exists = $DB->record_exists('page', ['id' => $id]);

$sql = "SELECT p.*, cm.id AS cmid
          FROM {page} p
          JOIN {course_modules} cm ON cm.instance = p.id
         WHERE p.course = :course";
$rows = $DB->get_records_sql($sql, ['course' => $courseid]);
```

Placeholders nomeados (`:course`). Concatenar valor de usuário na string é o buraco. `LIKE` usa `$DB->sql_like()` e `$DB->sql_like_escape()`.

`MUST_EXIST` lança `dml_missing_record_exception`. `IGNORE_MISSING` devolve `false`.

Transação: `$transaction = $DB->start_delegated_transaction();` … `$transaction->allow_commit();`.

## Referências

- [[4.5.8/Classes/Persistent]]
- [[4.5.8/Plugins/Criar]]
