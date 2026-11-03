# Lista de Plugins IOMAD

## Plugin Core

### local_iomad

O plugin principal do IOMAD que fornece a funcionalidade de multi-tenancy.

| Componente | Descrição |
|------------|-----------|
| **local_iomad** | Plugin principal com classes core |
| **local_iomadcustompage** | Páginas customizadas |
| **local_iomad_oidc_sync** | Sincronização OIDC |

## Plugins de Autenticação

### auth_iomadoidc

Autenticação OpenID Connect para IOMAD.

- Integração com provedores OIDC
- Mapeamento automático de usuários a empresas
- Sincronização de perfil

### auth_iomadsaml2

Autenticação SAML2 para IOMAD.

- Integração com provedores SAML
- Single Sign-On (SSO)
- Mapeamento de atributos

## Blocos (12 plugins)

| Plugin | Descrição |
|--------|-----------|
| **block_iomad_company_admin** | Painel administrativo da empresa |
| **block_iomad_company_selector** | Seletor de empresas |
| **block_iomad_reports** | Bloco de relatórios |
| **block_iomad_mycourses** | Meus cursos |
| **block_iomad_learningpath** | Caminho de aprendizagem |
| **block_iomad_commerce** | E-commerce |
| **block_iomad_html** | Bloco HTML personalizado |
| **block_iomad_link** | Bloco de links |
| **block_iomad_welcome** | Bloco de boas-vindas |
| **block_iomad_onlineusers** | Usuários online |
| **block_iomad_microlearning** | Microlearning |
| **block_iomad_approve_access** | Aprovação de acesso |

### Detalhes dos Blocos

#### block_iomad_company_admin
O bloco principal de administração da empresa. Fornece:
- Gestão de usuários
- Gestão de cursos
- Gestão de licenças
- Relatórios
- Configurações da empresa

#### block_iomad_company_selector
Permite aos usuários selecionar a empresa que estão visualizando (para admins que gerenciam múltiplas empresas).

#### block_iomad_reports
Bloco que exibe links para relatórios da empresa.

#### block_iomad_mycourses
Exibe os cursos do usuário na empresa atual.

#### block_iomad_learningpath
Apresenta cursos em sequência (caminho de aprendizagem).

#### block_iomad_commerce
Integração com e-commerce para venda de cursos.

#### block_iomad_html
Bloco HTML personalizado por empresa.

#### block_iomad_link
Bloco com links personalizados.

#### block_iomad_welcome
Mensagem de boas-vindas personalizada.

#### block_iomad_onlineusers
Lista usuários online da empresa.

#### block_iomad_microlearning
Suporte a microlearning.

#### block_iomad_approve_access
Aprovação manual de acesso a cursos.

## Módulos de Atividade

### mod_iomadcertificate

Módulo de certificado personalizado para IOMAD.

- Geração automática de PDF
- Logotipo da empresa
- Assinatura digital
- Bordas e marcas d'água
- Suporte a múltiplos templates

### mod_trainingevent

Módulo para eventos de treinamento presencial.

- Locais de treinamento
- Datas e horários
- Capacidade máxima
- Lista de presença
- Treinamento virtual

## Condições de Disponibilidade

### availability_iomad

Condição de disponibilidade baseada em licença do IOMAD.

- Verifica se usuário tem licença válida
- Controla acesso baseado em empresa
- Integrado com o sistema de licenças

## Plugins de Matrícula

### enrol_iomad

Plugin de matrícula do IOMAD.

- Matrícula automática baseada em empresa
- Controle por departamento
- Integração com licenças

## Relatórios (10+ plugins)

| Plugin | Descrição |
|--------|-----------|
| **report_companies** | Relatório de empresas |
| **report_completion** | Relatório de conclusão |
| **report_completion_monthly** | Conclusão mensal |
| **report_completion_overview** | Visão geral de conclusão |
| **report_users** | Relatório de usuários |
| **report_emails** | Relatório de emails |
| **report_license_usage** | Uso de licenças |
| **report_user_license_allocations** | Alocações de licença |
| **report_user_logins** | Logs de acesso |
| **report_attendance** | Presença |

Ver mais em [[Reports/Relatorios]]

## Ferramentas de Admin

| Plugin | Descrição |
|--------|-----------|
| **tool_iomadmerge** | Fusão de empresas |
| **tool_iomadpolicy** | Políticas IOMAD |
| **tool_iomadsite** | Configurações do site |

## Filtros

### filter_iomad

Filtro IOMAD para conteúdo personalizado por empresa.

## Temas

| Plugin | Descrição |
|--------|-----------|
| **theme_iomad** | Tema IOMAD principal |
| **theme_iomadboost** | Tema baseado no Boost |
| **theme_iomadbootstrap** | Tema baseado no Bootstrap |

## Dependências entre Plugins

```
local_iomad (core)
├── block_iomad_company_admin (depende de local_iomad)
├── block_iomad_company_selector (depende de local_iomad)
├── block_iomad_reports (depende de local_iomad)
├── block_iomad_mycourses (depende de local_iomad)
├── block_iomad_learningpath (depende de local_iomad)
├── block_iomad_commerce (depende de local_iomad)
├── block_iomad_html (depende de local_iomad)
├── block_iomad_link (depende de local_iomad)
├── block_iomad_welcome (depende de local_iomad)
├── block_iomad_onlineusers (depende de local_iomad)
├── block_iomad_microlearning (depende de local_iomad)
├── block_iomad_approve_access (depende de local_iomad)
├── mod_iomadcertificate (depende de local_iomad)
├── mod_trainingevent (depende de local_iomad)
├── availability_iomad (depende de local_iomad)
├── enrol_iomad (depende de local_iomad)
├── auth_iomadoidc (depende de local_iomad)
├── auth_iomadsaml2 (depende de local_iomad)
├── filter_iomad (depende de local_iomad)
└── report_* (dependem de local_iomad)
```

## Ver Também

- [[VisaoGeral]] - Visão geral do IOMAD
- [[Classes/Classes]] - Classes PHP do IOMAD
- [[Configuracao]] - Configurações do sistema
