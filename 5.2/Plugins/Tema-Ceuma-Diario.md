# Tema Ceuma — diário técnico + lições (Moodle 5.2)

Documento vivo: o que foi feito, o que quebrou, e como o **Moove** ensina a fazer certo.

Local do plugin: `public/theme/ceuma/`  
Identidade: OxyCertificados (`frontend_ofc`) — azul `#0747DE`, navy `#002C57`, tint `#EBF3FF`.

**Referência completa do plugin (classes, lib, AMD, templates):** [Tema-Ceuma.md](./Tema-Ceuma.md)  
**React ESM no Moodle 5.2 (não é o AMD do tema):** [../Frontend/React.md](../Frontend/React.md)

---

## 1.7.66 — Select: grupos visíveis

O select com busca listava só as opções e escondia o `<optgroup>`. Fonte do relatório (e qualquer select com grupo) agora mostra o nome do grupo acima das opções.

Purge caches `2026092502`.

---

## 1.7.65 — Capa no header + menu central + Mais por cima

Índice: imagem de fundo no **header** com o nome do curso em cima (logo do site escondido). Menu Curso/Configurações/… **centralizado**. “Mais” abre **por cima** da página (saiu do scroller).

Purge caches `2026092477` (tema + templates).

---

## 1.7.64 — Índice do curso: capa + nome (não logo do site)

No drawer do índice: some o “D DVIZIOON DVN” repetido. Entra **imagem de fundo + nome do curso** clicável → volta pra `/course/view.php`.

Purge caches `2026092476` (templates + tema).

---

## 1.7.63 — Curso: Mais + atividades + largura 100%

- Clicar atividade (ex.: Meet “Teste”) mantém menu **horizontal** (não troca pra sidesheet).
- “Mais” no secondary horizontal: dropdown não é mais cortado pelo `overflow`.
- Conteúdo do curso/atividade: **100%** largura, centralizado, cards arredondados.

Purge caches `2026092475`.

---

## 1.7.62 — Notificações + chat (popover / drawer)

Popover de notificações: `position: fixed` sob a navbar (sem sobrepor o sino), cantos arredondados, header limpo. Drawer de mensagens no mesmo visual Ceuma.

Purge caches `2026092474`.

---

## 1.7.61 — Calendário: sidesheet + título na navbar

Calendário igual Painel / Meus cursos: menu **vertical** (primary no sidesheet) e **Calendário** centralizado na navbar. Chip com engrenagem some.

Purge caches `2026092473`.

---

## 1.7.60 — Perfil: header central + título limpo

Nome não herda mais o chip com engrenagem do admin (`format-site`). Avatar + nome + Mensagem **centralizados**; título normal navy.

Purge caches `2026092472`.

---

## 1.7.59 — Perfil do usuário (hero + cards)

Página `/user/profile.php`: header com avatar em anel navy, nome em chip sólido, cards das seções com barra azul e lista limpa. Sem o “blocão” branco estreito.

Purge caches `2026092471`.

---

## 1.7.58 — Paginação + alfabeto (navy / cortadinho)

Paginação e barra Nome/Sobrenome: faixa com borda, ativo = **navy + texto branco** (não azul claro com texto escuro).

Purge caches `2026092470`.

---

## 1.7.57 — Horizontal = só /course/view.php

Moodle finge `pagetype=course-view-*` em backup/participantes/relatórios. Detecção agora é pela **URL** (`/course/view.php`). Demais páginas do curso → sidesheet vertical.

Purge caches `2026092469`.

---

## 1.7.56 — Horizontal só no course-view

Abas horizontais **somente** na homepage do curso (`course-view-*`). Reutilizar / participantes / config / atividades / admin → sidesheet **vertical**.

Purge caches `2026092468`.

---

## 1.7.55 — version bump (DB > disco)

Disco estava em 2464 com banco em 2466. Subiu para `2026092467`.

---

## 1.7.54 — Sidesheet: truncar labels longos

Itens do accordion (ex.: “Modelo de plano de aprendizado”) com `ellipsis` + `overflow-x: hidden` na rail — sem alargar o menu.

Purge caches `2026092464`.

---

## 1.7.53 — Gerenciar cursos: sidesheet de volta

`course-management` / `path-course` não são “estar no curso”. Horizontal só em `course`/`incourse` + `course-view` + `mod-*`. Gestão de categorias/cursos e admin voltam pro menu **vertical**.

