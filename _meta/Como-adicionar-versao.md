# Como adicionar outra versão do Moodle neste vault

1. Baixe o código em `Projetos/MOODLE/<versão>/` (ex.: `4.4.10`, `5.1`).
2. Leia `version.php` da raiz: `$release`, `$branch`, `$version`, PHP mínimo.
3. Crie `APP-MOODLE/<versão>/` espelhando a estrutura de [[4.5.8/README]]:

```text
<versão>/
├── README.md
├── Estrutura/
├── Plugins/     # Tipos, Criar, Forms, Settings, Exemplos
├── Classes/
├── DB/
├── Eventos/
├── WebServices/
├── Templates/
├── Frontend/
├── Seguranca/
├── Admin/
└── ReportBuilder/  # se existir no core
```

4. Documente diferenças reais vs 4.5.8 (pasta `public/`, React, tipos novos em `components.json`).
5. Atualize a tabela de versões no [[README]].
6. Não copie o core para dentro do vault — só as notas Markdown.
