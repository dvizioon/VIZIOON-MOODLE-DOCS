# Moodle 4.5.8 — Documentação do código fonte

← [[README|APP-MOODLE — índice de versões]] · [[5.2/README|Moodle 5.2]]

Análise do checkout em `/home/daniel/Área de trabalho/Projetos/MOODLE/4.5.8`. Os fatos abaixo saem dos arquivos deste diretório, não do guia do 5.2.

## Identidade desta build

Definida em `version.php` na raiz:

| Campo | Valor neste checkout |
|-------|----------------------|
| `$version` | `2024100708.06` |
| `$release` | `4.5.8+ (Build: 20260130)` |
| `$branch` | `405` |
| `$maturity` | `MATURITY_STABLE` |
| PHP mínimo | `8.1.0` (`lib/phpminimumversionlib.php`, exigência desde o Moodle 4.4) |

O código mora na **raiz** do repositório. Não existe pasta `public/`. Essa pasta aparece a partir do Moodle 5.1. Caminhos do guia 5.2 como `public/lib/...` e `public/theme/...` correspondem aqui a `lib/...` e `theme/...`.

## O que este checkout tem e o que não tem

Presente no core 4.5.8:

- Subsistema de **IA** (`ai/`), com placements `courseassist` e `editor`, providers `openai` e `azureai`
- **Report Builder** nativo (`reportbuilder/`)
- **Hooks PSR-14** (`lib/classes/hook/manager.php`, classe `core\hook\manager`)
- **SMS** (`sms/`, tipo de plugin `smsgateway`)
- **Comunicação** (`communication/`)
- Roteador (`lib/classes/router.php`, flag `$CFG->routerconfigured`)
- Temas **Boost** e **Classic** apenas

Ausente neste checkout (existem nas notas do 5.2 porque aquele material mistura core com plugins do projeto):

- IOMAD
- plugins Oxygeni (`mod_oxymsteams`, `tool_oxytemppass`, `webservice_oxywebapi`, `block_oxymylib`)
- tema Ceuma
- fonte custom `report_activities`
- React 19, import map e `react_autoinit` — o front do 4.5.8 é **AMD (RequireJS) + Mustache**. YUI 2.9.0 / 3.18.1 ainda é carregado por compatibilidade (`lib/setup.php`)

`local/` só contém `readme.txt` e `upgrade.txt`. Não há plugin local instalado no código.

## Mapa da documentação

- [[4.5.8/Estrutura/Base|Estrutura base, version.php, $CFG e bootstrap]]
- [[4.5.8/Estrutura/Arvore|Árvore completa deste checkout]]
- [[4.5.8/Lib/Bibliotecas|Bibliotecas de lib/]]
- [[4.5.8/Admin/Administracao|Administração]]
- [[4.5.8/Course/Mod|course/mod.php e modedit.php]]
- [[4.5.8/Plugins/Tipos|Tipos de plugin (components.json)]]
- [[4.5.8/Plugins/Criar|Como um mod_ entra no core]]
- [[4.5.8/Plugins/Forms|Forms — mod_form, block edit_form, moodleform]]
- [[4.5.8/Plugins/Settings|Settings — settings.php por tipo de plugin]]
- [[4.5.8/Plugins/Exemplos|Exemplos reais deste core]]
- [[4.5.8/DB/Schema|XMLDB e $DB]]
- [[4.5.8/Classes/Persistent|core\persistent]]
- [[4.5.8/Classes/Helper|Funções de uso diário]]
- [[4.5.8/Eventos/Observer|Eventos e hooks]]
- [[4.5.8/WebServices/Criar|Web services REST e SOAP]]
- [[4.5.8/Templates/Mustache|Mustache]]
- [[4.5.8/Frontend/AMD|JavaScript AMD]]
- [[4.5.8/Estrutura/Report-Plugin|Plugins report_]]
- [[4.5.8/ReportBuilder/Fontes|Fontes do Report Builder]]
- [[4.5.8/Seguranca/Funcoes|Segurança — funções e APIs]]
- [[4.5.8/Seguranca/Checklist|Segurança — checklist do plugin]]
- [[4.5.8/Seguranca/Anti-Padroes|Segurança — anti-padrões (plugins NTI)]]
