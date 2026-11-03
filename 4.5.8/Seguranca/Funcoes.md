# Funções e APIs de segurança — Moodle 4.5.8

Catálogo prático do que usar ao desenvolver (ou endurecer) plugins neste checkout (`/home/daniel/Área de trabalho/Projetos/MOODLE/4.5.8`). Cada item aponta o arquivo real. Os anti-padrões da análise dos plugins Oxygeni/NTI estão em [[4.5.8/Seguranca/Anti-Padroes|Anti-padrões]] e o roteiro de revisão em [[4.5.8/Seguranca/Checklist|Checklist]].

---

## 1. Login, sessão e CSRF

| Função | Arquivo | O que faz |
|--------|---------|-----------|
| `require_login($course?, $autologinguest?, $cm?, …)` | `lib/moodlelib.php` | Exige sessão. Com `$course`/`$cm`, exige acesso ao curso/módulo |
| `require_course_login($course, $autologinguest, $cm)` | `lib/moodlelib.php` | Variante usada em `view.php` de atividades |
| `isloggedin()` | `lib/accesslib.php` | Só testa sessão; **não** autoriza ação |
| `isguestuser()` | `lib/moodlelib.php` | Convidado logado ≠ usuário autenticado de verdade |
| `require_sesskey()` | `lib/sessionlib.php` | Exige `sesskey` válido; falha com exceção (POST/ação que muda estado) |
| `confirm_sesskey($sesskey = null)` | `lib/sessionlib.php` | Devolve bool; útil em formulários |
| `sesskey()` | `lib/sessionlib.php` | Gera/obtém a chave para colocar em URL ou hidden field |

```php
require_login($course, true, $cm);
require_capability('local/meu:manage', $context);
require_sesskey(); // em todo script que ALTERA dado (POST ou GET de ação)
```

Regra: `require_login` ≠ autorização. Sem `require_capability` + `require_sesskey` em escrita, qualquer aluno logado (ou CSRF via imagem/link) altera o sistema — exatamente o caso de `format_trail` (`mod_summary.php` / `editimage.php`) na análise.

Em Mustache/AMD, a sesskey já viaja com `core/ajax`. Em link PHP manual:

```php
$url = new moodle_url('/local/meu/action.php', [
    'id' => $id,
    'sesskey' => sesskey(),
]);
```

---

## 2. Contexto e capabilities

| Função / classe | Arquivo | Uso |
|-----------------|---------|-----|
| `context_system::instance()` | `lib/classes/context/system.php` | Site inteiro |
| `context_course::instance($id)` | `lib/classes/context/course.php` | Curso |
| `context_module::instance($cmid)` | `lib/classes/context/module.php` | Atividade |
| `context_user::instance($userid)` | `lib/classes/context/user.php` | Perfil |
| `context_helper::preload_from_record($rec)` | `lib/classes/context/helper.php` | Evita N+1 de context em loops |
| `has_capability($cap, $context, $user?)` | `lib/accesslib.php` | Bool |
| `require_capability($cap, $context, …)` | `lib/accesslib.php` | Interrompe com `required_capability_exception` |
| `require_all_capabilities(array, $context)` | `lib/accesslib.php` | Todas obrigatórias |
| `get_users_by_capability($context, $cap)` | `lib/accesslib.php` | Quem tem a cap (cuidado com performance) |

Definição em `db/access.php`:

```php
$capabilities = [
    'local/meu:viewusers' => [
        'riskbitmask'  => RISK_PERSONAL,   // vê dados pessoais
        'captype'      => 'read',
        'contextlevel' => CONTEXT_SYSTEM,
        'archetypes'   => [
            'manager' => CAP_ALLOW,
        ],
    ],
    'local/meu:manage' => [
        'riskbitmask'  => RISK_DATALOSS | RISK_XSS,
        'captype'      => 'write',
        'contextlevel' => CONTEXT_COURSE,
        'archetypes'   => [
            'editingteacher' => CAP_ALLOW,
            'manager'        => CAP_ALLOW,
        ],
    ],
];
```

Máscaras em `lib/accesslib.php`:

