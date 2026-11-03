---
name: moodle-admin-layout
description: >-
  Builds Moodle plugin admin UI with blue gradient header, hub card grid, and
  footer cards (OxyMsTeams/CatalogGate pattern). Use when creating admin pages,
  layout/Header.php, layout/Footer.php, hub de cards, or UI azul do plugin.
---

# Moodle admin layout (azul)

## Tokens

`bg_from` `#1d4ed8` · `bg_to` / primary `#0d6efd` · border `#0f172a`  
Sem roxo `#4c1d95` em plugin novo.

## Estrutura

```text
layout/Header.php   # {comp}_setup_page + {comp}_render_header
layout/Footer.php
admin/index.php     # hub cards
css/style.css
```

## Ciclo

```php
meu_setup_page([
    'title' => ..., 'subtitle' => ...,
    'back_url' => ..., 'bg_from' => '#1d4ed8', 'bg_to' => '#0d6efd',
]);
echo $OUTPUT->header();
echo meu_render_header();
// hub: row/col-md-4 cards, fa text-primary, btn-outline-primary
echo meu_render_footer();
echo $OUTPUT->footer();
```

## Refs

- Spec: `_meta/Layout-Admin-Padrao.md`
- Código: `PLUGINS - DESENVOLVIDOS/.../oxymsteams_v5/layout/`, `cataloggate/classes/output/page_header.php`
- Detalhe: [reference.md](reference.md)
