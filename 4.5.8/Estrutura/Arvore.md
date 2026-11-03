# Árvore deste checkout 4.5.8

Diretórios na raiz. O que cada um é no código, não uma lista genérica.

## Entrada HTTP

| Arquivo | Função |
|---------|--------|
| `index.php` | Frontpage. Sem `config.php`, manda para `install.php`. Logado com homepage Meu Moodle, redireciona para `/my/` |
| `install.php` | Instalador |
| `config.php` | Não versionado; modelo é `config-dist.php` |
| `pluginfile.php` | Entrega arquivo de uma file area |
| `draftfile.php` | Arquivo ainda no rascunho do file manager |
| `tokenpluginfile.php` | Arquivo via token (app / webservice) |
| `file.php` | Legado de course files |
| `r.php` | Recursos com slashargument |
| `help.php` / `help_ajax.php` | Pop-ups de ajuda |
| `editmode.php` | Liga/desliga modo edição |
| `brokenfile.php` | Placeholder de arquivo quebrado |

## Subsistemas (pasta = código de produto)

| Pasta | Componente | O que guarda |
|-------|------------|----------------|
| `admin/` | subsistema `admin` | UI de administração, upgrade, `tool_*` |
| `ai/` | subsistema `ai` | Placements e providers de IA |
| `analytics/` | `analytics` | Modelos de learning analytics |
| `auth/` | `auth_*` | Login |
| `availability/` | `availability_*` | Restrições de atividade |
| `backup/` | backup/restore | Inclui target import usado pelo duplicar de `course/mod.php` |
| `badges/` | insígnias | |
| `blocks/` | `block_*` | Blocos |
| `blog/` | blog | |
| `cache/` | MUC | Stores em `cache/stores` |
| `calendar/` | calendário | Tipos em `calendar/type` |
| `cohort/` | coortes | |
| `comment/` | comentários | |
| `communication/` | `communication_*` | Provedores de comunicação |
| `competency/` | competências | |
| `completion/` | conclusão de atividade/curso | |
| `contentbank/` | banco de conteúdo | Tipos em `contentbank/contenttype` |
| `course/` | curso | Formatos, matrícula na UI, **`mod.php`** |
| `customfield/` | campos custom | Tipos em `customfield/field` |
| `dataformat/` | export CSV, Excel, etc. | |
| `enrol/` | `enrol_*` | Métodos de matrícula |
| `filter/` | `filter_*` | Filtros de texto |
| `grade/` | livro de notas | `grade/report`, `grade/export`, `grade/import`, `grade/grading` |
| `group/` | grupos e agrupamentos | |
| `h5p/` | H5P | Bibliotecas em `h5p/h5plib` |
| `install/` | páginas do instalador | |
| `lang/` | `lang/en` do core | Pacotes de idioma ficam em dataroot, não aqui |
| `lib/` | core | Ver [[4.5.8/Lib/Bibliotecas]] |
| `local/` | `local_*` | Vazio neste checkout (só readme) |
| `login/` | telas de login, logout, senha | |
| `media/` | players | `media/player` |
| `message/` | mensagens | Saídas em `message/output` |
| `mnet/` | Moodle Network | |
| `mod/` | `mod_*` | Atividades |
| `my/` | Dashboard e Meus cursos | |
| `notes/` | anotações do usuário | |
| `payment/` | `paygw_*` | Gateways em `payment/gateway` |
| `pix/` | ícones do core | |
| `plagiarism/` | `plagiarism_*` | Vazio de plugins de terceiros; só o gancho |
| `portfolio/` | `portfolio_*` | |
| `privacy/` | API de privacidade | |
| `question/` | banco de questões | `type`, `behaviour`, `format`, `bank` |
| `rating/` | ratings | |
| `report/` | `report_*` | Relatórios de curso e de site |
| `reportbuilder/` | subsistema | Construtor de relatórios |
| `repository/` | `repository_*` | |
| `rss/` | feeds | |
| `search/` | busca global | Engines em `search/engine` |
| `sms/` | SMS | Gateways em `sms/gateway` |
| `tag/` | tags | |
| `theme/` | `theme_boost`, `theme_classic` | |
| `user/` | perfil, preferências | Campos em `user/profile/field` |
| `webservice/` | protocolos | `rest/` e `soap/` |
| `vendor/` | Composer | Não é plugin Moodle |

## Atividades em `mod/`

`assign`, `bigbluebuttonbn`, `book`, `chat`, `choice`, `data`, `feedback`, `folder`, `forum`, `glossary`, `h5pactivity`, `imscp`, `label`, `lesson`, `lti`, `page`, `quiz`, `resource`, `scorm`, `subsection`, `survey`, `url`, `wiki`, `workshop`.

`subsection` é atividade de subseção (4.5). `chat` continua no código desta branch.

## Formatos de curso

`course/format/`: `topics`, `weeks`, `social`, `singleactivity`, mais a base em `course/format/classes`.

## Temas

Só `theme/boost` e `theme/classic`. Boost é o tema padrão novo; Classic é o filho legado. Não há `theme_ceuma` nem outro child neste diretório.

## Referências

- [[4.5.8/Admin/Administracao]]
- [[4.5.8/Course/Mod]]
- [[4.5.8/Plugins/Tipos]]