| Constante | Quando marcar |
|-----------|----------------|
| `RISK_PERSONAL` | E-mail, nome, últimos acessos, notas… |
| `RISK_XSS` | Aceita HTML de usuário e renderiza |
| `RISK_SPAM` | Envia mensagem/e-mail em massa |
| `RISK_CONFIG` | Muda config do site/plugin |
| `RISK_DATALOSS` | Apaga ou sobrescreve dado irreversível |

A chave `'capabilities'` em `db/services.php` **não aplica** a checagem. Só documenta. Quem bloqueia é `require_capability()` dentro do `execute()`.

---

## 3. Web service / AJAX externo

Classe base: `core_external\external_api` em `lib/external/classes/external_api.php`.

| Método | Obrigatório? | Função |
|--------|--------------|--------|
| `self::validate_parameters($desc, $params)` | Sim | Aplica `PARAM_*`, rejeita chave extra |
| `self::validate_context($context)` | **Sim** | Restringe contexto do token/sessão + `require_login` interno |
| `require_capability($cap, $context)` | **Sim** em dado sensível | Autorização real |
| `\core_external\util::format_text(...)` | Em HTML/resumo | Sanitiza texto antes de devolver na API |
| `external_format_text(...)` | Alias legado | Mesmo papel |

Esqueleto mínimo seguro (o que faltava no `oxywebapi` / `oxymoodlecache`):

```php
public static function execute(int $page, int $perpage): array {
    $params = self::validate_parameters(self::execute_parameters(), [
        'page' => $page,
        'perpage' => $perpage,
    ]);

    // Limites defensivos — evita DoS / divisão por zero.
    $perpage = max(1, min(100, $params['perpage']));
    $page = max(0, $params['page']);

    $context = \context_system::instance();
    self::validate_context($context);
    require_capability('local/meu:viewusers', $context);

    // ... consulta com placeholders ...
}
```

`ajax => true` em `db/services.php` libera a função para **qualquer usuário logado** via `core/ajax` (sesskey da página). Se a função lista usuários/cursos do site, ou tire o `ajax`, ou a capability tem de ser restrita (nunca “qualquer aluno”).

Tipo de plugin: funções de negócio ficam em `local_` / `mod_` / `block_`. Plugin `webservice_` é para **protocolo** (rest/soap), não para API de domínio.

---

## 4. Entrada — limpar parâmetros

| Função | Arquivo |
|--------|---------|
| `required_param($name, $type)` | `lib/moodlelib.php` |
| `optional_param($name, $default, $type)` | `lib/moodlelib.php` |
| `clean_param($value, $type)` | `lib/moodlelib.php` |
| `clean_param_array($arr, $type)` | `lib/moodlelib.php` |

Tipos em `lib/classes/param.php` (constantes `PARAM_*`):

| Tipo | Uso típico |
|------|------------|
| `PARAM_INT` | ids, page, perpage |
| `PARAM_FLOAT` / `PARAM_LOCALISEDFLOAT` | números |
| `PARAM_BOOL` | flags |
| `PARAM_ALPHA` | `asc`/`desc`, códigos curtos |
| `PARAM_ALPHANUM` / `PARAM_ALPHANUMEXT` | tokens alfanuméricos |
| `PARAM_TEXT` | texto curto sem HTML perigoso |
| `PARAM_NOTAGS` | remove tags |
| `PARAM_CLEANHTML` | HTML “limpo” |
| `PARAM_RAW` | só quando você sanitiza depois (`format_text`) |
| `PARAM_URL` | URLs (nunca concatenar cru em `href`) |
| `PARAM_EMAIL` | e-mail |
| `PARAM_COMPONENT` / `PARAM_PLUGIN` | nomes de componente |
| `PARAM_SAFEDIR` / `PARAM_PATH` / `PARAM_FILE` | caminhos |

```php
$id = required_param('id', PARAM_INT);
$url = clean_param($joinurl, PARAM_URL);
if (empty($url)) {
    throw new moodle_exception('invalidurl');
}
```

---

## 5. Saída — XSS

