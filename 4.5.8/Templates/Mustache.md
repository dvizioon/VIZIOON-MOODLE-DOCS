# Mustache no Moodle 4.5.8

Motor: biblioteca `lib/mustache`, embrulhada por `core\output\mustache_engine`. Quem monta o engine é `renderer_base::get_mustache()` em `lib/classes/output/renderer_base.php`.

O escape padrão é a função `s()` do Moodle. `{{nome}}` sai escapado. `{{{nome}}}` sai cru — só para HTML que o próprio PHP já limpou (`format_text`, never para texto digitado pelo aluno).

Não existe helper `{{#react}}` neste checkout. Esse helper é do 5.x.

## Onde o arquivo fica

```text
mod/forum/templates/big_search_form.mustache   →  mod_forum/big_search_form
lib/templates/loginform.mustache                →  core/loginform
admin/templates/settings.mustache               →  core_admin/settings
reportbuilder/templates/...                     →  core_reportbuilder/...
```

Regra do nome: `<frankenstyle>/<caminho sem .mustache>`, com barras. Template na raiz de um subsistema do core usa `core` ou `core_<subsistema>`.

Cache compilado: `$CFG->localcachedir/mustache/<revisão do tema>/<tema>/`. Trocar o template em produção não aparece até a revisão do tema mudar (purge caches ou `theme_get_revision()`).

## Chamada no PHP

```php
echo $OUTPUT->render_from_template('mod_forum/big_search_form', $data);
```

`$data` é `stdClass` ou array. Objeto que implementa `renderable` e `templatable` passa por `export_for_template(\renderer_base $output)` e o renderer chama o template sozinho.

## Helpers registrados no 4.5.8

Montados em `get_mustache()`:

| Helper | Classe | Uso |
|--------|--------|-----|
| `{{#str}} chave, componente {{/str}}` | `mustache_string_helper` | `get_string` |
| `{{#cleanstr}}` | `mustache_clean_string_helper` | string já limpa para atributo |
| `{{#quote}}` | `mustache_quote_helper` | aspas para JS |
| `{{#js}}` | `mustache_javascript_helper` | AMD no fim do template. Proibido aninhado (`disallowednestedhelpers`) |
| `{{#pix}} icon, componente, alt {{/pix}}` | `mustache_pix_helper` | ícone |
| `{{#shortentext}}` | `mustache_shorten_text_helper` | corta texto |
| `{{#userdate}}` | `mustache_user_date_helper` | data no fuso do usuário |
| `{{#config}}` | array | só as configs expostas ao JS |

Pragma `BLOCKS` está ligado (`{{< template }}`, `{{$ bloco }}`). Lambda rendering está desligado: o retorno de um helper não é renderizado de novo.

## Sintaxe que o motor aceita

```mustache
{{nome}}
{{{htmlpronto}}}

{{#temnota}}
  <span>{{nota}}</span>
{{/temnota}}
{{^temnota}}
  <span>-</span>
{{/temnota}}

{{#linhas}}
  <li>{{aluno}}</li>
{{/linhas}}

{{#str}} modulename, page {{/str}}
{{#pix}} icon, mod_page, {{#str}} pluginname, page {{/str}} {{/pix}}
```

`{{#secao}}` é verdade se o valor não é vazio, false, 0 ou lista vazia. Lista percorre. `{{! comentário }}` não sai no HTML.

## AMD a partir do template

```mustache
{{#js}}
require(['mod_forum/discussion'], function(D) {
    D.init({{quote}}{{id}}{{/quote}});
});
{{/js}}
```

O helper `js` não pode aparecer dentro de outro helper. O engine zera a saída se isso acontecer — é trava de XSS, não um bug do template.

## Referências

- [[4.5.8/Frontend/AMD]]
- [[4.5.8/Classes/Helper]]
