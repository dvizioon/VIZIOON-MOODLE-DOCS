# Entendendo Licenças

## O que Licenças Controlam

Licenças no IOMAD controlam o acesso de usuários a cursos. Elas determinam:
- Quais cursos um usuário pode acessar
- Por quanto tempo o acesso é válido
- Quantos usuários podem acessar simultaneamente
- Quando o acesso expira

## Estrutura de uma Licença

### Tabela `local_iomad_company_licenses`

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | INT | ID único da licença |
| `name` | VARCHAR(255) | Nome da licença |
| `allocation` | INT | Número total de licenças disponíveis |
| `humanallocation` | INT | Alocação legível (para exibição) |
| `validlength` | INT | Dias de validade após alocação |
| `startdate` | INT | Data de início da validade |
| `expirydate` | INT | Data de expiração |
| `used` | INT | Licenças já utilizadas |
| `companyid` | INT | ID da empresa |
| `departmentid` | INT | ID do departamento |
| `parentid` | INT | Licença pai (para hierarquia) |
| `type` | INT | Tipo da licença |
| `program` | INT | Se é para programa de cursos |
| `reference` | VARCHAR(100) | Referência externa |
| `instant` | INT | Alocação imediata |
| `cutoffdate` | INT | Data de corte |
| `clearonexpire` | INT | Limpar ao expirar |

## Tipos de Licença

### Por Tipo (campo `type`)

| Tipo | Descrição |
|------|-----------|
| 0 | Padrão (alocação por usuário) |
| 1 | Validação por tempo |
| 2 | Expiração por data |
| 3 | Acesso ilimitado |
| 4 | Blanket (acesso a todos os cursos da licença) |

### Por Programa (campo `program`)

| Valor | Descrição |
|-------|-----------|
| 0 | Curso individual |
| 1 | Programa de cursos (múltiplos cursos) |

## Como Licenças Mapeiam para Cursos

### Tabela `local_iomad_company_license_courses`

```sql
CREATE TABLE local_iomad_company_license_courses (
    id         INT(10) NOT NULL AUTO_INCREMENT,
    licenseid  INT(20) NOT NULL,  -- FK para local_iomad_company_licenses
    courseid   INT(20) NOT NULL,  -- FK para course
    PRIMARY KEY (id)
);
```

Cada licença pode estar associada a múltiplos cursos. Um curso pode ter múltiplas licenças.

## Alocação de Usuários a Licenças

### Tabela `local_iomad_company_license_users`

```sql
CREATE TABLE local_iomad_company_license_users (
    id             INT(10) NOT NULL AUTO_INCREMENT,
    licenseid      INT(20) NOT NULL,  -- FK para local_iomad_company_licenses
    userid         INT(20) NOT NULL,  -- FK para user
    isusing        INT(1) NOT NULL DEFAULT 0,
    timecompleted  INT(20),
    score          DECIMAL(10,5),
    result         TEXT,
    courseid       INT(10) DEFAULT 0,
    issuedate      INT(20) DEFAULT 0,
    groupid        INT(20) DEFAULT 0,
    PRIMARY KEY (id),
    UNIQUE (userid, licenseid, courseid)
);
```

### Campos Importantes

| Campo | Descrição |
|-------|-----------|
| `isusing` | 0 = não iniciado, 1 = em uso |
| `timecompleted` | Data de conclusão |
| `issuedate` | Data de alocação |
| `score` | Nota obtida |

## Alocação Automática vs Manual

### Alocação Automática

Ocorre quando:
1. **Domínio de email**: Usuário se cadastra com email de domínio mapeado à empresa
2. **Auto-matrícula**: Curso configurado com `autoenrol = 1`
3. **Licença instantânea**: Campo `instant = 1`

```php
// Verificar se licença é instantânea
if ($license->instant) {
    // Alocar imediatamente
    company_user::allocate_license($userid, $licenseid, $courseid);
}
```

### Alocação Manual

Ocorre quando:
1. Administrador atribui licença manualmente
2. Importação em lote
3. API web service

```php
// Alocar licença manualmente
company_user::allocate_license($userid, $licenseid, $courseid);
```

## Expiração e Renovação de Licenças

### Cálculo de Expiração

```php
// Data de expiração = data de alocação + validlength
$expirydate = $issuedate + ($license->validlength * DAYSECS);
```

### Verificação de Expiração

```php
// Verificar se licença está válida
$isvalid = ($license->expirydate > time() || $license->expirydate == 0);
```

### Renovação

```php
// Renovar licença (estender validade)
$license->validlength += 30; // Adicionar 30 dias
$DB->update_record('local_iomad_company_licenses', $license);
```

## Fluxo de Licença

```
┌─────────────────────┐
│ Criar Licença       │
│ - allocation = 100  │
│ - validlength = 365 │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Associar a Cursos   │
│ license_courses     │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Alocar Usuários     │
│ license_users       │
│ - isusing = 0       │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Usuário Acessa      │
│ - isusing = 1       │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│ Conclui/Expira      │
│ - timecompleted     │
│ - OU expirydate     │
└─────────────────────┘
```

## Ver Também

- [[Licencas/Gerenciar]] - Gerenciando licenças
- [[Empresas/Gerenciar]] - Gerenciando empresas
- [[Database]] - Estrutura do banco de dados
