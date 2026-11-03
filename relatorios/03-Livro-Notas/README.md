# Livro de Notas - Guia Completo

## O que é o Livro de Notas?

O Livro de Notas é onde você organiza todas as notas do curso. Nele você:
- Cria categorias para agrupar atividades
- Define como as notas são calculadas (agregação)
- Acompanha o progresso dos alunos
- Exporta notas

---

## Exemplo Prático: Configurar o Livro de Notas

Vamos criar um Livro de Notas completo para uma disciplina fictícia com:
- **2 Provas** (P1 e P2)
- **2 Atividades** (Trabalho 1 e Trabalho 2)
- **1 Fórum** (Participação)

### Resultado Esperado

```
Matemática I
├── Provas (50% do total)
│   ├── Prova P1 (25%)
│   └── Prova P2 (25%)
├── Atividades (30% do total)
│   ├── Trabalho 1 (15%)
│   └── Trabalho 2 (15%)
└── Participação (20% do total)
    └── Fórum (20%)
```

---

## Passo 1: Criar as Categorias

### 1.1 Criar Categoria "Provas"

1. Acesse o curso
2. Clique em **"Mais"** (menu superior)
3. Clique em **"Livro de Notas"**
4. Clique em **"Configuração do Livro de Notas"**
5. Clique em **"Adicionar categoria"**
6. Preencha:
   - **Nome da categoria:** `Provas`
   - **Agregação:** `Média de notas`
   - **Apenas notas com valor:** Marque ✓
7. Clique em **"Salvar mudanças"**

### 1.2 Criar Categoria "Atividades"

1. Clique em **"Adicionar categoria"**
2. Preencha:
   - **Nome da categoria:** `Atividades`
   - **Agregação:** `Média de notas`
   - **Apenas notas com valor:** Marque ✓
3. Salve

### 1.3 Criar Categoria "Participação"

1. Clique em **"Adicionar categoria"**
2. Preencha:
   - **Nome da categoria:** `Participação`
   - **Agregação:** `Média de notas`
3. Salve

---

## Passo 2: Configurar o Peso das Categorias

### 2.1 Entendendo os Pesos

Agora precisamos definir que:
- Provas = 50% do total
- Atividades = 30% do total
- Participação = 20% do total

### 2.2 Configurar no Livro de Notas

1. Na Configuração do Livro de Notas, clique no ícone de **edição** ao lado da categoria **"Provas"**
2. Procure o campo **"Peso"** (ou "Ajuste de peso")
3. Digite: `50`
4. Salve

5. Repita para **"Atividades"**: peso = `30`
6. Repita para **"Participação"**: peso = `20`

### 2.3 Verificar os Pesos

A soma dos pesos deve dar 100:
- Provas: 50
- Atividades: 30
- Participação: 20
- **Total: 100** ✓

---

## Passo 3: Criar os Itens de Nota

### 3.1 Criar Prova P1

#### Opção A: Via Atividade Quiz (Recomendado)

1. Volte para o curso (clique no nome do curso)
2. Clique em **"Ativar edição"**
3. Clique em **"Adicionar uma atividade ou recurso"**
4. Selecione **"Quiz"**
5. Configure:
   - **Nome:** `Prova P1`
   - **Instruções:** `Responda todas as questões`
   - **Data de entrega:** `30/05/2025`
   - **Limite de tempo:** `60 minutos`
6. Salve
7. Clique em **"Editar prova"**
8. Adicione questões do Banco de Questões
9. Salve

#### Opção B: Nota Manual (Sem Quiz)

1. Volte para o Livro de Notas > Configuração
2. Clique em **"Adicionar item de nota"**
3. Configure:
   - **Nome do item:** `Prova P1`
   - **Tipo de nota:** `Valor`
   - **Nota máxima:** `10`
   - **Nota para aprovar:** `6`
   - **Categoria pai:** `Provas`
4. Salve

### 3.2 Criar Prova P2