Purge caches `2026092463`.

---

## 1.7.52 — Curso limpo: sem sidesheet (fallback CSS)

No **curso**: sidesheet proibida (pagelayout/pagetype/context). Menu só **horizontal** sob a navbar. Índice do curso fecha por padrão. CSS failsafe em `path-course` / `ceuma-in-course`. Admin mantém sidesheet.

Purge caches `2026092462` (tema + templates).

---

## 1.7.51 — Admin volta sidesheet; horizontal só no curso

Correção: horizontal era só pra curso; Administração / Painel / Meus cursos recuperam o menu lateral.

Purge caches `2026092461`.

---

## 1.7.50 — Curso: menu horizontal (sem sidesheet)

Dentro do **curso**: sidesheet some. Volta o menu secundário **horizontal** (Curso / Configurações / Participantes / …) sob a navbar. Sidesheet fica só no Painel / Meus cursos.

Purge caches `2026092460`.

---

## 1.7.49 — Título navbar: pega item ativo do menu

O nome no meio da navbar vem do item **ativo** do menu (Painel / Meus cursos / catálogo custom), não só de `$PAGE->heading` (que às vezes vem vazio).

Purge caches `2026092459` (templates + theme).

---

## 1.7.48 — Título da página no meio da navbar

Em páginas com menu no sidesheet (Painel, Meus cursos, catálogos custom): o nome da página aparece **centralizado na navbar** (não no conteúdo).

Purge caches `2026092458`.

---

## 1.7.47 — Separador do modo edição + some o título chip do Painel

- Barrinha antes da caneta/toggle na navbar
- Remove o chip de contexto (“Painel” / “Meus cursos” + engrenagem) no Painel e Meus cursos; conteúdo continua centralizado

Purge caches `2026092457`.

---

## 1.7.46 — Menu recolhido + Painel com sidesheet

- Ícones do menu **recolhido** maiores / sem corte (rail 88px)
- **Painel** ganha menu lateral (primary nav) + conteúdo **centralizado** (max ~1120px)

Purge caches `2026092456`.

---

## 1.7.45 — Backdrop na navegação rápida

Overlay escuro ao abrir quicknav (clique fora fecha). CSS de `.ceuma-quicknav-backdrop` que faltava.

Purge caches `2026092455`.

---

## 1.7.44 — Logo centrada no menu recolhido (sem corte)

Recolhido: some o nome **e** o hambúrguer; fica só a logo/mark **centrada** (sem cortar). Clique nela expande. Embaixo só as iniciais.

Purge caches `2026092454`.

---

## 1.7.43 — Edit = caneta + toggle; sidesheet colapsada = logo + iniciais

- Modo edição na navbar: **ícone caneta + switch** lado a lado
- Menu lateral: dá pra recolher (inclui admin); recolhido mostra só logo/mark e avatar (**DE**), sem nome
- Clique na logo quando recolhido **expande** de novo

Purge caches `2026092453`.

---

## 1.7.42 — Plugins = puzzle (data-key modules)

Admin “Plugins” no Moodle usa `data-key="modules"` / `#linkmodules` (não `plugins`). Ícone `fa-puzzle-piece` com `!important`.

Purge caches `2026092452`.

---

## 1.7.41 — Ícones Plugins + Atividades

- **Plugins** (admin): `fa-puzzle-piece` (`\f12e`)
- **Atividades** (`courseoverview`): `fa-file-lines` (`\f15c`)

Purge caches `2026092451`.

---

## 1.7.40 — Caneta centrada + cortada (off) / limpa (on)

Ícone do modo edição centrado no botão. Off = caneta com risco; on = caneta inteira (azul). Sem switch/barrinha.

Purge caches `2026092450`.

---

## 1.7.39 — Caneta de edição na navbar (ícone on/off)

Modo edição fica **sempre na navbar** (não na sidesheet). Ícone **pen** (off) ↔ **pen-to-square** (on, azul).

Purge caches `2026092449`.

---

## 1.7.38 — Userbar: avatar + nome + caneta de edição

Na sidesheet: **avatar + firstname/lastname** (truncate com `…`) e **modo edição como ícone de caneta** ao lado (não mais o switch com texto). Override `core/user_menu_metadata`.

Purge caches `2026092448`.

---

