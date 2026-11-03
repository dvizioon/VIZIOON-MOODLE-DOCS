# Checklist de segurança — plugins Moodle 4.5.8

Use antes de publicar qualquer `local_`, `mod_`, `block_`, `tool_`, `format_`, `filter_` ou função em `db/services.php`. Catálogo de funções: [[4.5.8/Seguranca/Funcoes]]. Exemplos do que já quebrou em produção/análise: [[4.5.8/Seguranca/Anti-Padroes]].

---

## Página PHP (`view.php`, `edit.php`, `action.php`, `ajax.php`)

- [ ] `require('../../config.php')` (ou `__DIR__` com níveis corretos — path errado = fatal, como no `format_timeline/post.php`)
- [ ] `required_param` / `optional_param` com `PARAM_*` adequado
- [ ] `require_login` / `require_course_login` com course/cm quando couber
- [ ] Contexto certo: `context_system` / `course` / `module`
- [ ] `require_capability` (ou `has_capability` + saída controlada)
- [ ] Se **altera** dado: `require_sesskey()` (nunca ação de escrita só em GET sem sesskey)
- [ ] IDs de seção/item validados contra o curso/contexto informado
- [ ] Saída com `s()`, `format_text`, template Mustache — sem concatenar HTML cru
- [ ] Erro via `moodle_exception`, não `print_error`

## Função externa (`classes/external/*.php`)

- [ ] `validate_parameters` no início
- [ ] `validate_context($context)` — **obrigatório**
- [ ] `require_capability` — a chave `capabilities` do `services.php` **não basta**
- [ ] `ajax => true` só se a capability for segura para usuário de sessão comum
- [ ] Paginação com teto (`perpage` 1..N) e `$DB->get_records_sql(..., $from, $limit)`
- [ ] Textos rich: `\core_external\util::format_text`
- [ ] `catch (\Throwable $e)` se precisar capturar
- [ ] Tipo do plugin: API de negócio em `local_`/`mod_`, não `webservice_` (protocolo)

## `db/access.php`

- [ ] Capability própria para dado sensível (`RISK_PERSONAL`, `RISK_XSS`, `RISK_DATALOSS`…)
- [ ] `contextlevel` coerente com o uso
- [ ] Archetypes mínimos (não liberar `user`/`student` em listagem global)

## Banco e cache

- [ ] Só placeholders (`?` / named); zero interpolação de input
- [ ] Sem `LIMIT`/`OFFSET` literais no SQL
- [ ] Transação em delete+insert em lote
- [ ] TTL no `db/caches.php`, não no `set()`
- [ ] Rate limit / token / contador **fora** de `config_plugins`

## HTTP, segredos, auth

- [ ] `new \curl()` + SSL verify ligado
- [ ] Escape XML/JSON ao montar payload
- [ ] Tokens: hash at-rest, uso único se for login, TTL
- [ ] Sem gravar arquivo em `$CFG->dirroot`
- [ ] Sem credenciais em `doc/`, comentários ou Git
- [ ] Webhook/API lenta → `adhoc_task`, não request do usuário

## Privacidade e pacote

- [ ] `classes/privacy/provider.php` (null ou completo)
- [ ] Sem `doc/oldSys`, testes expostos, zips, PDF gigante no plugin instalado
- [ ] `$plugin->version` sobe a cada release
- [ ] Dependências declaradas em `version.php` se o plugin depende de outro
- [ ] Não forkar `mod_*` core; preferir observer/subplugin

## Front

- [ ] AMD + `core/ajax` (sesskey automática) em vez de JS inline
- [ ] Sem `innerHTML` com dado do servidor; DOM API ou template
- [ ] Filtro de texto não chama `$PAGE->set_context`

## Ferramentas

```bash
# No clone do Moodle com o plugin em local/mod/...
vendor/bin/phpcs --standard=moodle path/to/plugin
# Ideal: moodle-plugin-ci (phplint, phpcs, phpdoc, validate, mustache, grunt)
```

Administração → Desenvolvimento → **Teste de aceitação de plugins** / validação de DB também pega schema e capabilities quebradas.
