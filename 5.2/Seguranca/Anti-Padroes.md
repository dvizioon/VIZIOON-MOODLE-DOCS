# Anti-padrões → correção (válido no Moodle 5.2)

Os plugins analisados em `analise-moodle-plugins.md` foram escritos na linha 4.5/5.x. **Os buracos são de API Moodle, não de versão:** falta de `validate_context`, sesskey, capability, `\curl`, privacy, etc. funcionam (e falham) igual no 5.2.

Lista completa com snippets: [[4.5.8/Seguranca/Anti-Padroes]]. Funções no 5.2: [[5.2/Seguranca/Funcoes]].

## Resumo dos padrões que mais se repetem

| Anti-padrão | Correção 5.2 |
|-------------|--------------|
| External sem `validate_context` / `require_capability` | Obrigatório no `execute()`; `ajax => true` = qualquer logado |
| Escrita só com `require_login` | + capability + `require_sesskey` |
| `LIMIT` no SQL / `perpage` sem teto | `$DB->get_records_sql(..., $from, $limit)` + clamp |
| `$cache->set($k, $v, $ttl)` | `ttl` em `db/caches.php` |
| Rate limit em `config_plugins` | MUC ou tabela |
| `catch (Exception` no namespace | `catch (\Throwable` |
| `curl_init` + SSL off | `new \curl()` + verify |
| XML/HTML concatenado | escape / DOM / Mustache / React sem HTML cru |
| PHP/token em `dirroot` / config plain | endpoint do plugin + hash + uso único |
| Fork de `mod_assign` com version futura | plugin à parte + hooks/tasks |
| Sem privacy provider | `classes/privacy/provider.php` |
| `doc/` antigo dentro do bloco | fora do pacote; rotacionar secrets |

Ao portar um plugin 4.5 → 5.2: **primeiro** feche esses itens; depois ajuste front (`public/`, React) e APIs deprecadas. Subir de versão sem capability/`validate_context` só leva o mesmo buraco para o 5.2.