## 1.7.22 — Sidebar full-height (ao lado do navbar/footer)

Layout em colunas: `[menu lateral 100vh] | [navbar + content + footer]`.
Navbar e footer ficam **100% só da coluna do conteúdo**, não por cima do menu.

Purge caches `2026092432`.

---

## 1.7.21 — Menu lateral permanente (estilo CEUMA)

O menu do curso **não fica mais escondido** (sem FAB/modal).
Virou **sidesheet** fixa à esquerda: logo + itens com ícones + usuário embaixo.
Pode recolher (só ícones). No mobile abre com botão. Empurra o conteúdo.

AMD: `theme_ceuma/sidesheet`. Purge caches `2026092431`.

---

## 1.7.20 — Sem backdrop fantasma no Menu

Removido backdrop separado do menu do curso (escurecia a página cedo / na frente). Overlay só existe com o modal aberto (`hidden` + `display:none` no fechado). Clique fora do card fecha.

Purge caches `2026092430`.

---

## 1.7.19 — Menu (só ícone) + FAB bússola + submenus internos

- Título **Menu** (não “Menu do curso”)
- FAB hambúrguer só ícone; ao lado FAB bússola (navegação rápida), com gap
- Itens do modal com ícones + mais espaço
- Submenus abrem **dentro** do menu (acordeão), não flutuando

Purge caches `2026092429`.

---

## 1.7.18 — Menu curso flutuante + navegação rápida

- **Menu do curso:** fora da navbar — FAB no canto; abre **modal central** com os itens
- **Navegação rápida:** ícone bússola ao lado do sol — modal com recentes + atalhos (localStorage), dá pra adicionar página atual ou link custom

Purge caches `2026092428`.

---

## 1.7.17 — Menu do curso lateral (não barra horizontal)

Secondary nav (Página inicial / Configurações / …) virou **painel flutuante** à esquerda:
- botão “Menu do curso” ao lado do logo
- abre lateralmente, para acima do footer
- submenus / “Mais” abrem para a **direita** (não em cima do footer)

AMD: `theme_ceuma/secondarypanel`. Purge caches `2026092427`.

---

## 1.7.16 — Login split OXY (form | imagem)

Layout igual frontend_ofc: **esquerda** azul (título + card Login + footer Oxygeni), **direita** estátua/prédio (`pix/login_estatua.svg` + waves). Override `core/login_layout`.

Purge caches após `2026092426`.

---

## 1.7.15 — Footer estilo Oxygeni Hub

Layout: redes (X / Instagram / LinkedIn / WhatsApp) | copyright | logo `pix/logo_oxygeni.svg` (copiado de `frontend_ofc/src/assets`).

Purge caches após `2026092425`.

---

## 1.7.14 — Buscar: botão separado e mesma altura

**Problema:** lupa navy do `simplesearchform` / `input-group` passava por cima do input (cantos arredondados + margin negativa do Bootstrap) e ficava um pouco mais alta.

**Fix (`_forms.scss`):**
- `gap: 0.5rem` entre input e botão (sem join do input-group)
- altura fixa `2.45rem` nos dois
- botão submit/lupa `2.45rem` quadrado, navy, `position: static`
- clear/close absoluto só dentro do campo

Purge caches após atualizar `2026092424`.

---

## Por que o Moove funciona e o Ceuma quebrava

### 1. Pipeline SCSS (causa #1 do “não aplica”)

**Moove faz assim** (`theme/moove/lib.php`):

```text
_variables.scss  +  Boost preset  +  default.scss (@import dos módulos)
```

O `default.scss` mora em `scss/` e usa `@import "moove/navbar"` — o compilador resolve pelo **caminho de arquivo**, com `scss/` no include path.

**Ceuma errava assim:**

- Concatenar `post.scss` (com `@import`) no **meio de uma string** junto do Boost, ou
- Carregar Google Fonts com `@import url(...)` no pre-SCSS (scssphp do Moodle pode falhar → **fallback** para CSS do Boost)
- Inventar flex/CSS que brigava com o Boost (navbar sobreposta)

**Ceuma agora (v1.4.0):** igual Moove:

```text
scss/ceuma/_variables.scss
scss/default.scss
  → @import variables
  → @import ../../boost/scss/preset/default
  → @import general, navbar, drawers, footer, login
```

### 2. Navbar HTML

