# IOMAD - Visão Geral

## O que é Multi-Tenancy

Multi-tenancy é uma arquitetura de software onde uma única instância do sistema serve múltiplos clientes (tenants). Cada tenant opera de forma isolada, com seus próprios dados, usuários, configurações e conteúdo, mas compartilha a mesma infraestrutura base.

No contexto de LMS (Learning Management System), multi-tenancy permite que uma organização hospede múltiplas empresas/departamentos em uma única instalação Moodle, mantendo Total entre elas.

## Como o IOMAD Estende o Moodle

O IOMAD (Inter-Organization Moodle Administration and Deployment) é um conjunto de plugins que adiciona funcionalidades de multi-tenancy ao Moodle. Ele não modifica o código core do Moodle, mas se integra através dos hooks e extensões oficiais.

### Contexto: CONTEXT_COMPANY = 13

O IOMAD introduz um novo nível de contexto no Moodle: **CONTEXT_COMPANY** (nível 13). Este contexto é definido em `local_iomad/classes/custom_context/context_company.php` e permite:

- Definir permissões e capacidades no nível da empresa
- Herdar permissões da hierarquia de contextos
- Isolar dados entre empresas

```php
// Definição do contexto
define('CONTEXT_COMPANY', 13);

class context_company extends context {
    public static function get_short_name(): string {
        return 'company';
    }
}
```

## Hierarquia de Contextos

```
System (CONTEXT_SYSTEM = 10)
├── Contexto Empresa (CONTEXT_COMPANY = 13)
│   ├── Contexto Categoria de Curso (CONTEXT_COURSECAT = 40)
│   │   ├── Contexto Curso (CONTEXT_COURSE = 50)
│   │   │   ├── Contexto Módulo (CONTEXT_MODULE = 70)
│   │   │   └── Contexto Bloco (CONTEXT_BLOCK = 80)
```

A hierarquia de contextos do IOMAD segue a estrutura padrão do Moodle, mas insere o contexto de empresa entre o sistema e as categorias de curso:

| Contexto | Constante | Nível |
|----------|-----------|-------|
| System | CONTEXT_SYSTEM | 10 |
| **Company** | **CONTEXT_COMPANY** | **13** |
| Course Category | CONTEXT_COURSECAT | 40 |
| Course | CONTEXT_COURSE | 50 |
| Module | CONTEXT_MODULE | 70 |
| Block | CONTEXT_BLOCK | 80 |

## Como o Isolamento Funciona

### Filtragem SQL

O IOMAD isola dados através de joins e filtros SQL específicos. A classe `local_iomad\tenancy` gera subqueries que restringem os dados à empresa do usuário atual:

```php
// Filtrar usuários da empresa
public static function get_users_subquery($sqlname = 'u.id') {
    $company = company::by_userid($USER->id);
    $myusers = company::get_my_users($company->id);
    return " AND $sqlname IN (" . join(',', array_keys($myusers)) . ") ";
}

// Filtrar cursos da empresa
public static function get_courses_subquery($sqlname = 'c.id') {
    $company = company::by_userid($USER->id);
    $mycourses = $company->get_menu_courses(true);
    return " AND $sqlname IN (" . join(',', array_keys($mycourses)) . ")";
}
```

### Filtragem de Categorias

A função `iomad::iomad_filter_categories()` filtra categorias de curso para mostrar apenas as da empresa atual:

```php
// Verificar se a categoria pertence à empresa
$company = $DB->get_record('local_iomad_companies', ['coursecategoryid' => $id]);
if ($company->id == $user->company->id) {
    $iomadcategories[$id] = $category;
}
```

### Filtragem de Cursos

A função `iomad::iomad_filter_courses()` garante que usuários só vejam cursos da sua empresa:

```php
// Verificar se o curso está atribuído à empresa
$DB->get_record('local_iomad_company_courses', [
    'courseid' => $id,
    'companyid' => $mycompanyid,
]);
```

## A Classe Tenancy

