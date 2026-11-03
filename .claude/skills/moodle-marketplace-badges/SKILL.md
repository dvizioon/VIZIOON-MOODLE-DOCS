---
name: moodle-marketplace-badges
description: >-
  Earns Moodle Plugins directory / Marketplace awards: Privacy friendly,
  Automated testing support, and Early bird. Use when the user mentions selo,
  badge, Privacy friendly, AUTO TEST, Early bird, GDPR, privacy provider,
  report_activities badges, or publishing to moodle.org/plugins.
---

# Selos Moodle Marketplace (Plugins directory)

Selos são **automáticos** na revisão/validação — não se pede por issue.  
Doc vault: `_meta/Marketplace-Selos.md`

## Privacy friendly

Indica Privacy API (GDPR/LGPD) correta.

### Se o plugin NÃO guarda PII (ex.: `report_activities` só lê notas)

`classes/privacy/provider.php`:

```php
namespace report_activities\privacy;

class provider implements \core_privacy\local\metadata\null_provider {
    public static function get_reason(): string {
        return 'privacy:metadata';
    }
}
```

`lang/en/<component>.php` (+ pt_br):

```php
$string['privacy:metadata'] = 'The Activities reports plugin does not store any personal data.';
```

### Se guarda dados / preferências

Implementar `\core_privacy\local\metadata\provider` (+ export/delete user data conforme o caso).

Checklist: arquivo existe · namespace autoload · string `privacy:metadata` · nova versão no Plugins directory.

## Automated testing support (AUTO TEST)

Repo com testes que o CI/revisão enxerga:

1. PHPUnit em `tests/` e/ou Behat em `tests/behat/*.feature`
2. `.github/workflows/ci.yml` com `moodle-plugin-ci phpunit` / `behat` (templates em `CI/`)
3. Testes **passando** na matrix

Sem testes → remova steps do CI; **sem** este selo.

Skill: `moodle-plugin-ci`.

## Early bird X.Y

Plugin atualizado/aprovado cedo para a release (ex.: Early bird 4.5).  
Exige release compatível publicada no directory pouco após o Moodle X.Y — processo editorial HQ, não só código.

## Antes de publicar versão

1. Privacy provider + strings
2. CI verde (quality + versions + databases + security)
3. Tag/release GitHub `moodle-<tipo>_<nome>`
4. Upload no Plugins directory

Exemplo vivo: `report_activities` já tem `null_provider` + `privacy:metadata` en/pt_br.
