# Configurar Agregação no Livro de Notas

## O que é Agregação?

Agregação é o método usado para calcular o total de notas de uma categoria ou do curso.

## Configurar Agregação

### Passo a Passo

1. Acesse: Curso > Livro de Notas > Configuração
2. Clique no ícone de edição da categoria
3. Selecione o "Método de agregação"
4. Configure as opções
5. Salve

## Métodos Disponíveis

### Média de Notas

**Fórmula:** `Σ(notas) / Quantidade`

**Exemplo:**
- Prova P1: 8
- Prova P2: 6
- Trabalho: 9
- **Total:** (8 + 6 + 9) / 3 = **7.67**

**Quando usar:** Todas as notas têm o mesmo peso.

---

### Média Ponderada

**Fórmula:** `Σ(peso × nota) / Σ(pesos)`

**Exemplo:**
- Prova P1: 8 (peso 30%)
- Prova P2: 6 (peso 30%)
- Trabalho: 9 (peso 40%)
- **Total:** (8×0.3 + 6×0.3 + 9×0.4) / (0.3+0.3+0.4) = **7.80**

**Quando usar:** Você quer controlar o peso de cada item.

---

### Média Ponderada Simples (Padrão Moodle)

**Fórmula:** `Σ(grademax × nota) / Σ(grademax)`

**Exemplo:**
- Prova P1: 8/10 (peso = 10)
- Prova P2: 6/10 (peso = 10)
- Trabalho: 9/20 (peso = 20)
- **Total:** (8×10 + 6×10 + 9×20) / (10+10+20) = **8.00**

**Quando usar:** Pesos proporcionais à nota máxima.

---

### Média com Créditos Extras

**Como funciona:** Itens marcados como "extra credit" somam ao total sem entrar no denominador.

**Exemplo:**
- Prova P1: 8/10
- Prova P2: 6/10
- Bônus: +2 pontos
- **Total:** (8 + 6) / 2 + 2 = **9.00**

**Quando usar:** Atividades bônus.

---

### Mediana

**Como funciona:** Ordena as notas e pega o valor central.

**Exemplo:**
- Notas: 4, 6, 7, 8, 10
- **Mediana:** 7

**Quando usar:** Evitar notas extremas.

---

### Menor Nota

**Como funciona:** Retorna a menor nota do grupo.

**Exemplo:**
- Notas: 4, 6, 7, 8, 10
- **Total:** 4

**Quando usar:** Tentativas múltiplas (melhor nota conta).

---

### Maior Nota

**Como funciona:** Retorna a maior nota do grupo.

**Exemplo:**
- Notas: 4, 6, 7, 8, 10
- **Total:** 10

**Quando usar:** Tentativas múltiplas (melhor nota conta).

---

### Moda

**Como funciona:** Retorna a nota mais frequente.

**Exemplo:**
- Notas: 5, 7, 7, 8, 9
- **Moda:** 7

**Quando usar:** Notas discretas.

---

### Natural (Padrão 5.2)

**Fórmula:** `Σ(peso × nota) / Σ(pesos)`

**Diferença da Média Ponderada:** Os pesos são calculados automaticamente pela nota máxima de cada item.

**Exemplo:**
- Prova P1: 8/10 (peso = 10)
- Prova P2: 6/10 (peso = 10)
- Trabalho: 9/20 (peso = 20)
- **Total:** (8×10 + 6×10 + 9×20) / (10+10+20) = **8.00**

**Quando usar:** Transparência total nos pesos.

---

## Configurações Adicionais

| Configuração | Descrição |
|---|---|
| Apenas notas com valor | Excluir notas vazias da agregação |
| Manter N mais altas | Manter apenas as N melhores notas |
| Descartar N mais baixas | Remover as N piores notas |
| Incluir resultados | Incluir outcomes na agregação |

## Exemplo Prático

### Configurar Notas de Prova

1. Criar categorias: "Provas", "Trabalhos", "Participação"
2. Configurar agregação em cada uma
3. Definir pesos das categorias
4. Ajustar itens individuais

### Estrutura Recomendada

```
Curso (Média Ponderada)
├── Provas (50% do total)
│   ├── Prova P1 (25%)
│   └── Prova P2 (25%)
├── Trabalhos (30% do total)
│   ├── Trabalho 1 (15%)
│   └── Trabalho 2 (15%)
└── Participação (20% do total)
    └── Forum (20%)
```
