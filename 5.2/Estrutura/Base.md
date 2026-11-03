# Estrutura Base do Moodle 5.2

## Visão Geral

O Moodle 5.2 é uma plataforma de ensino que utiliza arquitetura modular. Cada funcionalidade é implementada como um **plugin**, seguindo convenções rígidas de nomenclatura e estrutura de diretórios.

## Estrutura de Diretórios

```
moodle/
├── admin/              # Ferramentas administrativas (tool_*)
├── auth/               # Plugins de autenticação (auth_*)
├── availability/       # Restrições de disponibilidade
├── backup/             # Sistema de backup/restore
├── badges/             # Sistema de insígnias
├── blocks/             # Blocos laterais (block_*)
├── cache/              # Cache do sistema
├── calendar/           # Calendário
├── cohort/             # Cohorts
├── comment/            # Sistema de comentários
├── communication/      # Comunicação
├── competency/         # Competências
├── completion/         # Rastreamento de conclusão
├── contentbank/        # Banco de conteúdo
├── course/             # Gerenciamento de cursos
├── customfield/        # Campos personalizados
├── enrol/              # Matrículas (enrol_*)
├── error/              # Páginas de erro
├── files/              # Sistema de arquivos
├── filter/             # Filtros de texto (filter_*)
├── grade/              # Sistema de notas
├── group/              # Grupos
├── h5p/                # Conteúdo H5P
├── install/            # Instalação
├── lang/               # Arquivos de idioma (core)
├── lib/                # Bibliotecas centrais
├── local/              # Plugins locais (local_*)
├── login/              # Login
├── media/              # Tipos de mídia
├── message/            # Mensagens
├── mod/                # Módulos de atividade (mod_*)
├── payment/            # Pagamentos
├── pix/                # Ícones do core
├── plagiarism/         # Detecção de plágio
├── question/           # Tipos de questão (question_*)
├── rating/             # Sistema de avaliação
├── report/             # Relatórios (report_*)
├── reportbuilder/      # Construtor de relatórios
├── repository/         # Repositórios (repository_*)
├── search/             # Índice de busca
├── tag/                # Sistema de tags
├── theme/              # Temas (theme_*)
├── user/               # Gerenciamento de usuários
└── webservice/         # Web services (webservice_*)
```

## Descoberta de Plugins (version.php)

Cada plugin **obrigatoriamente** possui um `version.php` na raiz do seu diretório. Este arquivo é lido pelo Moodle para:
- Verificar se o plugin precisa de atualização
- Registrar o componente no banco de dados
- Definir requisitos e maturidade

### Estrutura do version.php

```php
<?php
defined('MOODLE_INTERNAL') || die();

$plugin->component = 'mod_meuplugin';   // Nome completo do componente
$plugin->version   = 2025062906;       // Versão (YYYYMMDDXX)
$plugin->requires  = 2022041900;       // Moodle mínimo exigido
$plugin->maturity  = MATURITY_STABLE;  // MATURITY_ALPHA, MATURITY_BETA, MATURITY_STABLE, MATURITY_RC
$plugin->release   = '1.0';            // Versão legível
```

### Formato da Versão

O `$plugin->version` segue o padrão `YYYYMMDDXX`:
- `YYYY` - Ano
- `MM` - Mês
- `DD` - Dia
- `XX` - Incremento (00-99)

Exemplo: `2025062906` = 29 de junho de 2025, incremento 06

### Campos Opcionais

```php
$plugin->dependencies = [              // Plugins dependentes
    'mod_outro' => 2025010100,
];
$plugin->incompatible = [              // Plugins incompatíveis
    'mod_antigo' => 2025010100,
];
$plugin->pathtolib = '/lib';          // Caminho para biblioteca
$plugin->plugindir = '/mod/meuplugin'; // Diretório relativo
```

## Convenções de Nomenclatura

