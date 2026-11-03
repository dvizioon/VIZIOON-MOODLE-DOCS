# Tipos de Plugin do Moodle 5.2

## Visão Geral

O Moodle 5.2 suporta dezenas de tipos de plugins, cada um com uma função específica no ecossistema. Todos seguem convenções rígidas de nomenclatura e estrutura.

## Lista Completa de Tipos

### mod_ — Módulos de Atividade

**O que faz:** Atividades que os alunos realizam dentro de um curso (tarefas, quizzes, fóruns, etc.)

**Diretório:** `/mod/nomemod/`

**Arquivos-chave:**
```
mod/meumod/
├── version.php           # Versão do plugin
├── lib.php               # Funções hook (add_instance, update_instance, etc.)
├── mod_form.php          # Formulário de configuração
├── view.php              # Página principal da atividade
├── index.php             # Lista de instâncias no curso
├── db/
│   ├── install.xml       # Estrutura do banco (XMLDB)
│   ├── access.php        # Capacidades (permissões)
│   ├── upgrade.php       # Scripts de atualização
│   └── events.php        # Observadores de eventos
├── classes/
│   └── event/            # Classes de eventos
├── lang/en/meumod.php    # Strings de idioma
├── templates/            # Templates Mustache
├── pix/                  # Ícones
└── amd/                  # JavaScript (RequireJS)
```

**Exemplos reais:** `mod_quiz`, `mod_forum`, `mod_oxymsteams`

**Hooks obrigatórios em lib.php:**
```php
function mod_MEUMOD_supports($feature) {}
function mod_MEUMOD_add_instance($data, $mform = null) {}
function mod_MEUMOD_update_instance($data, $mform = null) {}
function mod_MEUMOD_delete_instance($id) {}
function mod_MEUMOD_get_coursemodule_info($coursemodule) {}
```

---

### block_ — Blocos

**O que faz:** BlocosLaterais na interface (calendário, menu de cursos, bloco de busca)

**Diretório:** `/blocks/nomebloco/`

**Arquivos-chave:**
```
blocks/meubloco/
├── version.php
├── block_meubloco.php    # Classe principal (extende block_base)
├── edit_form.php         # Formulário de configuração do bloco
├── db/
│   ├── install.xml
│   └── access.php
├── lang/en/block_meubloco.php
├── templates/
│   └── meubloco.mustache
├── pix/
└── amd/
```

**Classe principal:**
```php
class block_meubloco extends block_base {
    public function init() {
        $this->title = get_string('pluginname', 'block_meubloco');
    }
    
    public function get_content() {
        $this->content = new stdClass();
        $this->content->text = 'Conteúdo do bloco';
        $this->content->footer = 'Rodapé';
        return $this->content;
    }
    
    public function specialization() {
        // Configurações específicas da instância
    }
}
```

**Exemplos reais:** `block_calendar_month`, `block_myprofile`

---

### auth_ — Autenticação

**O que faz:** Plugins de autenticação (LDAP, OAuth2, Shibboleth)

**Diretório:** `/auth/nomeauth/`

**Arquivos-chave:**
```
auth/nomeauth/
├── version.php
├── auth.php              # Classe principal (extende auth_plugin_base)
├── config.html.php       # Formulário de configuração
├── db/
│   └── install.xml
├── lang/en/auth_nomeauth.php
└── setup.php
```

**Classe principal:**
```php
class auth_plugin_nomeauth extends auth_plugin_base {
    public function loginpage_hook() {}
    public function login_hook($user) {}
    public function user_login($username, $password) {}
    public function getuserinfo($user) {}
}
```

**Exemplos:** `auth_ldap`, `auth_oauth2`, `auth_shibboleth`

---

### enrol_ — Matrículas

**O que faz:** Métodos de matrícula em cursos (manual, auto, LDAP, pagamentos)

**Diretório:** `/enrol/nomeenrol/`

