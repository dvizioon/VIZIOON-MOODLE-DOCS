# Helper Classes e Funções — Moodle 5.2

## debugging() — Função de Debug

### Uso

```php
// Debug simples
debugging('Mensagem de debug');

// Debug com nível
debugging('Mensagem importante', DEBUG_DEVELOPER);
debugging('Erro normal', DEBUG_MINIMAL);
debugging('Aviso', DEBUG_NORMAL);
```

### Níveis de Debug

| Nível | Constante | Quando usar |
|-------|-----------|-------------|
| 0 | `DEBUG_NONE` | Sem debug |
| 1 | `DEBUG_MINIMAL` | Erros apenas |
| 5 | `DEBUG_NORMAL` | Warnings |
| 10 | `DEBUG_ALL` | Tudo |
| 100 | `DEBUG_DEVELOPER` | Desenvolvimento |

### Exemplo

```php
function minha_funcao($param) {
    debugging('minha_funcao() chamada com: ' . $param, DEBUG_DEVELOPER);
    
    if (empty($param)) {
        debugging('Parâmetro vazio!', DEBUG_MINIMAL);
        return false;
    }
    
    // ...
}
```

## print_error() e moodle_exception

### print_error() (Legado)

```php
// Erro simples
print_error('Erro ao salvar registro');

// Erro com parâmetros
print_error('error_nosuchuser', 'moodle', '', $userinput);

// Erro com debug
print_error('Erro interno', '', '', null, 'Detalhes do erro');
```

### moodle_exception (Recomendado)

```php
// Lançar exceção
throw new moodle_exception(
    'error_nosuchuser',    // Código da string
    'moodle',              // Componente
    '',                    // URL (opcional)
    $userinput             // Parâmetros para a string
);

// Exemplo em um controller
if (!$record = $DB->get_record('meu_plugin', ['id' => $id])) {
    throw new moodle_exception('notfound', 'mod_meuplugin');
}

// Com parâmetros
throw new moodle_exception(
    'error_invalidparam',
    'mod_meuplugin',
    '',
    ['param' => 'nome', 'value' => $value]
);
```

### Criando Exceções Customizadas

```php
<?php
namespace mod_meuplugin\exception;

use moodle_exception;

defined('MOODLE_INTERNAL') || die();

class validation_error extends moodle_exception {
    public function __construct($errorcode, $a = null) {
        parent::__construct($errorcode, 'mod_meuplugin', '', $a);
    }
}

// Uso
throw new validation_error('error_nosuchuser', $userinput);
```

## require_login() e require_capability()

### require_login()

```php
// Login básico
require_login();

// Login no curso
require_login($courseid);

// Login no curso com módulo
require_login($course, true, $cm);

// Login com sessão
require_login($course, false, $cm, false, ['login' => true]);
```

### require_capability()

```php
// Verificar capacidade
require_capability('mod/meuplugin:edit', $context);

// Verificar e redirecionar se não tiver
if (!has_capability('mod/meuplugin:edit', $context)) {
    redirect(new moodle_url('/'));
}

// Verificar capacidade com mensagem customizada
require_capability('mod/meuplugin:delete', $context, '', 'Você não tem permissão para deletar.');
```

### has_capability()

```php
// Verificar sem morrer
if (has_capability('mod/meuplugin:edit', $context)) {
    // Pode editar
}

// Verificar para usuário específico
if (has_capability('mod/meuplugin:view', $context, $userid)) {
    // Pode visualizar
}

// Listar capacidades do usuário
$capabilities = get_user_capabilities($context, $userid);
```

### Contextos

```php
// Contexto do sistema
$context = context_system::instance();

// Contexto de curso
$context = context_course::instance($courseid);

// Contexto de módulo
$context = context_module::instance($cmid);

// Contexto de bloco
$context = context_block::instance($blockid);
```

## $OUTPUT — Sistema de Renderização

### Método Principais

