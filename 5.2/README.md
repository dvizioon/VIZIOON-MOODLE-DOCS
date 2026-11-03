# Moodle 5.2 - Documentação para Desenvolvimento

← [[README|APP-MOODLE — índice de versões]] · [[4.5.8/README|Moodle 4.5.8]]

## Visão Geral

Esta documentação é um guia prático para desenvolvimento de plugins e customizações no Moodle 5.2. Baseada na análise direta do código fonte. Forms e settings: [[Plugins/Forms]], [[Plugins/Settings]].

## Estrutura do Moodle 5.2

```
moodle/
├── admin/          # Administração e configurações
├── auth/           # Plugins de autenticação
├── backup/         # Sistema de backup/restore
├── blocks/         # Blocos (sidebar)
├── cache/          # Sistema de cache (MUC)
├── calendar/       # Calendário
├── comment/        # Sistema de comentários
├── completion/     # Rastreamento de conclusão
├── course/         # Gestão de cursos
├── enrol/          # Plugins de matrícula
├── files/          # Armazenamento de arquivos
├── filter/         # Filtros de texto
├── grade/          # Sistema de notas (Gradebook)
├── group/          # Gestão de grupos
├── lang/           # Pacotes de idioma
├── lib/            # Bibliotecas centrais (CORE)
├── local/          # Plugins locais
├── message/        # Sistema de mensagens
├── mod/            # Módulos de atividade (Quiz, Forum, etc.)
├── question/       # Banco de questões
├── rating/         # Sistema de avaliação
├── report/         # Plugins de relatório
├── repository/     # Repositórios de arquivos
├── search/         # Busca global
├── theme/          # Temas
├── user/           # Gestão de usuários
└── webservice/     # API REST/SOAP
```

## Links Úteis

- [[Estrutura/Base|Estrutura Base do Moodle]]
- [[Plugins/Tipos|Tipos de Plugin]]
- [[Plugins/Criar|Como Criar um Plugin]]
- [[Plugins/Forms|Forms — mod_form, block edit_form, moodleform]]
- [[Plugins/Settings|Settings — settings.php por tipo de plugin]]
- [[Classes/Persistent|Classe Persistent (Active Record)]]
- [[DB/Schema|Schema do Banco de Dados]]
- [[Templates/Mustache|Templates Mustache]]
- [[Frontend/React|React dentro do Moodle 5.2]]
- [[WebServices/Criar|Criar Web Services]]
- [[Eventos/Observer|Sistema de Eventos]]
- [[Plugins/Exemplos|Exemplos Reais (Oxygeni)]]
- [[Classes/Helper|Helper Classes e Funções]]
- [[ReportBuilder/Fonte-Atividades|Report Builder — Fonte Atividades (`report_activities`)]]
- [[Estrutura/Report-Plugin|Módulo de Relatórios (plugin report_)]]
- [[Seguranca/Funcoes|Segurança — funções e APIs]]
- [[Seguranca/Checklist|Segurança — checklist do plugin]]
- [[Seguranca/Anti-Padroes|Segurança — anti-padrões (plugins NTI)]]