**Arquivos-chave:**
```
enrol/nomeenrol/
├── version.php
├── lib.php               # Classe principal (extende enrol_plugin)
├── db/
│   ├── install.xml
│   └── access.php
├── lang/en/enrol_nomeenrol.php
└── settings.php          # Configurações admin
```

**Classe principal:**
```php
class enrol_nomeenrol extends enrol_plugin {
    protected $@showsubscribeui = true;
    
    public function allow_enrol(stdClass $instance) {}
    public function enrol_user(stdClass $instance, $userid, $roleid = null) {}
    public function get_new_enrol_link(stdClass $instance) {}
}
```

**Exemplos:** `enrol_manual`, `enrol_self`, `enrol_paypal`

---

### question_ — Tipos de Questão

**O que faz:** Tipos de questão para quizzes (multipla escolha, dissertativa, verdadeiro/falso)

**Diretório:** `/question/type/nometipo/`

**Arquivos-chave:**
```
question/type/nometipo/
├── version.php
├── questiontype.php      # Classe principal (extende question_type)
├── db/
│   └── install.xml
├── lang/en/qtype_nometipo.php
├── renderer.php          # Renderização
└── templates/
```

**Exemplos:** `qtype_multichoice`, `qtype_essay`, `qtype_truefalse`

---

### format_ — Formatos de Curso

**O que faz:** Organização visual do conteúdo do curso (tópicos, semanal, social)

**Diretório:** `/course/format/nomeformat/`

**Arquivos-chave:**
```
course/format/nomeformat/
├── version.php
├── lib.php               # Classe do formato
├── db/
│   └── install.xml
├── lang/en/format_nomeformat.php
├── templates/
│   └── courseformat.mustache
└── classes/
```

**Exemplos:** `format_topics`, `format_weeks`, `format_social`

---

### filter_ — Filtros de Texto

**O que faz:** Transformações no texto exibido (MathJax, links automáticos, emoticons)

**Diretório:** `/filter/nomefilter/`

**Arquivos-chave:**
```
filter/nomefilter/
├── version.php
├── filter.php            # Classe principal (extende filter_base)
├── db/
│   └── install.xml
└── lang/en/filter_nomefilter.php
```

**Exemplos:** `filter_tex`, `filter_urltolink`

---

### local_ — Plugins Locais

**O que faz:** Funcionalidades personalizadas que não se encaixam em outros tipos

**Diretório:** `/local/nomelocal/`

**Arquivos-chave:**
```
local/nomelocal/
├── version.php
├── lib.php
├── db/
│   ├── install.xml
│   └── access.php
├── classes/
├── lang/en/local_nomelocal.php
├── settings.php          # Configurações admin
└── templates/
```

**Uso:** Configurações personalizadas, integrações específicas, funcionalidades customizadas

---

### tool_ — Ferramentas Administrativas

**O que faz:** Ferramentas que aparecem no menu Administração do site

**Diretório:** `/admin/tool/nometool/`

**Arquivos-chave:**
```
admin/tool/nometool/
├── version.php
├── index.php             # Página principal da ferramenta
├── db/
│   └── access.php
├── classes/
├── lang/en/tool_nometool.php
└── settings.php
```

**Registro no settings.php:**
```php
$ADMIN->add('accounts', new admin_externalpage(
    'tool_nometool',
    get_string('pluginname', 'tool_nometool'),
    new moodle_url('/admin/tool/nometool/index.php'),
    'tool/nometool:use'
));
```

**Exemplos:** `tool_log`, `tool_phpunit`, `tool_oxytemppass`

---

### editor_ — Plugins de Editor

**O que faz:** Editores de texto (TinyMCE, Atto)

**Diretório:** `/lib/editor/nomeeditor/`

**Arquivos-chave:**
```
lib/editor/nomeeditor/
├── version.php
├── lib.php
├── db/
├── classes/
├── lang/
├── plugins/              # Plugins do editor
└── templates/
```

---

### webservice_ — Web Services

**O que faz:** Endpoints de API REST/SOAP para integrações externas

