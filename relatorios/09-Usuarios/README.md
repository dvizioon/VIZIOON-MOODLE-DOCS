# Gerenciar Usuários no Moodle

## Tipos de Usuário

| Tipo | Descrição |
|---|---|
| Administrador | Controle total do site |
| Professor | Cria e avalia atividades |
| Aluno | Acessa conteúdo e envia atividades |
| Monitor | Auxilia sem avaliar |
| Convidado | Acesso limitado |

## Adicionar Usuário

### Passo a Passo

1. Administração do Site > Usuários > Contas > Adicionar um novo usuário
2. Preencha:

| Campo | Descrição |
|---|---|
| Nome de usuário | "joao.silva" |
| Nome | "João" |
| Sobrenome | "Silva" |
| Email | "joao@exemplo.com" |
| Senha | "********" |
| Cidade | "São Paulo" |

3. Salve

### Dica: Criação em Lote

1. Administração do Site > Usuários > Contas > Carregar usuários
2. Faça upload de arquivo CSV
3. Formato: `username, firstname, lastname, email, password`
4. Revise e confirme

## Matricular Usuário em Curso

### Via Interface

1. Acesse o curso
2. Mais > Usuários > Inscrever usuários
3. Selecione o usuário
4. Selecione o papel (Aluno, Professor)
5. Selecione o período (opcional)
6. Clique em "Inscrever"

### Via CSV

1. Mais > Usuários > Inscrever usuários
2. "Inscrição em lote"
3. Faça upload de CSV
4. Formato: `userid, roleid, coursename`
5. Confirme

## Papéis (Roles)

### Papéis Padrão

| Papel | Permissões |
|---|---|
| Manager | Gerenciar curso e configurações |
| Editing teacher | Criar, editar, avaliar |
| Teacher | Avaliar (não cria) |
| Student | Acessar, enviar, ver notas |
| Guest | Apenas visualizar |
| Non-editing teacher | Auxiliar sem editar |

### Criar Papel Customizado

1. Administração do Site > Usuários > Permissões > Definir papéis
2. "Criar papel"
3. Nome: "Monitor"
4. Copiar de: "Non-editing teacher"
5. Ajuste as permissões
6. Salve

## Campo de Perfil

### Criar Campo Customizado

1. Administração do Site > Usuários > Campos de perfil
2. "Criar um novo campo de perfil"
3. Tipo: Texto, CheckBox, Date, Menu, etc.
4. Nome: "Matrícula"
5. Configurações
6. Salve

### Usar em Relatórios

Campos customizados aparecem em:
- Relatório de usuários
- Filtros de busca
- Exportação de dados

## Autenticação

### Métodos Disponíveis

| Método | Descrição |
|---|---|
| Email | Cadastro por email |
| Manual | Criação manual |
| LDAP | Diretório LDAP |
| OAuth2 | Google, Microsoft, etc. |
| Shibboleth | SSO institucional |
| LTI | Integração com outros sistemas |

### Configurar OAuth2 (Google)

1. Administração do Site > Serviços > OAuth2
2. Adicione o provedor (Google)
3. Insira Client ID e Secret
4. Configure os escopos
5. Salve

## Sincronização com LDAP

### Configuração

1. Administração do Site > Plugins > Autenticação > LDAP
2. Configure:

| Campo | Exemplo |
|---|---|
| Host | ldap://ldap.exemplo.com |
| Bind DN | cn=admin,dc=exemplo,dc=com |
| Senha | ******** |
| Usuário | uid |
| Context | ou=users,dc=exemplo,dc=com |

3. Salve
4. Clique em "Sincronizar usuários"

## Boas Práticas

1. **Princípio do menor privilégio** - Apenas permissões necessárias
2. **Revisão regular** - Verifique permissões periodicamente
3. **Backup** - Exporte lista de usuários regularmente
4. **Limpeza** - Remova usuários inativos
5. **Documentação** - Registre políticas de acesso
