# Criar um tema Moodle 5.2 (Boost child)

Guia prático para criar temas como o `theme_ceuma`. Use este documento sempre que for montar um tema novo a partir de uma identidade visual (Figma, frontend React, guidelines).

---

## 1. Conceitos

| Termo | Significado |
|-------|-------------|
| **theme_*** | Tipo de plugin Moodle (`public/theme/nome/`) |
| **Boost** | Tema pai oficial (Bootstrap 5 + Design System). Quase todo tema moderno é **filho do Boost**. |
| **Boost child** | Tema que declara `$THEME->parents = ['boost']` e só sobrescreve SCSS / alguns templates |
| **Preset** | Arquivo SCSS grande (`default.scss` / `plain.scss`) com Bootstrap + Moodle |
| **pre-SCSS** | Variáveis **antes** do preset (`$primary`, fontes…) |
| **post / extra SCSS** | Regras **depois** do preset (navbar, login, cards) |
| **Brand colour** | Setting admin → injeta `$primary: #hex;` (não existe `$brand-color` no Boost) |

No Moodle **5.2** o código fica em `public/theme/…`.

---

## 2. Checklist mínimo de arquivos

```text
public/theme/meutema/
├── version.php
├── config.php
├── lib.php
├── settings.php
├── scss/
│   ├── pre.scss              # tokens da marca
│   ├── post.scss             # chrome visual
│   └── preset/default.scss   # pode ser placeholder
├── lang/en/theme_meutema.php
├── lang/pt_br/theme_meutema.php   # opcional
├── classes/privacy/provider.php   # null_provider
├── pix/
│   ├── favicon.ico
│   ├── screenshot.png
│   └── logo.svg              # opcional (usar em Aparência → Logos)
└── README.md
```

Layouts e templates **não são obrigatórios** — herdam do Boost (drawers, login, etc.).

---

## 3. Extrair identidade visual (do frontend / design)

Antes de codar, monte uma tabela de tokens. Exemplo CEUMA (`OXY-CERTIFICADOS/frontend_ofc`):

| Papel | Token origem | Hex | Moodle / SCSS |
|-------|--------------|-----|---------------|
| Accent / CTA | `--accent` / primary-500 | `#0747DE` | `$primary` / brandcolor |
| Navbar / profundo | primary-550 | `#002C57` | `$ceuma-navy` |
| Tint ativo | `--accent-soft` | `#EBF3FF` | item ativo drawer |
| Fundo | `--background` | `#EFEFEF` | `$body-bg` |
| Card | `--surface` | `#FDFDFD` | `$card-bg` |
| Texto | `--foreground` | `#383839` | `$body-color` |
| Muted | `--muted` | `#919192` | `$secondary` |
| Borda | `--border` | `#E6E6E6` | `$border-color` |
| Success | secondary-green | `#05842B` | `$success` |
| Warning | secondary-yellow | `#D68B00` | `$warning` |
| Danger | secondary-red | `#BA2F2A` | `$danger` |
| Fonte | DM Sans | — | `$font-family-sans-serif` |

**Dica:** no Oxy, botões de página usam azul `#0747DE` e o `Button primary` usa navy `#002C57`. No Moodle, mapeie **brand = azul** e navy na **navbar / login CTA**.

---

## 4. `version.php`

```php
$plugin->component = 'theme_meutema';
$plugin->version   = 2026092400;      // YYYYMMDDXX
$plugin->requires  = 2026041000;      // Moodle 5.2 base
$plugin->supported = [502, 502];
$plugin->dependencies = [
    'theme_boost' => 2026042000,
];
```

---

## 5. `config.php` (esqueleto)

```php
$THEME->name = 'meutema';
$THEME->parents = ['boost'];
$THEME->sheets = [];
$THEME->scss = function ($theme) {
    return theme_meutema_get_main_scss_content($theme);
};
$THEME->prescsscallback = 'theme_meutema_get_pre_scss';
$THEME->extrascsscallback = 'theme_meutema_get_extra_scss';
$THEME->precompiledcsscallback = 'theme_meutema_get_precompiled_css';
$THEME->enable_dock = false;
$THEME->yuicssmodules = [];
$THEME->rendererfactory = 'theme_overridden_renderer_factory';
$THEME->iconsystem = \core\output\icon_system::FONTAWESOME;
$THEME->haseditswitch = true;
$THEME->usescourseindex = true;
$THEME->activityheaderconfig = ['notitle' => true];
// NÃO defina $THEME->layouts a menos que vá customizar layouts.
```

---

## 6. Pipeline SCSS (`lib.php`)

Ordem real de compilação:

