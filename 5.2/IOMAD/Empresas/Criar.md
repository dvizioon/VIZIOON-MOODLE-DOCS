# Criando uma Empresa

## Navegação do Admin

1. Acesse **Site administration** → **IOMAD** → **Company administration**
2. Clique em **Create a new company**
3. Preencha os campos do formulário
4. Clique em **Save changes**

## Campos ao Criar uma Empresa

### Campos Obrigatórios

| Campo | Descrição | Validação |
|-------|-----------|-----------|
| **Company name** | Nome completo da empresa | Max 50 caracteres, sem tags |
| **Company shortname** | Nome abreviado | Max 25 caracteres, apenas `[A-Za-z0-9_]` |
| **City** | Cidade | Max 50 caracteres |
| **Country** | País | Código ISO de 2 letras (ex: BR, PT) |

### Campos Opcionais

| Campo | Descrição |
|-------|-----------|
| **Company code** | Código externo para integração com sistemas externos |
| **Address** | Endereço completo |
| **Region** | Estado/Região |
| **Postcode** | Código postal |

### Configurações de Aparência

| Campo | Descrição | Padrão |
|-------|-----------|--------|
| **Theme** | Tema visual da empresa | Tema do site |
| **Company logo** | Logotipo principal | - |
| **Company logo (compact)** | Logotipo compacto | - |
| **Favicon** | Ícone do navegador | - |
| **Header background colour** | Cor de fundo do cabeçalho | - |
| **Content background colour** | Cor de fundo do conteúdo | - |
| **Main text colour** | Cor do texto principal | - |
| **Heading colour** | Cor dos títulos | - |
| **Link colour** | Cor dos links | - |
| **Custom CSS** | CSS personalizado | - |

### Configurações de Usuário

| Campo | Descrição | Padrão |
|-------|-----------|--------|
| **Language** | Idioma padrão | en |
| **Timezone** | Fuso horário | 99 (sistema) |
| **Mail display** | Visibilidade do email | 2 |
| **Mail format** | Formato do email | 1 (HTML) |
| **Mail digest** | Resumo de emails | 0 |
| **Auto subscribe** | Auto-inscrição em fóruns | 1 |
| **Track forums** | Rastrear fóruns | 0 |
| **HTML editor** | Editor HTML | 1 |
| **Screen reader** | Leitor de tela | 0 |

### Configurações de Empresa

| Campo | Descrição | Padrão |
|-------|-----------|--------|
| **Parent company** | Empresa pai (hierarquia) | Nenhuma |
| **Suspended** | Empresa suspensa | Não |
| **Terminated** | Empresa encerrada | Não |
| **Valid to** | Data de validade | - |
| **Max users** | Limite de usuários | 0 (ilimitado) |
| **Suspend after** | Dias após vencimento para suspender | - |
| **Hostname** | Domínio para acesso | - |
| **E-commerce** | Habilitar e-commerce | Não |

### Configurações de Notificação

| Campo | Descrição | Padrão |
|-------|-----------|--------|
| **Manager notify** | Notificar gerente | 0 (nunca) |
| **Manager digest day** | Dia do resumo do gerente | 0 |
| **Email profile field** | Campo de perfil para CC | - |
| **Supervisor profile field** | Campo de perfil do supervisor | - |

### Configurações de Template

| Campo | Descrição |
|-------|-----------|
| **Role template** | Template de roles para aplicar |
| **Email template** | Conjunto de templates de email |
| **Dashboard** | Página personalizada como dashboard |

### Configurações de Certificado

| Campo | Descrição | Padrão |
|-------|-----------|--------|
| **Use logo** | Usar logo no certificado | 1 |
| **Use signature** | Usar assinatura | 1 |
| **Use border** | Usar borda | 1 |
| **Use watermark** | Usar marca d'água | 1 |
| **Show grade** | Mostrar nota | 1 |
| **Certificate seal** | Imagem do selo | - |
| **Certificate signature** | Imagem da assinatura | - |
| **Certificate border** | Imagem da borda | - |
| **Certificate watermark** | Imagem da marca d'água | - |

### Configurações de Domínio

| Campo | Descrição |
|-------|-----------|
| **Company domains** | Domínios para auto-atribuição (um por linha) |

### Campos Customizados

| Campo | Descrição |
|-------|-----------|
| **Custom 1** | Campo customizado 1 |
| **Custom 2** | Campo customizado 2 |
| **Custom 3** | Campo customizado 3 |
| **Custom menu items** | Itens de menu personalizados |
| **Payment account** | Conta de pagamento |

## O que é Criado Automaticamente

Ao criar uma empresa, o IOMAD cria automaticamente:

### 1. Categoria de Perfil de Usuário

```php
$catdata = (object) [];
$catdata->sortorder = $DB->count_records('user_info_category') + 1;
$catdata->name = $data->shortname;
$data->profilecategoryid = $DB->insert_record('user_info_category', $catdata);
```

Uma categoria de perfil de usuário é criada com o shortname da empresa para armazenar campos de perfil específicos da empresa.

### 2. Departamento Padrão

```php
self::initialise_departments($companyid);
```

Um departamento raiz é criado automaticamente com o nome da empresa.

### 3. Categoria de Curso

```php
$coursecat = (object) [];
$coursecat->name = $data->name;
$coursecat->sortorder = 999;
$coursecat->id = $DB->insert_record('course_categories', $coursecat);
```

Uma categoria de curso é criada para agrupar todos os cursos da empresa. O ID é armazenado em `coursecategoryid`.

### 4. Contexto da Empresa

```php
$companycontext = context_company::instance($companyid);
```

Um novo contexto `CONTEXT_COMPANY` (nível 13) é registrado no sistema de contextos do Moodle.

## Mapeamento de Domínio

O mapeamento de domínio permite que usuários sejam automaticamente atribuídos a uma empresa baseado no domínio do email:

```php
// Adicionar domínios
$domainsarray = preg_split('/[\r\n]+/', $data->companydomains, -1, PREG_SPLIT_NO_EMPTY);
foreach ($domainsarray as $domain) {
    $DB->insert_record('local_iomad_company_domains', [
        'companyid' => $companyid,
        'domain' => $domain
    ]);
}
```

**Exemplo:**
- Domínio: `empresa.com.br`
- Email do usuário: `joao@empresa.com.br`
- Resultado: Usuário é atribuído automaticamente à empresa

## Páginas Customizadas e Dashboard

O IOMAD permite criar páginas customizadas que podem ser usadas como dashboard da empresa:

```php
// Configurar dashboard
$DB->delete_records('local_iomad_company_pages', [
    'companyid' => $companyid,
    'type' => 'dashboard'
]);
if (!empty($data->dashboard)) {
    $DB->insert_record('local_iomad_company_pages', [
        'companyid' => $companyid,
        'pageid' => $data->dashboard,
        'type' => 'dashboard'
    ]);
}
```

## Eventos Disparados

Ao criar uma empresa, o evento `company_created` é disparado:

```php
$event = company_created::create([
    'context' => $systemcontext,
    'userid' => $USER->id,
    'objectid' => $companyid,
    'other' => ['companyid' => $companyid],
]);
$event->trigger();
```

## Ver Também

- [[Empresas/Gerenciar]] - Gerenciando empresas
- [[VisaoGeral]] - Visão geral do IOMAD
- [[Configuracao]] - Configurações do sistema
