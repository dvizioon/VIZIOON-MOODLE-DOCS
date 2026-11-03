# Funções e APIs de segurança — Moodle 5.2

Mesmo contrato de segurança do [[4.5.8/Seguranca/Funcoes|4.5.8]]: login, capability, sesskey, `validate_context`, `$DB`, `\curl`, privacy. Abaixo: onde os arquivos moram **neste** tree 5.2 e o que mudou na prática do desenvolvedor.

Checkout de referência: `/home/daniel/Área de trabalho/Projetos/MOODLE/5.2`. A partir do 5.1 o front público pode ficar sob `public/`; APIs de `lib/` continuam no core. Confirme no seu checkout se o path é `lib/...` ou `public/lib/...`.

Anti-padrões dos plugins NTI: [[5.2/Seguranca/Anti-Padroes]]. Checklist: [[5.2/Seguranca/Checklist]].

---

## O que é idêntico ao 4.5.8 (use do mesmo jeito)

| Área | Funções |
|------|---------|
| Sessão | `require_login`, `require_course_login`, `require_sesskey`, `confirm_sesskey`, `sesskey` |
| Cap | `has_capability`, `require_capability`, `context_*::instance`, `RISK_*` |
| External | `external_api::validate_parameters`, `validate_context`, `require_capability` no `execute` |
| Input | `required_param`, `optional_param`, `clean_param`, `PARAM_*` |
| Output | `s()`, `format_text()`, `format_string()`, Mustache `{{ }}` |
| DB | `$DB->*` com placeholders; limite via 3º/4º arg de `get_records_sql` |
| HTTP | `new \curl()` + SSL; security helper SSRF |
| Senha | `hash_internal_user_password`, `update_internal_user_password`, `hash_equals`, `random_string` |
| Cache | TTL em `db/caches.php`, **não** no `set($k,$v,$ttl)` |
| Privacy | `classes/privacy/provider.php` |
| Erro | `throw new moodle_exception` — sem `print_error` |

Esqueleto external seguro (válido 4.5 e 5.2):

```php
public static function execute(int $page, int $perpage): array {
    $params = self::validate_parameters(self::execute_parameters(), compact('page', 'perpage'));
    $perpage = max(1, min(100, $params['perpage']));
    $page = max(0, $params['page']);

    $context = \context_system::instance();
    self::validate_context($context);
    require_capability('local/meu:viewusers', $context);

    return []; // dados já autorizados
}
```

---

## Diferenças relevantes no 5.2

### Front: React além de AMD

No 5.2 o core adiciona caminho React (ver [[5.2/Frontend/React]]). Regras de XSS **não mudam**:

- Dado do PHP → props: trate como não confiável.
- Não use `dangerouslySetInnerHTML` com texto de usuário sem sanitizar (equivalente a `{{{ }}}` no Mustache).
- Chamadas ao backend: web service com `validate_context` + capability; o bridge JS ainda depende de sessão/sesskey do Moodle.

AMD + Mustache continuam válidos; plugins legados 4.5 sobem sem trocar o modelo de autorização.

### Tipo `webservice_` vs `local_`

Continua igual: protocolo em `webservice/`; API de negócio em `local_`/`mod_`/`block_`. `'capabilities'` em `db/services.php` segue sendo documentação, não enforcement.

### Hooks PSR-14

Observers clássicos e hooks novos coexistentes. Webhook/integração: preferir hook/observer **não interno** + `adhoc_task` (evita POST síncrono na request). Mesma recomendação da análise do `mod_assign` fork.

### Pacote do plugin

Não colocar `doc/`, credenciais, PHP de teste ou zip dentro do diretório instalável — o web server serve esses paths. No 5.2 com `public/`, o risco de expor artefatos mal colocados no docroot continua o mesmo se o deploy copiar a pasta inteira do plugin.

---

## Tabela rápida “o que chamar”

| Situação | Chamar |
|----------|--------|
| Abrir página | `require_login` → contexto → `require_capability` |
| Salvar / apagar / POST | + `require_sesskey()` |
| Função AJAX/WS | `validate_parameters` + `validate_context` + `require_capability` |
| Echo de texto | `s()` ou `{{mustache}}` |
| Echo de HTML de professor | `format_text` no contexto certo |
| URL em atributo | `clean_param(..., PARAM_URL)` |
| SQL paginado | `$DB->get_records_sql($sql, $params, $from, $limit)` |
| HTTP egress | `new \curl()` |
| Token de login | hash + uso único + TTL; nunca arquivo em `dirroot` |
| PII no plugin | privacy provider |

---

## Referências

- [[5.2/Seguranca/Checklist]]
- [[5.2/Seguranca/Anti-Padroes]]
- [[5.2/WebServices/Criar]]
- [[5.2/Classes/Helper]]
- [[5.2/Frontend/React]]
- [[4.5.8/Seguranca/Funcoes]] (catálogo completo, line-by-line no core 4.5.8)