1. **`theme_*_get_pre_scss`** → brandcolor admin  
2. **`theme_*_get_main_scss_content`** → **padrão Moove**: `_variables.scss` + `default.scss` (`@import` Boost + módulos)  
3. **`theme_*_get_extra_scss`** → imagens / SCSS cru  

**Não faça:** concatenar um `post.scss` com `@import` no meio de uma string solta, nem `@import url(https://fonts...)` no pre sem testar — o scssphp do Moodle pode falhar e cair no CSS fallback do Boost (parece que o tema “não aplica”).

Referência que funciona neste projeto: `theme/moove/lib.php` + `theme/ceuma/lib.php` (v1.4+).  
Diário de erros reais: [Tema-Ceuma-Diario.md](./Tema-Ceuma-Diario.md).

---

## 7. O que colocar em `pre.scss` vs `post.scss`

### `pre.scss` (variáveis)

- Hex da marca
- `$primary`, `$success`, `$body-bg`, `$font-family-sans-serif`
- `@import url(...)` de Google Fonts (se necessário)
- `$border-radius`, focus shadow

### `post.scss` (visual)

- `.navbar` (cor de fundo navy)
- Cards / blocks (borda, radius, sem sombra pesada)
- `.btn-primary` hover
- Login (`body.pagelayout-login`)
- Drawer item ativo (tint + borda azul)
- Alerts com fundos soft

---

## 8. Settings

Copie o bloco de tabs do Boost/Classic:

- `preset` + `presetfiles`
- `brandcolor` (colour picker) → `theme_reset_all_caches`
- `backgroundimage` / `loginbackgroundimage`
- `scsspre` / `scss` (raw)

Default do brandcolor = hex da marca (ex.: `#0747DE`).

---

## 9. Ativar e depurar

```bash
# Upgrade
php public/admin/cli/upgrade.php

# Ou UI: Administração → Notificações
```

Depois:

1. **Aparência → Temas → Seletor de temas** → Meu tema  
2. **Aparência → Temas → Meu tema** → Brand colour  
3. **Purge all caches**  
4. Enquanto desenvolve SCSS: **Theme designer mode** (recompila a cada request — mais lento)

Se o CSS não muda: purge + confira erros de SCSS em `php://stderr` / logs.

---

## 10. Logos e favicon

| Arquivo | Uso |
|---------|-----|
| `pix/favicon.ico` | Favicon do tema |
| `pix/screenshot.png` | Seletor de temas |
| `pix/logo.svg` | Upload manual em **Aparência → Logos** |

Moodle **não** puxa `pix/logo.svg` sozinho como logo do site — configure em Aparência.

---

## 11. Privacy

Se o tema não grava preferências próprias:

```php
class provider implements \core_privacy\local\metadata\null_provider {
    public static function get_reason(): string {
        return 'privacy:metadata';
    }
}
```

(Boost pai já trata drawers; filho normalmente é null.)

---

## 12. Referência viva neste projeto

| Item | Caminho |
|------|---------|
| Tema CEUMA | `public/theme/ceuma/` |
| Tokens Oxy | `OXY-CERTIFICADOS/frontend_ofc/src/app/globals.css` |
| Logos CEUMA | `frontend_ofc/src/assets/logo_ceuma*.svg` → `theme/ceuma/pix/` |
| Pai Boost | `public/theme/boost/` |
| Filho core Classic | `public/theme/classic/` |
| Filho rico Moove | `public/theme/moove/` |

---

## 13. Roadmap típico de evolução

1. **v1** — tokens + navbar + botões + login (como `theme_ceuma` 1.0)  
2. **v1.1** — Mustache `navbar` / footer com logo embutido  
3. **v1.2** — Layout login split (painel azul + card)  
4. **v2** — Frontpage custom, AMD, settings de tipografia  

---

## 14. Erros comuns

| Sintoma | Causa | Correção |
|---------|-------|----------|
| Tema não aparece | Pasta fora de `public/theme/` ou sem upgrade | Instalar + Notificações |
| Cor não muda | Cache / `$primary` depois do preset | Variável no **pre**; purge |
| Fonte não carrega | `@import` bloqueado | Verificar CSP / carregar via additional HTML |
| SCSS compile fail | Sintaxe / variável indefinida | Theme designer + logs |
| Layout quebrado | Redefiniu `$THEME->layouts` mal | Remova layouts e herde Boost |

---

## 15. Comandos úteis

```bash
# Lint PHP do tema
find public/theme/ceuma -name '*.php' -exec php -l {} \;

# Upgrade
php public/admin/cli/upgrade.php

# Purge caches
php public/admin/cli/purge_caches.php
```
