# Relatórios no Moodle

## Tipos de Relatórios Padrão

### 1. Relatório de Logs

**Caminho:** Curso > Mais > Relatórios > Logs

**O que mostra:** Todas as ações dos alunos e professores.

**Dados exibidos:**
- Data e hora da ação
- Nome do aluno
- Ação realizada
- Activity
- IP de acesso

**Como usar:**
1. Acesse o curso
2. Clique em "Mais"
3. Clique em "Relatórios"
4. Selecione "Logs"
5. Filtre por: período, aluno, atividade

---

### 2. Relatório de Atividade

**Caminho:** Curso > Mais > Relatórios > Atividade

**O que mostra:** Resumo de todas as atividades do curso.

**Dados exibidos:**
- Nome da atividade
- Tipo (forum, quiz, assignment)
- Visualizações
- Envios
- Nota média

---

### 3. Relatório de Conclusão

**Caminho:** Curso > Mais > Relatórios > Conclusão

**O que mostra:** Quais alunos concluíram quais atividades.

**Pré-requisito:** Ativar "Rastreamento de conclusão" nas configurações do curso.

---

### 4. Relatório de Notas

**Caminho:** Curso > Notas > Relatório do avaliador

**O que mostra:** Matriz de notas (alunos × atividades).

---

### 5. Relatório de Participação

**Caminho:** Curso > Mais > Relatórios > Participation

**O que mostra:** Quais alunos participaram de atividades específicas.

---

## Relatórios Personalizados (Custom Reports)

### O que são?

Relatórios personalizados permitem criar relatórios customizados no Moodle, selecionando colunas específicas, filtros, agrupamentos e ordenação.

### Pré-requisito

O Moodle 5.2 já vem com o **Relatórios Customizados** integrado. Não precisa instalar nada.

### Como Criar um Relatório Personalizado

#### Passo 1: Acessar

1. **Curso > Mais > Relatórios > Relatórios customizados**
2. Ou: **Administração do Site > Relatórios > Relatórios customizados**

#### Passo 2: Criar Novo Relatório

1. Clique em **"Criar relatório"**
2. Preencha:
   - **Nome:** "Relatório de Notas por Atividade"
   - **Descrição:** "Lista de notas dos alunos por atividade"
   - **Tipo:** Selecione o contexto (Curso, Usuário, etc.)

#### Passo 3: Adicionar Colunas

1. Clique em **"Adicionar coluna"**
2. Selecione os campos desejados:

| Campo                   | Descrição             |
| ----------------------- | --------------------- |
| user.firstname          | Nome do aluno         |
| user.lastname           | Sobrenome do aluno    |
| user.email              | Email do aluno        |
| grade_items.itemname    | Nome da atividade     |
| grade_grades.finalgrade | Nota final            |
| grade_grades.feedback   | Feedback do professor |
| course.fullname         | Nome do curso         |

3. Repita para cada coluna desejada

#### Passo 4: Adicionar Filtros

1. Clique em **"Adicionar filtro"**
2. Selecione o campo e a condição:

| Filtro | Exemplo |
|---|---|
| grade_grades.finalgrade >= | 7 (notas maiores que 7) |
| grade_grades.finalgrade <= | 10 (notas menores que 10) |
| user.firstname LIKE | %João% (alunos com "João" no nome) |
| grade_items.itemname = | "Prova P1" (apenas uma atividade) |
| course.id = | ID do curso específico |

#### Passo 5: Adicionar Agrupamento

1. Clique em **"Adicionar agrupamento"**
2. Selecione o campo:

| Agrupamento | Quando usar |
|---|---|
| user.lastname | Agrupar por sobrenome |
| grade_items.itemname | Agrupar por atividade |
| course.fullname | Agrupar por curso |

#### Passo 6: Adicionar Ordenação

1. Clique em **"Adicionar ordenação"**
2. Selecione o campo e a direção:

| Ordenação | Direção |
|---|---|
| user.lastname | Ascendente (A-Z) |
| grade_grades.finalgrade | Descendente (maior nota primeiro) |

#### Passo 7: Salvar e Visualizar

1. Clique em **"Salvar"**
2. Clique em **"Executar"**
3. Veja o relatório gerado

### Exemplo: Relatório de Notas Acima da Média

**Configuração:**
- **Colunas:** user.firstname, user.lastname, grade_grades.finalgrade
- **Filtro:** grade_grades.finalgrade >= 7
- **Ordenação:** grade_grades.finalgrade (descendente)

**Resultado:** Lista de alunos com nota >= 7, do maior para o menor.

---

## Exemplos de Relatórios Práticos

### 1. Relatório de Notas por Atividade

