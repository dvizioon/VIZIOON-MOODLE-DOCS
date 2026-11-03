# Report Builder no Moodle 4.5.8

Subsistema em `reportbuilder/`. Componente `core_reportbuilder`. Não é um `report_`. A UI fica em:

- `reportbuilder/index.php` — lista de relatórios customizados
- `reportbuilder/edit.php` — colunas, condições, filtros, ordenação
- `reportbuilder/view.php` — ver um relatório
- `reportbuilder/download.php` — exportar

Menu: categoria criada em `admin/settings/reportbuilder.php`. Capabilities em `lib/db/access.php`: `moodle/reportbuilder:view`, `moodle/reportbuilder:viewall`, `moodle/reportbuilder:edit`, `moodle/reportbuilder:editall`, `moodle/reportbuilder:scheduleviewas`.

As notas do 5.2 descrevem uma fonte **Atividades** do plugin `report_activities` (aluno × atividade com nota, mais uma fonte “Nota final”). Esse plugin **não está** neste checkout. As fontes que existem são as do core, cada uma uma classe que estende `core_reportbuilder\datasource`.

## Fontes neste código

| UI (entidade) | Classe | O que uma linha representa |
|---------------|--------|----------------------------|
| Usuários | `core_user\reportbuilder\datasource\users` | um usuário |
| Cursos | `core_course\reportbuilder\datasource\courses` | um curso |
| Categorias de curso | `core_course\reportbuilder\datasource\categories` | uma categoria |
| Participantes do curso | `core_course\reportbuilder\datasource\participants` | matrícula: usuário no curso, com papel, grupo, conclusão, último acesso |
| Coortes | `core_cohort\reportbuilder\datasource\cohorts` | uma coorte |
| Insígnias | `core_badges\reportbuilder\datasource\badges` | uma insígnia |
| Insígnias emitidas | `core_badges\reportbuilder\datasource\users` | insígnia concedida a um usuário |
| Competências | `core_competency\reportbuilder\datasource\competencies` | uma competência |
| Grupos | `core_group\reportbuilder\datasource\groups` | um grupo |
| Comentários | `core_comment\reportbuilder\datasource\comments` | um comentário |
| Tags | `core_tag\reportbuilder\datasource\tags` | uma tag |
| Anotações | `core_notes\reportbuilder\datasource\notes` | uma anotação |
| Blogs | `core_blog\reportbuilder\datasource\blogs` | um post |
| Arquivos | `core_files\reportbuilder\datasource\files` | um arquivo armazenado |
| Papéis | `core_role\reportbuilder\datasource\roles` | uma atribuição de papel |
| Logs de tarefa | `core_admin\reportbuilder\datasource\task_logs` | uma execução de scheduled task |

A fonte de participantes (`course/classes/reportbuilder/datasource/participants.php`) junta as entidades `user`, `course`, `course_category`, `enrolment`, `enrol`, `role`, `group`, `access` e `completion`. É o lugar do core para “quem está no curso”, não para nota de cada atividade.

Nota de atividade continua no livro (`grade/`) e nos relatórios `gradereport_*` (`grade/report/grader`, `grade/report/user`, `grade/report/overview`). Não há datasource de `grade_grades` neste core.

## Como uma fonte é feita

Classe em `<componente>/classes/reportbuilder/datasource/<nome>.php`:

```php
namespace core_course\reportbuilder\datasource;

use core_reportbuilder\datasource;

class participants extends datasource {
    public static function get_name(): string {
        return get_string('participants');
    }
    protected function initialise(): void {
        // add_entity(), set_main_table(), add_columns_from_entity(), add_filters_from_entity()
    }
    public function get_default_columns(): array { /* ... */ }
    public function get_default_filters(): array { /* ... */ }
}
```

A base `core_reportbuilder\datasource` está em `reportbuilder/classes/datasource.php`. Entidades reutilizáveis ficam em `reportbuilder/classes/local/entities/` (`user`, `course`) e em `<componente>/classes/reportbuilder/local/entities/`.

Coluna, filtro e condição são objetos do subsistema (`local/report/column`, `filter`, `aggregation`). Agregações (soma, média, contagem) já vêm no core; não é preciso calcular porcentagem 0–10 na fonte, como a fonte externa do 5.2 faz.

Audiência (quem pode ver o relatório customizado) é configurada na UI do próprio relatório. As tabelas estão no XMLDB do core, `lib/db/install.xml`: `reportbuilder_report`, `reportbuilder_column`, `reportbuilder_filter`, `reportbuilder_audience`, `reportbuilder_schedule`. Não há `reportbuilder/db/install.xml`; o subsistema não é um plugin.

## Exportar

`download.php` usa os plugins `dataformat_*` da pasta `dataformat/` (csv, excel, html, json, ods, pdf). O botão da view aponta para essa página com o id do relatório.

## Referências

- [[4.5.8/Estrutura/Report-Plugin]]
- [[4.5.8/Admin/Administracao]]
