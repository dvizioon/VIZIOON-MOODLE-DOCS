# Sistema de Templates — Mustache

## Visão Geral

O Moodle usa **Mustache** como motor de templates. Mustache é uma linguagem de templates simples que separa lógica de apresentação. Os templates são renderizados no servidor e retornam HTML.

Ponto de montagem React (`{{#react}}`): [Frontend/React](../Frontend/React.md).

## Localização dos Templates

```
meu_plugin/
├── templates/
│   ├── view.mustache          # Template principal
│   ├── partials/
│   │   ├── header.mustache    # Partial (reutilizável)
│   │   └── footer.mustache
│   └── components/
│       └── button.mustache    # Componente
```

### Regras de Nomenclatura

- Usar `snake_case` para nomes
- Extensão: `.mustache`
- Organizar em subpastas: `partials/`, `components/`

## Sintaxe Básica

### Variáveis

```mustache
{{nome}}
{{#usuario}}Olá, {{nome}}!{{/usuario}}
```

### Tags Condicais

```mustache
{{#logado}}
    <p>Bem-vindo, {{nome}}!</p>
{{/logado}}

{{#admin}}
    <a href="{{url_admin}}">Painel Admin</a>
{{/admin}}
```

### Inversão Condicional

```mustache
{{#logado}}
    <p>Bem-vindo!</p>
{{/logado}}
{{^logado}}
    <p>Faça login</p>
{{/logado}}
```

### Listas

```mustache
{{#cursos}}
    <li>{{nome}} — {{professor}}</li>
{{/cursos}}
```

### Mustache HTML Escapado vs Raw

```mustache
{{#escapeado}}<script>alert('xss')</script>{{/escapeado}}
{{{bruto}}}<script>alert('xss')</script>{{{/bruto}}}
```

> **Atenção:** Use `{{{ }}}` apenas quando tiver certeza do conteúdo. Nunca use com dados do usuário.

### Comentários

```mustache
{{! Este é um comentário que não aparece no HTML }}
```

## Helpers do Moodle

### pix_icon — Ícones

```mustache
{{#pix}} icon, mod_meuplugin {{/pix}}
{{#pix}} i/edit, core {{/pix}}
```

### str — Strings de Idioma

```mustache
{{#str}} modulename, mod_meuplugin {{/str}}
{{#str}} name, core {{/str}}
```

###OUTPUT — Renderização

```mustache
{{#output}}heading, {{nome}}{{/output}}
```

### userdate — Datas

```mustache
{{#userdate}} {{timestamp}}, {{#str}} strftimedate, core {{/str}} {{/userdate}}
```

### link — Links

```mustache
{{#link}} view.php?id={{cmid}} {{/link}}
```

## Chamando Templates no PHP

### Renderização Simples

```php
$dados = [
    'nome' => 'João Silva',
    'cursos' => [
        ['nome' => 'Matemática', 'nota' => 8.5],
        ['nome' => 'Português', 'nota' => 7.2],
    ],
    'admin' => true,
];

echo $OUTPUT->render_from_template('mod_meuplugin/view', $dados);
```

### Com Renderer Customizado

```php
// Em classes/output/renderer.php
class renderer extends plugin_renderer_base {
    public function render_view(stdClass $dados) {
        return $this->render_from_template('mod_meuplugin/view', (array) $dados);
    }
}

// Uso
$output = $PAGE->get_renderer('mod_meuplugin');
echo $output->render_view($dados);
```

## Exemplo Completo

### Template: templates/view.mustache

```mustache
<div class="meuplugin-view">
    <div class="card">
        <div class="card-header">
            <h3>{{#pix}} icon, mod_meuplugin {{/pix}} {{nome}}</h3>
        </div>
        
        <div class="card-body">
            {{#tem_descricao}}
                <p class="lead">{{{descricao}}}</p>
            {{/tem_descricao}}
            
            <div class="row">
                {{#cursos}}
                <div class="col-md-6">
                    <div class="card mb-3">
                        <div class="card-body">
                            <h5 class="card-title">{{nome}}</h5>
                            <p class="card-text">
                                {{#str}} professor, mod_meuplugin {{/str}}: {{professor}}
                            </p>
                            <p class="card-text">
                                <small class="text-muted">
                                    {{#userdate}} {{data_inicio}}, {{#str}} strftimedate, core {{/str}} {{/userdate}}
                                </small>
                            </p>
                        </div>
                    </div>
                </div>
                {{/cursos}}
            </div>
            
            {{^cursos}}
                <div class="alert alert-info">
                    {{#str}} nocursos, mod_meuplugin {{/str}}
                </div>
            {{/cursos}}
        </div>
        
        <div class="card-footer">
            <a href="{{url_voltar}}" class="btn btn-secondary">
                {{#pix}} i/arrowleft, core {{/pix}} {{#str}} voltar, mod_meuplugin {{/str}}
            </a>
            
            {{#pode_editar}}
            <a href="{{url_editar}}" class="btn btn-primary float-right">
                {{#pix}} i/edit, core {{/pix}} {{#str}} editar, core {{/str}}
            </a>
            {{/pode_editar}}
        </div>
    </div>
</div>
```