**Colunas:**
- user.firstname
- user.lastname
- grade_items.itemname
- grade_grades.finalgrade

**Filtro:** Nenhum (mostrar todos)

**Ordenação:** grade_items.itemname, user.lastname

### 2. Relatório de Alunos Reprovados

**Colunas:**
- user.firstname
- user.lastname
- user.email
- grade_grades.finalgrade
- grade_items.itemname

**Filtro:** grade_grades.finalgrade < 6

**Ordenação:** user.lastname

### 3. Relatório de Atividades Mais Difíceis

**Colunas:**
- grade_items.itemname
- AVG(grade_grades.finalgrade) como "Nota Média"
- COUNT(grade_grades.id) como "Total de Respostas"

**Agrupamento:** grade_items.itemname

**Ordenação:** Nota Média (ascendente - mais difícil primeiro)

### 4. Relatório de Participação por Fórum

**Colunas:**
- user.firstname
- user.lastname
- forum_posts.id como "Total de Posts"

**Filtro:** forum_posts.course = ID do curso

**Agrupamento:** user.lastname

### 5. Relatório de Conclusão de Curso

**Colunas:**
- user.firstname
- user.lastname
- course_completions.timecompleted
- course_completions.reaggregate

**Filtro:** course_completions.timecompleted IS NOT NULL

**Ordenação:** course_completions.timecompleted (descendente)

---

## Exportar Relatórios

### Exportar como CSV

1. No relatório executado
2. Clique em **"Exportar"**
3. Selecione **"CSV"**
4. O arquivo é baixado

### Exportar como Excel

1. No relatório executado
2. Clique em **"Exportar"**
3. Selecione **"Excel"**
4. O arquivo .xlsx é baixado

### Exportar como PDF

1. No relatório executado
2. Clique em **"Exportar"**
3. Selecione **"PDF"**
4. O arquivo PDF é baixado

---

## Dicas de Relatórios Personalizados

### 1. Use Filtros Inteligentes

| Filtro | Uso |
|---|---|
| date | Filtrar por período |
| is null / is not null | Encontrar registros vazios/preenchidos |
| greater than / less than | Comparar valores |
| like | Buscar por texto parcial |

### 2. Agrupe para Organizar

| Agrupamento | Resultado |
|---|---|
| Por aluno | Lista completa por aluno |
| Por atividade | Lista completa por atividade |
| Por curso | Lista completa por curso |
| Por período | Lista por data |

### 3. Use Colunas Calculadas

O Moodle permite criar colunas com expressões:
- `AVG(grade_grades.finalgrade)` - Média
- `COUNT(grade_grades.id)` - Quantidade
- `MAX(grade_grades.finalgrade)` - Máximo
- `MIN(grade_grades.finalgrade)` - Mínimo

### 4. Salve Relatórios Úteis

1. Crie o relatório
2. Clique em **"Salvar"**
3. Dê um nome descritivo
4. Acesse depois em **"Meus relatórios"**

### 5. Compartilhe com Outros Professores

1. Salve o relatório
2. Configure as permissões
3. Outros professores podem copiar e usar

---

## Relatórios via Web Services (API)

### Acessar Relatórios via API

```php
// Chamada para obter notas via web service
$functionname = 'core_grades_get_grades';
$params = [
    'courseid' => $courseid,
    'itemids' => [$itemid],
];
$result = $DB->get_records_sql("
    SELECT u.firstname, u.lastname, g.finalgrade
    FROM {user} u
    JOIN {grade_grades} g ON (u.id = g.userid)
    JOIN {grade_items} gi ON (g.itemid = gi.id)
    WHERE gi.courseid = :courseid
", ['courseid' => $courseid]);
```

### Endpoints Disponíveis

| Função | Descrição |
|---|---|
| core_grades_get_grades | Obter notas |
| core_grades_get_grade_items | Obter itens de nota |
| core_report_get_ordered_reports | Listar relatórios |
| core_report_get_report_data | Obter dados do relatório |

---

## Relatórios no IOMAD (Multi-Tenancy)

Se você usa IOMAD, existem relatórios adicionais:

| Relatório | Descrição |
|---|---|
| Companies | Relatório de empresas |
| Completion | Conclusão por empresa |
| License Usage | Uso de licenças |
| User Logins | Logs de acesso |
| Attendance | Presença em treinamentos |

**Caminho:** Site administration > IOMAD > Reports

---

## Exportação

| Formato | Quando usar |
|---|---|
| ODS | LibreOffice |
| XLS | Excel |
| TXT | Sistemas externos |
| XML | Integração |
| PDF | Impressão |
| CSV | Análise em outro sistema |
