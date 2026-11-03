# React dentro do Moodle 5.2

O Moodle 5.2 já sobe **React 19** na página. Não é preciso CDN, `create-react-app` nem um segundo React. O browser importa ESM pelo **import map** do core e o `react_autoinit` monta o componente no HTML.

O tema Ceuma e a maior parte dos plugins antigos continuam em **AMD** (`amd/src` + Mustache). React é outro caminho: use quando a tela é uma app (catálogo, editor, diagrama), não para um botão ou um ajuste de CSS.

## Como a página sobe

No `<head>`, o core imprime:

1. `<script type="importmap">` com `react`, `react-dom` e o prefixo `@moodle/lms/`.
2. `<script type="module">import "@moodle/lms/core/react_autoinit";</script>`.

O autoinit (`public/lib/js/esm/src/react_autoinit.ts`) faz isto:

- procura `[data-react-component]`
- o valor tem de ser `@moodle/lms/<componente>/<ficheiro>`
- lê `data-react-props` (JSON)
- `import()` dinâmico e monta o **export default**
- um `MutationObserver` monta conteúdo que chega depois (AJAX / fragment)

`createRoot` fica em `@moodle/lms/core/mount` (`mountReactApp` / `unmountReactApp`). Não chame `createRoot` à parte se o ponto de montagem já tem `data-react-component`.

## Onde o arquivo mora

```text
public/<tipo>/<plugin>/js/esm/build/<nome>.js
```

| Specifier | Arquivo |
|-----------|---------|
| `@moodle/lms/local_cataloggate/catalog` | `public/local/cataloggate/js/esm/build/catalog.js` |
| `@moodle/lms/block_relator/editor` | `public/blocks/relator/js/esm/build/editor.js` |
| `@moodle/lms/core/react_autoinit` | `public/lib/js/esm/build/react_autoinit.js` |
| `react` / `react-dom` | `public/lib/js/bundles/react/` e `react-dom/` |

O mapa está em `core\output\requirements\import_map`. O specifier `@moodle/lms/<component>/<modulo>` vira `<dir do plugin>/js/esm/build/<modulo>.js`.

## Contrato do módulo

Export **default** de um function component. Props vêm do JSON do HTML.

```javascript
import {createElement as h, useState} from "react";

export default function MeuPainel(props) {
    const titulo = (props && props.titulo) || "";
    const [n, setN] = useState(0);
    return h("button", {type: "button", onClick: () => setN(n + 1)}, titulo + " " + n);
}
```

Importe `react` e `react-dom` pelos nomes do import map. Não empacote outra cópia do React dentro do plugin: o Relator deixa React **external** no build do React Flow exatamente por isso.

Neste checkout, o CatalogGate escreve o componente com `createElement` direto no `js/esm/build/`. Se usar JSX, compile **para esse mesmo arquivo** e deixe `react` / `react-dom` de fora do bundle.

## Mustache

Helper `{{#react}}` em `core\output\mustache_react_helper`. O JSON vai no início da seção; o HTML de dentro é fallback (aparece até o React montar, e fica se o JS falhar).

```mustache
{{#react}}
{
    "component": "@moodle/lms/local_meuplugin/painel",
    "props": {
        "titulo": "{{titulo}}",
        "courseid": {{courseid}}
    },
    "id": "meu-painel",
    "class": "meu-painel"
}
<p>Carregando…</p>
{{/react}}
```

Isso vira:

```html
<div id="meu-painel" class="meu-painel"
     data-react-component="@moodle/lms/local_meuplugin/painel"
     data-react-props='{"titulo":"...","courseid":2}'>
    <p>Carregando…</p>
</div>
```

`data-react-props` é JSON em aspas simples. O helper já faz o encode. Props são strings/números/arrays/objetos; nada de função.

## PHP (sem Mustache)

Mesmo contrato, como o CatalogGate em `local/cataloggate/classes/renderer.php`:

```php
$json = json_encode($props, JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT | JSON_UNESCAPED_UNICODE);
echo \html_writer::div($fallbackhtml, 'meu-painel', [
    'data-react-component' => '@moodle/lms/local_meuplugin/painel',
    'data-react-props' => $json,
]);
```

O autoinit já está no rodapé de toda página. Não registre AMD para montar isso.

## Bundles do React (uma vez no site)

React 19 não vem versionado em `lib/js/bundles/` até alguém rodar o script do core. Na raiz do Moodle:

```bash
npm install
# ou só:
npm run update-react
```

Isso baixa os bundles ESM (`scripts/update-react-bundle.mjs`) para `public/lib/js/bundles/react` e `react-dom`. Sem esses arquivos, `import "react"` quebra no browser.

Modo desenvolvedor (`$CFG->jsrev = -1`, cache JS desligado) usa o `.development.js` quando existe, com aviso melhor no console.

## AMD continua válido

| | AMD | React ESM |
|--|-----|-----------|
| Pasta | `amd/src/*.js` → `amd/build/*.min.js` | `js/esm/build/*.js` |
| Loader | `require(['theme_ceuma/menunav'], …)` | import map + `<script type="module">` |
| Uso | tema, menus, toggles, modais | app com estado |
| Build | `grunt amd` | o arquivo em `build/` já é o que o browser carrega |

Não misture os dois no mesmo botão. Um ponto de montagem React, o resto da página pode continuar Mustache/AMD.

## Exemplos neste repositório

- **CatalogGate** — `public/local/cataloggate/js/esm/build/catalog.js`. Um arquivo, `createElement`, props do PHP, fallback Mustache nos cards.
- **Relator** — vários módulos `@moodle/lms/block_relator/*`. React Flow é bundle do plugin (`npm run build` em `public/blocks/relator`); React do core fica de fora.

## Checklist

1. Componente em `js/esm/build/<nome>.js` com `export default function`.
2. HTML com `data-react-component="@moodle/lms/<component>/<nome>"`.
3. Props em `data-react-props` (JSON).
4. `npm run update-react` se `lib/js/bundles/react` não existir.
5. Sem segundo React, sem CDN, sem `require()` AMD para o mesmo root.