**Moove:** `<nav>` flat, sem `container-fluid` interno, itens filhos diretos.

**Ceuma errava:** `container-fluid` + `max-width` + flex custom → marca e menu no mesmo espaço (sobreposição).

**Ceuma agora:** navbar flat estilo Moove + tile “C” + secondary fixa.

### 3. Layouts

**Moove** só declara `base` + `frontpage` no `config.php`.  
Os outros layouts herdam do Boost (`file => drawers.php`), e o Moodle acha **primeiro** `theme/moove/layout/drawers.php`.

**Ceuma agora:** mesmo padrão (`base` + `login`), com `layout/drawers.php` e `layout/login.php` próprios que renderizam `theme_ceuma/drawers` / `theme_ceuma/login`.

### 4. Secondary navigation

**Moove:** secondary **dentro do navbar.mustache**, `position: fixed; top: 70px`.  
Body ganha classe `has-secondarynavigation` no `layout/drawers.php`.

**Ceuma agora:** igual — secondary no navbar + offset de página/drawers.

### 5. Content sheet

**Moove:** fundo cinza + `.main-inner` branco elevado; `full_header` **fora** do sheet.

**Ceuma agora:** igual, com tokens CEUMA.

---

## Estrutura atual (anotada)

```text
public/theme/ceuma/
├── version.php              # 1.7.0 / 2026092410
├── config.php               # parents=boost; layouts base+login
├── lib.php                  # pipeline SCSS estilo Moove
├── settings.php             # brandcolor, presets, raw SCSS
├── layout/
│   ├── drawers.php          # render theme_ceuma/drawers + has-secondarynavigation
│   └── login.php            # render theme_ceuma/login
├── templates/
│   ├── navbar.mustache      # flat + brand C + secondary
│   ├── drawers.mustache     # shell Moove
│   ├── footer.mustache
│   ├── login.mustache
│   └── core/
│       ├── full_header.mustache
│       └── login_panel.mustache
├── scss/
│   ├── default.scss         # ENTRYPOINT (como Moove)
│   ├── pre.scss / post.scss # deprecated (vazio)
│   └── ceuma/
│       ├── _variables.scss  # tokens CEUMA
│       ├── _general.scss
│       ├── _navbar.scss     # 70px + secondary 60px
│       ├── _drawers.scss
│       ├── _footer.scss
│       └── _login.scss
├── lang/en + pt_br/
├── classes/privacy/
└── pix/
```

---

## Checklist ao criar / depurar um tema Boost child

1. **Copiar o wiring do Moove**, não reinventar o Boost.
2. SCSS: `variables` → `default.scss` com `@import` de arquivo (não `@import` solto concatenado à toa).
3. **Nunca** colocar `@import url(https://fonts...)` no pre-SCSS sem testar compile.
4. Navbar: HTML flat (como Moove). Só depois pintar.
5. Secondary: no `navbar.mustache` + `has-secondarynavigation` no layout PHP.
6. Ter `layout/drawers.php` no tema filho mesmo se `config` só listar `base`.
7. Depois de mudar SCSS: **Purge all caches** (senão parece que “não aplica”).
8. Se o visual voltar ao Boost puro: SCSS falhou → olhar logs / Theme designer mode.

---

## Tokens CEUMA (fonte: Oxy `globals.css`)

| Token | Hex | Uso |
|-------|-----|-----|
| blue | `#0747DE` | primary, secondary bar, botões |
| navy | `#002C57` | footer, CTA login |
| tint | `#EBF3FF` | ativo |
| bg | `#EFEFEF` | canvas |
| surface | `#FDFDFD` | cards / navbar |
| text | `#383839` | corpo |
| muted | `#919192` | secundário |
| border | `#E6E6E6` | bordas |

---

## Histórico de versões

