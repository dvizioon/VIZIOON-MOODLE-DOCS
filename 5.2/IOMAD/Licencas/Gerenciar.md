# Gerenciando Licenças

## Criando Licenças

### Navegação

1. Acesse **Site administration** → **IOMAD** → **Company administration**
2. Selecione a empresa
3. Vá para **Licenses** → **Create a new license**

### Campos ao Criar

| Campo | Descrição | Obrigatório |
|-------|-----------|-------------|
| **License name** | Nome da licença | Sim |
| **Allocation** | Número de licenças disponíveis | Sim |
| **Valid length** | Dias de validade após alocação | Não |
| **Start date** | Data de início | Não |
| **Expiry date** | Data de expiração | Não |
| **Type** | Tipo da licença | Sim |
| **Program** | Se é programa de cursos | Sim |
| **Reference** | Referência externa | Não |
| **Instant** | Alocação imediata | Não |
| **Clear on expire** | Limpar ao expirar | Não |

### Exemplo de Criação

```php
$license = new stdClass();
$license->name = 'Treinamento Anual 2024';
$license->allocation = 50;
$license->validlength = 365;
$license->startdate = time();
$license->expirydate = strtotime('+1 year');
$license->type = 0; // Padrão
$license->program = 0; // Curso individual
$license->companyid = $companyid;

$licenseid = company::create_license($license);
```

## Atribuindo Licenças a Usuários

### Navegação

1. Acesse a licença desejada
2. Clique em **Allocate licenses**
3. Selecione os usuários
4. Confirme a alocação

### Métodos de Alocação

#### Alocação Individual

```php
// Alocar um usuário a uma licença
company_user::allocate_license($userid, $licenseid, $courseid);

// Verificar se usuário tem licença válida
$haslicense = company_user::has_valid_license($userid, $courseid);
```

#### Alocação em Lote

```php
// Alocar múltiplos usuários
$users = [$userid1, $userid2, $userid3];
foreach ($users as $userid) {
    company_user::allocate_license($userid, $licenseid, $courseid);
}
```

### Via Interface

1. Na página da licença, clique em **Allocate**
2. Use o seletor de usuários para escolher
3. Clique em **Allocate selected users**
4. Confirme a operação

## Revogando Licenças

### Navegação

1. Acesse a licença desejada
2. Vá para **Allocated users**
3. Encontre o usuário
4. Clique em **Revoke**

### Métodos de Revogação

```php
// Revogar licença de um usuário
company_user::revoke_license($userid, $licenseid, $courseid);

// Verificar se licença está em uso
$isusing = $DB->get_field('local_iomad_company_license_users', 'isusing', [
    'userid' => $userid,
    'licenseid' => $licenseid,
    'courseid' => $courseid
]);
```

## Relatórios de Uso de Licença

### Relatório de Alocação de Usuários

**Navegação:** Site administration → IOMAD → Reports → User License Allocations

**Métricas:**
- Total de alocações
- Alocações ativas
- Alocações expiradas
- Licenças não utilizadas

### Relatório de Uso de Licença

**Navegação:** Site administration → IOMAD → Reports → License Usage

**Métricas:**
- Licenças por empresa
- Taxa de utilização
- Licenças próximas ao vencimento
- Licenças expiradas

### Via PHP

```php
// Obter uso da licença
$usage = $DB->get_records_sql("
    SELECT 
        l.name,
        l.allocation,
        l.used,
        (l.allocation - l.used) as available
    FROM {local_iomad_company_licenses} l
    WHERE l.companyid = :companyid
", ['companyid' => $companyid]);
```

## Alocação em Lote

### Importação CSV

1. Prepare um CSV com colunas: `userid, licenseid, courseid`
2. Acesse **IOMAD** → **Company administration** → **Licenses**
3. Clique em **Bulk allocation**
4. Faça upload do arquivo
5. Confirme a importação

### Via API

```php
// Exemplo de alocação em lote
$allocations = [
    ['userid' => 1, 'licenseid' => 10, 'courseid' => 100],
    ['userid' => 2, 'licenseid' => 10, 'courseid' => 100],
    ['userid' => 3, 'licenseid' => 10, 'courseid' => 100],
];

foreach ($allocations as $alloc) {
    company_user::allocate_license($alloc['userid'], $alloc['licenseid'], $alloc['courseid']);
}
```

## Gerenciamento de Expiração

### Verificar Licenças Próximas ao Vencimento

```php
// Licenças que expiram nos próximos 30 dias
$expiring = $DB->get_records_sql("
    SELECT * FROM {local_iomad_company_licenses}
    WHERE companyid = :companyid
    AND expirydate > :now
    AND expirydate < :deadline
", [
    'companyid' => $companyid,
    'now' => time(),
    'deadline' => time() + (30 * DAYSECS)
]);
```

### Renovar Licença

```php
// Estender validade
$license = $DB->get_record('local_iomad_company_licenses', ['id' => $licenseid]);
$license->validlength += 30; // +30 dias
$license->expirydate += (30 * DAYSECS);
$DB->update_record('local_iomad_company_licenses', $license);
```

### Limpar Licenças Expiradas

```php
// Licenças com clearonexpire = 1
$expired = $DB->get_records_sql("
    SELECT * FROM {local_iomad_company_licenses}
    WHERE expirydate < :now
    AND clearonexpire = 1
", ['now' => time()]);

foreach ($expired as $license) {
    // Remover alocações
    $DB->delete_records('local_iomad_company_license_users', ['licenseid' => $license->id]);
}
```

## Eventos Disparados

| Evento | Quando |
|--------|--------|
| `user_license_assigned` | Usuário recebe licença |
| `user_license_unassigned` | Licença revogada |
| `user_license_used` | Usuário inicia uso da licença |
| `company_license_created` | Licença criada |
| `company_license_deleted` | Licença excluída |
| `company_license_updated` | Licença atualizada |

## Ver Também

- [[Licencas/Entender]] - Entendendo licenças
- [[Empresas/Gerenciar]] - Gerenciando empresas
- [[Reports/Relatorios]] - Relatórios disponíveis
