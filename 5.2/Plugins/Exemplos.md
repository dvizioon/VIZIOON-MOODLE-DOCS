# Exemplos Reais — Plugins Oxygeni

## Visão Geral

Este documento analisa os plugins reais do projeto Oxygeni, documentando como seguem (ou desviam dos) padrões do Moodle 5.2.

## mod_oxymsteams — Módulo de Atividade

### Estrutura

```
mod/oxymsteams/
├── version.php                    # Versão do plugin
├── lib.php                        # Funções hook (1300+ linhas)
├── mod_form.php                   # Formulário de configuração
├── view.php                       # Página principal (500+ linhas)
├── index.php                      # Lista no curso
├── settings.php                   # Configurações admin
├── connect.php                    # Conexão OAuth2
├── disconnect.php                 # Desconexão OAuth2
├── reopen.php                     # Reabrir reunião
├── report.php                     # Relatório de presença
├── report_link.php                # Link para relatório
├── link.php                       # Acesso ao link
├── linkedusers.php                # Usuários vinculados
├── linkedusers_link.php           # Link para usuários
├── db/
│   ├── install.xml                # 8 tabelas definidas
│   ├── access.php                 # 9 capacidades
│   ├── messages.php               # Mensagens do plugin
│   └── upgrade.php                # Scripts de upgrade
├── classes/
│   ├── event/
│   │   └── course_module_viewed.php
│   └── reportbuilder/
│       ├── load_attendance_report.php
│       ├── load_system_reports.php
│       └── local/
│           ├── entity/
│           │   ├── attendance.php
│           │   ├── button_preset.php
│           │   ├── linked_account.php
│           │   ├── survey_response.php
│           │   ├── usage_editor.php
│           │   └── usage_log.php
│           └── systemreport/
│               ├── attendance.php
│               ├── attendance_link.php
│               ├── button_presets.php
│               ├── linked_accounts.php
│               ├── survey.php
│               ├── usage.php
│               ├── usage_editor.php
│               └── usage_editor_links.php
├── lang/
│   ├── en/oxymsteams.php          # Strings em inglês
│   └── pt_br/oxymsteams.php       # Strings em português
├── templates/                     # Templates PHP (não Mustache)
│   ├── padrao.php
│   ├── simples.php
│   ├── destaque.php
│   └── limpo.php
├── pix/                           # Ícones SVG/PNG
│   ├── logo.png
│   ├── logo.svg
│   ├── monologo.svg
│   └── icons/
│       └── icons8-microsoft-teams-*.svg
├── css/                           # Estilos customizados
│   ├── style.css
│   └── survey.css
├── scss/
│   └── style.scss
├── amd/src/                       # JavaScript AMD
│   ├── button_presets_form.js
│   ├── calendar_sync.js
│   ├── emoji_picker.js
│   ├── link_restriction.js
│   ├── modal.js
│   ├── scheduled_message.js
│   ├── sortable_table.js
│   ├── survey_carousel.js
│   └── toggle.js
├── lib/                           # Bibliotecas customizadas
│   ├── variables.php
│   ├── survey_ui.php
│   ├── components/
│   │   └── emoji_icon_picker.php
│   ├── emojionearea/              # Lib externa
│   └── fontIconpicker/            # Lib externa
├── layout/                        # Layouts customizados
│   ├── Header.php
│   └── Footer.php
├── backup/moodle2/                # Backup/Restore
│   ├── backup_oxymsteams_activity_task.class.php
│   └── backup_oxymsteams_stepslib.php
├── plugins/                       # Sub-plugins
│   └── info.json
└── test/                          # Testes
    ├── test_calendar.php
    └── test_notify.php
```

### Análise do version.php

```php
$plugin->version   = 2025062906;
$plugin->requires  = 2022041900;  // Moodle 4.0+
$plugin->component = 'mod_oxymsteams';
$plugin->maturity  = MATURITY_BETA;
$plugin->release   = '1.0';
```

**Observação:** Usa `$plugin->` em vez de `$version`. Padrão correto.

### Capacidades (db/access.php)

```php
$capabilities = [
    'mod/oxymsteams:view' => [...],
    'mod/oxymsteams:addinstance' => [...],
    'mod/oxymsteams:createmeeting' => [...],
    'mod/oxymsteams:updatemeeting' => [...],
    'mod/oxymsteams:deletemeeting' => [...],
    'mod/oxymsteams:viewlinkedusers' => [...],
    'mod/oxymsteams:reopenmeeting' => [...],
    'mod/oxymsteams:managebuttonpresets' => [...],
    'mod/oxymsteams:ownbuttonpresets' => [...],
];
```

**Destaque:** Capacidade `reopenmeeting` com `RISK_DATALOSS` — demonstra consciente de segurança.

### Estrutura do Banco (install.xml)

