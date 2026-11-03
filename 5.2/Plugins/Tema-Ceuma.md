# Tema Ceuma (`theme_ceuma`) — documentação do plugin

**Moodle:** 5.2 · **Parent:** Boost · **Release:** 1.7.40 · **Component:** `theme_ceuma`  
**Pasta:** `public/theme/ceuma/`  
**Diário de mudanças:** [Tema-Ceuma-Diario.md](./Tema-Ceuma-Diario.md)  
**Guia genérico Boost child:** [Temas-Boost-Child.md](./Temas-Boost-Child.md)  
**React no Moodle 5.2 (ESM, fora do AMD do tema):** [../Frontend/React.md](../Frontend/React.md)

Identidade visual Oxy/CEUMA (`frontend_ofc`): azul `#0747DE`, navy `#002C57`, tint `#EBF3FF`.  
Ícones: **Font Awesome 6** (sistema do Boost), não Bootstrap Icons.

---

## 1. Visão geral

Boost child com shell tipo OXY Admin:

```text
[ sidesheet curso | navbar + conteúdo + footer ]
```

| Área | Comportamento |
|------|----------------|
| Curso com secondary nav | Sidesheet permanente à esquerda (logo, menu, usuário) |
| Sem secondary | Brand + usermenu na navbar |
| Modo edição | Caneta na **navbar** (off = risco; on = caneta limpa) |
| Login | Layout split (form \| visual) |
| Dark mode | Preferência por usuário + `data-bs-theme` |

---

## 2. Estrutura de pastas

```text
theme/ceuma/
├── version.php              # versão + requires
├── config.php               # $THEME (layouts, callbacks, parent)
├── lib.php                  # SCSS + pluginfile
├── settings.php             # abas admin (Logo / Cores / Geral / Avançado)
├── layout/
│   ├── drawers.php          # shell principal + contexto sidesheet
│   └── login.php
├── classes/
│   ├── output/core_renderer.php
│   ├── api/darkmode.php
│   ├── api/courseprogress.php
│   └── privacy/provider.php
├── db/services.php          # web services AJAX
├── amd/src/                 # JS (sempre gerar amd/build/*.min.js)
├── templates/               # Mustache (tema + overrides core)
├── scss/
│   ├── default.scss         # entry: variables → Boost → módulos
│   └── ceuma/_*.scss
├── lang/en + pt_br/
└── pix/
```

---

## 3. Config (`config.php`)

| Propriedade | Valor / efeito |
|-------------|----------------|
| `$THEME->parents` | `['boost']` |
| `$THEME->scss` | `theme_ceuma_get_main_scss_content` |
| `$THEME->prescsscallback` | `theme_ceuma_get_pre_scss` (cores admin → tokens) |
| `$THEME->extrascsscallback` | `theme_ceuma_get_extra_scss` |
| `$THEME->precompiledcsscallback` | `theme_ceuma_get_precompiled_css` |
| `$THEME->layouts['login']` | `login.php` |
| `$THEME->layouts['base']` | `drawers.php` |
| `$THEME->rendererfactory` | `theme_overridden_renderer_factory` |
| `$THEME->iconsystem` | Font Awesome |
| `$THEME->haseditswitch` | `true` |
| `$THEME->usescourseindex` | `true` |

---

## 4. Callbacks (`lib.php`)

### `theme_ceuma_get_main_scss_content($theme)`
Monta CSS do tema: tokens `_variables.scss` + preset (`default.scss` ou `plain.scss` ou arquivo uploadado).

### `theme_ceuma_get_pre_scss($theme)`
Mapeia settings de cor → variáveis SCSS/Bootstrap:

| Setting | Tokens |
|---------|--------|
| `brandcolor` | `$primary`, `$ceuma-blue`, `$info` |
| `navycolor` | `$ceuma-navy` |
| `linkcolor` / `linkhovercolor` | `$link-color` / `$link-hover-color` |
| `tintcolor` | `$ceuma-tint` |
| `bgcolor` | `$ceuma-bg`, `$body-bg` |
| `surfacecolor` | `$ceuma-surface`, `$card-bg` |
| `textcolor` / `mutedcolor` / `bordercolor` | texto / muted / border |
| `successcolor` / `warningcolor` / `dangercolor` | semânticas |

Só aceita hex `#RGB`…`#RRGGBBAA`. Inclui `scsspre` se preenchido.

### `theme_ceuma_get_extra_scss($theme)`
Background de página / login + `scss` raw do admin.

### `theme_ceuma_get_precompiled_css()`
Fallback: CSS do Boost.

