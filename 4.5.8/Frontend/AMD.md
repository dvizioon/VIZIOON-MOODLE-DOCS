# JavaScript no Moodle 4.5.8 — AMD

O front desta versão é **RequireJS (AMD)** mais Mustache. Não há React no core, não há `<script type="importmap">`, não há `react_autoinit` e não há helper `{{#react}}`. Esses pontos aparecem nas notas do 5.2 porque aquele código já está na linha 5.x. Copiar um componente React do 5.2 para este 4.5.8 não monta.

YUI 2.9.0 e 3.18.1 ainda são declarados em `lib/setup.php` (`$CFG->yui2version`, `$CFG->yui3version`). Módulo novo não usa YUI. O que resta está em `lib/yui` e em alguns `*/yui` antigos (`course/yui`, `enrol/yui`).

## Onde o arquivo mora

```text
mod/forum/amd/src/discussion.js     fonte
mod/forum/amd/build/discussion.min.js   o que o browser pede
```

Nome do módulo: `mod_forum/discussion` (sem `.js`). Core: `lib/amd/src/ajax.js` vira `core/ajax`.

O endpoint que entrega o arquivo é `lib/requirejs.php` (`lib/javascript.php` e `lib/jslib.php` participam da página). `$PAGE->requires` em `lib/outputrequirementslib.php` escreve o `require()` no rodapé.

## Chamar do PHP

```php
$PAGE->requires->js_call_amd('mod_forum/discussion', 'init', [$discussionid]);
```

O módulo devolve um objeto. `init` é a função exportada:

```javascript
define(['jquery', 'core/ajax', 'core/notification', 'core/str'], function($, Ajax, Notification, Str) {
    var init = function(discussionid) {
        Ajax.call([{
            methodname: 'mod_forum_get_discussion_posts',
            args: { discussionid: discussionid },
            done: function(response) {},
            fail: Notification.exception
        }]);
    };
    return { init: init };
});
```

`core/ajax` só chama função com `'ajax' => true` em `db/services.php`, na sessão do usuário. Não usa token de webservice.

Módulos do core que todo plugin usa: `core/ajax`, `core/str`, `core/notification`, `core/modal`, `core/templates`, `core/prefetch`, `core/form-autocomplete`.

## Build

Na raiz há `Gruntfile.js` e `package.json`.

```bash
npx grunt amd
```

Sem o `amd/build/*.min.js`, a página em produção (com `$CFG->jsrev` e cache de JS) não acha o módulo. Em debug de desenvolvedor o Moodle pode servir `amd/src` direto; não conte com isso fora do `DEBUG_DEVELOPER`.

## O que não fazer neste 4.5.8

- Não empacotar React à parte e apontar para `@moodle/lms/...`. Esse specifier não existe aqui.
- Não colocar `<script src>` solto no `view.php`. O caminho é AMD, para o Moodle controlar ordem, idioma e cache.
- jQuery ainda entra como dependência AMD (`jquery`). Código novo do core prefere `core/ajax` e DOM sem plugin jQuery novo.

## Referências

- [[4.5.8/Templates/Mustache]]
- [[4.5.8/WebServices/Criar]]