| Função | Arquivo | Quando |
|--------|---------|--------|
| `s($text)` | `lib/weblib.php` | Escapa HTML (`htmlspecialchars`) para atributo/texto |
| `p($text)` | `lib/weblib.php` | Echo de `s()` |
| `format_text($text, $format, $options)` | `lib/weblib.php` | Conteúdo formatado + filtros |
| `format_string($string, $striplinks?)` | `lib/weblib.php` | Nomes curtos (curso, atividade) |
| `html_writer::*` | `lib/output/xhtml_container_stack` / weblib | Montar HTML sem concatenação crua |
| `addslashes_js($var)` | `lib/weblib.php` | Se ainda precisar embutir em JS (prefira AMD + json) |
| Mustache `{{nome}}` | templates | Escape automático |
| Mustache `{{{html}}}` | templates | **Sem** escape — só HTML já sanitizado |

```php
echo html_writer::span(s($user->email), 'email');
echo format_text($summary, FORMAT_HTML, ['context' => $context]);
```

No JS (AMD): criar nós com DOM (`document.createElement`), não `innerHTML = '...'+ data.url +'...'`. No Tiny/filtro, `clean_param($url, PARAM_URL)` antes de `href`.

XML enviado a API externa: `htmlspecialchars($v, ENT_XML1 | ENT_QUOTES, 'UTF-8')` ou `XMLWriter`/`DOMDocument` — nunca interpolar nome/e-mail cru no XML (caso `block_oxymylib`).

---

## 6. Banco de dados

| API | Por quê |
|-----|---------|
| `$DB->get_record('tabela', ['id' => $id])` | Placeholders internos |
| `$DB->get_records_sql($sql, $params, $limitfrom, $limitnum)` | Paginação **portável** (não escreva `LIMIT`/`OFFSET` no SQL) |
| `$DB->get_recordset_sql($sql, $params)` | Resultado grande / chaves duplicadas no 1º campo |
| `$DB->execute($sql, $params)` | DML com `?` ou `:nome` |
| `$DB->insert_record` / `update_record` / `delete_records` | CRUD |
| `$DB->start_delegated_transaction()` | Atomicidade (ex.: apagar + reinserir presença) |
| `{tabela}` no SQL | Prefixo `$CFG->prefix` |

```php
// Certo — limite via API
$rows = $DB->get_records_sql($sql, $params, $page * $perpage, $perpage);

// Errado — quebra MSSQL/Oracle e foi flagado na análise
$sql = "SELECT * FROM {user} LIMIT {$limit}";
```

`get_records_sql` indexa pelo **primeiro** campo do SELECT. Se a chave se repete (mesmo `aluno_id` em vários cursos), só a última linha sobra. Use `get_recordset_sql` ou uma coluna única (`CONCAT` / alias) como primeira.

Nunca: concatenar input em SQL, guardar contador de rate-limit em `config_plugins` (incha e trava), fazer `context_*::instance()` + query de arquivo **dentro** de loop sem preload.

---

## 7. HTTP de saída (`\curl`)

Classe: `curl` em `lib/filelib.php`. Respeita proxy Moodle e blocklist SSRF (`\core\files\curl_security_helper`).

```php
$curl = new \curl();
// SSL ligado (não desligar verifypeer em produção)
$curl->setopt([
    'CURLOPT_SSL_VERIFYPEER' => true,
    'CURLOPT_SSL_VERIFYHOST' => 2,
    'CURLOPT_TIMEOUT' => 10,
]);
$response = $curl->post($endpoint, $payload);
$info = $curl->get_info();
```

Evite `curl_init` cru: ignora proxy, hosts bloqueados e política do site. Integrações longas / webhooks: dispare `\core\task\adhoc_task` a partir do observer (`'internal' => false`), não POST síncrono na request do aluno.

---

## 8. Senhas, tokens e segredos

| Função | Arquivo | Uso |
|--------|---------|-----|
| `hash_internal_user_password($password)` | `lib/moodlelib.php` | Hash no formato Moodle |
| `update_internal_user_password($user, $password)` | `lib/moodlelib.php` | Troca senha + eventos adequados |
| `random_string($length = 15)` | `lib/moodlelib.php` | Token aleatório |
| `generate_password($maxlen = 10)` | `lib/moodlelib.php` | Senha temporária legível |
| `hash_equals($known, $user)` | PHP nativo | Comparação em tempo constante (JWT, token) |
| `set_config` / `get_config` | `lib/moodlelib.php` | Config **estática** do plugin — não rate-limit nem token de sessão |

