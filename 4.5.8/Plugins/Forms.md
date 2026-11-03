# Formulários de plugin — Moodle 4.5.8

Três camadas que se confundem:

| Camada | Arquivo / classe | Onde aparece |
|--------|------------------|--------------|
| Form genérico | `moodleform` (`lib/formslib.php`) | Qualquer página PHP do plugin |
| Form de **atividade** | `moodleform_mod` → `mod_<nome>_mod_form` em `mod_form.php` | Adicionar/editar atividade (`course/modedit.php`) |
| Form de **instância de bloco** | `block_edit_form` → `block_<nome>_edit_form` em `edit_form.php` | Configurar bloco na página |
| Form de **admin** | `admin_setting_*` em `settings.php` | Árvore de administração — ver [[4.5.8/Plugins/Settings]] |

Checkout: `4.5.8/`. Exemplos vivos: `mod/page/mod_form.php`, `blocks/html/edit_form.php`.

---

## 1. `moodleform` (base)

```php
require_once($CFG->libdir . '/formslib.php');

class local_meu_form extends moodleform {
    public function definition() {
        $mform = $this->_form;

        $mform->addElement('header', 'general', get_string('general'));
        $mform->addElement('text', 'name', get_string('name'), ['size' => 48]);
        $mform->setType('name', PARAM_TEXT);           // obrigatório em todo campo
        $mform->addRule('name', null, 'required', null, 'client');
        $mform->setDefault('name', 'valor');

        $mform->addElement('select', 'mode', get_string('mode', 'local_meu'), [
            'a' => 'A', 'b' => 'B',
        ]);
        $mform->addElement('advcheckbox', 'enabled', get_string('enabled', 'local_meu'));
        $mform->addElement('editor', 'body', get_string('body', 'local_meu'), null, [
            'maxfiles' => EDITOR_UNLIMITED_FILES,
            'context'  => $this->_customdata['context'],
        ]);
        $mform->setType('body', PARAM_RAW);

        $this->add_action_buttons(true, get_string('savechanges'));
    }

    public function validation($data, $files) {
        $errors = parent::validation($data, $files);
        if (($data['name'] ?? '') === 'admin') {
            $errors['name'] = get_string('invalidname', 'local_meu');
        }
        return $errors;
    }
}
```

Ciclo na página:

```php
$mform = new local_meu_form(null, ['context' => $context]);
if ($mform->is_cancelled()) {
    redirect($returnurl);
}
if ($data = $mform->get_data()) {
    // gravar…
    redirect($returnurl);
}
echo $OUTPUT->header();
$mform->display();
echo $OUTPUT->footer();
```

Elementos comuns: `text`, `textarea`, `editor`, `select`, `autocomplete`, `advcheckbox`, `date_time_selector`, `filemanager`, `filepicker`, `hidden`, `html`, `static`, `header`, `submit`.

Dependências de UI: `$mform->hideIf('campo', 'outro', 'eq', 'valor')`, `$mform->disabledIf(...)`.

Dados extras no construtor: segundo argumento vira `$this->_customdata`.

---

## 2. `mod_form.php` — atividade (`moodleform_mod`)

Classe base: `course/moodleform_mod.php`. O core instancia `mod_<modname>_mod_form` a partir de `mod/<mod>/mod_form.php`.

### Esqueleto (baseado em `mod/page`)

```php
defined('MOODLE_INTERNAL') || die();
require_once($CFG->dirroot . '/course/moodleform_mod.php');

class mod_page_mod_form extends moodleform_mod {
    public function definition() {
        $mform = $this->_form;

        $mform->addElement('header', 'general', get_string('general', 'form'));
        $mform->addElement('text', 'name', get_string('name'), ['size' => 48]);
        $mform->setType('name', PARAM_TEXT);
        $mform->addRule('name', null, 'required', null, 'client');

        // Intro padrão (editor + “exibir descrição na página do curso”).
        $this->standard_intro_elements();

        // Campos do SEU módulo.
        $mform->addElement('header', 'contentsection', get_string('contentheader', 'page'));
        $mform->addElement('editor', 'page', get_string('content', 'page'), null, /* options */);
        $mform->addRule('page', get_string('required'), 'required', null, 'client');

        // Visibilidade, ID number, grupos, conclusão, restrição, notas…
        $this->standard_coursemodule_elements();

        // Botões “Salvar e mostrar” / “Salvar e voltar”.
        $this->add_action_buttons();
    }

    /** Carrega draft areas / deserializa options antes de exibir. */
    public function data_preprocessing(&$defaultvalues) {
        // Ex.: file_prepare_draft_area para o editor 'page'.
    }

    /** Opcional: validação extra. */
    public function validation($data, $files) {
        return parent::validation($data, $files);
    }
}
```