| Versão | O que aconteceu |
|--------|-----------------|
| 1.0 | Boost child básico (só tintas) — fraco |
| 1.1–1.2 | CSS custom agressivo; navbar não carregava (template Boost) |
| 1.3 | Shell Moove (secondary + sheet) mas SCSS/flex quebrados → sobreposição |
| 1.3.1 | Tentativa de flex forçado |
| **1.4.0** | Rebuild: pipeline + navbar + layouts **iguais ao Moove**, tokens CEUMA |
| **1.5.0** | Curso em cards (seções + atividades), ícones no menu primário/secundário e no índice |
| **1.5.1** | Login: remove card-dentro-de-card; forgot password student-friendly |
| **1.6.0** | Painel + cards maiores; selects pesquisáveis; tabelas; login card maior |
| **1.6.1** | Selects: enhancer em quase todos os `<select>` (não só os longos) |
| **1.7.0** | Visual mais fino; fundo claro; inputs; dark/light; checkbox→toggle |
| **1.7.1** | Fix: select enhancer não mexe em roles/grupos (participantes) |
| **1.7.2** | Fix: datepicker alinhado (não sobe pro canto); ignore selects de data |
| **1.7.3** | Bloco cinza (não branco); azul mais suave; select custom nos filtros |
| **1.7.4** | Sheet cinza mais visível; filtros com select CEUMA; secondary navy |
| **1.7.5** | Select custom também nas datas (dia/mês/ano/hora) sem quebrar calendário |
| **1.7.6** | Painel full-width; cards maiores; blocos brancos no canvas |
| **1.7.7** | Cards estilo Oxy (badge, meta, Ver detalhes / Abrir curso) |
| **1.7.8** | Shell Coursera: header/footer fixos; menu empurra; só content rola |
| **1.7.9** | Shell OXY-GRADES (flex); fundo claro; botões menos redondos; imagem no card |
| **1.7.10** | Menu compacto + cores iguais; scrollbar custom; secondary no fluxo |
| **1.7.11** | Modal “Ver detalhes” com atividades + progresso do curso |
| **1.7.12** | Fix scroll: #page overflow-y auto (admin/environment e páginas longas) |
| **1.7.13** | Capa no índice do curso; remove ícones do secondary (Notas); radius 6/8 |

### 1.7.13 — Índice do curso + nav

- Drawer do curso: imagem de capa + nome por cima
- Secondary nav sem ícones FA (Notas/admin limpo)
- Radius 6px / 8px

### 1.7.12 — Scroll quebrado

- Boost forçava `overflow-y: visible` no `#page.drawers`
- Shell agora usa `overflow-y: auto !important` em `#page` + `display: block` pra não travar flex

### 1.7.11 — Modal detalhes do curso

- Botão **Ver detalhes** abre modal Bootstrap
- WS `theme_ceuma_get_course_progress`: lista atividades, status e % geral
- Link **Abrir curso** no rodapé do modal

### 1.7.10 — Navbar + scroll

- Primary nav empacotado (sem espaço enorme entre itens)
- Texto/ícones na mesma cor cinza/navy (como Administração)
- Menu do curso (secondary) compacto no fluxo
- Scrollbar fina custom no content e drawers

### 1.7.9 — Visual OXY-GRADES

- Layout = `AdminLayout`: header/footer no fluxo, só content com `overflow-y`
- Canvas `#F9FAFB`, cards brancos, radius 4/6px
- Course cards com imagem de capa de novo + badges/meta/botões

### 1.7.8 — Layout shell

- Header (navbar + secondary) e footer fixos
- Drawer esquerdo/direito no fluxo (push) no desktop — sem overlay por cima do content
- Apenas `#page.drawers` tem scroll
- Sidebar branca com item ativo estilo Coursera (tint + barra azul)

### 1.7.7 — Cards Oxy no Painel

- Override `core_course/coursecard` + `block_myoverview/view-cards`
- Visual: faixa navy, badges verde/âmbar, título, Ler mais, grid Categoria/Código/Data, 2 botões outline
- SCSS `_coursecards.scss` (tokens Oxy)

### 1.7.6 — Painel

- `.main-inner` do dashboard em 100% (ignora limitedwidth / teto 1400px)
- Sem sheet cinza no meio — blocos brancos no fundo da página
- Grid de cursos fluido; 1 curso ≈ 360–420px (não carimbo no centro)

### 1.7.5 — Selects de data

- Dia / mês / ano / hora / minuto usam `.ceuma-ss--compact`
- Select nativo fica invisível mas mensurável (YUI alinha o calendário em `.one('select')`)
- CSS do datepicker não esconde mais o componente CEUMA

### 1.7.4 — Participantes: cinza + selects

- `.main-inner` e painéis internos em cinza (`#EBEDF0` / `#F3F4F6`) — sem ilhas brancas
- Secondary nav forçada navy; botões/links menos neon
- Select custom nos filtros (`Nenhum`/`Qualquer`/`Todos`, tipo de filtro); papéis/grupos da tabela continuam no autocomplete Moodle
- AMD `searchable` carrega independente do drawer