Repita o processo da P1:
- **Nome:** `Prova P2`
- **Nota máxima:** `10`
- **Categoria pai:** `Provas`

### 3.3 Criar Trabalho 1

1. **"Adicionar uma atividade ou recurso"**
2. Selecione **"Assignment"** (Tarefa)
3. Configure:
   - **Nome:** `Trabalho 1`
   - **Instruções:** `Entregue o trabalho sobre...`
   - **Data de entrega:** `15/05/2025`
   - **Tipo de nota:** `Escala` ou `Valor`
   - **Nota máxima:** `10`
4. Salve

### 3.4 Criar Trabalho 2

Repita o processo:
- **Nome:** `Trabalho 2`
- **Nota máxima:** `10`
- **Categoria pai:** `Atividades`

### 3.5 Criar Fórum de Participação

1. **"Adicionar uma atividade ou recurso"**
2. Selecione **"Forum"**
3. Configure:
   - **Nome:** `Fórum de Participação`
   - **Tipo:** `Postagem única`
   - **Modo de agrupamento:** `Grupos visíveis`
   - **Avaliação:** `Escala` ou `Valor`
   - **Nota máxima:** `10`
4. Salve

---

## Passo 4: Mover Itens para as Categorias

### 4.1 Verificar se os Itens Estão nas Categorias Certas

1. Volte para **Livro de Notas > Configuração**
2. Verifique se:
   - Prova P1 está na categoria **Provas**
   - Prova P2 está na categoria **Provas**
   - Trabalho 1 está na categoria **Atividades**
   - Trabalho 2 está na categoria **Atividades**
   - Fórum está na categoria **Participação**

### 4.2 Mover Item (se necessário)

1. Selecione o item (marque a caixa)
2. No menu **"Com com as questões selecionadas..."**
3. Escolha **"Mover para..."**
4. Selecione a categoria de destino
5. Confirme

---

## Passo 5: Configurar a Agregação

### 5.1 Método de Agregação

Cada categoria pode ter um método diferente:

| Categoria | Método | Por quê? |
|---|---|---|
| Provas | Média de notas | P1 e P2 com mesmo peso |
| Atividades | Média de notas | T1 e T2 com mesmo peso |
| Participação | Média de notas | Só 1 item |
| **Curso** | **Média ponderada** | **Peso de cada categoria** |

### 5.2 Configurar no Livro de Notas

1. Na Configuração do Livro de Notas
2. Clique no ícone de edição da categoria **raiz** (nome do curso)
3. Selecione **"Média ponderada de notas"**
4. Salve

### 5.3 Como Funciona a Média Ponderada

```
Total do Curso = (Nota Provas × 50% + Nota Atividades × 30% + Nota Participação × 20%)
```

**Exemplo com um aluno:**

| Categoria | Nota | Peso | Contribuição |
|---|---|---|---|
| Provas | 8.0 | 50% | 4.0 |
| Atividades | 7.0 | 30% | 2.1 |
| Participação | 9.0 | 20% | 1.8 |
| **Total** | | | **7.9** |

---

## Passo 6: Atribuir Pesos Individuais (Opcional)

### 6.1 O que é?

Além do peso da categoria, você pode definir pesos individuais para cada item dentro da categoria.

### 6.2 Exemplo: Provas com Pesos Diferentes

Se P1 vale mais que P2:

1. Na Configuração do Livro de Notas
2. Clique no ícone de edição ao lado de **Prova P1**
3. Procure **"Peso"**
4. Digite: `60` (P1 vale 60% das provas)
5. Salve

6. Clique no ícone de edição ao lado de **Prova P2**
7. Digite: `40` (P2 vale 40% das provas)
8. Salve

### 6.3 Resultado

```
Nota Provas = (P1 × 60% + P2 × 40%)
```

Se P1 = 8 e P2 = 6:
```
Nota Provas = (8 × 0.6 + 6 × 0.4) = 4.8 + 2.4 = 7.2
```

---

## Passo 7: Visualizar o Livro de Notas

### 7.1 Relatório do Avaliador

