# `settings.php` por tipo — Moodle 5.2

Mesmas regras do [[4.5.8/Plugins/Settings|4.5.8]]. O `plugininfo` inclui o arquivo e injeta `$ADMIN`, `$hassiteconfig`, e (em mod/block/…) `$settings`.

## Resumo por tipo

| Tipo | Padrão |
|------|--------|
| `mod_` | `$settings` já existe → `$settings->add(new admin_setting_…)` |
| `block_` | Precisa `has_config(): true` + `$settings->add` |
| `local_` | Você cria `admin_settingpage` / `admin_externalpage` e `$ADMIN->add('localplugins', …)` |
| `tool_` | Idem sob `'tools'` |
| `auth_` / `enrol_` / `theme_` | `$settings->add` na page que o core criou |

## Local (exemplo real deste tree)

`public/local/cataloggate/settings.php` (se o checkout usar `public/`):

```php
if ($hassiteconfig) {
    $ADMIN->add('localplugins', new admin_category(
        'local_cataloggate',
        get_string('pluginname', 'local_cataloggate')
    ));

    $settings = new admin_settingpage(
        'local_cataloggate_settings',
        get_string('settingsheading', 'local_cataloggate')
    );
    $settings->add(new admin_setting_configselect(
        'local_cataloggate/theme',
        get_string('catalogtheme', 'local_cataloggate'),
        get_string('catalogtheme_desc', 'local_cataloggate'),
        'bootstrap',
        \local_cataloggate\appearance::theme_options()
    ));
    $ADMIN->add('local_cataloggate', $settings);

    $ADMIN->add('local_cataloggate', new admin_externalpage(
        'local_cataloggate_managepages',
        get_string('managepages', 'local_cataloggate'),
        new moodle_url('/local/cataloggate/pages.php'),
        'local/cataloggate:manage'
    ));
}
```

Leitura: `get_config('local_cataloggate', 'theme')`.

## Mod / block

Igual 4.5: `if ($ADMIN->fulltree) { $settings->add(...); }`.  
Bloco: config global em `settings.php`; config da instância em `edit_form.php` (`config_*`) — ver [[5.2/Plugins/Forms]].

## Classes úteis

`admin_setting_configtext`, `configtextarea`, `configcheckbox`, `configselect`, `configmultiselect`, `configpasswordunmask`, `configduration`, `heading`, `admin_externalpage`, `admin_category` — em `lib/adminlib.php`.

## Referências

- [[4.5.8/Plugins/Settings]] (tabela completa + checklist)
- [[5.2/Plugins/Forms]]
- [[5.2/Plugins/Tipos]]
- [[4.5.8/Admin/Administracao]] (árvore admin detalhada; 5.2 segue o mesmo modelo)
