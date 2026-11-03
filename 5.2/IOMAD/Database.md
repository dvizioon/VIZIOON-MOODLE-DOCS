# Estrutura do Banco de Dados

## Visão Geral

O IOMAD adiciona mais de 40 tabelas ao banco de dados Moodle. Todas começam com o prefixo `local_iomad_`.

## Tabelas Principais

### local_iomad_companies

Tabela principal de empresas.

```sql
CREATE TABLE local_iomad_companies (
    id                      INT(10) NOT NULL AUTO_INCREMENT,
    name                    VARCHAR(50) NOT NULL,
    shortname               VARCHAR(25) NOT NULL UNIQUE,
    code                    VARCHAR(255),
    address                 TEXT,
    city                    VARCHAR(50) NOT NULL,
    region                  VARCHAR(50),
    postcode                VARCHAR(20),
    country                 VARCHAR(2) NOT NULL,
    maildisplay             INT(2) NOT NULL DEFAULT 2,
    mailformat              INT(1) NOT NULL DEFAULT 1,
    maildigest              INT(1) NOT NULL DEFAULT 0,
    autosubscribe           INT(1) NOT NULL DEFAULT 1,
    trackforums             INT(1) NOT NULL DEFAULT 0,
    htmleditor              INT(1) NOT NULL DEFAULT 1,
    screenreader            INT(1) NOT NULL DEFAULT 0,
    timezone                VARCHAR(100) NOT NULL DEFAULT '99',
    lang                    VARCHAR(30) NOT NULL DEFAULT 'en',
    bgcolor_header          VARCHAR(7),
    bgcolor_content         VARCHAR(7),
    theme                   VARCHAR(50) NOT NULL,
    coursecategoryid        INT(20) NOT NULL DEFAULT 0,
    profilecategoryid       INT(10) NOT NULL DEFAULT 0,
    suspended               INT(1) NOT NULL DEFAULT 0,
    customcss               TEXT,
    maincolor               VARCHAR(20) DEFAULT 'null',
    headingcolor            VARCHAR(20) DEFAULT 'null',
    linkcolor               VARCHAR(20) DEFAULT 'null',
    emailprofileid          INT(20),
    supervisorprofileid     INT(10) NOT NULL DEFAULT 0,
    managernotify           INT(10) NOT NULL DEFAULT 0,
    parentid                INT(20) NOT NULL DEFAULT 0,
    ecommerce               INT(1) NOT NULL DEFAULT 0,
    custommenuitems         TEXT,
    managerdigestday        INT(1) NOT NULL DEFAULT 0,
    previousroletemplateid  INT(20) NOT NULL DEFAULT 0,
    previousemailtemplateid INT(20) NOT NULL DEFAULT 0,
    hostname                VARCHAR(200),
    maxusers                INT(20) NOT NULL DEFAULT 0,
    validto                 INT(20),
    suspendafter            INT(10),
    isterminated            INT(1) NOT NULL DEFAULT 0,
    custom1                 VARCHAR(255),
    custom2                 VARCHAR(255),
    custom3                 VARCHAR(255),
    paymentaccountid        INT(10),
    departmentprofileid     INT(20) NOT NULL DEFAULT 0,
    PRIMARY KEY (id),
    UNIQUE (shortname)
);
```

### local_iomad_company_users

Relação entre usuários e empresas.

```sql
CREATE TABLE local_iomad_company_users (
    id           INT(10) NOT NULL AUTO_INCREMENT,
    companyid    INT(10) NOT NULL,  -- FK para local_iomad_companies
    userid       INT(10) NOT NULL,  -- FK para user
    managertype  INT(1) NOT NULL DEFAULT 0,  -- 0=User, 1=Manager, 2=DeptManager, 3=Educator, 4=Reporter
    departmentid INT(10) NOT NULL,  -- FK para local_iomad_company_departments
    suspended    INT(1) NOT NULL DEFAULT 0,
    educator     INT(1) NOT NULL DEFAULT 0,
    lastused     INT(20),
    PRIMARY KEY (id),
    UNIQUE (companyid, userid, departmentid)
);
```

### local_iomad_company_licenses

Licenças da empresa.

