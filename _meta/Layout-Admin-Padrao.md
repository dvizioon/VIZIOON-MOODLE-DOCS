# Layout admin padrão (azul)

Padrão visual/estrutural para páginas admin de plugins do time. Inspirado em:

- `mod/oxymsteams` → `layout/Header.php`, `layout/Footer.php`, `admin/index.php`
- `local_cataloggate` → `classes/output/page_header.php` + cards de gestão

Skill Cursor: `moodle-admin-layout` (em `.cursor/skills/` do workspace MOODLE).

---

## Paleta (cor geral = azul)

| Uso | Hex |
|-----|-----|
| Gradiente início | `#1d4ed8` |
| Gradiente fim / primary Bootstrap | `#0d6efd` |
| Borda superior footer | `#0f172a` |
| Texto muted | `#64748b` |
| Fundo card | `#ffffff` |

Legado oxymsteams usa roxo (`#4c1d95` → `#7c3aed`). **Plugins novos: só azul.**

---

## Estrutura de pastas

```text
layout/
  Header.php     # setup + render do hero
  Footer.php     # cards de rodapé
admin/
  index.php      # hub (grid de cards)
  *.php          # subpáginas (relatório, presets…)
css/style.css    # tokens --*-primary etc.
```

Em `local_`, páginas podem ficar na raiz (`pages.php`, `setup.php`) usando a mesma classe de header.

---

## Anatomia da página

1. Bootstrap Moodle (`config.php`, login, capability, `$PAGE`)
2. `*_setup_page([...])` **antes** de `$OUTPUT->header()`
3. `$OUTPUT->header()` → `*_render_header()`
4. Corpo (hub / form / tabela / KPIs)
5. `*_render_footer()` → `$OUTPUT->footer()`

### Hero

- Card full-bleed interno, gradiente 135°, ~110px
- Back pill claro à esquerda
- Ícone/logo + título + subtítulo
- Botões extras à direita (`btn-outline-light` ou `btn-light`)

### Hub

- `row` + `col-md-4`
- Card centralizado, ícone FA `text-primary`, CTA `btn-outline-primary`

### Footer

- 2–3 cards com borda superior slate e botão outline primary

---

## Exemplo mínimo de chamada

```php
meu_setup_page([
    'title'    => get_string('admin_panel', 'meu'),
    'subtitle' => get_string('pluginadministration', 'meu'),
    'back_url' => new moodle_url('/admin/settings.php', ['section' => 'modsettingmeu']),
    'bg_from'  => '#1d4ed8',
    'bg_to'    => '#0d6efd',
    'icon'     => 'fa-cogs',
]);
```

Detalhe de opções: comentário de cabeçalho em `oxymsteams_v5/layout/Header.php` (trocar cores).

---

## Checklist

- [ ] Capability na página
- [ ] Cores azuis (não roxo)
- [ ] Prefixo CSS = componente
- [ ] Strings em `lang/`
- [ ] `s()` em textos dinâmicos
- [ ] Hub ou conteúdo legível em mobile (`col-12` nos footers)
