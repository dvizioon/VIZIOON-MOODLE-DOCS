# Construtor de Relatórios Personalizados - Guia Completo

## O que é o Construtor de Relatórios?

O Construtor de Relatórios é a ferramenta do Moodle para criar relatórios personalizados. Ele permite selecionar exatamente quais campos aparecem, filtrar, agrupar e exportar dados.

---

## Tela de Criação do Relatório

### Campo: Nome

**O que é:** Título do relatório

**Exemplo:** "Relatório de Frequência por Curso"

**Dica:** Use um nome descritivo que identifique facilmente o relatório.

---

### Campo: Fonte do Relatório

**O que é:** De onde vêm os dados

**Opções:**
- **Curso** - Dados de um curso específico
- **Usuário** - Dados dos usuários
- **Frequência** - Dados de presença/frequência
- **Atividades** (`report_activities`) - Aluno + tipo de atividade + nota (%, 0–10, final)
- **Sistema** - Dados globais do site

**Exemplo:** Se quer ver notas por atividade, selecione **Atividades**. Se quer ver presença, selecione "Frequência".

Doc: [[../../5.2/ReportBuilder/Fonte-Atividades|Fonte Atividades]]

---

### Seção: Anotações

**O que são:** Notas pessoais sobre o relatório

**Opções:**
- **Incluir configuração padrão** - Usa as configurações automáticas
- **Remover qualquer linha duplicada** - Evita dados repetidos

---

### Seção: Tags

**O que são:** Palavras-chave para organizar relatórios

**Como usar:**
1. Clique em "Gerenciar tags"
2. Adicione tags como: "frequência", "notas", "relatório mensal"
3. As tags ajudam a encontrar o relatório depois

---

## Campos Disponíveis para Selecionar

### Grupo: AUDIÊNCIA

Estes campos controlam quem pode ver o relatório.

| Campo | Descrição |
|---|---|
| **Audiência** | Quem tem acesso ao relatório |
| **Cronogramas** | Quando o relatório é executado |
| **Acesso** | Permissões de acesso |

---

### Grupo: EDITOR

Estes campos são usados para criar e editar o relatório.

---

### Grupo: FREQUÊNCIA

Estes campos são usados para relatórios de presença/aula.

#### Campos de Sessão

| Campo | Descrição | Exemplo de uso |
|---|---|---|
| **Nome** | Nome da sessão/aula | "Aula 1 - Introdução" |
| **Descrição da sessão** | O que foi ensinado | "Capítulo 1 do livro" |
| **Data da sessão** | Quando aconteceu | "21/09/2026" |
| **Duração da sessão** | Quanto tempo durou | "2 horas" |
| **Tempo da última sessão (professor)** | Última vez que o professor registrou | "21/09/2026 10:09" |
| **Sessão do usuário registrada** | Se o aluno estava presente | "Sim" / "Não" |
| **Status da sessão do usuário** | Código de presença | "Pr" (Presente), "Au" (Ausente), "At" (Atrasado), "Di" (Dispensado) |
| **Nota da sessão do usuário** | Nota pela participação | "2.00" |
| **Observações da sessão do usuário** | Anotações do professor | "Participou ativamente" |

#### Campos de Estatísticas

| Campo | Descrição |
|---|---|
| **Número de sessões realizadas** | Quantas aulas o aluno assistiu |
| **Pontos durante as sessões realizadas** | Nota total nas aulas presentes |
| **Porcentagem durante as sessões realizadas** | % de presença nas aulas feitas |
| **Número total de sessões** | Total de aulas do curso |
| **Pontos em todas as sessões** | Nota total considerando todas as aulas |
| **Porcentagem em todas as sessões** | % de presença geral |
| **Pontos possíveis máximos** | Nota máxima possível |
| **Porcentagem possível máxima** | 100% de presença |

#### Campos de Status por Período

| Campo | Descrição |
|---|---|
| **Status Pr - Contagem total** | Total de presenças |
| **Status Pr - Contagem total para a semana atual** | Presenças esta semana |
| **Status Pr - Contagem total para a semana anterior** | Presenças semana passada |
| **Status Au - Contagem total** | Total de ausências |
| **Status Au - Contagem total para a semana atual** | Ausências esta semana |
| **Status Au - Contagem total para a semana anterior** | Ausências semana passada |
| **Status At - Contagem total** | Total de atrasos |
| **Status At - Contagem total para a semana atual** | Atrasos esta semana |
| **Status At - Contagem total para a semana anterior** | Atrasos semana passada |
| **Status Di - Contagem total** | Total de dispensas |
| **Status Di - Contagem total para a semana atual** | Dispensas esta semana |
| **Status Di - Contagem total para a semana anterior** | Dispensas semana passada |

