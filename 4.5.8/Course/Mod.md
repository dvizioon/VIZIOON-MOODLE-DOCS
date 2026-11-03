# `course/mod.php` e `course/modedit.php`

`course/mod.php` não desenha o formulário da atividade. O cabeçalho do arquivo diz o contrato: *moves, adds, updates, duplicates or deletes modules in a course*. Quase todo caminho termina em `redirect()`. O único HTML que ele imprime é a confirmação de exclusão.

`course/modedit.php` é quem adiciona e atualiza, via `moodleform_mod`.

## Parâmetros que `mod.php` aceita

Lidos no topo com `optional_param`:

| Parâmetro | Tipo | Ação |
|-----------|------|------|
| `add` | alfanumérico | Nome do módulo (`forum`, `quiz`, …). Redireciona para `modedit.php` |
| `update` | int | `course_modules.id`. Redireciona para `modedit.php` |
| `duplicate` | int | Copia a atividade no mesmo curso |
| `delete` | int | Apaga, com confirmação |
| `hide` | int | Oculta |
| `show` | int | Mostra |
| `stealth` | int | Disponível mas não visível na página do curso |
| `copy` | int | Marca a atividade para mover (não duplica) |
| `cancelcopy` | bool | Cancela o modo mover |
| `moveto` | int | Solta antes de outro cm |
| `movetosection` | int | Solta numa seção |
| `indent` | int | Soma ao indent (pode ser negativo) |
| `groupmode` | int | `-1` significa "não mexer" |
| `course` | int | Usado na URL, não como alvo principal |
| `type` | alpha | Repassado no redirect de `add` |
| `sr` | int | Seção para a qual voltar. Menor que 0 vira `null` |
| `confirm` | bool | Segunda etapa do delete |

Toda ação que muda dados, exceto `add` e `update` (que só redirecionam), exige `confirm_sesskey()`.

A página chama `require_login()` sem curso antes de decidir o ramo. Cada ramo depois chama `require_login($course, false, $cm)` de novo, já com o módulo.

## `add` e `update` — só redirect

`add` exige também `id` (id do curso), `section` (número da seção), e lê opcionais `return` e `beforemod`. Monta a URL:

`/course/modedit.php?add=...&type=...&course=...&section=...&return=...&beforemod=...&sr=...`

`update` carrega o cm com `get_coursemodule_from_id('', $update, 0, true, MUST_EXIST)` e redireciona para `/course/modedit.php?update=<cmid>`.

O formulário, o `mod_*_add_instance` e o `mod_*_update_instance` rodam em `modedit.php`, que inclui `course/modlib.php`, `gradelib.php`, `completionlib.php` e `plagiarismlib.php`.

## `duplicate`

Exige as capabilities `moodle/backup:backuptargetimport` e `moodle/restore:restoretargetimport` no contexto do curso (as duas, via `require_all_capabilities`). Chama `duplicate_module($course, $cm)` — backup/restore interno, não um INSERT copiado à mão — e volta para `course_get_url(...)`.

## `delete`

Capability: `moodle/course:manageactivities` no contexto do módulo.

Sem `confirm` ou sem sesskey, imprime `$OUTPUT->confirm(...)` com botões sim/não. O sim aponta de volta para `course/mod.php` com `confirm=1`, `delete=<cmid>` e `sesskey`. O pagetype fica `mod-<modname>-delete`.

Com confirmação, chama `course_delete_module($cm->id)` e redireciona para a seção. Essa função (em `course/lib.php`) apaga o cm, a instância na tabela do módulo, notas, conclusão e dispara o evento de módulo removido.

## Mover (`copy`, `moveto`, `movetosection`, `cancelcopy`)

`copy` não copia. Grava na sessão:

- `$USER->activitycopy` = cm id
- `$USER->activitycopycourse`
- `$USER->activitycopyname`
- `$USER->activitycopysectionreturn`

`moveto` / `movetosection` leem `$USER->activitycopy`. Exigem `moodle/course:manageactivities`. `movetosection` coloca no fim da seção (`$beforecm = null`). `moveto` coloca antes do cm indicado. Os dois chamam `moveto_module($cm, $section, $beforecm)` e limpam as quatro chaves da sessão.

Se a sessão não está em modo mover, a exceção é `needcopy`.

`cancelcopy` só limpa a sessão e volta ao curso. Se o cm já não existe, `get_coursemodule_from_id` usa `IGNORE_MISSING`.

## Visibilidade

| Ação | Capability | Chamada |
|------|------------|---------|
| `hide` | `moodle/course:activityvisibility` | `set_coursemodule_visible($cm->id, 0)` |
| `show` | a mesma | `set_coursemodule_visible($cm->id, 1)` |
| `stealth` | a mesma | `set_coursemodule_visible($cm->id, 1, 0)` — visível para quem tem o link, oculto na página |

Quando a função retorna verdadeiro, dispara `\core\event\course_module_updated::create_from_cm(...)`.

## Indent e groupmode

Os dois exigem `moodle/course:manageactivities`.

`indent`: lê `id` do cm, soma `$cm->indent += $indent`, trava em 0 se ficar negativo, grava com `$DB->set_field('course_modules', 'indent', ...)`, chama `\course_modinfo::purge_course_module_cache` e `rebuild_course_cache($cm->course, false, true)`.

`groupmode` (valor `> -1`): `set_coursemodule_groupmode($cm->id, $groupmode)` e o mesmo evento `course_module_updated`.

## Nenhum parâmetro reconhecido

`throw new \moodle_exception('unknowaction')`. O código da string no core é esse, com o typo histórico `unknow`.

## O que fica em `modedit.php`

Responsabilidade separada, para não procurar no `mod.php`:

- Valida que `section` não passa de `course_get_format($course)->get_max_sections()` (comentário MDL-69431: número alto demais criava seções vazias no backup).
- Instancia `mod_<nome>_mod_form`, que estende `moodleform_mod` (`course/moodleform_mod.php`).
- No submit, `add_moduleinfo()` ou `update_moduleinfo()` em `course/modlib.php`. Essas funções chamam `mod_<nome>_add_instance` / `mod_<nome>_update_instance` do `lib.php` do módulo, gravam `course_modules` e `course_sections`, notas e conclusão.
- `showonly` (PARAM_TAGLIST) deixa um grupo de campos do form aberto e esconde o resto.

Arquivos vizinhos que também alteram módulos, fora do `mod.php`:

| Arquivo | Função |
|---------|--------|
| `course/modedit.php` | Criar e editar |
| `course/modlib.php` | `add_moduleinfo`, `update_moduleinfo`, delete helpers |
| `course/modduplicate.php` | Duplicar pela UI nova (o `mod.php?duplicate` continua válido) |
| `course/lib.php` | `course_delete_module`, `moveto_module`, `set_coursemodule_visible` |
| `lib/modinfolib.php` | Cache da lista de módulos do curso |

## Referências

- [[4.5.8/Plugins/Criar]]
- [[4.5.8/Estrutura/Arvore]]