```php
global $OUTPUT;

// Cabeçalho e rodapé
echo $OUTPUT->header();
echo $OUTPUT->footer();

// Títulos
echo $OUTPUT->heading('Título');
echo $OUTPUT->heading('Subtítulo', 2);
echo $OUTPUT->heading_with_para('Título com parágrafo');

// Caixas
echo $OUTPUT->box('Conteúdo');
echo $OUTPUT->box('Conteúdo', 'classname');
echo $OUTPUT->box_start('classname');
echo $OUTPUT->box_end();

// Ícones
echo $OUTPUT->pix_icon('icon', 'alt', 'mod_meuplugin');
echo $OUTPUT->pix_icon('i/edit', 'Editar', 'core');

// Botões
echo $OUTPUT->single_button($url, 'Texto');
echo $OUTPUT->single_button($url, 'Texto', 'get', ['class' => 'btn-primary']);
```

### Renderização de Templates

```php
// Template simples
echo $OUTPUT->render_from_template('mod_meuplugin/view', $data);

// Com renderer customizado
$output = $PAGE->get_renderer('mod_meuplugin');
echo $OUTPUT->render_view($data);
```

### Navegação

```php
// Adicionar à navegação
$nav = $PAGE->activitiesnav;
$node = $nav->add('Meu Item', $url);
$node->make_active();

// Adicionar ao bloco de navegação
$PAGE->settingsnav->add('Meu Link', $url);
```

## Funções de Navegação

### moodle_url

```php
// URL simples
$url = new moodle_url('/mod/meuplugin/view.php');

// Com parâmetros
$url = new moodle_url('/mod/meuplugin/view.php', ['id' => $cmid]);

// URL absoluta
$url = new moodle_url('https://example.com/plugin/');

// Métodos
$url->out();                    // URL completa
$url->out(false);               // Sem HTML escape
$url->out_as_local_url(false);  // URL local
$url->get_path();               // Caminho
$url->get_params();             // Parâmetros
```

### redirect()

```php
// Redirecionar
redirect($url);

// Com mensagem
redirect($url, 'Registro salvo com sucesso!');

// Com delay
redirect($url, 'Redirecionando...', 3);

// Redirecionar para URL externa
redirect('https://example.com/', 'Saindo...', 0, true);
```

## Form API (moodleform)

### Criando Formulário

```php
<?php
require_once($CFG->libdir . '/formslib.php');

class meu_form extends moodleform {
    public function definition() {
        $mform = $this->_form;

        // Elementos
        $mform->addElement('text', 'name', 'Nome');
        $mform->setType('name', PARAM_TEXT);
        $mform->addRule('name', 'Obrigatório', 'required');

        $mform->addElement('editor', 'content', 'Conteúdo');
        $mform->setType('content', PARAM_RAW);

        $mform->addElement('filemanager', 'files', 'Arquivo');

        $this->add_action_buttons();
    }

    public function validation($data, $files) {
        $errors = parent::validation($data, $files);
        if (strlen($data['name']) < 3) {
            $errors['name'] = 'Nome muito curto';
        }
        return $errors;
    }
}

// Uso
$form = new meu_form();
if ($form->is_cancelled()) {
    redirect($backurl);
} else if ($data = $form->get_data()) {
    // Processar dados
}
```

### Elementos Disponíveis

| Elemento | Uso |
|----------|-----|
| `text` | Campo de texto |
| `textarea` | Área de texto |
| `select` | Dropdown |
| `advcheckbox` | Checkbox |
| `radio` | Radio button |
| `date_time_selector` | Data/hora |
| `editor` | Editor rico |
| `filemanager` | Upload |
| `hidden` | Oculto |
| `static` | Texto estático |
| `html` | HTML puro |
| `group` | Grupo de elementos |
| `date_selector` | Data |
| `duration` | Duração |
| `color` | Seletor de cor |

## HMAC / Funções de Segurança

### hash_internal_secret()

