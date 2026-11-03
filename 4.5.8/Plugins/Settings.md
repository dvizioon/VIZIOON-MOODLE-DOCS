# `settings.php` por tipo de plugin — Moodle 4.5.8

Configuração de **site** (Administração). Não confundir com form de instância (`mod_form` / `edit_form` do bloco) — isso é [[4.5.8/Plugins/Forms]].

O core monta a árvore em `admin_get_root()` (`lib/adminlib.php`) e, em `admin/settings/plugins.php`, chama `load_settings()` de cada `core\plugininfo\*`. Esse método **inclui** o `settings.php` do plugin, com variáveis injetadas.

Visão geral da árvore: [[4.5.8/Admin/Administracao]].

---

## Variáveis que o core injeta no `settings.php`

| Variável | Significado |
|----------|-------------|
| `$ADMIN` | `admin_root` — use `$ADMIN->add(...)` |
| `$hassiteconfig` | Usuário tem `moodle/site:config` |
| `$settings` | `admin_settingpage` **já criado** (mod, block, auth, enrol, …) — ou você cria (local, tool) |
| `$plugininfo` | Instância `core\plugininfo\...` |
| `$CFG`, `$DB`, `$OUTPUT`, `$PAGE`, `$USER` | Globais usuais |

Sempre:

```php
defined('MOODLE_INTERNAL') || die();
```

---

## Diferença crítica: quem cria o `$settings`

| Tipo | Quem cria a página | O que o `settings.php` faz |
|------|--------------------|----------------------------|
| `mod` | `plugininfo\mod` cria `admin_settingpage` e depois `include` | Só `$settings->add(...)`. Pode zerar `$settings = null` para não aparecer |
| `block` | Idem, **só se** `has_config()` do bloco for true | `$settings->add(...)` |
| `auth` / `enrol` / `filter` / `editor` / … | plugininfo cria a page | `$settings->add(...)` |
| `local` | **Ninguém** cria page automática | Você faz `$ADMIN->add(...)` com `admin_settingpage` / `admin_externalpage` / categoria |
| `tool` | Em geral **você** monta sob a categoria `tools` | `$ADMIN->add('tools', ...)` |

Leitura: `lib/classes/plugininfo/mod.php`, `block.php`, `local.php`.

---

## 1. Módulo (`mod_/settings.php`)

Exemplo real: `mod/page/settings.php`.

```php
defined('MOODLE_INTERNAL') || die();

if ($ADMIN->fulltree) {
    $settings->add(new admin_setting_configmultiselect(
        'page/displayoptions',
        get_string('displayoptions', 'page'),
        get_string('configdisplayoptions', 'page'),
        $defaultdisplayoptions,
        $displayoptions
    ));

    $settings->add(new admin_setting_heading(
        'pagemodeditdefaults',
        get_string('modeditdefaults', 'admin'),
        get_string('condifmodeditdefaults', 'admin')
    ));

    $settings->add(new admin_setting_configcheckbox(
        'page/printintro',
        get_string('printintro', 'page'),
        get_string('printintroexplain', 'page'),
        0
    ));
}
```

Nomes gravados: `'page/printintro'` → `get_config('page', 'printintro')` / `set_config('printintro', $v, 'page')`.

`$ADMIN->fulltree` evita trabalho pesado quando a árvore só precisa dos nós.

---

## 2. Bloco (`blocks/<nome>/settings.php`)

1. Em `block_<nome>.php`:

```php
public function has_config() {
    return true; // sem isso o settings.php NÃO é carregado
}
```

2. `settings.php` (exemplo `blocks/html/settings.php`):

```php
defined('MOODLE_INTERNAL') || die();

if ($ADMIN->fulltree) {
    $settings->add(new admin_setting_configcheckbox(
        'block_html_allowcssclasses',
        get_string('allowadditionalcssclasses', 'block_html'),
        get_string('configallowadditionalcssclasses', 'block_html'),
        0
    ));
}
```

Isso é config **global** do tipo de bloco. Config **por instância** (título, HTML) fica no `edit_form.php` (`config_*`), não aqui.

---

## 3. Local (`local/<nome>/settings.php`)

`plugininfo\local` só faz `include` — **não** cria `$settings`. Padrão (como `local_cataloggate` no 5.2):

```php
defined('MOODLE_INTERNAL') || die();

if ($hassiteconfig) {
    $ADMIN->add('localplugins', new admin_category(
        'local_meu',
        get_string('pluginname', 'local_meu')
    ));

    // Página de configs.
    $settings = new admin_settingpage(
        'local_meu_settings',
        get_string('settings', 'local_meu')
    );
    $settings->add(new admin_setting_configtext(
        'local_meu/apikey',
        get_string('apikey', 'local_meu'),
        get_string('apikey_desc', 'local_meu'),
        '',
        PARAM_RAW_TRIMMED
    ));
    $ADMIN->add('local_meu', $settings);

    // Página PHP própria (CRUD, relatório…).
    $ADMIN->add('local_meu', new admin_externalpage(
        'local_meu_manage',
        get_string('manage', 'local_meu'),
        new moodle_url('/local/meu/manage.php'),
        'local/meu:manage'   // capability exigida
    ));
}
```