```sql
CREATE TABLE local_iomad_company_licenses (
    id            INT(10) NOT NULL AUTO_INCREMENT,
    name          VARCHAR(255) NOT NULL,
    allocation    INT(20) NOT NULL DEFAULT 0,
    humanallocation INT(20) NOT NULL DEFAULT 0,
    validlength   INT(20) NOT NULL DEFAULT 0,
    startdate     INT(20) NOT NULL DEFAULT 0,
    expirydate    INT(20) NOT NULL DEFAULT 0,
    used          INT(20) NOT NULL DEFAULT 0,
    companyid     INT(20),  -- FK para local_iomad_companies
    departmentid  INT(20),  -- FK para local_iomad_company_departments
    parentid      INT(20) NOT NULL DEFAULT 0,  -- FK para local_iomad_company_licenses
    type          INT(1) NOT NULL DEFAULT 0,
    program       INT(1) NOT NULL DEFAULT 0,
    reference     VARCHAR(100),
    instant       INT(1) NOT NULL DEFAULT 0,
    cutoffdate    INT(10) NOT NULL DEFAULT 0,
    clearonexpire INT(1) NOT NULL DEFAULT 0,
    PRIMARY KEY (id)
);
```

### local_iomad_tracks

Rastreamento de conclusão.

```sql
CREATE TABLE local_iomad_tracks (
    id                INT(10) NOT NULL AUTO_INCREMENT,
    courseid          INT(11) NOT NULL,  -- FK para course
    coursename        VARCHAR(254),
    userid            INT(11) NOT NULL,  -- FK para user
    timecompleted     INT(11),
    timeenrolled      INT(11),
    timestarted       INT(11),
    timeexpires       INT(11),
    finalscore        DECIMAL(10,5) NOT NULL DEFAULT 0,
    companyid         INT(20) NOT NULL,  -- FK para local_iomad_companies
    licenseid         INT(20) DEFAULT 0,  -- FK para local_iomad_company_licenses
    licensename       VARCHAR(255),
    licenseallocated  INT(20),
    expirysent        INT(20),
    notstartedstop    INT(1) NOT NULL DEFAULT 0,
    completedstop     INT(1) NOT NULL DEFAULT 0,
    expiredstop       INT(1) NOT NULL DEFAULT 0,
    coursecleared     INT(1) NOT NULL DEFAULT 0,
    modifiedtime      INT(20) NOT NULL DEFAULT 0,
    PRIMARY KEY (id)
);
```

## Tabelas de Relacionamento

### local_iomad_company_courses

Atribuição de cursos a empresas.

```sql
CREATE TABLE local_iomad_company_courses (
    id           INT(10) NOT NULL AUTO_INCREMENT,
    companyid    INT(11) NOT NULL,  -- FK para local_iomad_companies
    courseid     INT(11) NOT NULL,  -- FK para course
    departmentid INT(10) NOT NULL,  -- FK para local_iomad_company_departments
    PRIMARY KEY (id),
    UNIQUE (companyid, courseid)
);
```

### local_iomad_company_departments

Departamentos da empresa.

```sql
CREATE TABLE local_iomad_company_departments (
    id         INT(10) NOT NULL AUTO_INCREMENT,
    name       VARCHAR(255) NOT NULL,
    shortname  VARCHAR(32) NOT NULL,
    companyid  INT(20) NOT NULL DEFAULT 0,  -- FK para local_iomad_companies
    parentid   INT(20),  -- FK para local_iomad_company_departments
    PRIMARY KEY (id)
);
```

### local_iomad_company_license_users

Alocação de licenças a usuários.

```sql
CREATE TABLE local_iomad_company_license_users (
    id            INT(10) NOT NULL AUTO_INCREMENT,
    licenseid     INT(20) NOT NULL,  -- FK para local_iomad_company_licenses
    userid        INT(20) NOT NULL,  -- FK para user
    isusing       INT(1) NOT NULL DEFAULT 0,
    timecompleted INT(20),
    score         DECIMAL(10,5),
    result        TEXT,
    courseid      INT(10) DEFAULT 0,
    issuedate     INT(20) DEFAULT 0,
    groupid       INT(20) DEFAULT 0,
    PRIMARY KEY (id),
    UNIQUE (userid, licenseid, courseid)
);
```

### local_iomad_company_license_courses

Cursos associados a licenças.

```sql
CREATE TABLE local_iomad_company_license_courses (
    id        INT(10) NOT NULL AUTO_INCREMENT,
    licenseid INT(20) NOT NULL,  -- FK para local_iomad_company_licenses
    courseid  INT(20) NOT NULL,  -- FK para course
    PRIMARY KEY (id)
);
```

### local_iomad_company_shared_courses

Cursos compartilhados entre empresas.

```sql
CREATE TABLE local_iomad_company_shared_courses (
    id        INT(10) NOT NULL AUTO_INCREMENT,
    companyid INT(20) NOT NULL,  -- FK para local_iomad_companies
    courseid  INT(20) NOT NULL,  -- FK para course
    PRIMARY KEY (id)
);
```

### local_iomad_company_created_courses

Cursos que podem ser gerenciados pela empresa.