```php
// Gerar hash HMAC
$hash = hash_internal_secret('dados_para_hash');

// Verificar hash
if (hash_internal_secret('dados') === $hash) {
    // Hash válido
}
```

### password_hash() e password_verify()

```php
// Gerar hash de senha
$hash = password_hash($password, PASSWORD_BCRYPT);

// Verificar senha
if (password_verify($password, $hash)) {
    // Senha correta
}
```

### random_string()

```php
// String aleatória
$string = random_string(32);

// Com caracteres específicos
$string = random_string(16, 'alnum');  // Alfanumérico
$string = random_string(8, 'alpha');   // Apenas letras
$string = random_string(8, 'hex');     // Apenas hex
```

### sesskey()

```php
// Gerar/verificar sesskey
$sesskey = sesskey();

// Verificar em formulário
require_sesskey();

// Verificar sem morrer
if (!confirm_sesskey()) {
    // Sesskey inválido
}
```

## Funções de Usuário

### fullname()

```php
// Nome completo do usuário
$name = fullname($user);

// Com opções
$name = fullname($user, true);  // Com link
$name = fullname($user, false, true);  // Sem link, com imagem
```

### is_siteadmin()

```php
// Verificar se é admin do site
if (is_siteadmin($USER->id)) {
    // É admin
}

// Verificar para outro usuário
if (is_siteadmin($userid)) {
    // É admin
}
```

### get_user_roles()

```php
// Obter papéis do usuário
$roles = get_user_roles($context, $userid);

// Como array de IDs
$roleids = array_keys($roles);
```

## Funções de Texto

### format_text()

```php
// Formatar texto
$formatted = format_text($text, FORMAT_HTML);
$formatted = format_text($text, FORMAT_MOODLE);
$formatted = format_text($text, FORMAT_PLAIN);

// Com opções
$options = [
    'noclean' => false,
    'para' => false,
    'newlines' => false,
    'context' => $context,
];
$formatted = format_text($text, FORMAT_HTML, $options);
```

### s()

```php
// Escapar para HTML
$safe = s($text);
// Equivalente a htmlspecialchars($text, ENT_QUOTES, 'UTF-8')
```

### html_to_text()

```php
// Converter HTML para texto plano
$text = html_to_text($html);
```

## Funções de Arquivo

### file_save_draft_area_files()

```php
// Salvar arquivos do draft
file_save_draft_area_files(
    $draftitemid,      // ID do draft
    $contextid,        // Contexto
    'mod_meuplugin',   // Componente
    'myfilearea',      // Área
    $itemid,           // ID do item
    ['maxfiles' => 1, 'accepted_types' => ['image']]
);
```

### file_get_submitted_draft_itemid()

```php
// Obter ID do draft submetido
$draftid = file_get_submitted_draft_itemid('filearea');
```

### file_prepare_draft_area()

```php
// Preparar draft area
file_prepare_draft_area(
    $draftitemid,
    $contextid,
    'mod_meuplugin',
    'myfilearea',
    $itemid,
    ['maxfiles' => 1]
);
```

## Funções de Mensagem

### message_send()

```php
// Enviar mensagem
$message = new \core\message\message();
$message->component = 'mod_meuplugin';
$message->name = 'meu_notificacao';
$message->userfrom = $sender;
$message->userto = $recipient;
$message->subject = 'Assunto';
$message->fullmessage = 'Corpo da mensagem';
$message->fullmessageformat = FORMAT_HTML;
$message->fullmessagehtml = '<p>Corpo HTML</p>';
$message->smallmessage = 'Resumo';

$msgid = message_send($message);
```

### notifify_user()

```php
// Enviar notificação
notifify_user($user, $from, 'component', 'message', [
    'fullmessage' => 'Mensagem completa',
    'smallmessage' => 'Resumo',
]);
```

## Referências

- [[Base]] — Estrutura geral
- [[5.2/Plugins/Criar]] — Criação de plugins
- [[Templates/Mustache]] — Templates
- [[Eventos/Observer]] — Sistema de eventos