A classe `local_iomad\tenancy` é responsável por gerar as subqueries SQL que isolam os dados. Ela fornece métodos estáticos para:

| Método | Descrição |
|--------|-----------|
| `get_users_subquery()` | Filtra usuários da empresa |
| `get_courses_subquery()` | Filtra cursos da empresa |
| `get_groups_subquery()` | Filtra grupos da empresa |
| `get_enrolments_subquery()` | Filtra matrículas da empresa |

**Fluxo de Isolamento:**
1. Obtém o ID da empresa do usuário atual
2. Busca todos os usuários/cursos/grupos da empresa
3. Retorna uma subquery SQL com os IDs filtrados
4. O padrão padrão é `AND 1 = 2` (não retorna nada) caso não haja empresa

## Conceitos-Chave

### Empresa (Company)

Uma empresa é a unidade principal de isolamento no IOMAD. Cada empresa possui:

- **name**: Nome completo
- **shortname**: Nome abreviado (único, apenas letras/números)
- **theme**: Tema visual específico
- **logo**: Logotipo personalizado
- **coursecategoryid**: Categoria de curso raiz
- **profilecategoryid**: Categoria de campos de perfil
- **parentid**: Empresa pai (para hierarquia)
- **hostname**: Domínio para mapeamento
- **suspended/isterminated**: Status da empresa

Ver mais em [[5.2/IOMAD/Empresas/Criar]] e [[Empresas/Gerenciar]]

### Departamento (Department)

Departamentos são subdivisiones dentro de uma empresa:

- **name**: Nome do departamento
- **shortname**: Nome abreviado
- **companyid**: ID da empresa
- **parentid**: Departamento pai (hierarquia)

### Licença (License)

Licenças controlam o acesso a cursos:

- **allocation**: Número total de licenças
- **used**: Licenças utilizadas
- **validlength**: Dias de validade após alocação
- **startdate/expirydate**: Período de validade
- **type**: Tipo de licença (alocação, validade, etc.)
- **program**: Se é para um programa de cursos

Ver mais em [[Licencas/Entender]] e [[Licencas/Gerenciar]]

### Track (Rastreamento)

Tracks registram o progresso e conclusão de cursos:

- **courseid**: ID do curso
- **userid**: ID do usuário
- **companyid**: ID da empresa
- **timecompleted**: Data de conclusão
- **finalscore**: Nota final
- **timeexpires**: Data de expiração

## Diagrama de Relacionamentos

```
┌─────────────────────┐
│ local_iomad_companies│
│ - id (PK)           │
│ - name              │
│ - shortname         │
│ - parentid (FK)     │
└─────────┬───────────┘
          │
          ├──────────────────────────────┐
          │                              │
          ▼                              ▼
┌─────────────────────┐    ┌──────────────────────────┐
│local_iomad_company_ │    │ local_iomad_company_      │
│      users          │    │       departments         │
│ - companyid (FK)    │    │ - companyid (FK)          │
│ - userid (FK)       │    │ - parentid (FK)           │
│ - departmentid (FK) │    └──────────────────────────┘
│ - managertype       │
└─────────────────────┘
          │
          ▼
┌─────────────────────────┐
│ local_iomad_company_     │
│       licenses           │
│ - companyid (FK)         │
│ - departmentid (FK)      │
└─────────┬───────────────┘
          │
          ▼
┌─────────────────────────┐
│local_iomad_company_     │
│   license_users         │
│ - licenseid (FK)        │
│ - userid (FK)           │
│ - courseid (FK)         │
└─────────────────────────┘
```

## Ver Também

- [[Configuracao]] - Configurações do admin
- [[Plugins/Lista]] - Lista completa de plugins
- [[Classes/Classes]] - Documentação das classes PHP
- [[Database]] - Estrutura do banco de dados
- [[5.2/IOMAD/Empresas/Criar]] - Criando uma empresa
- [[Licencas/Entender]] - Entendendo licenças
