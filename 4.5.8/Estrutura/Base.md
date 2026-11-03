# Estrutura base do Moodle 4.5.8

## Como uma requisição começa

1. O servidor aponta para um script PHP (`index.php`, `course/view.php`, `admin/index.php`, …).
2. Esse script faz `require('config.php')`.
3. `config.php` (cópia de `config-dist.php` no servidor) cria `$CFG` com `wwwroot`, `dataroot`, `dbtype`, `dbhost`, `dbname`, `dbuser`, `dbpass`, `prefix` e inclui `lib/setup.php`.
4. `lib/setup.php` fixa caminhos, sobe o autoload, abre o banco, a sessão e os globais.
5. O script de entrada lê parâmetros, chama `require_login()` / `require_capability()` e imprime com `$OUTPUT`.

`index.php` da raiz, se não achar `config.php`, redireciona para `install.php`.

## O que setup.php faz, nesta ordem

Trechos reais de `lib/setup.php`:

1. `$CFG->dirroot = dirname(__DIR__)` — a raiz é o diretório pai de `lib/`, não um `public/`.
2. Permissões padrão de diretório `02777` e umask derivado.
3. Se `$CFG->behat_*` estiver definido e a URL for o site de teste, troca `wwwroot`, `prefix` e `dataroot` pelos valores Behat.
4. Exige `dataroot` existente e gravável, e `wwwroot` diferente de `http://example.com/moodle`.
5. `$CFG->routerconfigured` fica `true` só se o `config.php` marcar o roteador.
6. Define a constante `MOODLE_INTERNAL`. Sem ela, as libs morrem no `defined('MOODLE_INTERNAL') || die()`.
7. Carrega `lib/classes/component.php` e registra o autoload PSR-4 em `\core\component::register_autoloader()`.
8. Se a constante `ABORT_AFTER_CONFIG` existir, para aqui (scripts que só precisam de config, sem banco).
9. Inclui as bibliotecas padrão (lista em [[4.5.8/Lib/Bibliotecas]]).
10. Instancia `$OUTPUT` como `bootstrap_renderer` até o tema real entrar.
11. `set_exception_handler('default_exception_handler')` e `set_error_handler('default_error_handler')`.
12. Se `WS_SERVER` estiver definido, troca o handler para `early_ws_exception_handler`.
13. Conecta em `$DB`, inicia sessão, carrega `$USER`, `$SITE`, `$COURSE`, `$PAGE`.

YUI ainda é declarado aqui: `$CFG->yui2version = '2.9.0'` e `$CFG->yui3version = '3.18.1'`. Código novo usa AMD, não YUI.

## Globais

| Global | Papel |
|--------|--------|
| `$CFG` | Config de `config.php` mais a tabela `config` |
| `$DB` | `moodle_database`. Todo SQL passa por ele |
| `$USER` | Registro do usuário atual. Visitante anônimo recebe o guest |
| `$SESSION` | Dados de sessão que não são o registro de usuário |
| `$SITE` | Curso da página inicial (`id = 1`) |
| `$COURSE` | Atalho de `$PAGE->course` |
| `$PAGE` | `moodle_page`: URL, contexto, layout, navbar, JS exigido |
| `$OUTPUT` | Renderer do tema (`core_renderer` ou subclasse) |
| `$FULLME`, `$ME`, `$SCRIPT` | URL corrente. Para link da página use `$PAGE->url` |

`$CFG->libdir` aponta para `lib/`. `$CFG->admin` costuma ser a string `admin` (a pasta pode ser renomeada). `$CFG->httpswwwroot` é só alias de `$CFG->wwwroot`.

Leitura de config de plugin: `get_config('mod_forum', 'chave')`. Escrita administrativa: `set_config()`.

## version.php do core e do plugin

O core usa variáveis soltas em `version.php`:

```php
$version  = 2024100708.06;
$release  = '4.5.8+ (Build: 20260130)';
$branch   = '405';
$maturity = MATURITY_STABLE;
```

O formato é `YYYYMMDD` da branch (07/10/2024 = 4.5), `RR` da release (08 = 4.5.8) e `.XX` incremental.

Um plugin usa o objeto `$plugin` no próprio `version.php`:

```php
$plugin->component = 'mod_task';
$plugin->version   = 2024100700;   // YYYYMMDDXX
$plugin->requires  = 2024100700;   // mínimo: este 4.5
$plugin->maturity  = MATURITY_STABLE;
$plugin->release   = '1.0';
```

`lib/classes/component.php` lê `lib/components.json` e cada `version.php` para montar o mapa de plugins. O cache de componentes é invalidado no upgrade (`admin/index.php` chama `opcache_invalidate` em `version.php` e `core_component::get_core_subsystems()`).

## Autoload

`lib/components.json` declara tipos e subsistemas. A classe `\core\component` (arquivo `lib/classes/component.php`, com alias histórico `core_component`) mapeia:

- `\core\persistent` → `lib/classes/persistent.php`
- `\mod_forum\...` → `mod/forum/classes/...`
- subsistema sem pasta (`"access": null`) → classes em `lib/classes/` com prefixo `core_`

## Descoberta de plugins

Cada tipo em `components.json` → `plugintypes` é um diretório. O nome da pasta vira o frankenstyle: pasta `mod/forum` + tipo `mod` = componente `mod_forum`. Subplugins vêm de `db/subplugins.json` do plugin pai.

## Referências

- [[4.5.8/Estrutura/Arvore]]
- [[4.5.8/Lib/Bibliotecas]]
- [[4.5.8/Plugins/Tipos]]