8 tabelas definidas:
1. `oxymsteams` — Tabela principal
2. `oxymsteams_log` — Log de criação
3. `oxymsteams_attendance` — Presença
4. `oxymsteams_survey_question` — Perguntas
5. `oxymsteams_survey_option` — Opções
6. `oxymsteams_survey_response` — Respostas
7. `oxymsteams_survey_answer` — Respostas individuais
8. `oxymsteams_editor_links` — Links do editor
9. `oxymsteams_button_presets` — Predefinições de botão

### Hooks em lib.php

O plugin implementa:
- `oxymsteams_supports()` — Features suportadas
- `oxymsteams_add_instance()` — Criar atividade
- `oxymsteams_update_instance()` — Atualizar
- `oxymsteams_delete_instance()` — Deletar
- `oxymsteams_get_coursemodule_info()` — Info para curso
- `mod_oxymsteams_cm_info_view()` — Exibição no curso

**Desvio:** Usa `oxymsteams_` em vez de `mod_oxymsteams_` para funções auxiliares. Aceitável mas não padrão.

### Integração Microsoft Graph

```php
function oxymsteams_create_meeting_via_graph($subject, $startts, $endts, &$joinurl, &$meetingid) {
    // Usa OAuth2 para autenticar com Microsoft Graph
    $client = \core\oauth2\api::get_user_oauth_client($issuer, $currenturl, $scopes, true);
    $token = $client->get_accesstoken();
    
    // Cria reunião via API REST
    $response = $client->post($url, $body);
}
```

**Boa prática:** Integração completa com OAuth2 sem expor chaves.

### Templates Customizados

Diferente do padrão Mustache, usa templates PHP:

```
templates/
├── padrao.php     # Template padrão
├── simples.php    # Template simples
├── destaque.php   # Template destaque
└── limpo.php      # Template limpo
```

**Desvio:** Não usa templates Mustache. Templates PHP permitem mais flexibilidade mas são menos portáveis.

## tool_oxytemppass — Ferramenta Admin

### Estrutura (v0.0.3)

```
tool/oxytemppass/
├── version.php
├── lib.php
├── index.php
├── settings.php
├── token.php
├── user.php
├── roles.php
├── uninstall.php
├── db/
│   ├── access.php
│   └── tasks.php
├── classes/
│   ├── local/
│   │   └── permissions.php
│   ├── report/
│   │   └── users.php
│   └── task/
│       └── expire_temppass.php
├── lang/
│   ├── en/tool_oxytemppass.php
│   └── pt_br/tool_oxytemppass.php
└── pix/
    ├── logo.png
    └── e/
        ├── copy.svg
        ├── key.svg
        ├── link.svg
        └── refresh.svg
```

### version.php

```php
$plugin->component = 'tool_oxytemppass';
$plugin->version   = 2026022402;
$plugin->requires  = 2024100100;  // Moodle 4.5+
$plugin->maturity  = MATURITY_ALPHA;
$plugin->release   = '0.2.1';
```

### Settings.php — Páginas Admin

```php
if ($hassiteconfig || has_capability('tool/oxytemppass:use', context_system::instance())) {
    $ADMIN->add('accounts', new admin_externalpage(
        'tool_oxytemppass',
        get_string('pluginname', 'tool_oxytemppass'),
        new moodle_url('/admin/tool/oxytemppass/index.php'),
        'tool/oxytemppass:use'
    ));
}
```

**Boa prática:** Permite acesso a não-admins com capability específica.

### Scheduled Tasks

```php
// db/tasks.php
$tasks = [
    [
        'classname' => 'tool_oxytemppass\task\expire_temppass',
        'blocking' => 0,
        'minute' => '*/5',
        'hour' => '*',
    ],
];
```

**Boa prática:** Tarefa agendada para expiração de senhas temporárias.

## webservice_oxywebapi — Web Service

### Estrutura

```
webservice/oxywebapi/
├── version.php
├── externallib.php
├── lib.php
├── endpoints.php
├── index.php
├── settings.php
├── db/
│   ├── services.php
│   ├── access.php
│   ├── cache.php
│   ├── install.php
│   ├── install.xml
│   └── upgrade.php
├── classes/
│   └── external/
│       ├── get_categories.php
│       ├── get_courses.php
│       └── get_users.php
├── lang/
│   ├── en/webservice_oxywebapi.php
│   └── pt_br/webservice_oxywebapi.php
└── pix/
    └── logo.png
```

### services.php

```php
$functions = [
    'webservice_oxywebapi_get_courses' => [
        'classname'   => 'webservice_oxywebapi_external',
        'methodname'  => 'get_courses',
        'classpath'   => 'webservice/oxywebapi/externallib.php',
        'description' => 'Get courses with cursor pagination and filters',
        'type'        => 'read',
        'ajax'        => true,
        'capabilities'=> 'moodle/course:view',
    ],
];

$services = [
    'oxyWebAPI Service' => [
        'functions' => ['webservice_oxywebapi_get_courses'],
        'restrictedusers' => 0,
        'enabled' => 1,
    ],
];
```