### 1.7.3 — Cores + filtros

- Sheet `.main-inner` cinza; secondary navy
- Select enhancer nos filtros (não nas células da tabela)

### 1.7.2 — Datepicker

YUI alinha o calendário no primeiro `select` do `.fdate_time_selector`. O enhancer CEUMA escondia esses selects → painel ia para (0,0).  
Agora: selects de data/hora ficam nativos + CSS do painel com z-index alto.

### 1.7.1 — Select de grupo/papel

O enhancer CEUMA escondia o `<select>` nativo do autocomplete/inplace editable → seletor de grupo/papel bugava.  
Agora ignora: autocomplete, tags, inplace editable, tabelas dinâmicas e página de participantes (exceto bulk action).

### 1.7.0 — Refino visual + dark mode

- Radius menor (6–8px): cards, botões, badges (não mais “bolha”)
- Fundo canvas `#F5F6F8` (mais leve)
- Inputs com hover/focus consistentes
- Checkbox vira **toggle switch**
- Toggle **claro/escuro** na navbar (`theme_ceuma_darkmode` + localStorage)

### 1.6.1 — Selects consistentes

Antes só virava “select com busca” se tivesse **≥7 opções** e classe `form-select`.  
Agora: todo `<select>` simples (≥2 opções) vira o componente CEUMA; campo **Pesquisar** aparece a partir de 5 opções.

### 1.6.0 — Painel / componentes

- Login: card `max-width: 34rem` (antes 26rem — “encolhido”)
- Course cards: grid `md-2 / xl-3` + imagem maior + badge categoria
- Selects: visual CEUMA; `theme_ceuma/searchable` (select ≥7 opções + dropdown longo com busca)
- Tabelas: header soft, hover tint, radius 14px

### ⚠️ Incidente: menu sumiu + `No define call for core/first`

**Causa:** o AMD `theme_ceuma/searchable` entrou no **combo** do `lib/requirejs.php` (produção junta TODOS os módulos AMD num arquivo só). A 1ª versão do JS usava `export` (ES module) **sem** `define()` → SyntaxError no combo inteiro → RequireJS quebra → some menu (`core/moremenu`), cards do painel, drawers, etc.

**Fix já no código:**
1. `amd/src/searchable.js` + `amd/build/searchable.min.js` só com `define([], function(){...})` (padrão Moodle clássico)
2. No `drawers.mustache`: carregar `theme_ceuma/searchable` **depois** do loader/drawer, com fail silencioso (não bloqueia o shell)

**O que limpar (você, no admin):**
1. Administração do site → **Desenvolver** → **Purge all caches** (ou Notificações após bump de versão)
2. Ctrl+F5 no browser
3. Se ainda falhar: apagar cache JS do moodledata (`localcache/requirejs/` e `cache/`) e purge de novo

**Regra:** nunca colocar `export`/`import` ES6 cru em AMD de tema sem passar pelo grunt do Moodle. Sempre `define([...], function(){ return { init }; })`.

### 1.5.1 — Login

**Causa do card duplo:** CSS pintava `.loginform` **e** `.login-form` (form filho) com borda/sombra.

**Fix:** um card só em `.loginform`; `.login-form` transparente.  
Forgot password (`#page-login-forgot_password`): intro card (renderer) + formulário no mesmo bloco visual, “ou” entre usuário/e-mail, link voltar ao login.

### 1.5.0 — experiência do aluno

Arquivo novo: `scss/ceuma/_course.scss`

- Seções do curso = **cards** (borda, radius 16px, header com badge azul + ícone)
- Atividades (modo aluno) = **mini-cards** com hover tint
- Menu topo / secondary = ícones Font Awesome por `href`
- Índice do curso (drawer) = pastas + item ativo tint

Purge caches após atualizar.

1. Administração → Notificações (instala/atualiza `2026092408`)
2. **Purge all caches**
3. Ctrl+F5
4. Conferir: login card largo; Painel com cards de curso maiores; selects/tabelas CEUMA

Se ainda falhar: ativar **Theme designer mode**, recarregar, inspecionar se o CSS da página contém `ceuma-brand-mark` / `ceuma-secondary`. Se não contiver → compile SCSS falhou (logs do PHP).
