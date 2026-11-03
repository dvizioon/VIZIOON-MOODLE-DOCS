# Funções de uso diário no 4.5.8

Onde cada uma mora de verdade neste checkout. Vários nomes do guia 5.2 não existem aqui.

## Erro

`print_error()` não está em `lib/moodlelib.php` nem em `lib/deprecatedlib.php` desta build. O caminho é exceção:

```php
throw new moodle_exception('invalidcoursemodule');
throw new moodle_exception('nopermissions', 'error', '', get_capability_string($cap));
```

O handler instalado em `lib/setup.php` é `default_exception_handler`. Em web service, com `WS_SERVER`, o handler inicial é `early_ws_exception_handler`.

`debugging($msg, DEBUG_DEVELOPER)` está em `setuplib.php`. As constantes deste arquivo são máscaras de erro do PHP, não os números 1, 5 e 10 de documentação antiga:

| Constante | Valor em `lib/setuplib.php` |
|-----------|-----------------------------|
| `DEBUG_NONE` | `0` |
| `DEBUG_MINIMAL` | `E_ERROR \| E_PARSE` |
| `DEBUG_NORMAL` | `E_ERROR \| E_PARSE \| E_WARNING \| E_NOTICE` |
| `DEBUG_ALL` | `E_ALL` sem `E_STRICT` |
| `DEBUG_DEVELOPER` | `E_ALL \| E_STRICT` |

## Login e capability

`require_login()` em `moodlelib.php`.

```php
require_login();                              // só sessão
require_login($course);                       // curso
require_login($course, true, $cm);            // curso + módulo; o true aplica a matrícula automática se o enrol permitir
```

`require_capability('moodle/course:manageactivities', $context)` em `accesslib.php` interrompe com exceção. `has_capability()` só devolve bool. `require_all_capabilities([...], $context)` exige todas — `course/mod.php` usa isso no duplicate.

Contextos (classes em `lib/classes/context/`):

```php
$context = context_system::instance();
$context = context_course::instance($courseid);
$context = context_module::instance($cmid);
$context = context_user::instance($userid);
```

`require_sesskey()` / `confirm_sesskey()` protegem POST e links que alteram dado. `sesskey()` devolve a chave da sessão.

## URL, redirect, parâmetros

```php
$id = required_param('id', PARAM_INT);
$sr = optional_param('sr', null, PARAM_INT);

$url = new moodle_url('/course/view.php', ['id' => $courseid]);
redirect($url);
redirect($url, get_string('changessaved'), null, \core\output\notification::NOTIFY_SUCCESS);
```

`PARAM_*` está em `lib/classes/param.php` (e constantes globais). Os que `course/mod.php` usa: `PARAM_INT`, `PARAM_BOOL`, `PARAM_ALPHA`, `PARAM_ALPHANUM`.

`s($text)` escapa HTML. `format_text($text, $format, $options)` aplica filtros. `fullname($user)` respeita a política de nome do site.

## `$OUTPUT` e `$PAGE`

```php
$PAGE->set_url($url);
$PAGE->set_context($context);
$PAGE->set_title($title);
$PAGE->set_heading($course->fullname);
$PAGE->set_pagelayout('incourse');   // admin, standard, course, frontpage, ...

echo $OUTPUT->header();
echo $OUTPUT->heading('Título');
echo $OUTPUT->notification('Salvo', 'notifysuccess');
echo $OUTPUT->footer();

echo $OUTPUT->render_from_template('mod_forum/big_search_form', $data);
$PAGE->requires->js_call_amd('mod_forum/discussion', 'init', [$id]);
```

Tabela simples: `html_table` + `html_writer::table($table)`.

## Formulário

`lib/formslib.php`: classe estende `moodleform`. Módulo estende `moodleform_mod` (`course/moodleform_mod.php`), que já traz intro, conclusão, restrição, notas e os botões padrão.

```php
$mform->addElement('text', 'name', get_string('name'));
$mform->setType('name', PARAM_TEXT);
$mform->addRule('name', null, 'required', null, 'client');
```

Ciclo na página: `is_cancelled()`, `get_data()`, senão `$form->display()`.

## Arquivo

File API em `lib/filelib.php` e `lib/filestorage/`:

```php
$draftitemid = file_get_submitted_draft_itemid('attachments');
file_prepare_draft_area($draftitemid, $context->id, 'mod_forum', 'attachment', $postid);
file_save_draft_area_files($draftitemid, $context->id, 'mod_forum', 'attachment', $postid, $options);
```

Servir na URL: `pluginfile.php` → callback `<componente>_pluginfile()` no `lib.php`.

## Mensagem

`lib/messagelib.php`:

```php
$message = new \core\message\message();
$message->component = 'mod_forum';
$message->name = 'posts';
$message->userfrom = $userfrom;
$message->userto = $userto;
$message->subject = $subject;
$message->fullmessage = $plain;
$message->fullmessageformat = FORMAT_PLAIN;
$message->fullmessagehtml = $html;
$message->smallmessage = $small;
$message->contexturl = $url->out(false);
message_send($message);
```

O nome `posts` tem de existir em `db/messages.php` do componente. Não há função `notifify_user` neste código.

## Senha e segredo

Senha de usuário: `hash_internal_user_password()` / `validate_internal_user_password()` em `moodlelib.php` (bcrypt). `password_hash` do PHP não substitui isso no login do Moodle.

Segredo de plugin entre requisições: `$CFG->secretdataroot` não é a API. Use `complex_random_string()` ou o secret do site via funções de `moodlelib.php` (`get_site_identifier()`, HMAC com as helpers de weblib quando o código do core já faz isso). Não invente um `hash_internal_secret()` — esse nome não está no `moodlelib.php` desta árvore como API pública de plugin.

## Referências

- [[4.5.8/Lib/Bibliotecas]]
- [[4.5.8/Templates/Mustache]]
- [[4.5.8/Course/Mod]]
