# Instalar Plugins no Moodle

## Tipos de Plugin

| Tipo | Diretório | Exemplo |
|---|---|---|
| Atividade | mod/ | mod_quiz, mod_assignment |
| Bloco | blocks/ | block_navigation |
| Autenticação | auth/ | auth_ldap |
| Matrícula | enrol/ | enrol_manual |
| Filtro | filter/ | filter_multilang |
| Tema | theme/ | theme_boost |
| Relatório | report/ | report_logs |
| Formato | format/ | format_topics |
| Repositório | repository/ | repository_box |
| Ferramenta | admin/tool/ | tool_log |

## Métodos de Instalação

### 1. Via Interface Web (Recomendado)

1. Administração do Site > Plugins > Instalar plugins
2. Faça upload do arquivo .zip do plugin
3. O Moodle verifica compatibilidade
4. Clique em "Continuar"
5. Siga as instruções
6. Confirme a instalação

### 2. Via FTP/SSH

1. Baixe o plugin
2. Descompacte no diretório correto
3. Acesse: Administração do Site > Notificações
4. O Moodle detecta automaticamente
5. Clique em "Continuar"
6. Siga as instruções

### 3. Via Composer (PHP)

```bash
# No diretório do Moodle
composer require moodle/local_meuplugin
```

## Estrutura de um Plugin

```
local/meuplugin/
├── version.php          # Informações da versão
├── db/
│   ├── install.xml      # Schema do banco
│   ├── access.php       # Permissões
│   ├── services.php     # Web services
│   └── events.php       # Eventos
├── classes/
│   ├── form/            # Formulários
│   └── output/          # Renderizadores
├── lang/
│   └── en/
│       └── local_meuplugin.php  # Strings
├── templates/           # Templates Mustache
├── pix/                 # Ícones
├── amd/                 # JavaScript
├── lib.php              # Biblioteca
├── settings.php         # Configurações
└── README.md            # Documentação
```

## version.php

```php
<?php
defined('MOODLE_INTERNAL') || die();

$plugin->component = 'local_meuplugin';
$plugin->version = 2025010100;
$plugin->requires = 2024010100;
$plugin->maturity = MATURITY_STABLE;
$plugin->release = '1.0';
```

## Atualizar Plugin

### Via Interface

1. Administração do Site > Notificações
2. O Moodle detecta atualizações
3. Clique em "Atualizar"
4. Confirme

### Via SSH

```bash
cd /path/to/moodle
git pull
php admin/cli/upgrade.php
```

## Remover Plugin

### Via Interface

1. Administração do Site > Plugins > Plugins instalados
2. Selecione o plugin
3. Clique em "Desinstalar"
4. Confirme

### Via SSH

```bash
# Mova o diretório para fora do Moodle
mv local/meuplugin /backup/
php admin/cli/upgrade.php
```

## Solução de Problemas

### Erro de Compatibilidade

1. Verifique a versão mínima do Moodle
2. Atualize o Moodle se necessário
3. Baixe versão compatível do plugin

### Erro de Banco de Dados

1. Verifique se o install.xml está correto
2. Verifique as permissões do banco
3. Consulte o log de erros

### Plugin não Aparece

1. Verifique se está no diretório correto
2. Verifique permissões de arquivo
3. Limpe o cache: Administração > Desenvolvimento > Purge caches

## Plugins Úteis

### Padrão Moodle

| Plugin | Função |
|---|---|
| mod_attendance | Controle de frequência |
| block_configurable_reports | Relatórios customizados |
| mod_h5p | Conteúdo H5P |
| tool_lp | Planos de aprendizagem |
| auth_oauth2 | Login com Google/Microsoft |

### Comunidade

| Plugin | Função |
|---|---|
| qtype_wordtable | Questões em tabela |
| filter_poodll | Áudio/vídeo inline |
| mod_collaborative | Colaboração em tempo real |
| block_xp | Sistema de XP/gamificação |

## Boas Práticas

1. **Backup antes** - Sempre faça backup do site
2. **Teste em dev** - Instale primeiro em ambiente de teste
3. **Verifique compatibilidade** - Versão do Moodle e PHP
4. **Documentação** - Leia o README do plugin
5. **Atualize** - Mantenha plugins atualizados
6. **Monitore** - Verifique logs após instalação
