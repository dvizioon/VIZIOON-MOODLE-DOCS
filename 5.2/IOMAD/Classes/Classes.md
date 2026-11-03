# Classes Principais do IOMAD

## local_iomad\iomad

Classe estática de utilidades do IOMAD. Localizada em `local/iomad/classes/iomad.php`.

### Métodos Principais

#### Gerenciamento de Empresa

```php
// Obter ID da empresa do usuário atual
public static function get_my_companyid(object $context, bool $required = true): int

// Verificar se usuário é de uma empresa
public static function is_company_user(?object $user): bool|int

// Verificar se usuário é admin da empresa
public static function is_company_admin(object $user): bool|int

// Obter ID da empresa
public static function companyid(): int

// Obter shortname da empresa
public static function companyshortname(): string

// Carregar empresa do usuário
public static function load_company(): void
```

#### Filtragem de Dados

```php
// Filtrar categorias por empresa
public static function iomad_filter_categories($categories): array

// Filtrar cursos por empresa
public static function iomad_filter_courses(array $courses): array

// Filtrar categorias de perfil
public static function iomad_filter_profile_categories(array $categories, int $userid = 0, int $companyid = 0): array

// Verificar se categoria é visível
public static function iomad_check_category(object $category): bool

// Verificar se curso é acessível
public static function iomad_check_course(int $checkid = 0, string $name = '', string $idnumber = '', bool $checkhidden = false): bool
```

#### SQL e Joins

```php
// Gerar JOIN para cursos da empresa
public static function join_company_course(string $alias = "{course}"): string

// Gerar JOIN para usuários da empresa
public static function join_company_user(string $alias = "{user}"): string
```

#### Cursos

```php
// Adicionar cursos com licença
public static function iomad_add_license_courses(array &$mycourses): void

// Adicionar cursos compartilhados
public static function iomad_add_shared_courses(array &$courses): void

// Adicionar cursos de treinamento ao calendário
public static function add_calendar_trainingevent_courses(array $courses): array
```

#### Competências

```php
// Obter IDs de frameworks da empresa
public static function get_company_frameworkids(int $companyid): array

// Obter IDs de templates da empresa
public static function get_company_templateids(int $companyid): array
```

#### CSS e Aparência

```php
// Obter CSS customizado da empresa
public static function get_company_customcss(int $companyid): string

// Obter cor principal
public static function get_company_maincolor(int $companyid): string

// Obter cor de títulos
public static function get_company_headingcolor(int $companyid): string

// Obter cor de links
public static function get_company_linkcolor(int $companyid): string
```

---

## local_iomad\company

Classe de entidade de empresa. Localizada em `local/iomad/classes/company.php`.

### Propriedades

```php
public $id = 0;              // ID da empresa
protected $companyrecord;    // Registro da empresa
public $context = null;      // Contexto da empresa
public $cssfields = ['bgcolor_header', 'bgcolor_content'];
```

### Construtor

```php
public function __construct(int $companyid)
```

### Métodos Estáticos

```php
// Criar ou atualizar empresa
public static function create_company(stdClass $data): company

// Excluir empresa
public static function delete_company($companyid, $verbose = false): void

// Obter empresa por ID de usuário
public static function by_userid(int $userid, bool $login = false): company|bool

// Obter nome da empresa
public static function get_companyname_byid(int $companyid): string

// Obter empresa por ID de usuário
public static function get_company_byuserid(int $userid): object

// Obter lista de empresas (RecordSet)
public static function get_companies_rs(int $page=0, int $perpage=0)

// Obter select de empresas
public static function get_companies_select(bool $showsuspended=false, bool $useprepend = true, bool $showchildren = true, string $sort = 'name', string $search = ''): array
```

### Métodos de Instância

```php
// Obter campos específicos
public function get($fields, $onlyifexists = false): string|object|null

// Obter todos os campos
public function get_all()

// Obter nome
public function get_name(): string

// Obter shortname
public function get_shortname(): string

// Obter tema
public function get_theme(): string

// Obter ID do pai
public function get_parentid(): int|bool

// Obter wwwroot
public function get_wwwroot(): string

// Obter empresa raiz
public function get_topcompanyid(): int

// Obter logo
public static function get_logo_url(int $companyid, $maxwidth = null, $maxheight = 200): string|bool

// Obter opções de curso IOMAD
public function get_iomad_course_options(int $courseid): object|bool

// Definir opções de curso
public function set_iomad_course_options(object $courserec, string $optionname, ?int $optionvalue)

// Obter empresas filhas
public function get_child_companies(): array

// Obter empresas filhas recursivamente
public function get_child_companies_recursive(): array

// Obter empresas pai recursivamente
public function get_parent_companies_recursive(): array

// Obter tipos de gerente disponíveis
public function get_managertypes(bool $full = false): array
```

---

## local_iomad\tenancy

Classe de isolamento SQL. Localizada em `local/iomad/classes/tenancy.php`.

