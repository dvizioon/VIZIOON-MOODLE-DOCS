# Anti-padrões → correção (plugins reais)

Mapeamento direto dos achados de `analise-moodle-plugins.md` (commit `9afcd8a`) para o método Moodle 4.5.8 correto. Detalhe das APIs: [[4.5.8/Seguranca/Funcoes]].

---

## External / AJAX sem autorização

**Onde:** `webservice_oxywebapi`, `local_oxymoodlecache` (`search_courses` / `get_users`).

**Erro:** `execute()` sem `validate_context` + `require_capability`. `'capabilities'` no `services.php` não bloqueia. Com `ajax => true`, aluno chama `core/ajax` e lista usuários/cursos ocultos.

**Correção:**

```php
$context = \context_system::instance();
self::validate_context($context);
require_capability('local/oxywebapi:viewusers', $context); // capability própria + RISK_PERSONAL
```

Tire `ajax => true` se só integração externa usa a função. Modelo bem feito no próprio repo: `webservice_oxybrigde_notas` (já tem validate + cap).

---

## Página PHP que altera estado só com `require_login`

**Onde:** `format_trail` — `mod_summary.php`, `editimage.php`.

**Erro:** qualquer logado muda resumo/imagem de qualquer curso; GET sem sesskey = CSRF.

**Correção:**

```php
require_login($course);
$context = context_course::instance($course->id);
require_capability('moodle/course:update', $context);
require_sesskey();
// validar que sectionid pertence a este courseid
```

---

## `LIMIT`/`OFFSET` no SQL + `perpage` sem teto

**Onde:** oxywebapi, oxymoodlecache.

**Erro:** quebra em MSSQL/Oracle; `perpage=0` → divisão por zero; `perpage` enorme → DoS.

**Correção:**

```php
$perpage = max(1, min(100, (int)$perpage));
$page = max(0, (int)$page);
$rows = $DB->get_records_sql($sql, $params, $page * $perpage, $perpage);
```

---

## `$cache->set($key, $data, $ttl)` e rate limit em `config_plugins`

**Onde:** oxywebapi (TTL ignorado), oxymoodlecache (contador em config).

**Erro:** 3º arg de `set()` não é TTL na MUC. `set_config` a cada request incha `config_plugins`.

**Correção:** `'ttl' => 300` em `db/caches.php`; rate limit em cache MUC ou tabela com purge.

---

## `catch (Exception $e)` dentro de namespace

**Onde:** oxywebapi, oxymoodlecache.

**Erro:** resolve para `Plugin\Namespace\Exception` — nunca captura `\Exception`/`moodle_exception`.

**Correção:** `catch (\Throwable $e)`.

---

## `curl_init` + SSL off + XML interpolado

**Onde:** `block_oxymylib`.

**Erro:** MITM na API key; nome com `&`/`<` quebra/injeta XML; ignora proxy/blocklist.

**Correção:** `new \curl()` + SSL on + `htmlspecialchars($v, ENT_XML1 | ENT_QUOTES, 'UTF-8')`.

---

## Token / senha temporária insegura

**Onde:** `tool_oxytemppass`.

**Erro:** PHP gravado em `dirroot`; token em texto puro em config; reuso até expirar; hash de senha na UI; restauração sobrescreve senha nova.

**Correção:** endpoint no plugin; só hash do token; uso único; `update_internal_user_password`; eventos; não echo de hash; bloquear `nologin`.

---

## Fork de core com `version` no futuro

**Onde:** `mod_assign` (`2026050930`).

**Erro:** bloqueia upgrade do core; perde patches de segurança do assign oficial.

**Correção:** plugin separado (`local_` / `assignfeedback_`) + observers; version = core +1 no máximo se for patch mínimo inevitável.

---

## Webhook síncrono no observer

**Onde:** assign custom.

**Erro:** POST na request do aluno, às vezes antes do commit; timeout trava UI.

**Correção:** observer `'internal' => false` + `adhoc_task`.

---

## Filtro que muda `$PAGE->set_context` / offsets errados

**Onde:** `filter_oxymsteams`, `format_timeline` paths.

**Erro:** contexto da página muda no meio do render; `preg_match_all` + mutate string invalida offsets.

**Correção:** só `js_call_amd` no filtro; processar matches de trás para frente ou DOMDocument.

---

## `get_records_sql` com chave duplicada

**Onde:** `oxybrigde_notas` `get_grade_history`.

**Erro:** indexa pelo 1º campo — linhas somem em silêncio.

**Correção:** `get_recordset_sql` ou 1ª coluna única.

---

## Pasta `doc/` / credenciais / zip dentro do plugin

**Onde:** `block_oxymylib/doc/oxymoodlebanner`, zips versionados.

**Erro:** PHP antigo sem `require_login` publicado em `/blocks/.../doc/...`; senha MySQL no Git.

**Correção:** doc fora do pacote instalável; secrets só em config/env; rotacionar credenciais vazadas; `.gitignore` de zips.

---

## Sem `privacy/provider.php`

**Onde:** oxymsteams (guarda e-mail/presença), oxytemppass.

**Erro:** ferramenta de privacidade do Moodle / LGPD incompleta.

**Correção:** `null_provider` ou provider completo em `classes/privacy/provider.php`.

---

## Checklist rápido por PR de plugin

1. Toda página de escrita: `require_login` + `require_capability` + `require_sesskey`.
2. Todo `external_*::execute`: `validate_parameters` + `validate_context` + `require_capability`.
3. Todo SQL: placeholders + limite via `$DB`, não `LIMIT` cru.
4. Toda saída HTML/JS/XML: `s` / Mustache / `format_text` / escape XML.
5. Todo HTTP: `\curl` com SSL.
6. Todo segredo: hash, não plain; fora de `dirroot` e de Git.
7. Todo plugin com PII: privacy provider.
8. `version.php` incrementa a cada release publicada.
