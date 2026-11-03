# Formulários de plugin — Moodle 5.2

O contrato é o **mesmo** do [[4.5.8/Plugins/Forms|4.5.8]]: `moodleform`, `moodleform_mod` + `mod_form.php`, `block_edit_form` + `edit_form.php` com `config_*`.

Confirme paths no seu checkout (`lib/formslib.php` vs `public/lib/...`). Classes e nomes de arquivo não mudaram na prática do plugin author.

## Atividade — `mod_form.php`

```php
require_once($CFG->dirroot . '/course/moodleform_mod.php');

class mod_task_mod_form extends moodleform_mod {
    public function definition() {
        $mform = $this->_form;

        $mform->addElement('header', 'general', get_string('general', 'form'));
        $mform->addElement('text', 'name', get_string('name'), ['size' => 48]);
        $mform->setType('name', PARAM_TEXT);
        $mform->addRule('name', null, 'required', null, 'client');

        $this->standard_intro_elements();
        // campos do módulo…
        $this->standard_coursemodule_elements();
        $this->add_action_buttons();
    }
}
```

## Bloco — `edit_form.php`

```php
class block_meu_edit_form extends block_edit_form {
    protected function specific_definition($mform) {
        $mform->addElement('text', 'config_title', get_string('configtitle', 'block_meu'));
        $mform->setType('config_title', PARAM_TEXT);
    }
}
```

## Local / tool — `moodleform` próprio

Página PHP + classe em `classes/form/`. Ciclo: `is_cancelled` → `get_data` → `display`.

## Settings de site

Não é form de instância: [[5.2/Plugins/Settings]].

## Referências

- [[4.5.8/Plugins/Forms]] (detalhe completo + checklist)
- [[5.2/Plugins/Criar]]
- [[5.2/Plugins/Settings]]
- [[5.2/Seguranca/Funcoes]]