### Métodos

```php
// Subquery para filtrar usuários da empresa
public static function get_users_subquery($sqlname = 'u.id'): string

// Subquery para filtrar cursos da empresa
public static function get_courses_subquery($sqlname = 'c.id'): string

// Subquery para filtrar grupos da empresa
public static function get_groups_subquery($sqlname = 'g.id'): string

// Subquery para filtrar matrículas da empresa
public static function get_enrolments_subquery($sqlname = 'e.id'): string
```

### Padrão de Retorno

Todos os métodos retornam `AND 1 = 2` (não retorna nada) quando não há empresa associada ao usuário.

---

## local_iomad\company_user

Classe de relação usuário-empresa. Localizada em `local/iomad/classes/company_user.php`.

### Métodos Principais

```php
// Criar usuário na empresa
public static function create(object $data, int $companyid = 0): int

// Excluir usuário da empresa
public static function delete(int $userid, int $companyid): void

// Alocar licença
public static function allocate_license(int $userid, int $licenseid, int $courseid): bool

// Revogar licença
public static function revoke_license(int $userid, int $licenseid, int $courseid): bool

// Verificar se tem licença válida
public static function has_valid_license(int $userid, int $courseid): bool

// Definir tipo de gerente
public static function set_manager_type(int $userid, int $companyid, int $managertype, int $departmentid): void

// Gerar username único
public static function generate_username(string $email, bool $useemail = false): string
```

---

## local_iomad\track

Classe de rastreamento de conclusão. Localizada em `local/iomad/classes/track.php`.

### Métodos Principais

```php
// Registrar conclusão de curso
public static function course_completed(int $courseid, int $userid): void

// Atualizar track
public static function update_entry(int $trackid, array $data): void

// Excluir track
public static function delete_entry(int $trackid, bool $deletefiles = false): void

// Obter tracks por empresa
public static function get_company_tracks(int $companyid, array $filters = []): array

// Obter certificados do curso
private static function get_certificates($courseid): array

// Armazenar certificado
private static function store_certificate($contextid, $filename, $trackid, $certificate, $content): void
```

---

## local_iomad\email

Classe de motor de emails. Localizada em `local/iomad/classes/email.php`.

### Métodos Principais

```php
// Verificar se pode enviar template diretamente
public static function allow_sending_to_template($templatename): bool

// Criar linha padrão do template
public static function create_default_template_row($templatename, $enable, $lang, $prefix, $templatesetid = 0): object
```

---

## local_iomad\observer

Observador de eventos. Localizada em `local/iomad/classes/observer.php`.

### Propriedade Estática

```php
public static $disablehandler = false; // Desabilitar handler temporariamente
```

### Métodos (Eventos Observados)

```php
// Evento: empresa atualizada
public static function company_course_updated($event): bool

// Evento: empresa criada
public static function company_created($event): bool

// Evento: empresa excluída
public static function company_deleted($event): bool

// Evento: licença criada
public static function company_license_created($event): bool

// Evento: licença excluída
public static function company_license_deleted($event): bool

// E outros eventos...
```

---

## local_iomad\custom_context\context_company

Classe de contexto customizado. Localizada em `local/iomad/classes/custom_context/context_company.php`.

### Constante

```php
define('CONTEXT_COMPANY', 13);
```

### Métodos

```php
// Nome curto do contexto
public static function get_short_name(): string

// Nome legível do nível
public static function get_level_name()

// Nome do contexto
public static function get_context_name($withprefix = true, $short = false, $escape = true)

// URL mais relevante
public function get_url(): moodle_url

// Obtendo instância
public static function instance(int $companyid, bool $strict = true): context_company
```

---

## Diagrama de Classes

```
┌─────────────────────┐
│    local_iomad\     │
│       iomad         │
│ (static utility)    │
└─────────┬───────────┘
          │ usa
          ▼
┌─────────────────────┐      ┌─────────────────────┐
│ local_iomad\company │◄─────│local_iomad\         │
│   (entity)          │      │  company_user       │
└─────────┬───────────┘      │ (relationship)      │
          │                  └─────────────────────┘
          │ usa
          ▼
┌─────────────────────┐      ┌─────────────────────┐
│local_iomad\tenancy  │      │local_iomad\track    │
│ (SQL isolation)     │      │ (completion)        │
└─────────────────────┘      └─────────────────────┘

┌─────────────────────┐      ┌─────────────────────┐
│local_iomad\email    │      │local_iomad\observer │
│ (email engine)      │      │ (event handler)     │
└─────────────────────┘      └─────────────────────┘

┌─────────────────────────────┐
│local_iomad\custom_context\  │
│    context_company          │
│ (CONTEXT_COMPANY = 13)      │
└─────────────────────────────┘
```

## Ver Também

- [[VisaoGeral]] - Visão geral do IOMAD
- [[Database]] - Estrutura do banco de dados
- [[Plugins/Lista]] - Lista de plugins