### `theme_ceuma_pluginfile(...)`
Serve fileareas: `logo`, `logocompact`, `favicon`, `backgroundimage`, `loginbackgroundimage`, `preset`.

---

## 5. Classes PHP

### `theme_ceuma\output\core_renderer`  
extends `theme_boost\output\core_renderer`

| Método | Função |
|--------|--------|
| `body_attributes()` | Classe `ceuma-dark` + `data-bs-theme` conforme preferência |
| `render_darkmode_toggle()` | Template `theme_ceuma/darkmode` |
| `render_quicknav()` | Botão/modal navegação rápida (só logado) |
| `get_logo_url()` | Logo do tema ou core |
| `get_compact_logo_url()` | Logo compacta (navbar/sidesheet) |
| `should_display_navbar_logo()` | Se há URL de logo compacta |
| `favicon()` | Favicon do tema ou parent |
| `box()` | Card intro friendly em `login-forgot_password` |

### `theme_ceuma\api\darkmode`  
external_api

| Método | Função |
|--------|--------|
| `toggle($enabled)` | Grava `theme_ceuma_darkmode` (user preference) |
| `toggle_parameters` / `toggle_returns` | Contrato WS |

**WS:** `theme_ceuma_toggle_darkmode` (ajax, write, login).

### `theme_ceuma\api\courseprogress`  
external_api

| Método | Função |
|--------|--------|
| `get($courseid)` | Atividades visíveis + completion do usuário |

Retorno: `percent`, `done`, `tracked`, `activities[]` (`cmid`, `name`, `url`, `state`, `complete`, …).  
Pula `label`. Exige login no curso.

**WS:** `theme_ceuma_get_course_progress` (ajax, read, login).

### `theme_ceuma\privacy\provider`
Metadata + export/delete da preferência `theme_ceuma_darkmode`.

---

## 6. Settings admin (`settings.php`)

Abas (`theme_boost_admin_settingspage_tabs`):

| Aba | Conteúdo |
|-----|----------|
| **Logo** | `logo`, `logocompact`, `favicon` |
| **Cores** | brand, navy, links, tint, bg, surface, text, muted, border, success/warning/danger |
| **Geral** | preset, backgroundimage, loginbackgroundimage |
| **Avançado** | `scsspre`, `scss` raw |

Toda mudança de arquivo/cor: `theme_reset_all_caches`.

---

## 7. Layouts

### `layout/drawers.php`
Monta contexto Boost drawers + extras Ceuma:

- Brand do **site**: `sitefullname` / `sitename` / `siteinitial`
- Cover do curso: `courseimage`, `hascoursecover`
- Usuário: `userfullname`, `userrole`, `userpicture`, `userprofileurl`
- `hassidesheet` / `sidesheetmoremenu` → **só** primary no Painel / Meus cursos (curso **não** usa sidesheet)
- Curso: `secondarymoremenu` horizontal (`.ceuma-course-secondary`) sob a navbar
- `hidesprimaryinnavbar` → no Painel com sidesheet, some o primary da navbar (vai pro rail)

### `layout/login.php`
Layout de login dedicado (templates login + login_layout).

---

## 8. Templates Mustache

| Template | Papel |
|----------|--------|
| `drawers.mustache` | Shell: sidesheet \| coluna (navbar + main + footer fora da coluna se necessário) |
| `sidesheet.mustache` | Rail do curso: brand, moremenu, usermenu |
| `navbar.mustache` | Primary nav; edit pen sempre; usermenu só sem sidesheet |
| `footer.mustache` | Footer Oxygeni (redes + copyright + logo) |
| `darkmode.mustache` | Toggle sol/lua |
| `quicknav.mustache` | Modal navegação rápida |
| `course_details_modal.mustache` | Modal detalhes/progresso do curso |
| `core/user_menu_metadata.mustache` | **Override:** avatar + `userfullname` truncado |
| `core/login_layout.mustache` | Split login OXY |
| `core/loginform.mustache` / `login_panel` / `login.mustache` | Chrome login |
| `core/full_header.mustache` | Header de página |
| `core_course/coursecard(s).mustache` | Cards de curso (meta limpa) |
| `block_myoverview/view-cards.mustache` | Overview em cards |

---

## 9. AMD (`amd/src` → `amd/build`)

