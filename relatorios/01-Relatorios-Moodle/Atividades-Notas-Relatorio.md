# Relatórios Personalizados - Atividades e Notas

## Resposta Rápida

**Sim, é possível incluir notas no relatório personalizado**, mas com limitações. Veja abaixo o que pode e o que não pode ser feito.

---

## O que PODE ser Incluído

### 1. Notas (Grade Items)

O construtor permite adicionar campos de nota:

**Campos disponíveis:**
- `grade_grades.finalgrade` - Nota final do aluno
- `grade_grades.feedback` - Feedback do professor
- `grade_grades.rawgrade` - Nota bruta
- `grade_grades.overridden` - Se a nota foi sobrescrita
- `grade_grades.excluded` - Se a nota foi excluída

**Como adicionar:**
1. Na criação do relatório, procure o grupo **"Notas"** ou **"Grade"**
2. Selecione os campos desejados
3. Configure filtros se necessário

### 2. Itens de Nota (Grade Items)

**Campos disponíveis:**
- `grade_items.itemname` - Nome da atividade
- `grade_items.grademax` - Nota máxima
- `grade_items.grademin` - Nota mínima
- `grade_items.gradetype` - Tipo (valor, escala, texto)

### 3. Conclusão de Atividade (Activity Completion)

**Campos disponíveis:**
- `course_modules_completion.completed` - Se concluiu (1) ou não (0)
- `course_modules_completion.timecompleted` - Data de conclusão
- `course_modules_completion.view观let` - Se visualizou
- `course_modules_completion.overridden` - Se foi sobrescrito

---

## O que NÃO pode ser Incluído (diretamente)

### 1. Dados Específicos de Atividade

O construtor **não permite** adicionar campos específicos de cada tipo de atividade:

| Atividade | Campo não disponível |
|---|---|
| **Quiz** | Tentativas, respostas individuais, tempo gasto |
| **Assignment** | Data de entrega, status de envio, arquivos enviados |
| **Forum** | Posts, comentários, likes |
| **Workshop** | Avaliações entre pares |
| **Choice** | Resposta escolhida |

### 2. Logs Detalhados

O construtor **não mostra** logs detalhados de acesso. Para isso, use o Relatório de Logs padrão.

---

## Alternativas para Relatórios com Atividades

### Opção 1: Usar o Relatório de Conclusão

**Caminho:** Curso > Mais > Relatórios > Conclusão

Este relatório mostra:
- Todas as atividades do curso
- Status de conclusão de cada aluno
- Data de conclusão

**É mais completo** que o construtor para este fim.

### Opção 2: Usar o Relatório de Atividade

**Caminho:** Curso > Mais > Relatórios > Atividade

Este relatório mostra:
- Resumo de cada atividade
- Visualizações
- Envios
- Nota média

### Opção 3: Relatório de Notas (Grade Report)

**Caminho:** Curso > Notas > Relatório do avaliador

Este relatório mostra:
- Matriz completa (alunos × atividades)
- Nota de cada aluno em cada atividade
- Total do curso

### Opção 4: Web Services (API)

Se precisar de dados específicos de atividades, use a API:

```php
// Obter tentativas de quiz
$functionname = 'mod_quiz_get_user_attempts';
$params = ['quizid' => $quizid, 'userid' => $userid];

// Obter envios de assignment
$functionname = 'mod_assign_get_submissions';
$params = ['assignmentids' => [$assignmentid]];

// Obter posts do forum
$functionname = 'mod_forum_get_forum_discussions';
$params = ['forumid' => $forumid];
```

### Opção 5: Fonte **Atividades** (plugin `report_activities`)

No Construtor de Relatórios (Moodle 5.2 deste projeto), use a fonte **Atividades**:

1. Relatórios → Construtor de relatórios → Novo relatório
2. Fonte: **Atividades**
3. Colunas padrão: usuário, curso, nome/tipo da atividade, %, nota 0–10, nota final

Documentação técnica: [[../../5.2/ReportBuilder/Fonte-Atividades|Fonte Atividades]]

### Opção 6: Outros plugins customizados

Para relatórios muito específicos, considere:
- **Custom Reports** (plugin da comunidade)
- **Configurable Reports** (plugin avançado)
- Desenvolvimento de plugin próprio (ver [[../../5.2/Estrutura/Report-Plugin|Report-Plugin]])

---

## Exemplo: Relatório com Notas

### Configuração no Construtor

1. **Nome:** "Notas por Atividade"
2. **Fonte:** Curso
3. **Campos:**
   - `user.firstname` - Nome
   - `user.lastname` - Sobrenome
   - `grade_items.itemname` - Atividade
   - `grade_grades.finalgrade` - Nota
   - `grade_grades.feedback` - Feedback

4. **Agrupamento:** `grade_items.itemname`

5. **Ordenação:** `user.lastname`

### Resultado

```
João Silva | Prova P1 | 8.5 | "Bom trabalho"
João Silva | Trabalho 1 | 7.0 | "Pode melhorar"
Maria Santos | Prova P1 | 9.0 | "Excelente"
Maria Santos | Trabalho 1 | 8.5 | "Muito bom"
```

---

## Resumo

| Dado | Pode incluir? | Como? |
|---|---|---|
| Notas | ✅ Sim | Campos grade_grades |
| Itens de nota | ✅ Sim | Campos grade_items |
| Conclusão | ✅ Sim | Campos course_modules_completion |
| Feedback | ✅ Sim | Campo grade_grades.feedback |
| Tentativas de quiz | ❌ Não | Usar relatório padrão |
| Envios de assignment | ❌ Não | Usar relatório padrão |
| Posts do forum | ❌ Não | Usar relatório padrão |
| Logs detalhados | ❌ Não | Usar relatório de logs |

---

## Dica Final

Para relatórios completos com atividades, combine:
1. **Relatório personalizado** para notas e conclusão
2. **Relatório de atividade** para resumo das atividades
3. **Relatório de logs** para detalhes de acesso
