# Selos (Awards) — Moodle Plugins directory / Marketplace

Os badges da página do plugin (ex.: **Privacy friendly**, **Automated testing support**, **Early bird 4.5**) são concedidos **automaticamente** na validação/revisão. Não se abre issue pedindo selo.

Skill Cursor/OpenCode/Claude: `moodle-marketplace-badges`.

---

## Privacy friendly

**Significado:** o plugin declara e implementa a Privacy API (GDPR/LGPD) de forma transparente.

### Checklist

| Passo | O quê |
|-------|--------|
| 1 | `classes/privacy/provider.php` no plugin |
| 2 | `null_provider` se **não** armazena PII; senão `metadata\provider` (+ export/delete) |
| 3 | String `privacy:metadata` em `lang/en/` (e pt_br) |
| 4 | Nova versão no Plugins directory — o robô detecta a API |

### Exemplo `report_activities` (null provider)

```php
namespace report_activities\privacy;

class provider implements \core_privacy\local\metadata\null_provider {
    public static function get_reason(): string {
        return 'privacy:metadata';
    }
}
```

```php
// lang/en/report_activities.php
$string['privacy:metadata'] = 'The Activities reports plugin does not store any personal data.';
```

Já existe no checkout `5.2/public/report/activities/`.

CI: `CI/ci-security.yml` falha se há `db/install.xml` sem privacy provider.

---

## Automated testing support (AUTO TEST)

**Significado:** o repositório tem suporte a testes automatizados reconhecidos na revisão.

| Precisa | Detalhe |
|---------|---------|
| Testes | PHPUnit (`tests/`) e/ou Behat (`tests/behat/`) |
| CI | `.github/workflows/*.yml` com `moodle-plugin-ci phpunit` / `behat` |
| Verde | Jobs passando |

Templates: [[CI/README]]. Sem testes no plugin → não deixe steps phpunit/behat no workflow (job falha e também não ganha o selo).

---

## Early bird X.Y

**Significado:** plugin pronto/aprovado cedo para a versão X.Y do Moodle (ex.: 4.5).

Depende de calendário e processo do Plugins directory (release compatível publicada cedo). Código: `$plugin->supported` / `$plugin->requires` corretos + CI na branch `MOODLE_XYY_STABLE`.

---

## Fluxo recomendado pra ganhar Privacy + AUTO TEST

1. Privacy provider + strings (`moodle-marketplace-badges`)
2. Escrever pelo menos 1 PHPUnit ou Behat mínimo
3. Copiar `CI/ci-quality.yml` + `ci-security.yml` + matrix de versões
4. Repo `moodle-report_activities` (ou frankenstyle do plugin)
5. Tag + upload no moodle.org/plugins

Ver também: [[4.5.8/Seguranca/Funcoes]] · [[_meta/Nomenclatura-GitHub]] · [[CI/README]]
