---
name: moodle-plugin-security
description: >-
  Hardens and reviews Moodle plugins for authz, CSRF, SQL, XSS, secrets, external
  APIs, and privacy. Use when the user mentions segurança, validate_context,
  sesskey, capability, XSS, SQL injection, oxywebapi, análise de plugins, LGPD,
  or privacy provider.
---

# Segurança de plugins Moodle

## Docs no vault

- `4.5.8/Seguranca/Funcoes.md` — catálogo de APIs
- `4.5.8/Seguranca/Checklist.md`
- `4.5.8/Seguranca/Anti-Padroes.md` — casos NTI reais
- `analise-moodle-plugins.md` (workspace Projetos/MOODLE)

## Mandatory pattern (external)

```php
$params = self::validate_parameters(...);
$context = \context_system::instance(); // ou course/module
self::validate_context($context);
require_capability('local/meu:view', $context);
```

`'capabilities'` em `db/services.php` **não** enforce.

## Mandatory pattern (page write)

```php
require_login($course);
require_capability('...', $context);
require_sesskey();
```

## Quick audit order

1. Todas as `classes/external/*` e `ajax => true`
2. Scripts PHP que alteram estado (GET sem sesskey?)
3. SQL com string interpolada / LIMIT cru
4. `curl_init` / SSL off / XML concat
5. Tokens/senhas em config ou UI
6. `doc/` ou PHP antigo no pacote
7. `privacy/provider.php`

## Output format when reviewing

Use severidade: Crítico / Alto / Médio / Baixo — com arquivo e correção em uma linha (estilo Anti-Padroes).
