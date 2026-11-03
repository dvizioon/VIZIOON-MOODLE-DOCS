# Configuração do IOMAD

## Navegação

**Site administration** → **IOMAD** → **Settings**

As configurações são organizadas em 4 abas: General, Company, Report e Signup.

## Aba: General Settings

| Configuração | Tipo | Descrição | Padrão |
|--------------|------|-----------|--------|
| `use_email_as_username` | checkbox | Usar email como username ao criar usuários | Não |
| `allow_username` | checkbox | Permitir username manual | Não |
| `enforce_username_match` | checkbox | Exigir correspondência de username | Não |
| `use_mandatory_courses` | checkbox | Usar cursos obrigatórios | Não |
| `clearonselfunenrol` | checkbox | Limpar quando usuário se auto-desmatricula | Não |
| `autoreallocate_licenses` | checkbox | Realocar licenças automaticamente | Não |
| `useicons` | checkbox | Usar ícones na interface | Não |
| `showcompanydropdown` | checkbox | Mostrar dropdown de empresa | Sim |
| `emaildelay` | text | Atraso em segundos para envio de emails | 0 |
| `date_format` | select | Formato de data | `%Y-%m-%d` |
| `max_list_users` | text | Máximo de itens na lista de usuários | 30 |
| `max_list_courses` | text | Máximo de itens na lista de cursos | 30 |
| `max_list_templates` | text | Máximo de itens na lista de templates | 30 |
| `max_list_companies` | text | Máximo de itens na lista de empresas | 30 |
| `max_list_licenses` | text | Máximo de itens na lista de licenças | 30 |
| `max_list_classrooms` | text | Máximo de itens na lista de salas | 30 |
| `max_list_email_templates` | text | Máximo de itens na lista de templates de email | 30 |
| `max_list_competencies` | text | Máximo de itens na lista de competências | 30 |
| `max_list_frameworks` | text | Máximo de itens na lista de frameworks | 30 |
| `max_select_users` | text | Máximo de seleção de usuários | 100 |
| `max_select_courses` | text | Máximo de seleção de cursos | 200 |
| `max_select_templates` | text | Máximo de seleção de templates | 200 |
| `max_select_frameworks` | text | Máximo de seleção de frameworks | 200 |

## Aba: Company Settings

| Configuração | Tipo | Descrição | Padrão |
|--------------|------|-----------|--------|
| `show_company_structure` | checkbox | Mostrar estrutura hierárquica de empresas | Sim |
| `sync_institution` | select | Sincronizar instituição (shortname/nome) | shortname |
| `sync_department` | select | Sincronizar departamento | setfromcompany |
| `autoenrol_managers` | checkbox | Auto-matricular gerentes | Sim |
| `iomadcertificate_logo` | storedfile | Logo padrão do certificado | - |
| `iomadcertificate_signature` | storedfile | Assinatura padrão do certificado | - |
| `iomadcertificate_border` | storedfile | Borda padrão do certificado | - |
| `iomadcertificate_watermark` | storedfile | Marca d'água padrão do certificado | - |

### Opções de Sincronização

**sync_institution:**
- `0` - Não sincronizar
- `1` - Usar shortname da empresa
- `2` - Usar nome da empresa

**sync_department:**
- `0` - Não sincronizar
- `1` - Definir a partir da empresa
- `2` - Definir para a empresa

## Aba: Report Settings

| Configuração | Tipo | Descrição | Padrão |
|--------------|------|-----------|--------|
| `hidevalidcourses` | checkbox | Ocultar cursos válidos nos relatórios | Não |
| `showcharts` | checkbox | Mostrar gráficos nos relatórios | Sim |
| `downloaddetails` | checkbox | Permitir download de detalhes | Sim |
| `report_fields` | text | Campos extras nos relatórios | - |
| `report_grade_places` | text | Casas decimais para notas | 0 |

## Aba: Signup Settings

