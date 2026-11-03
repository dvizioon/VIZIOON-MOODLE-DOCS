# Gerenciando Empresas

## Hierarquia de Empresas

O IOMAD suporta hierarquia de empresas (parent-child):

```
Empresa Pai (parentid = 0)
├── Empresa Filha 1 (parentid = 1)
│   ├── Sub-empresa 1.1 (parentid = 2)
│   └── Sub-empresa 1.2 (parentid = 2)
└── Empresa Filha 2 (parentid = 1)
```

### Campos de Hierarquia

A tabela `local_iomad_companies` possui o campo `parentid` que define a relação pai-filho:

| Campo      | Descrição                    |
| ---------- | ---------------------------- |
| `parentid` | ID da empresa pai (0 = raiz) |

### Métodos de Navegação

```php
// Obter empresa raiz
$topcompanyid = $company->get_topcompanyid();

// Obter empresas filhas diretas
$children = $company->get_child_companies();

// Obter todas as empresas filhas recursivamente
$allchildren = $company->get_child_companies_recursive();

// Obter empresas pai recursivamente
$parents = $company->get_parent_companies_recursive();
```

## Gerenciamento de Usuários

### Atribuição de Usuários a Empresas

A tabela `local_iomad_company_users` armazena a relação usuário-empresa:

```sql
CREATE TABLE local_iomad_company_users (
    id          INT(10) NOT NULL AUTO_INCREMENT,
    companyid   INT(10) NOT NULL,  -- FK para local_iomad_companies
    userid      INT(10) NOT NULL,  -- FK para user
    managertype INT(1) NOT NULL DEFAULT 0,  -- 0=User, 1=Manager, 2=DeptManager, 3=Educator, 4=Reporter
    departmentid INT(10) NOT NULL,  -- FK para local_iomad_company_departments
    suspended   INT(1) NOT NULL DEFAULT 0,
    educator    INT(1) NOT NULL DEFAULT 0,
    lastused    INT(20),
    UNIQUE (companyid, userid, departmentid)
);
```

### Tipos de Usuário (managertype)

| Valor | Tipo | Descrição |
|-------|------|-----------|
| 0 | User | Usuário comum |
| 1 | Company Manager | Gerente da empresa |
| 2 | Department Manager | Gerente de departamento |
| 3 | Educator | Educador/instrutor |
| 4 | Company Reporter | Relator da empresa |

### Criar Usuário na Empresa

```php
// Criar um novo usuário e associar à empresa
$user = company_user::create($data, $companyid);

// Onde $data contém:
// - firstname, lastname, email (obrigatórios)
// - company (shortname da empresa)
// - departmentid
// - managertype
```

### Gerenciar Papéis

```php
// Obter tipos de disponíveis para a empresa
$managertypes = $company->get_managertypes();

// Atribuir papel a um usuário
company_user::set_manager_type($userid, $companyid, $managertype, $departmentid);
```

## Atribuição de Cursos a Empresas

### Tabela de Relacionamento

```sql
CREATE TABLE local_iomad_company_courses (
    id           INT(10) NOT NULL AUTO_INCREMENT,
    companyid    INT(11) NOT NULL,  -- FK para local_iomad_companies
    courseid     INT(11) NOT NULL,  -- FK para course
    departmentid INT(10) NOT NULL,  -- FK para local_iomad_company_departments
    UNIQUE (companyid, courseid)
);
```

### Métodos de Atribuição

```php
// Atribuir curso à empresa
$company->assign_course($courseid, $departmentid);

// Remover curso da empresa
$company->unassign_course($courseid);

// Obter cursos da empresa
$courses = $company->get_menu_courses(true, false, false, false, false, true, false);
```

## Cursos Compartilhados entre Empresas

### Tabela de Compartilhamento

```sql
CREATE TABLE local_iomad_company_shared_courses (
    id        INT(10) NOT NULL AUTO_INCREMENT,
    companyid INT(20) NOT NULL,  -- FK para local_iomad_companies
    courseid  INT(20) NOT NULL,  -- FK para course
    UNIQUE (companyid, courseid)
);
```

### Configurações de Compartilhamento

Na tabela `local_iomad_courses`:

| Campo | Descrição |
|-------|-----------|
| `shared` | 1 = curso compartilhado com todas as empresas |
| `licensed` | 1 = requer licença para acessar |

### Métodos de Compartilhamento

```php
// Compartilhar curso com outra empresa
$company->share_course($courseid, $targetcompanyid);

// Parar de compartilhar
$company->unshare_course($courseid, $targetcompanyid);

// Obter cursos compartilhados
$shared = $company->get_shared_courses();
```

## Configurações Específicas da Empresa

### Tabela de Opções de Curso

```sql
CREATE TABLE local_iomad_company_course_options (
    id             INT(10) NOT NULL AUTO_INCREMENT,
    companyid      INT(20) NOT NULL,
    courseid       INT(20) NOT NULL,
    autoenrol      INT(1) NOT NULL DEFAULT 0,
    mandatory      INT(1) NOT NULL DEFAULT 0,
    validlength    INT(20),
    warnexpire     INT(20),
    warncompletion INT(20),
    notifyperiod   INT(20),
    expireafter    INT(20),
    warnnotstarted INT(20),
    hasgrade       INT(1)
);
```

### Métodos de Configuração

```php
// Obter opções de curso para a empresa
$options = $company->get_iomad_course_options($courseid);

// Definir opção específica
$company->set_iomad_course_options($courserec, 'mandatory', 1);
```

## Restrições de Papel

### Tabela de Restrições

```sql
CREATE TABLE local_iomad_company_role_restrictions (
    id          INT(10) NOT NULL AUTO_INCREMENT,
    companyid   INT(11) NOT NULL,
    roleid      INT(11) NOT NULL,
    capability  VARCHAR(255) NOT NULL,
    UNIQUE (roleid, companyid, capability)
);
```

### Usar Restrições

```php
// Verificar se uma capacidade está restrita
$restricted = $DB->record_exists('local_iomad_company_role_restrictions', [
    'companyid' => $companyid,
    'roleid' => $roleid,
    'capability' => $capability
]);
```

## Suspender e Terminar Empresa

### Suspender

```php
// Suspender empresa
$company->suspend();

// Verificar se está suspensa
$is_suspended = $company->is_suspended();
```

### Terminar

```php
// Terminar empresa
$company->terminate();
```

## Excluir Empresa

```php
// Excluir empresa (método estático)
company::delete_company($companyid, true);
```

**O que é excluído:**
- Certificados emitidos
- Tracks de conclusão
- Licenças e alocações
- Frameworks e templates de competência
- Restrições de papel
- Templates de email
- Usuários da empresa
- Cursos exclusivos (não compartilhados)
- Categoria de curso
- Campos de perfil
- Departamentos
- Registro da empresa

## Ver Também

- [[5.2/IOMAD/Empresas/Criar]] - Criando uma empresa
- [[Licencas/Entender]] - Entendendo licenças
- [[Licencas/Gerenciar]] - Gerenciando licenças
- [[VisaoGeral]] - Visão geral
