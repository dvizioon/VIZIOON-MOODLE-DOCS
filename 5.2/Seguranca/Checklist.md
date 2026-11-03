# Checklist de segurança — plugins Moodle 5.2

Igual em espírito ao [[4.5.8/Seguranca/Checklist|checklist 4.5.8]]. APIs: [[5.2/Seguranca/Funcoes]]. Anti-padrões NTI: [[5.2/Seguranca/Anti-Padroes]].

---

## Página PHP

- [ ] Bootstrap `config.php` com path correto (`__DIR__ . '/../...'`)
- [ ] `required_param` / `optional_param` + `PARAM_*`
- [ ] `require_login` / `require_course_login`
- [ ] Contexto + `require_capability`
- [ ] Escrita → `require_sesskey()`
- [ ] IDs amarrados ao curso/contexto
- [ ] Output: `s` / `format_text` / Mustache / React sem HTML cru de usuário
- [ ] `moodle_exception`, não `print_error`

## External / AJAX

- [ ] `validate_parameters`
- [ ] `validate_context`
- [ ] `require_capability` (não confiar só em `services.php`)
- [ ] Revisar `ajax => true` (sessão de qualquer logado)
- [ ] Clamp de `page`/`perpage` + limite via `$DB`
- [ ] `\core_external\util::format_text` em HTML
- [ ] `catch (\Throwable $e)`
- [ ] API de domínio em `local_`/`mod_`, não protocolo `webservice_`

## Caps, DB, cache

- [ ] `db/access.php` com `RISK_*` corretos
- [ ] SQL só com placeholders
- [ ] Sem `LIMIT` literal
- [ ] TTL em `db/caches.php`
- [ ] Sem contador/token volátil em `config_plugins`

## HTTP / segredos / privacy

- [ ] `\curl` + SSL
- [ ] Escape XML/JSON
- [ ] Token: hash, TTL, uso único se login
- [ ] Nada gravado em `$CFG->dirroot`
- [ ] Sem secret no Git/`doc/`
- [ ] Integração lenta → `adhoc_task`
- [ ] `classes/privacy/provider.php`

## 5.2 específico

- [ ] Se usar React: sem `dangerouslySetInnerHTML` com input de usuário
- [ ] Conferir paths `public/` no deploy
- [ ] Hooks novos preferem task assíncrona para side-effects de rede
- [ ] Dependências e `version` incrementados no port 4.5 → 5.2

## Ferramentas

```bash
vendor/bin/phpcs --standard=moodle path/to/plugin
# Recomendado: moodle-plugin-ci no CI do repositório do plugin
```