| Configuração | Tipo | Descrição | Padrão |
|--------------|------|-----------|--------|
| `signup_enable` | checkbox | Habilitar auto-cadastro | Sim |
| `signup_showinstructions` | checkbox | Mostrar instruções | Sim |
| `signup_useemail` | checkbox | Usar email no cadastro | Sim |
| `signup_autoenrol` | checkbox | Auto-matricular ao cadastrar | Sim |
| `signup_autoenrol_unassigned` | checkbox | Auto-matricular não atribuídos | Não |
| `signup_auth` | multicheckbox | Métodos de autenticação permitidos | - |
| `signup_role` | select | Papel padrão para novos usuários | Nenhum |
| `signup_company` | select | Empresa padrão | Nenhuma |

## Tarefas Agendadas (11 tasks)

O IOMAD registra 11 tarefas agendadas em `local/iomad/db/tasks.php`:

| Tarefa | Frequência | Descrição |
|--------|------------|-----------|
| `cron_task` | A cada 1 minuto | Tarefa principal do cron |
| `course_not_started_task` | Diário (00:00) | Verificar cursos não iniciados |
| `course_not_completed_task` | Diário (00:00) | Verificar cursos não concluídos |
| `course_expiry_warning_task` | Diário (00:00) | Enviar avisos de expiração |
| `manager_completion_digest_task` | Diário (00:00) | Digest de conclusão para gerentes |
| `manager_expiring_digest_task` | Diário (00:00) | Digest de expiração para gerentes |
| `manager_warning_digest_task` | Diário (00:00) | Digest de avisos para gerentes |
| `trainingevent_not_selected_task` | Diário (00:00) | Eventos de treinamento não selecionados |
| `company_license_expiring_task` | Diário (00:00) | Licenças de empresa expirando |
| `email_cron_task` | A cada 5 minutos | Processar fila de emails |
| `refreshlangpacks` | Mensal (dia 1) | Atualizar pacotes de idioma |

### Detalhes das Tarefas

#### cron_task
Tarefa principal que executa a cada minuto. Processa:
- Verificação de expiração
- Envio de emails pendentes
- Limpeza de dados temporários

#### course_not_started_task
Verifica usuários que não iniciaram cursos e envia lembretes.

#### course_not_completed_task
Verifica usuários com cursos em andamento por muito tempo.

#### course_expiry_warning_task
Envia avisos quando cursos estão próximos de expirar.

#### manager_completion_digest_task
Envia resumo diário de conclusões para gerentes.

#### manager_expiring_digest_task
Envia resumo diário de expirações para gerentes.

#### manager_warning_digest_task
Envia resumo diário de avisos para gerentes.

#### trainingevent_not_selected_task
Verifica eventos de treinamento sem seleção.

#### company_license_expiring_task
Verifica licenças de empresa prestes a expirar.

#### email_cron_task
Processa a fila de emails do IOMAD.

#### refreshlangpacks
Atualiza os pacotes de idioma do IOMAD.

## Configurações por Empresa

Além das configurações globais, cada empresa pode ter configurações específicas:

### Campos de Perfil

```php
// Criar categoria de perfil para a empresa
$catdata = (object) [];
$catdata->sortorder = $DB->count_records('user_info_category') + 1;
$catdata->name = $data->shortname;
$data->profilecategoryid = $DB->insert_record('user_info_category', $catdata);
```

### Campos Customizados

| Campo | Descrição |
|-------|-----------|
| `custom1` | Campo customizado 1 |
| `custom2` | Campo customizado 2 |
| `custom3` | Campo customizado 3 |
| `custommenuitems` | Itens de menu personalizados |

## Configurações de Cache

O IOMAD usa caches para performance:

```php
// Cache de categorias de todas as empresas
$allcompanycategoriescache = cache::make('local_iomad', 'allcompanycategories');

// Cache de categorias da empresa atual
$companycategoriescache = cache::make('local_iomad', 'companycategories');

// Cache de categorias de curso da empresa
$companycoursecategoriescache = cache::make('local_iomad', 'companycoursecategories');
```

## Ver Também

- [[VisaoGeral]] - Visão geral do IOMAD
- [[5.2/IOMAD/Empresas/Criar]] - Criando uma empresa
- [[Plugins/Lista]] - Lista de plugins