Regras duras:

1. Token de “link mágico”: guardar **só hash** (`hash('sha256', $token)`), uso **único**, TTL curto, bloquear `auth = nologin` / suspensos, logar evento.
2. Não gravar PHP em `$CFG->dirroot` em runtime (`oxytemppass`). Endpoint dentro do plugin: `/admin/tool/seu/token.php`.
3. Não versionar senha MySQL, API key, JWT secret em `doc/` dentro do plugin.
4. Segredos de atividade (webhook): tabela própria do **plugin local/subplugin**, não coluna nova em tabela core (`assign`).
5. Nunca echo de pedaço de hash de senha na UI.

---

## 9. Cache (MUC)

Definição em `db/caches.php`. O TTL **não** é o 3º argumento de `set()` — esse argumento é ignorado na MUC.

```php
// db/caches.php
$definitions = [
    'catalog' => [
        'mode' => cache_store::MODE_APPLICATION,
        'simplekeys' => true,
        'ttl' => 300, // segundos — aqui sim
    ],
];

$cache = cache::make('local_meu', 'catalog');
$cache->set($key, $data);
$data = $cache->get($key);
```

Rate limit: store MUC ou tabela própria com limpeza; nunca `config_plugins` por request.

---

## 10. Privacidade (LGPD) e erros

Todo plugin que guarda PII precisa de `classes/privacy/provider.php`.

Sem dado pessoal:

```php
namespace local_meu\privacy;
class provider implements \core_privacy\local\metadata\null_provider {
    public static function get_reason(): string {
        return 'privacy:metadata';
    }
}
```

Com dado: implementar `metadata\provider` + `core_userlist_provider` / `user_preference_provider` conforme o caso (modelo vivo: vários `mod/*/classes/privacy/provider.php`).

Erros:

```php
throw new \moodle_exception('nopermissions', 'error', '', get_capability_string($cap));
// print_error() está obsoleto desde 4.0 — não use
```

Em namespace, `catch (Exception $e)` captura `Seu\Namespace\Exception`, **não** `\Exception`. Use `catch (\Throwable $e)`.

`debugging($msg, DEBUG_DEVELOPER)` — nunca logar senha, XML com API key ou PII se `DEBUG_DEVELOPER` puder estar ligado em produção.

---

## 11. Arquivos e páginas do plugin

| API | Papel |
|-----|-------|
| `file_prepare_draft_area` / `file_save_draft_area_files` | `lib/filelib.php` — upload via draft |
| `<component>_pluginfile(...)` em `lib.php` | Servir arquivo **com** `require_login` + capability |
| `$PAGE->set_context($context)` | Só no controller da página — **nunca** dentro de filtro de texto |

Filtros (`filter_*`): só transformar texto / `js_call_amd`. Trocar `$PAGE` contexto no meio da renderização quebra blocos/rodapé.

Não publique pastas `doc/`, `test/`, zips ou sistemas PHP antigos dentro do plugin instalável — o docroot do Moodle as serve.

---

## 12. Front (AMD) e formulários

```php
// PHP
$PAGE->requires->js_call_amd('local_meu/actions', 'init', [$id, sesskey()]);

// Formulário
$mform->setType('name', PARAM_TEXT);
$mform->addRule('name', null, 'required', null, 'client');
```

Preferir `moodleform` a endpoints GET que alteram estado. No AMD, chamar web services via `core/ajax` (já manda sesskey) em vez de inventar `fetch` sem chave.

---

## Referências neste vault

- [[4.5.8/Seguranca/Checklist]]
- [[4.5.8/Seguranca/Anti-Padroes]]
- [[4.5.8/WebServices/Criar]]
- [[4.5.8/Classes/Helper]]
- [[4.5.8/DB/Schema]]
- [[4.5.8/Frontend/AMD]]