### PHP Controller: view.php

```php
<?php
require_once('../../config.php');
require_once($CFG->dirroot . '/mod/meuplugin/lib.php');

$id = required_param('id', PARAM_INT);
$cm = get_coursemodule_from_id('meuplugin', $id, 0, false, MUST_EXIST);
$course = $DB->get_record('course', ['id' => $cm->course], '*', MUST_EXIST);
$meuplugin = $DB->get_record('meuplugin', ['id' => $cm->instance], '*', MUST_EXIST);

require_course_login($course, true, $cm);

$context = context_module::instance($cm->id);

// Dados para o template
$dados = [
    'nome' => $meuplugin->name,
    'descricao' => format_text($meuplugin->description, $meuplugin->descriptionformat),
    'tem_descricao' => !empty($meuplugin->description),
    'cursos' => $DB->get_records('meuplugin_cursos', ['meupluginid' => $meuplugin->id]),
    'url_voltar' => new moodle_url('/course/view.php', ['id' => $course->id]),
    'url_editar' => new moodle_url('/mod/meuplugin/edit.php', ['id' => $cm->id]),
    'pode_editar' => has_capability('mod/meuplugin:edit', $context),
];

// Renderizar
$PAGE->set_url('/mod/meuplugin/view.php', ['id' => $cm->id]);
$PAGE->set_title($course->shortname . ': ' . $meuplugin->name);
$PAGE->set_heading($meuplugin->name);

echo $OUTPUT->header();
echo $OUTPUT->render_from_template('mod_meuplugin/view', $dados);
echo $OUTPUT->footer();
```

## Partials (Templates Parciais)

### templates/partials/header.mustache

```mustache
<div class="meuplugin-header">
    <h2>{{titulo}}</h2>
    {{#subtitulo}}<p class="text-muted">{{subtitulo}}</p>{{/subtitulo}}
</div>
```

### Uso

```mustache
{{> mod_meuplugin/partials/header }}
```

Ou com dados:

```mustache
{{> mod_meuplugin/partials/header titulo="Meu Título" subtitulo="Subtítulo" }}
```

## Layout Templates

### templates/layout.mustache

```mustache
<div class="meuplugin-layout">
    {{> mod_meuplugin/partials/header }}
    
    <div class="meuplugin-content">
        {{{conteudo}}}
    </div>
    
    {{> mod_meuplugin/partials/footer }}
</div>
```

## Renderers

### Definindo um Renderer

```php
// classes/output/renderer.php
namespace mod_meuplugin\output;

defined('MOODLE_INTERNAL') || die();

class renderer extends \plugin_renderer_base {
    
    public function render_view(\mod_meuplugin\output\view $data) {
        return $this->render_from_template('mod_meuplugin/view', $data->export_for_template($this));
    }
    
    public function render_from_template($template, $data) {
        return parent::render_from_template($template, $data);
    }
}
```

### Renderable

```php
// classes/output/view.php
namespace mod_meuplugin\output;

defined('MOODLE_INTERNAL') || die();

class view implements \renderable {
    public $instance;
    public $course;
    public $cm;
    
    public function __construct($instance, $course, $cm) {
        $this->instance = $instance;
        $this->course = $course;
        $this->cm = $cm;
    }
    
    public function export_for_template(\renderer_base $output) {
        return [
            'nome' => $this->instance->name,
            'descricao' => format_text($this->instance->description, $this->instance->descriptionformat),
            'cursos' => $this->get_cursos(),
            'url_voltar' => new \moodle_url('/course/view.php', ['id' => $this->course->id]),
        ];
    }
    
    private function get_cursos() {
        global $DB;
        return $DB->get_records('meuplugin_cursos', ['meupluginid' => $this->instance->id]);
    }
}
```

### Usando Renderer

```php
// Em view.php
$output = $PAGE->get_renderer('mod_meuplugin');
$view = new \mod_meuplugin\output\view($meuplugin, $course, $cm);
echo $output->render($view);
```

## Boas Práticas

1. **Não colocar lógica complexa nos templates** — Use PHP para preparar dados
2. **Usar partials para componentes reutilizáveis**
3. **Escapar HTML do usuário** — Nunca usar `{{{ }}}` com dados do usuário
4. **Separar templates por funcionalidade**
5. **Usar classes CSS do Bootstrap** (Boost é o tema padrão)
6. **Documentar variáveis do template** com comentários

## Referências

- [[5.2/Plugins/Criar]] — Criação de plugins
- [[Base]] — Estrutura geral
- [[Plugins/Exemplos]] — Exemplos reais