---

### Grupo: USUÁRIO

Estes campos mostram informações dos alunos/usuários.

#### Dados Pessoais

| Campo                                                         | Descrição                   | Exemplo                |
| ------------------------------------------------------------- | --------------------------- | ---------------------- |
| **Nome completo**                                             | Nome + Sobrenome            | "João Silva"           |
| **Nome completo com link**                                    | Nome clicável para o perfil | [João Silva](link)     |
| **Nome completo com foto**                                    | Foto + Nome                 | 🖼️ João Silva         |
| **Nome completo com foto e link**                             | Foto + Nome clicável        | [🖼️ João Silva](link) |
| **Imagem**                                                    | Apenas a foto               | 🖼️                    |
| p´[;]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]**Nome** | Apenas o primeiro nome      | "João"                 |
| **Sobrenome**                                                 | Apenas o sobrenome          | "Silva"                |

#### Contato

| Campo | Descrição |
|---|---|
| **Endereço de e-mail** | Email do usuário |
| **Cidade/Município** | Cidade de residência |
| **País** | País de residência |
| **Fone** | Telefone fixo |
| **Telefone celular** | Telefone celular |
| **Endereço** | Endereço completo |

#### Configurações

| Campo | Descrição |
|---|---|
| **Idioma** | Idioma preferido |
| **Zona de fuso horário** | Fuso horário |
| **Tema** | Tema visual escolhido |
| **Descrição** | Biografia do usuário |
| **Autenticação** | Método de login (email, LDAP, etc.) |

#### Dados Acadêmicos

| Campo | Descrição |
|---|---|
| **Número de identificação** | Matrícula ou ID |
| **Instituição** | Instituição de vínculo |
| **Departamento** | Departamento |
| **CPF** | CPF do usuário |
| **BOLSISTA** | Se é bolsista (campo customizado) |

#### Atividade

| Campo | Descrição |
|---|---|
| **Primeiro acesso** | Data do primeiro login |
| **Último acesso** | Data do último login |
| **Último endereço de IP** | IP da última conexão |
| **Suspenso** | Se a conta está suspensa |
| **Confirmado** | Se o email foi confirmado |
| **Identificação de usuário** | Username |
| **Data/Hora da criação** | Quando a conta foi criada |
| **Hora de modificação** | Última modificação |

---

### Grupo: CURSO

Estes campos mostram informações do curso.

#### Dados do Curso

| Campo | Descrição |
|---|---|
| **Nome completo do curso com link** | Nome clicável para o curso |
| **Nome breve do curso com link** | Shortname clicável |
| **"ID number" do curso com link** | ID number clicável |
| **URL do curso** | Link direto para o curso |
| **Nome completo do curso** | Nome sem link |
| **Nome breve do curso** | Shortname sem link |
| **Número de identificação do curso** | ID number sem link |
| **Sumário do curso** | Descrição do curso |
| **Formato** | Formato (semanal, por tópicos, etc.) |

#### Configurações do Curso

| Campo | Descrição |
|---|---|
| **Data de início do curso** | Quando o curso começa |
| **Data de término do curso** | Quando o curso termina |
| **Visibilidade do curso** | Visível ou oculto |
| **Modalidade grupo** | Modalidade (ensino, empresa, etc.) |
| **Forçar modalidade grupo** | Forçar modalidade |
| **Forçar idioma** | Idioma forçado |
| **Forçar calendário** | Calendário forçado |
| **Tema** | Tema do curso |
| **Ativar acompanhamento de conclusão** | Se completion tracking está ativo |
| **Baixar o conteúdo do curso** | Se download está permitido |

#### Categoria do Curso

| Campo | Descrição |
|---|---|
| **Categoria do curso** | Categoria onde está |
| **Nome da categoria** | Nome da categoria |
| **Nome da categoria com link** | Nome clicável |
| **Caminho de categoria** | Hierarquia (ex: "Matemática > Álgebra") |
| **Número ID da categoria** | ID da categoria |
| **Descrição** | Descrição da categoria |
| **Tema** | Tema da categoria |
| **Contagem de cursos** | Quantos cursos na categoria |

---

### Grupo: FREQUÊNCIA (Combinação)

Estes campos combinam dados de múltiplas tabelas.