**Diretório:** `/webservice/nomews/`

**Arquivos-chave:**
```
webservice/nomews/
├── version.php
├── db/
│   ├── services.php      # Definição das funções
│   └── access.php
├── classes/
│   └── external/
│       └── funcao.php    # Classe da função externa
├── lang/en/webservice_nomews.php
└── settings.php
```

**Definição em services.php:**
```php
$functions = [
    'webservice_nomews_get_data' => [
        'classname'   => 'webservice_nomews_external',
        'methodname'  => 'get_data',
        'classpath'   => 'webservice/nomews/externallib.php',
        'description' => 'Obtém dados',
        'type'        => 'read',
        'ajax'        => true,
        'capabilities'=> 'moodle/site:config',
    ],
];

$services = [
    'NomewS Service' => [
        'functions' => ['webservice_nomews_get_data'],
        'restrictedusers' => 0,
        'enabled' => 1,
    ],
];
```

**Exemplos reais:** `webservice_oxywebapi`, `webservice_oxybrigde_notas`

---

### report_ — Relatórios

**O que faz:** Relatórios e dashboards

**Diretório:** `/report/nomerelatorio/`

---

### repository_ — Repositórios

**O que faz:** Fontes de arquivos (localStorage, Dropbox, YouTube)

**Diretório:** `/repository/nomerepo/`

---

### theme_ — Temas

**O que faz:** Aparência visual do Moodle (quase sempre filho do **Boost** no 5.2)

**Diretório:** `public/theme/nometema/`

**Exemplo neste projeto:** `theme_ceuma` (identidade CEUMA)

**Guia completo (criar qualquer Boost child):** [Temas-Boost-Child.md](./Temas-Boost-Child.md)

**Diário do tema Ceuma (erros reais + padrão Moove):** [Tema-Ceuma-Diario.md](./Tema-Ceuma-Diario.md)

**Arquivos-chave:**
```
theme/meutema/
├── version.php / config.php / lib.php / settings.php
├── scss/pre.scss          # tokens ($primary, fontes)
├── scss/post.scss         # navbar, cards, login
├── lang/en/theme_meutema.php
├── classes/privacy/provider.php
└── pix/                   # favicon, screenshot, logo
```

**Pipeline SCSS:** pre (variáveis) → preset Boost → post → extra (admin)

**Brand colour** no admin mapeia para `$primary` (não `$brand-color`).

---

### customfield_ — Campos Personalizados

**O que faz:** Campos customizados para various entidades

**Diretório:** `/customfield/field/nometipo/`

---

### dataformat_ — Formatos de Dados

**O que faz:** Formatos de exportação (CSV, Excel, PDF)

**Diretório:** `/dataformat/nomeformat/`

---

### plagiarism_ — Plágio

**O que faz:** Detecção de plágio (Turnitin, Urkund)

**Diretório:** `/plagiarism/nomeplagiarism/`

---

### availability_ — Restrições de Disponibilidade

**O que faz:** Condições para disponibilizar atividades

**Diretório:** `/availability/condition/nomecond/`

---

### messaging_ — Providers de Mensagem

**O que faz:** Canais de notificação (email, SMS, push)

**Diretório:** `/message/output/nomesaida/`

---

### search_ — Plugins de Busca

**O que faz:** Motores de busca

**Diretório:** `/search/engine/nomemotor/`

---

### tag_ — Plugins de Tag

**O que faz:** Tipos de tags

**Diretório:** `/tag/nometag/`

---

### payment_ — Gateways de Pagamento

**O que faz:** Processadores de pagamento

**Diretório:** `/payment/gateway/nomegateway/`

---

## Ver também

- [[5.2/Estrutura/Base|Estrutura geral do Moodle]]
- [[5.2/Plugins/Criar|Como criar plugins]]
- [[5.2/Plugins/Forms|Forms (mod_form, block)]]
- [[5.2/Plugins/Settings|Settings por tipo]]
- [[5.2/Plugins/Exemplos|Exemplos reais]]
