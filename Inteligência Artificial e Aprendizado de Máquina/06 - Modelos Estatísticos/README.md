# 06 - Modelos Estatísticos (2025)

## SUMÁRIO

## UNIDADE 01

### TEMAS ABORDADOS

1. Fundamentos da regressão linear: equação da reta de regressão, método dos mínimos quadrados.
2. Formulação do modelo de regressão linear: variáveis dependentes e independentes, termo de erro
3. Interpretação dos coeficientes de regressão: coeficiente angular, coeficiente linear, significância estatística.
4. Avaliação da qualidade do ajuste do modelo: coeficiente de determinação ajustado (R² ajustado), F-teste de significância global.
5. Diagnóstico de multicolinearidade, heterocedasticidade e outros problemas potenciais do modelo.
6. Aplicações práticas e estudos de caso

### OBJETIVOS DA MODELAGEM ESTATÍSTICAS

- Explorar o papel fundamental dos modelos estatísticos na análise de dados e na tomada de decisões.
- Estudar a relação das variáveis.
- Os modelos podem fornecer insights valiosos e prever tendências, auxiliando em diversos contexto.

1. Descrição 
2. Inferência
3. Previsão
4. Controle e otimização

### OS 5 PRINCIPAIS MODELOS ESTATÍSTICOS

1. Regressão Linear
2. Análise de Variância (ANOVA)
3. Regressão Logística
4. Análise de Sobrevivência
5. Séries Temporais

### O QUE É UM MODELO ESTATÍSTICO

- *Representação simplificada e abstrata de um fenômeno* ou sistema real que se baseia em príncipios estatísticos e matemáticos.
- *Descreve a relação entre variáveis* e fornece uma estrutura para *entender*, *analisar* e *prever* dados.
- São amplamente utilizados em ciências de dados para *compreender padrões, explorar relações e tomar decisões* informadas com base em evidências quantitativas.

### PORQUE MODELAR?

- Compreensão do fenômeno
- Previsão e predição
- Teste de hipóteses

### ETAPAS DA MODELAGEM ESTATÍSTICA

1. Formulação do problema
2. Coleta de dados
3. Exploração de dados
4. Seleção do modelo
5. Estimação do parâmetros
6. Validação do modelo
7. Interpretação dos resultados

### REGRESSÃO LINEAR

#### CORRELAÇÃO

Correlação linear: 
Determinado através de gráficos de dispersão e do coeficiente de variação.

![Força da Correlação](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/06%20-%20Modelos%20Estatísticos/images/forcaCorrelacao.png)

![Equação da Correlação](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/06%20-%20Modelos%20Estatísticos/images/equacaoCorrelacao.png)

![Força da Correlação 2](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/06%20-%20Modelos%20Estatísticos/images/forcaCorrelacao2.png)

É usado para determinar se existe relação linear entre variáveis aleatórias quantitativas.
A correlação *r* assume valores entre -1 e 1

- Quando r > 0, então existe uma associação (linear) positiva.
- Quando r < 0, então existe uma associação (linear) negativa.
- Quando r = 0, então não existe uma associação (linear).

> Existe também correlação de Kendall e de Spearman. Que são correlações não paramétricas.