| Campo | Descrição |
|---|---|
| **Curso • Nome completo do curso** | Nome do curso junto com dados de frequência |
| **Frequência • Nome** | Nome da sessão |
| **Usuário • Nome completo** | Nome do aluno |
| **Frequência • Data da sessão** | Data da aula |
| **Frequência • Sessão do usuário registrada** | Se estava presente |
| **Frequência • Status da sessão do usuário** | Código de presença |
| **Frequência • Nota da sessão do usuário** | Nota pela participação |

---

## Agregação

### O que é?

A agregação controla como os dados são resumidos quando há múltiplos registros.

### Opções

| Agregação | Quando usar |
|---|---|
| **Sem agregação** | Mostrar todos os registros individuais |
| **Contar** | Contar quantos registros existem |
| **Soma** | Somar valores numéricos |
| **Média** | Calcular média |
| **Mínimo** | Menor valor |
| **Máximo** | Maior valor |

### Exemplo

Se você tem 5 registros de presença para um aluno:
- **Sem agregação:** Mostra 5 linhas
- **Contar:** Mostra "5"
- **Soma:** Mostra a soma das notas
- **Média:** Mostra a média das notas

---

## Exemplo Prático: Relatório de Frequência

### Configuração

1. **Nome:** "Relatório de Frequência - Setembro 2026"
2. **Fonte:** Frequência
3. **Campos selecionados:**
   - Curso • Nome completo do curso
   - Frequência • Nome
   - Usuário • Nome completo
   - Frequência • Data da sessão
   - Frequência • Sessão do usuário registrada
   - Frequência • Status da sessão do usuário
   - Frequência • Nota da sessão do usuário

### Resultado

```
Curso Daniel | PRESENÇA - REGIMENTAL | Gabrielle Brasil | 21/09/2026 | Pr | 2.00
Curso Daniel | PRESENÇA - REGIMENTAL | Lucas Campos | 21/09/2026 | Pr | 2.00
CURSO FIC | Presença | Jose Paulo | 31/08/2026 | Pr | 2.00
```

---

## Agendamento

### O que é?

O agendamento permite que o relatório seja executado automaticamente.

### Configuração

| Campo | Descrição | Exemplo |
|---|---|---|
| **Formato** | Formato do arquivo | CSV, Excel, PDF |
| **Iniciando em** | Data/hora inicial | 22/09/2026 14:16 |
| **Recorrência** | Frequência | Nenhum, Diário, Semanal, Mensal |

### Opções de Recorrência

| Recorrência | Quando executa |
|---|---|
| **Nenhum** | Uma única vez |
| **Diário** | Todo dia |
| **Semanal** | Toda semana |
| **Mensal** | Todo mês |

### Ver o Relatório Como

| Opção | Descrição |
|---|---|
| **Agendamento criado** | Mostra que o agendamento foi criado |

---

## Audiência

### O que é?

A audiência controla quem pode ver o relatório.

### Campos

| Campo | Descrição |
|---|---|
| **Audiência** | Grupo de pessoas |
| **Não existem públicos-alvo** | Nenhum público configurado |

---

## Mensagem

### O que é?

Configuração de email para enviar quando o relatório é executado.

### Campos

| Campo | Descrição |
|---|---|
| **Assunto** | Assunto do email |
| **Corpo** | Texto do email |

---

## Avançado

### O que são?

Configurações avançadas de acesso e busca.

### Campos

| Campo | Descrição |
|---|---|
| **Pesquisar** | Campos de busca |
| **Site** | Escopo do site |
| **Administradores do site** | Quem são os admins |
| **Membro do coorte** | Filtrar por coorte |
| **Papel do sistema atribuído** | Filtrar por papel |
| **Todos os usuários** | Incluir todos |
| **Usuários adicionados manualmente** | Apenas adicionados manualmente |

---

## Resumo dos Campos

### Por Categoria

| Categoria | Campos | Para que serve |
|---|---|---|
| **Audiência** | Acesso, Cronogramas | Controle de quem vê |
| **Frequência** | Sessão, Status, Notas | Presença dos alunos |
| **Usuário** | Dados pessoais, Contato | Informações do aluno |
| **Curso** | Dados do curso, Configurações | Informações do curso |
| **Frequência+** | Combinações | Dados mistos |

### Status de Presença

| Código | Significado |
|---|---|
| **Pr** | Presente |
| **Au** | Ausente |
| **At** | Atrasado |
| **Di** | Dispensado |
