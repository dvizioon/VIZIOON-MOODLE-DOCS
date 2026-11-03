# Relatórios Disponíveis no IOMAD

O IOMAD fornece 10+ relatórios para monitoramento e análise.

**Caminho geral:** Site administration → IOMAD → Reports

---

## 1. Relatório de Empresas

- **Plugin:** `report_companies`
- **Caminho:** Site administration → IOMAD → Reports → Companies

**O que mostra:**
- Total de empresas ativas, suspensas e encerradas
- Usuários por empresa
- Cursos por empresa
- Licenças por empresa

| Coluna | Descrição |
|---|---|
| Nome | Nome da empresa |
| Shortname | Nome abreviado |
| Usuários | Total de usuários |
| Cursos | Total de cursos |
| Status | Ativa / Suspensa / Encerrada |

---

## 2. Relatório de Conclusão

- **Plugin:** `report_completion`
- **Caminho:** Site administration → IOMAD → Reports → Completion

**O que mostra:**
- Cursos concluídos, em andamento e não iniciados
- Taxa de conclusão
- Tempo médio de conclusão

| Coluna | Descrição |
|---|---|
| Usuário | Nome do usuário |
| Curso | Nome do curso |
| Início | Data de início |
| Conclusão | Data de conclusão |
| Nota | Nota final |
| Status | Concluído / Em andamento / Não iniciado |

---

## 3. Relatório de Conclusão Mensal

- **Plugin:** `report_completion_monthly`
- **Caminho:** Site administration → IOMAD → Reports → Completion Monthly

**O que mostra:**
- Conclusões por mês
- Comparativo mês a mês
- Tendências de conclusão

| Coluna | Descrição |
|---|---|
| Mês/Ano | Período de referência |
| Conclusões | Total de conclusões |
| Usuários | Usuários que concluíram |
| Cursos | Cursos concluídos |

---

## 4. Relatório de Visão Geral de Conclusão

- **Plugin:** `report_completion_overview`
- **Caminho:** Site administration → IOMAD → Reports → Completion Overview

**O que mostra:**
- Resumo geral de conclusão por empresa
- Progresso por departamento
- Top cursos mais concluídos

| Coluna | Descrição |
|---|---|
| Empresa | Nome da empresa |
| Departamento | Nome do departamento |
| Total | Total de matriculados |
| Concluíram | Total de conclusões |
| Taxa | Percentual de conclusão |

---

## 5. Relatório de Usuários

- **Plugin:** `report_users`
- **Caminho:** Site administration → IOMAD → Reports → Users

**O que mostra:**
- Total de usuários ativos e suspensos
- Último acesso
- Cursos matriculados

| Coluna | Descrição |
|---|---|
| Nome | Nome completo |
| Email | Endereço de email |
| Empresa | Empresa atribuída |
| Departamento | Departamento |
| Papel | Tipo de usuário |
| Último acesso | Data do último login |
| Status | Ativo / Suspenso |

---

## 6. Relatório de Emails

- **Plugin:** `report_emails`
- **Caminho:** Site administration → IOMAD → Reports → Emails

**O que mostra:**
- Emails enviados, pendentes e com erro
- Templates mais usados

| Coluna | Descrição |
|---|---|
| Destinatário | Usuário destinatário |
| Assunto | Assunto do email |
| Template | Template utilizado |
| Enviado | Data de envio |
| Status | Enviado / Pendente / Erro |

---

## 7. Relatório de Uso de Licença

- **Plugin:** `report_license_usage`
- **Caminho:** Site administration → IOMAD → Reports → License Usage

**O que mostra:**
- Licenças por empresa
- Taxa de utilização
- Licenças próximas ao vencimento

| Coluna | Descrição |
|---|---|
| Licença | Nome da licença |
| Empresa | Empresa |
| Alocação | Total de licenças |
| Usadas | Licenças utilizadas |
| Disponíveis | Licenças disponíveis |
| Vencimento | Data de expiração |

---

## 8. Relatório de Alocação de Licença

- **Plugin:** `report_user_license_allocations`
- **Caminho:** Site administration → IOMAD → Reports → User License Allocations

**O que mostra:**
- Alocações por usuário
- Alocações ativas e expiradas
- Histórico de alocações

| Coluna | Descrição |
|---|---|
| Usuário | Nome do usuário |
| Licença | Nome da licença |
| Curso | Curso associado |
| Data Alocação | Data da alocação |
| Expira em | Data de expiração |
| Status | Ativa / Expirada / Revogada |

---

## 9. Relatório de Logs de Acesso

- **Plugin:** `report_user_logins`
- **Caminho:** Site administration → IOMAD → Reports → User Logins

**O que mostra:**
- Total de logins por empresa
- Logins por período
- Usuários mais ativos

| Coluna | Descrição |
|---|---|
| Usuário | Nome do usuário |
| Empresa | Empresa |
| Data/Hora | Data e hora do login |
| IP | Endereço IP |
| Navegador | User agent |

---

## 10. Relatório de Presença

- **Plugin:** `report_attendance`
- **Caminho:** Site administration → IOMAD → Reports → Attendance

**O que mostra:**
- Presença em treinamentos presenciais
- Faltas e atrasos
- Taxa de presença

| Coluna | Descrição |
|---|---|
| Usuário | Nome do usuário |
| Evento | Nome do evento |
| Data | Data do evento |
| Status | Presente / Ausente / Atrasado |
| Tempo | Duração |

---

## Acesso via PHP

```php
// Dados de conclusão da empresa
$completion = $DB->get_records_sql("
    SELECT 
        u.firstname,
        u.lastname,
        c.fullname,
        lit.timecompleted,
        lit.finalscore
    FROM {local_iomad_tracks} lit
    JOIN {user} u ON (lit.userid = u.id)
    JOIN {course} c ON (lit.courseid = c.id)
    WHERE lit.companyid = :companyid
    ORDER BY lit.timecompleted DESC
", ['companyid' => $companyid]);

// Uso de licença
$licenseusage = $DB->get_records_sql("
    SELECT 
        l.name,
        l.allocation,
        l.used,
        (l.allocation - l.used) as available
    FROM {local_iomad_company_licenses} l
    WHERE l.companyid = :companyid
", ['companyid' => $companyid]);
```

---

## Configurações de Relatório

Em Site administration → IOMAD → Settings → Report settings:

| Configuração | Descrição | Padrão |
|---|---|---|
| hidevalidcourses | Ocultar cursos válidos | Não |
| showcharts | Mostrar gráficos | Sim |
| downloaddetails | Permitir download de detalhes | Sim |
| report_fields | Campos extras no relatório | - |
| report_grade_places | Casas decimais da nota | 0 |

---

## Ver Também

- [[IOMAD/VisaoGeral]] - Visão geral do IOMAD
- [[IOMAD/Licencas/Entender]] - Entendendo licenças
- [[IOMAD/Configuracao]] - Configurações do sistema
