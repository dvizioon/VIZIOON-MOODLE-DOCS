# IOMAD - Multi-Tenancy para Moodle

## O que é IOMAD?

IOMAD (Multi-tenancy Suite) é um conjunto de plugins que transforma uma instalação Moodle em uma **plataforma multi-tenant**. Cada "tenant" é chamado de **Company** (Empresa).

**Desenvolvedor:** e-Learn Design Ltd (Moodle Partner)
**Versão:** 5.2.3 (Build: 20260914)
**Requer:** Moodle 5.2+

## Conceito Central: A Empresa (Company)

Cada empresa no IOMAD é um **tenant independente** com:
- Seus próprios cursos e categorias
- Seus usuários e gestores
- Suas licenças de acesso
- Seu tema visual (logo, cores, CSS)
- Seus templates de e-mail
- Seus certificados
- Seus domínios (para auto-atribuição)
- Suas páginas customizadas

## Como Funciona na Prática

```
┌─────────────────────────────────────────┐
│              MOODLE 5.2                 │
│         (Instalação Única)              │
├─────────────┬─────────────┬─────────────┤
│  Empresa A  │  Empresa B  │  Empresa C  │
│  (Tenant 1) │  (Tenant 2) │  (Tenant 3) │
├─────────────┼─────────────┼─────────────┤
│ • Cursos    │ • Cursos    │ • Cursos    │
│ • Usuários  │ • Usuários  │ • Usuários  │
│ • Licenças  │ • Licenças  │ • Licenças  │
│ • Tema      │ • Tema      │ • Tema      │
│ • E-mails   │ • E-mails   │ • E-mails   │
└─────────────┴─────────────┴─────────────┘
```

## Vantagens do IOMAD

| Recurso      | Descrição                              |
| ------------ | -------------------------------------- |
| Multi-tenant | Várias empresas numa só instalação     |
| Isolamento   | Dados de cada empresa separados        |
| Licenças     | Controle de acesso por licença         |
| Temas        | Cada empresa com sua identidade visual |
| E-mails      | Templates customizados por empresa     |
| Certificados | Certificados com logo da empresa       |
| Relatórios   | Relatórios por empresa/departamento    |
| SSO          | Autenticação OIDC/SAML por empresa     |
| Comércio     | Venda de licenças (e-commerce)         |
| Capacitação  | Learning paths e microlearning         |

## Links

- [[IOMAD/VisaoGeral|Visão Geral Completa]]
- [[5.2/IOMAD/Empresas/Criar|Criando uma Empresa]]
- [[IOMAD/Empresas/Gerenciar|Gerenciando Empresas]]
- [[IOMAD/Licencas/Entender|Entendendo Licenças]]
- [[IOMAD/Licencas/Gerenciar|Gerenciando Licenças]]
- [[IOMAD/Plugins/Lista|Lista de Plugins IOMAD]]
- [[IOMAD/Classes/Classes|Classes Principais]]
- [[IOMAD/Reports/Relatorios|Relatórios Disponíveis]]
- [[IOMAD/Configuracao|Configuração do Sistema]]
