# Report Builder — Fonte "Atividades"

Plugin: `report_activities`  
Moodle: **5.2**  
Caminho: `public/report/activities/`

## O que é

Fonte de relatório do **Construtor de Relatórios** (`/reportbuilder/index.php`) chamada **Atividades**.

Cada linha do relatório = **um aluno × uma atividade com nota** (quiz, tarefa, fórum avaliado, etc.).



## Fontes neste plugin

| Fonte (UI) | Classe | O que lista |
|------------|--------|-------------|
| **Atividades** | `...\datasource\activities` | Aluno × atividade com nota (%, 0–10, nota da atividade) |
| **Nota final** | `...\datasource\coursefinal` | Aluno × total do caderno do curso (`itemtype = course`), já com fórmula |

O plugin é do tipo **`report_`** (não `local_`), o mesmo tipo dos relatórios do core (`report_log`, `report_outline`, …). As fontes do Report Builder ficam em `classes/reportbuilder/datasource/`.

### Se você tinha instalado `report_activities`

1. Remova/desinstale o plugin local antigo (Administração → Plugins → Plugins locais), se ainda aparecer.
2. Instale `report_activities` via Notificações / upgrade.
3. Relatórios já criados com a fonte antiga precisam ser recriados (a classe mudou de namespace).

## Onde aparece

1. Administração do site → Relatórios → Construtor de relatórios  
   ou: `https://seu-moodle/reportbuilder/index.php`
2. **Novo relatório**
3. Em **Fonte do relatório**, grupo do plugin **Atividades**, opção **Atividades**

## Dados disponíveis

| Grupo | Campos |
|-------|--------|
| **Usuário** | Nome, e-mail, ID, perfil, campos customizados (entidade core) |
| **Curso** | Nome, shortname, URL, datas, visibilidade… |
| **Categoria do curso** | Nome, caminho, ID… |
| **Atividade** | Nome da atividade, tipo (Questionário, Tarefa…), nota máx/mín |
| **Nota** | Nota da atividade no caderno, nota bruta, **porcentagem**, **nota 0–10**, feedback, data |

### Porcentagem e nota 0–10

- **Porcentagem:** `((finalgrade - grademin) / (grademax - grademin)) * 100` → ex.: `73%`
- **Nota (0–10):** mesma proporção × 10, arredondamento half-up (`PHP_ROUND_HALF_UP`)
  - `7.3` → `7`
  - `7.5` → `8`
  - `7.6` → `8`

## Colunas padrão (ao criar o relatório)

1. Usuário (nome com link)
2. Curso (nome com link)
3. Nome da atividade
4. Tipo de atividade
5. Porcentagem
6. Nota (0–10)
7. Nota final (valor da atividade no caderno)

O total do curso **não** entra nesta fonte. Use a fonte **Nota final**.

## Fonte Nota final

Mesmo grupo do plugin. Uma linha = **um aluno × o total do caderno daquele curso**.

O valor exibido é o retorno de `grade_get_course_grades()` (`public/grade/querylib.php`): o total do curso já agregado, com os pesos do caderno. Se o curso estiver marcado para recálculo, essa função recalcula antes de devolver o número. A consulta só lista aluno e curso; não monta a nota.

Colunas padrão: usuário, curso, nota final.

## Revisão plugins.moodle.org (1.3.5)

- `LICENSE` (GPL-3.0)
- README em inglês (`README.md`); PT em `README.pt_br.md`
- Feedback com `format_text` + `feedbackformat`; nome da atividade com `format_string`
- Capability `report/activities:view` usada em `index.php` e `settings.php`
- Release com `git archive` (sem `.git`); `screenshots/` em `export-ignore`
- Nome de repo recomendado: `moodle-report_activities`

Upgrade `2026101600`.

## Filtros padrão (Atividades)

- Curso
- Tipo de atividade
- Nome da atividade
- Usuário

## Estrutura do plugin

```
report/activities/
├── version.php
├── classes/
│   ├── privacy/provider.php          # null_provider
│   └── reportbuilder/
│       ├── datasource/activities.php # Fonte "Atividades"
│       └── local/entities/
│           ├── grade_item.php        # Atividade (grade_items)
│           └── grade.php             # Nota (grade_grades)
└── lang/
    ├── en/report_activities.php
    └── pt_br/report_activities.php
```

## Como o Report Builder descobre a fonte

`core_reportbuilder\manager::get_report_datasources()` varre todas as classes em:

```
*\reportbuilder\datasource\*
```

que estendem `core_reportbuilder\datasource` e estão disponíveis.

Namespace usado:

```
report_activities\reportbuilder\datasource\activities
```

## Modelo SQL (conceitual)

```sql
FROM grade_grades gg
JOIN grade_items gi ON gi.id = gg.itemid AND gi.itemtype = 'mod'
JOIN user u ON u.id = gg.userid AND u.deleted = 0
JOIN course c ON c.id = gi.courseid
LEFT JOIN course_categories cc ON cc.id = c.category
```

`itemtype = 'mod'` exclui totais de categoria e nota do curso — só atividades.

## Instalação / upgrade

```bash
cd public
php admin/cli/upgrade.php --non-interactive
```

Ou: Administração → Notificações.

## Capabilidades

Não define capabilities próprias. Usa as do Report Builder:

- `moodle/reportbuilder:edit`
- `moodle/reportbuilder:view`

## Privacidade

Não grava dados próprios (`null_provider`). Lê `grade_*`, `user`, `course` já existentes.

## Exemplo de uso

1. Criar relatório → fonte **Atividades**
2. Condição: Tipo de atividade = Questionário (se quiser só quizzes)
3. Filtro: Curso = "Curso X"
4. Exportar CSV / agendar envio

## Relacionado

- [[../Estrutura/Report-Plugin|Plugins de relatório clássicos]]
- [[../../relatorios/01-Relatorios-Moodle/Construtor-Relatorios|Construtor de Relatórios]]
- [[../../relatorios/01-Relatorios-Moodle/Atividades-Notas-Relatorio|Atividades e Notas]]