| Módulo | Função | Storage / API |
|--------|--------|----------------|
| `sidesheet` | Collapse sidesheet + mobile + chama `menunav` | `localStorage: theme_ceuma_sidesheet_collapsed` |
| `menunav` | Submenus em acordeão; **pula** tabs admin (`data-bs-toggle=tab`, `#link…`) | — |
| `quicknav` | Recentes + pins | `theme_ceuma_quicknav_recent` / `_pins` |
| `darkmode` | Toggle UI + AJAX | pref + `localStorage: theme_ceuma_darkmode` |
| `coursedetails` | Modal progresso (`theme_ceuma_get_course_progress`) | Modal Boost |
| `searchable` | Select custom + busca | — |
| `secondarypanel` | **Legado** FAB/modal do menu (substituído pela sidesheet) | — |

**Build:** editar `amd/src/*.js` e gerar `amd/build/*.min.js` (purge caches AMD depois).

---

## 10. SCSS (`scss/ceuma/`)

Entry: `scss/default.scss`.

| Arquivo | Escopo |
|---------|--------|
| `_variables.scss` | Tokens CEUMA |
| `_general.scss` | Tipografia, badges admin, base |
| `_shell.scss` | Flex shell sidesheet + coluna; footer full-width |
| `_navbar.scss` | Primary nav + **`.ceuma-navbar-editpen`** (caneta edição) |
| `_sidesheet.scss` | Rail lateral, brand, userbar, collapse |
| `_drawers.scss` | Drawers Boost (blocos / course index) |
| `_navmenu.scss` | Ícones por `data-key`; tabs admin em linha. Plugins=`modules`→`puzzle-piece`, Atividades=`courseoverview`→`file-lines` |
| `_course.scss` | Cover, seções, atividades |
| `_coursecards.scss` / `_dashboard.scss` | Cards / painel |
| `_forms.scss` / `_datepicker.scss` / `_toggles.scss` / `_tables.scss` | Controles |
| `_footer.scss` | Footer |
| `_login.scss` | Login split |
| `_darkmode.scss` | Overrides dark |

Caneta edição (navbar): Font Awesome `pencil` `\f303`; off = `::after` risco; on = sem risco + tint azul.

---

## 11. Preferências e localStorage

| Chave | Onde | Uso |
|-------|------|-----|
| `theme_ceuma_darkmode` | user preference + LS | Dark mode |
| `theme_ceuma_sidesheet_collapsed` | LS | Sidesheet recolhida |
| `theme_ceuma_quicknav_recent` | LS | Páginas recentes |
| `theme_ceuma_quicknav_pins` | LS | Atalhos fixos |
| `drawer-open-index` / `drawer-open-block` | core prefs | Drawers Boost |

---

## 12. Fluxos principais

### Shell com curso
1. `drawers.php` detecta secondary nav → `secondarymoremenu`
2. `drawers.mustache` inclui `sidesheet`
3. `sidesheet.js` + `menunav.js` inicializam
4. Navbar **esconde** usermenu (fica na sidesheet); **mantém** caneta de edição

### Modo edição
1. `{{{ output.edit_switch }}}` dentro de `.ceuma-navbar-editpen`
2. CSS esconde o switch; label vira botão FA
3. Clique continua no checkbox core (`core/edit_switch`)

### Progresso do curso (card)
1. Clique `[data-action="ceuma-course-details"]`
2. `coursedetails.js` → WS `theme_ceuma_get_course_progress`
3. Render `course_details_modal`

---

## 13. Operação

```bash
# Após mudar version.php / SCSS / templates / AMD:
# Administração → Desenvolvimento → Purge all caches
# ou CLI:
php public/admin/cli/purge_caches.php
```

Bump: incrementar `$plugin->version` e `$plugin->release` em `version.php` e registrar no [diário](./Tema-Ceuma-Diario.md).

---

## 14. Notas / armadilhas

1. **Secondary = sidesheet** — não reintroduzir FAB/modal como fluxo principal (`secondarypanel` é legado).
2. **Admin tabs** — `menunav` não pode virar acordeão em `data-bs-toggle=tab`.
3. **Footer** — fora da coluna que o drawer de blocos cobre, senão corta.
4. **Brand** — sempre `fullname`/`shortname` do site, não string fixa.
5. **AMD** — `src` sem `build` minificado = JS antigo em produção.
6. **Ícones** — FA6 via CSS `::before` / classes `fa`; não misturar Bootstrap Icons.
7. **Média ponderada no livro de notas** — não é do tema; admin libera tipos de agregação em *Notas → Configurações de categoria*. Total costuma ser **/100** (80 ≠ 8).

---

## 15. Créditos

Dvizioon / CEUMA · tokens OxyCertificados · parent Boost · GPL v3+