**Padrão correto:** Seguiu exatamente a estrutura documentada.

### Paginação com Cursor

```php
public static function execute($cursor = 0, $limit = 20, $search = '') {
    $sql = "SELECT * FROM {course} WHERE id > :minid";
    $params = ['minid' => max(1, $cursor)];
    
    // ... filtros ...
    
    $sql .= " ORDER BY id ASC";
    $sql .= " LIMIT " . ($limit + 1);
    
    $courses = $DB->get_records_sql($sql, $params);
    $hasmore = count($courses) > $limit;
    
    return [
        'courses' => array_values($courses),
        'hasmore' => $hasmore,
        'nextcursor' => $hasmore ? end($courses)->id : 0,
    ];
}
```

**Boa prática:** Paginação eficiente usando cursor em vez de OFFSET.

### Rate Limiting

```php
if (!webservice_oxywebapi_check_rate_limit('get_courses', $USER->id)) {
    throw new \moodle_exception('error_ratelimit', 'webservice_oxywebapi');
}
```

**Boa prática:** Proteção contra abuso de API.

## webservice_oxybrigde_notas — Web Service de Notas

### Estrutura

```
webservice/oxybrigde_notas/
├── version.php
├── externallib.php
├── settings.php
├── db/
│   ├── services.php
│   └── access.php
├── classes/
│   ├── external/
│   │   ├── grade_history.php
│   │   └── grade_history_timeline.php
│   └── privacy/
│       └── provider.php
├── lang/
│   ├── en/webservice_oxybrigde_notas.php
│   ├── pt_br/webservice_oxybrigde_notas.php
│   └── pt/webservice_oxybrigde_notas.php
├── templates/
│   └── doc.mustache
└── doc/
    └── index.php
```

### version.php com $plugin Objeto

```php
$plugin = new stdClass();
$plugin->component = 'webservice_oxybrigde_notas';
$plugin->version = 2026043002;
$plugin->requires = 2022041900;
$plugin->maturity = MATURITY_STABLE;
$plugin->release = '1.0.0';
```

**Observação:** Usa `new stdClass()` em vez de atribuição direta. Ambos são válidos.

### Privacy Provider

```php
// classes/privacy/provider.php
class provider implements \core_privacy\local\metadata\provider {
    public static function get_metadata(collection $collection) {
        $collection->add_database_table(
            'webservice_oxybrigde_notas_log',
            [
                'userid' => 'privacy:metadata:userid',
                'courseid' => 'privacy:metadata:courseid',
            ],
            'privacy:metadata:tablesummary'
        );
        return $collection;
    }
}
```

**Boa prática:** Implementa LGPD/GDPR com Privacy API.

## block_oxymylib — Bloco

### Estrutura

```
blocks/oxymylib/
├── version.php
├── block_oxymylib.php
├── edit_form.php
├── db/
│   └── install.xml
├── lang/
│   ├── en/block_oxymylib.php
│   └── pt_br/block_oxymylib.php
├── pix/
│   ├── logo.png
│   └── logo_minha_biblioteca.png
└── doc/
    └── oxymoodlebanner/    # Sub-plugin de banner
```

### lang/en/block_oxymylib.php

```php
$string['pluginname'] = 'My Library';
$string['token'] = 'API Key';
$string['target'] = 'Link Target';
$string['targetself'] = 'Same window';
$string['targetblank'] = 'New window';
$string['targetmodal'] = 'Modal (Internal)';
$string['targetpopup'] = 'Popup (External)';
```

**Boa prática:** Strings bem organizadas com nomes descritivos.

## Padrões Observados

### O que os plugins fazem certo

1. **version.php correto** — Todos usam `$plugin->` com campos obrigatórios
2. **Capacidades bem definidas** — Seguem padrão `plugin:capability`
3. **strings multilíngue** — Inglês + Português
4. **Rate limiting** — Web services com proteção
5. **Privacy API** — Implementam LGPD
6. **Integrações OAuth2** — Microsoft Graph sem expor chaves

### Desvios dos padrões

1. **Templates PHP vs Mustache** — oxymsteams usa templates PHP em vez de Mustache
2. **Nomenclatura de funções** — Algumas usam `oxymsteams_` em vez de `mod_oxymsteams_`
3. **Estrutura de diretórios** — Alguns têm `lib/` com bibliotecas externas

### Boas Práticas Identificadas

1. **Scheduled tasks** — Para tarefas periódicas (expiração)
2. **Cache** — Web services com cache de consultas
3. **Rate limiting** — Proteção contra abuso
4. **Backup/Restore** — Suporte completo
5. **Report Builder** — Integração com construtor de relatórios

## Referências

- [[Base]] — Estrutura geral
- [[Tipos]] — Tipos de plugin
- [[5.2/Plugins/Criar]] — Criação de plugins