| Prefixo | Tipo | Exemplo | Localização |
|---------|------|---------|-------------|
| `mod_` | Módulos de atividade | `mod_quiz` | `/mod/quiz/` |
| `block_` | Blocos | `block_calendar_month` | `/blocks/calendar_month/` |
| `auth_` | Autenticação | `auth_ldap` | `/auth/ldap/` |
| `enrol_` | Matrículas | `enrol_manual` | `/enrol/manual/` |
| `question_` | Tipos de questão | `question_multichoice` | `/question/type/multichoice/` |
| `format_` | Formatos de curso | `format_topics` | `/course/format/topics/` |
| `filter_` | Filtros de texto | `filter_tex` | `/filter/tex/` |
| `local_` | Plugins locais | `local_oxygeni` | `/local/oxygeni/` |
| `tool_` | Ferramentas admin | `tool_log` | `/admin/tool/log/` |
| `editor_` | Editores | `editor_tiny` | `/lib/editor/tiny/` |
| `webservice_` | Web services | `webservice_restful` | `/webservice/restful/` |
| `report_` | Relatórios | `report_log` | `/report/log/` |
| `repository_` | Repositórios | `repository_filesystem` | `/repository/filesystem/` |
| `theme_` | Temas | `theme_boost` | `/theme/boost/` |
| `dataformat_` | Formatos de dados | `dataformat_csv` | `/dataformat/csv/` |
| `plagiarism_` | Plágio | `plagiarism_turnitin` | `/plagiarism/turnitin/` |
| `portfolio_` | Portfólios | `portfolio_picasa` | `/portfolio/picasa/` |
| `message_` | Mensagens | `message_slack` | `/message/output/slack/` |
| `customfield_` | Campos custom | `customfield_text` | `/customfield/field/text/` |

## O Objeto Global $CFG

`$CFG` é o objeto global de configuração do Moodle, carregado em `config.php`.

### Propriedades Principais

```php
global $CFG;

// Caminhos do sistema
$CFG->dirroot    = '/var/www/html/moodle';        // Raiz do Moodle
$CFG->dataroot   = '/var/www/moodledata';          // Diretório de dados
$CFG->wwwroot    = 'https://moodle.exemplo.com.br'; // URL base
$CFG->admin      = 'admin';                        // Pasta admin

// Configurações de banco
$CFG->dbtype    = 'mysqli';     // Tipo de banco
$CFG->dbhost    = 'localhost';  // Host
$CFG->dbname    = 'moodle';     // Nome do banco
$CFG->dbuser    = 'moodle';     // Usuário
$CFG->dbpass    = 'senha';      // Senha
$CFG->prefix    = 'mdl_';       // Prefixo das tabelas

// Configurações de cache
$CFG->cachejs   = true;         // Habilitar cache de JS
$CFG->theme     = 'boost';      // Tema ativo

// Configurações de debug
$CFG->debug     = DEBUG_MINIMAL; // Nível de debug
$CFG->debugdisplay = 0;          // Exibir erros na tela
```

### Como Usar $CFG em Plugins

```php
// Nunca definir $CFG, apenas ler
global $CFG;

// Usar para construir caminhos
require_once($CFG->dirroot . '/mod/meuplugin/lib.php');
$libraio = $CFG->libdir . '/xmldb/xmldbobject.php';

// Usar para configs do plugin
$configuracao = get_config('meuplugin', 'chave_config');

// URLs
$url = new moodle_url('/mod/meuplugin/view.php', ['id' => $cmid]);
```

## Como o Moodle Carrega Código

### Fluxo de Inicialização

1. **`config.php`** → Carrega configurações do banco
2. **`lib/setup.php`** → Inicializa o ambiente Moodle
3. **`lib/weblib.php`** → Funções web básicas
4. **`lib/outputlib.php`** → Sistema de renderização
5. **Autoloading PSR-4** → Classes em `classes/` são carregadas automaticamente

### Autoloading de Classes

```
meu_plugin/
├── classes/
│   ├── factory.php        → \mod_meuplugin\factory
│   ├── manager.php        → \mod_meuplugin\manager
│   └── event/
│       └── viewed.php     → \mod_meuplugin\event\viewed
```

O Moodle usa PSR-4: o namespace `\mod_meuplugin\` mapeia para `mod/meuplugin/classes/`.

### Carregamento de Bibliotecas

```php
// Em view.php ou outros arquivos de entrada
require_once('../../config.php');           // Configuração Moodle
require_once($CFG->dirroot . '/mod/meuplugin/lib.php'); // Biblioteca do plugin
require_once($CFG->libdir . '/gradelib.php');            // Biblioteca do core
```

### Ordem de Carregamento

1. `config.php` (configurações)
2. `lib/setup.php` (inicialização)
3. `lib/datalib.php` (manipulação de dados)
4. `lib/weblib.php` (funções web)
5. `lib/outputlib.php` (renderização)
6. Arquivo de entrada (view.php, index.php, etc.)
7. Bibliotecas do plugin via `require_once`

## Referências

- [[Tipos]] - Todos os tipos de plugin
- [[5.2/Plugins/Criar]] - Como criar um plugin
- [[DB/Schema]] - Banco de dados
- [[Templates/Mustache]] - Sistema de templates