1. **Curso > Notas > Relatório do avaliador**
2. Veja a matriz:
   - **Linhas:** Alunos
   - **Colunas:** Atividades
   - **Última coluna:** Nota total

### 7.2 Editar Notas

1. No Relatório do Avaliador
2. Clique no ícone de **edição** ao lado da nota
3. Digite a nota
4. Pressione Enter
5. A nota é salva automaticamente

### 7.3 Adicionar Feedback

1. Clique no ícone de **edição**
2. Digite a nota
3. Clique em **"Mostrar mais"**
4. Digite o feedback
5. Salve

---

## Passo 8: Notas dos Alunos

### 8.1 Como o Aluno Vê

1. O aluno acessa o curso
2. Clica em **"Notas"**
3. Vê suas notas por atividade
4. Vê a nota total

### 8.2 Relatório do Aluno

1. **Curso > Notas > Relatório do aluno**
2. Selecione o aluno
3. Veja:
   - Nota de cada atividade
   - Percentual de contribuição
   - Feedback
   - Nota total

---

## Passo 9: Configurações Importantes

### 9.1 Tipo de Exibição

**Caminho:** Livro de Notas > Configurações do curso

| Configuração | Opções |
|---|---|
| Tipo de exibição | Número real, Porcentagem, Letra |
| Casas decimais | 0, 1, 2, 3 |
| Posição do total | Primeiro ou Último |

### 9.2 Notas Ocultas

| Configuração | O que acontece |
|---|---|
| Ocultar total se tiver notas ocultas | Total fica invisível |
| Mostrar total menos notas ocultas | Total parcial |
| Mostrar total real | Mostra tudo |

### 9.3 Nota para Aprovar

1. Clique no ícone de edição do item
2. **"Nota para aprovar":** `6`
3. O Moodle mostra ✓ (aprovado) ou ✗ (reprovado)

---

## Passo 10: Exportar Notas

### 10.1 Exportar em Excel

1. **Curso > Notas > Exportar**
2. Selecione **"Planilha"**
3. Configure:
   - Incluir feedback: Sim
   - Apenas notas atualizadas: Sim
4. Clique em **"Exportar"**
5. O arquivo .xls é baixado

### 10.2 Exportar em Texto

1. **Curso > Notas > Exportar**
2. Selecione **"Texto simples"**
3. Formato: Tab-separado
4. Exportar

### 10.3 Importar Notas

1. **Curso > Notas > Importar**
2. Selecione **"CSV"**
3. Formato do arquivo:
   ```
   userid,itemid,grade,feedback
   2,101,8.5,"Bom trabalho"
   3,101,7.0,"Pode melhorar"
   ```
4. Faça upload
5. Revise o preview
6. Confirme

---

## Resumo: Configuração Completa

### Estrutura Final

```
Matemática I
├── Provas (Média de notas, peso 50%)
│   ├── Prova P1 (nota: 8.0)
│   └── Prova P2 (nota: 6.0)
├── Atividades (Média de notas, peso 30%)
│   ├── Trabalho 1 (nota: 7.0)
│   └── Trabalho 2 (nota: 9.0)
└── Participação (Média de notas, peso 20%)
    └── Fórum (nota: 9.0)
```

### Cálculo do Total

```
Provas = (8.0 + 6.0) / 2 = 7.0
Atividades = (7.0 + 9.0) / 2 = 8.0
Participação = 9.0

Total = (7.0 × 50% + 8.0 × 30% + 9.0 × 20%)
Total = (3.5 + 2.4 + 1.8)
Total = 7.7
```

---

## Dicas Importantes

1. **Crie categorias antes** - Organize antes de adicionar itens
2. **Defina pesos claramente** - Documente os pesos para os alunos
3. **Use nota para aprovar** - Ajuda a identificar reprovados
4. **Revise regularmente** - Verifique se os cálculos estão corretos
5. **Exporte backup** - Baixe as notas periodicamente
6. **Comunique aos alunos** - Explique como o total é calculado