Categoria pai usual: `localplugins` (lista em Administração → Plugins → Plugins locais).

---

## 4. Tool (`admin/tool/<nome>/settings.php`)

Mesma ideia do local, categoria `tools`:

```php
if ($hassiteconfig) {
    $ADMIN->add('tools', new admin_externalpage(
        'tool_meu',
        get_string('pluginname', 'tool_meu'),
        new moodle_url('/admin/tool/meu/index.php'),
        'moodle/site:config'
    ));

    $settings = new admin_settingpage('tool_meu_settings', get_string('settings', 'tool_meu'));
    $settings->add(new admin_setting_configcheckbox(
        'tool_meu/enabled',
        get_string('enabled', 'tool_meu'),
        '',
        1
    ));
    $ADMIN->add('tools', $settings);
}
```

---

## 5. Classes `admin_setting_*` mais usadas

Definidas em `lib/adminlib.php`:

| Classe | Uso |
|--------|-----|
| `admin_setting_heading` | Título/descrição sem gravar valor |
| `admin_setting_configtext` | Texto / número (`PARAM_INT` no 5º arg) |
| `admin_setting_configtextarea` | Texto longo |
| `admin_setting_confightmleditor` | HTML |
| `admin_setting_configpasswordunmask` | Segredo (API key) |
| `admin_setting_configcheckbox` | On/off |
| `admin_setting_configmulticheckbox` | Vários checks |
| `admin_setting_configselect` | Select |
| `admin_setting_configmultiselect` | Multi select |
| `admin_setting_configduration` | Duração (s/min/h) |
| `admin_setting_configtime` | Horário |
| `admin_setting_configfile` / `configdirectory` / `configexecutable` | Paths no servidor |
| `admin_setting_configcolourpicker` | Cor (se disponível no core) |
| `admin_setting_configselect_autocomplete` | Select com busca |

Construtor típico do text:

```php
new admin_setting_configtext(
    $name,      // 'local_meu/chave' ou 'modname/chave'
    $visiblename,
    $description,
    $defaultsetting,
    $paramtype = PARAM_RAW,  // opcional
    $size = null
);
```

Leitura/escrita:

```php
$apikey = get_config('local_meu', 'apikey');
set_config('apikey', $value, 'local_meu');
// ou get_config('local_meu') → objeto com todas as chaves
```

---

## 6. `admin_externalpage` vs `admin_settingpage`

| | `admin_settingpage` | `admin_externalpage` |
|--|---------------------|----------------------|
| UI | Form gerado pelos `admin_setting_*` | Seu PHP (`moodleform`, tabelas…) |
| Save | Core (`admin_write_settings`) | Você no script |
| Cap | Em geral `moodle/site:config` | Capability passada no construtor |

---

## 7. Auth, enrol, filter, theme (resumo)

| Tipo | Detalhe |
|------|---------|
| `auth` | `settings.php` obrigatório (não use `config.html` legado). Seção `authsetting<nome>` |
| `enrol` | `$settings->add`; pode ter página de teste |
| `filter` | `settings.php` ou legado `filtersettings.php` |
| `theme` | Settings ricos (cores, preset SCSS); lidos via `get_config('theme_xxx')` |
| `report` / `gradereport` | settings opcional; muitas vezes só página do relatório |
| `webservice` (protocolo) | settings do protocolo; funções de API ficam no `db/services.php` do `local_`/`mod_` |

---

## 8. Checklist

- [ ] `defined('MOODLE_INTERNAL') || die();`
- [ ] Bloco: `has_config()` retorna true se tem `settings.php`
- [ ] Mod/block/auth: usar `$settings->add` (page já existe)
- [ ] Local/tool: criar page/categoria e `$ADMIN->add`
- [ ] Nomes `componente/chave` coerentes com `get_config`
- [ ] Senhas/API keys → `admin_setting_configpasswordunmask`
- [ ] Strings via `get_string`, não PT fixo
- [ ] Guardar com `$ADMIN->fulltree` / `$hassiteconfig` quando fizer sentido
- [ ] Não misturar config de **instância** (form) com config de **site** (settings)

## Referências

- [[4.5.8/Plugins/Forms]]
- [[4.5.8/Admin/Administracao]]
- [[4.5.8/Plugins/Tipos]]
- [[4.5.8/Plugins/Criar]]
- [[4.5.8/Seguranca/Funcoes]]