```sql
CREATE TABLE local_iomad_company_created_courses (
    id        INT(10) NOT NULL AUTO_INCREMENT,
    companyid INT(20) NOT NULL,  -- FK para local_iomad_companies
    courseid  INT(20) NOT NULL,  -- FK para course
    PRIMARY KEY (id)
);
```

### local_iomad_company_course_groups

Grupos de curso da empresa.

```sql
CREATE TABLE local_iomad_company_course_groups (
    id        INT(10) NOT NULL AUTO_INCREMENT,
    companyid INT(20) NOT NULL,  -- FK para local_iomad_companies
    groupid   INT(20) NOT NULL,  -- FK para groups
    courseid  INT(20) NOT NULL,  -- FK para course
    PRIMARY KEY (id)
);
```

### local_iomad_company_course_options

Opções específicas de curso por empresa.

```sql
CREATE TABLE local_iomad_company_course_options (
    id             INT(10) NOT NULL AUTO_INCREMENT,
    companyid      INT(20) NOT NULL,  -- FK para local_iomad_companies
    courseid       INT(20) NOT NULL,  -- FK para course
    autoenrol      INT(1) NOT NULL DEFAULT 0,
    mandatory      INT(1) NOT NULL DEFAULT 0,
    validlength    INT(20),
    warnexpire     INT(20),
    warncompletion INT(20),
    notifyperiod   INT(20),
    expireafter    INT(20),
    warnnotstarted INT(20),
    hasgrade       INT(1),
    PRIMARY KEY (id)
);
```

## Tabelas de Configuração

### local_iomad_courses

Configurações IOMAD dos cursos.

```sql
CREATE TABLE local_iomad_courses (
    id              INT(10) NOT NULL AUTO_INCREMENT,
    courseid        INT(20) NOT NULL,  -- FK para course
    licensed        INT(1) DEFAULT 0,
    shared          INT(1) DEFAULT 0,
    validlength     INT(20),
    warnexpire      INT(20) NOT NULL DEFAULT 0,
    warncompletion  INT(20) NOT NULL DEFAULT 0,
    notifyperiod    INT(10) NOT NULL DEFAULT 0,
    expireafter     INT(10) NOT NULL DEFAULT 0,
    warnnotstarted  INT(20) NOT NULL DEFAULT 0,
    hasgrade        INT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (id)
);
```

### local_iomad_company_role_restrictions

Restrições de papel por empresa.

```sql
CREATE TABLE local_iomad_company_role_restrictions (
    id          INT(10) NOT NULL AUTO_INCREMENT,
    companyid   INT(11) NOT NULL,  -- FK para local_iomad_companies
    roleid      INT(11) NOT NULL,  -- FK para role
    capability  VARCHAR(255) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (roleid, companyid, capability)
);
```

### local_iomad_company_domains

Domínios associados à empresa.

```sql
CREATE TABLE local_iomad_company_domains (
    id        INT(10) NOT NULL AUTO_INCREMENT,
    companyid INT(10) NOT NULL,  -- FK para local_iomad_companies
    domain    TEXT NOT NULL,
    PRIMARY KEY (id)
);
```

## Tabelas de Templates

### local_iomad_company_role_templates

Templates de papel.

```sql
CREATE TABLE local_iomad_company_role_templates (
    id   INT(10) NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);
```

### local_iomad_company_role_templates_caps

Capacidades dos templates de papel.

```sql
CREATE TABLE local_iomad_company_role_templates_caps (
    id          INT(10) NOT NULL AUTO_INCREMENT,
    templateid  INT(20) NOT NULL,  -- FK para local_iomad_company_role_templates
    roleid      INT(10) NOT NULL,  -- FK para role
    capability  VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);
```

### local_iomad_company_role_templates_ass

Atribuição de templates a empresas.

```sql
CREATE TABLE local_iomad_company_role_templates_ass (
    id         INT(10) NOT NULL AUTO_INCREMENT,
    companyid  INT(20) NOT NULL,  -- FK para local_iomad_companies
    templateid INT(20) NOT NULL,  -- FK para local_iomad_company_role_templates
    PRIMARY KEY (id)
);
```

## Tabelas de Email

### local_iomad_email_templates

Templates de email da empresa.

```sql
CREATE TABLE local_iomad_email_templates (
    id                    INT(10) NOT NULL AUTO_INCREMENT,
    companyid             INT(10) NOT NULL,  -- FK para local_iomad_companies
    name                  VARCHAR(50) NOT NULL,
    disabled              INT(1) NOT NULL DEFAULT 0,
    disabledmanager       INT(1) NOT NULL DEFAULT 0,
    disabledsupervisor    INT(1) NOT NULL DEFAULT 0,
    emailto               VARCHAR(1333),
    emailtoother          VARCHAR(1333),
    emailcc               VARCHAR(1333),
    emailccother          VARCHAR(1333),
    emailfrom             INT(20),
    emailfromother        VARCHAR(100),
    emailreplyto          INT(20),
    emailreplytoother     VARCHAR(100),
    repeatperiod          INT(10) NOT NULL DEFAULT 0,
    repeatvalue           INT(10) NOT NULL DEFAULT 0,
    repeatday             INT(10) NOT NULL DEFAULT 0,
    emailfromothername    TEXT,
    PRIMARY KEY (id)
);
```

