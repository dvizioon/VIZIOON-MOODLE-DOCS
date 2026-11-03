# Escala de Notas

## O que é?

Uma escala é um conjunto de valores separados por vírgulas que o Moodle usa para avaliar.

## Criar Escala

1. Administração do Site > Notas > Escalas
2. Clique em "Adicionar uma escala"
3. Nome: "Nível de Desempenho"
4. Escala: "Insuficiente, Regular, Bom, Excelente"
5. Salve

## Usar em Atividade

1. Crie/edite uma atividade
2. Tipo de nota: Escala
3. Escolha a escala

## Resultados (Outcomes)

**Habilitar:** Administração do Site > Recursos Avançados > Habilitar resultados

**Criar:** Administração do Site > Notas > Resultados > Adicionar um resultado

## Banco de Dados

| Tabela | Campos principais |
|---|---|
| scale | id, courseid, name, scale, description |
| grade_outcomes | id, shortname, fullname, scaleid |