### Métodos da base que importam

| Método | Função |
|--------|--------|
| `standard_intro_elements($label?)` | Campo `introeditor` (+ `showdescription` se o feature permitir) |
| `standard_coursemodule_elements()` | CM completo — **não pular** ou o save quebra partes do cm |
| `add_action_buttons()` | Dois submits padrão do modedit |
| `data_preprocessing(&$defaultvalues)` | Preparar defaults (arquivos, serialize) |
| `definition_after_data()` | Ajustes depois dos defaults aplicados |
| `$this->context` / `$this->current` / `$this->course` | Contexto, registro atual, curso |

Features do módulo (`<mod>_supports` / `FEATURE_*`) ligam pedaços do form (conclusão, nota, etc.).

### O que o form grava

`course/modedit.php` → `add_moduleinfo` / `update_moduleinfo` em `course/modlib.php`:

1. Chama `*_add_instance` / `*_update_instance` do `lib.php` com o `$data` do form.
2. O plugin grava a tabela `{page}` (ou similar).
3. O core grava `course_modules` e a seção.

Campos do editor costumam chegar como array `['text','format','itemid']` — o `add_instance` converte e chama `file_save_draft_area_files`.

---

## 3. Bloco — `edit_form.php` (`block_edit_form`)

Base: `blocks/edit_form.php` (estende `\core_form\dynamic_form` neste 4.5.8). Cada bloco pode ter `blocks/<nome>/edit_form.php`:

```php
class block_html_edit_form extends block_edit_form {
    protected function specific_definition($mform) {
        $mform->addElement('header', 'configheader', get_string('blocksettings', 'block'));

        // Prefixo config_ → vira propriedade em $this->config do bloco.
        $mform->addElement('text', 'config_title', get_string('configtitle', 'block_html'));
        $mform->setType('config_title', PARAM_TEXT);

        $mform->addElement('editor', 'config_text', get_string('configcontent', 'block_html'), null, [
            'maxfiles' => EDITOR_UNLIMITED_FILES,
            'noclean'  => true,
            'context'  => $this->block->context,
        ]);
        $mform->setType('config_text', PARAM_RAW);
    }

    /** Mostrar o form já na hora de adicionar o bloco. */
    public static function display_form_when_adding(): bool {
        return true;
    }
}
```

Regras:

- Campos da instância: prefixo **`config_`**. Viram `$this->config->title`, `$this->config->text` em `block_<nome>`.
- Campos de região/peso/visível: a base `block_edit_form` já cria; não reimplemente.
- Acesso ao bloco: `$this->block` (instância `block_base`).
- Override `set_data` se precisar de draft area (como `block_html`).

Sem `edit_form.php`, o bloco só tem as opções padrão de aparência/região.

---

## 4. Outros forms por tipo

| Tipo | Form típico |
|------|-------------|
| `local_` / `tool_` | `moodleform` em `classes/form/*.php` + página própria |
| `enrol_` | Forms em `classes/` + UI de método de matrícula |
| `auth_` | Em geral só `settings.php` (admin); tela de login é do core |
| `format_` | Pode ter forms em `classes/output` / edit section |
| `theme_` | Quase tudo via `settings.php` + customizer; raro `moodleform` |
| `qtype_` | `edit_<qtype>_form.php` estendendo form de questão |

Página admin “solta” (não `admin_setting`): `admin_externalpage` aponta para um PHP que usa `moodleform` — padrão comum em `tool_` e `local_`.

---

## 5. Checklist rápido de form

- [ ] Todo elemento com `setType(..., PARAM_*)`
- [ ] `addRule` / `validation()` para regras de negócio
- [ ] `mod_`: `standard_intro_elements` + `standard_coursemodule_elements` + `add_action_buttons`
- [ ] `block_`: campos `config_*` em `specific_definition`
- [ ] Editor/arquivo: draft area (`file_prepare_draft_area` / `file_save_draft_area_files`)
- [ ] Cancel → `redirect`; sucesso → `redirect` com notificação
- [ ] Strings em `lang/`, não hardcoded

## Referências

- [[4.5.8/Plugins/Settings]]
- [[4.5.8/Plugins/Criar]]
- [[4.5.8/Course/Mod]]
- [[4.5.8/Classes/Helper]]
- [[4.5.8/Seguranca/Funcoes]]