### local_iomad_emails

Fila de emails enviados.

```sql
CREATE TABLE local_iomad_emails (
    id             INT(10) NOT NULL AUTO_INCREMENT,
    templatename   VARCHAR(100),
    modifiedtime   INT(20) NOT NULL,
    sent           INT(20),
    subject        VARCHAR(255) NOT NULL,
    body           TEXT NOT NULL,
    varsreplaced   INT(20),
    companyid      INT(20) NOT NULL DEFAULT 0,  -- FK para local_iomad_companies
    courseid       INT(20),  -- FK para course
    userid         INT(20) NOT NULL,  -- FK para user
    invoiceid      INT(20),  -- FK para invoice
    classroomid    INT(20),  -- FK para local_iomad_training_locations
    senderid       INT(20),  -- FK para user
    headers        TEXT,
    due            INT(20) NOT NULL DEFAULT 0,
    PRIMARY KEY (id)
);
```

## Tabelas de Competência

### local_iomad_company_comp_frameworks

Frameworks de competência da empresa.

```sql
CREATE TABLE local_iomad_company_comp_frameworks (
    id           INT(10) NOT NULL AUTO_INCREMENT,
    companyid    INT(20) NOT NULL,  -- FK para local_iomad_companies
    frameworkid  INT(20) NOT NULL,  -- FK para competency_framework
    PRIMARY KEY (id)
);
```

### local_iomad_company_comp_templates

Templates de plano de aprendizagem.

```sql
CREATE TABLE local_iomad_company_comp_templates (
    id         INT(10) NOT NULL AUTO_INCREMENT,
    companyid  INT(20) NOT NULL,  -- FK para local_iomad_companies
    templateid INT(20) NOT NULL,  -- FK para competency_template
    PRIMARY KEY (id)
);
```

### local_iomad_templates

Configurações de templates de competência.

```sql
CREATE TABLE local_iomad_templates (
    id         INT(10) NOT NULL AUTO_INCREMENT,
    templateid INT(20) NOT NULL,  -- FK para competency_template
    shared     INT(1) NOT NULL DEFAULT 0,
    PRIMARY KEY (id)
);
```

### local_iomad_frameworks

Configurações de frameworks de competência.

```sql
CREATE TABLE local_iomad_frameworks (
    id           INT(10) NOT NULL AUTO_INCREMENT,
    frameworkid  INT(20) NOT NULL,  -- FK para competency_framework
    shared       INT(1) NOT NULL DEFAULT 0,
    PRIMARY KEY (id)
);
```

## Diagrama de Relacionamentos

```
┌─────────────────────────┐
│ local_iomad_companies   │◄─────────────────────────────────────┐
└─────────┬───────────────┘                                      │
          │                                                      │
          ├──────────────────────┬───────────────────────────────┐
          │                      │                               │
          ▼                      ▼                               ▼
┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────────┐
│local_iomad_company_ │  │ local_iomad_company_ │  │local_iomad_company_     │
│      users          │  │     departments      │  │      licenses           │
└─────────────────────┘  └─────────────────────┘  └─────────┬───────────────┘
                                                            │
                                                            ▼
                                              ┌─────────────────────────┐
                                              │local_iomad_company_     │
                                              │    license_users        │
                                              └─────────────────────────┘

┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────────┐
│local_iomad_company_ │  │ local_iomad_company_ │  │local_iomad_company_     │
│     courses         │  │   shared_courses     │  │   course_options        │
└─────────────────────┘  └─────────────────────┘  └─────────────────────────┘

┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────────┐
│   local_iomad_      │  │local_iomad_company_  │  │local_iomad_company_     │
│     courses         │  │  course_groups       │  │  role_restrictions      │
└─────────────────────┘  └─────────────────────┘  └─────────────────────────┘

┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────────┐
│   local_iomad_      │  │local_iomad_company_  │  │local_iomad_company_     │
│     tracks          │  │  certifcates         │  │     domains             │
└─────────────────────┘  └─────────────────────┘  └─────────────────────────┘
```

## Ver Também

- [[VisaoGeral]] - Visão geral do IOMAD
- [[Classes/Classes]] - Classes PHP do IOMAD
- [[Empresas/Gerenciar]] - Gerenciando empresas
- [[Licencas/Entender]] - Entendendo licenças
