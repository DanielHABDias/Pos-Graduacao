# 06 - Modelos Estatísticos (2025)

## SUMÁRIO

- [Unidade 01](#unidade-01)
    - [Objetivos da modelagem estatística](#objetivos-da-modelagem-estatística)
    - [Os 5 principais modelos estatísticos](#os-5-principais-modelos-estatísticos)
    - [O que é um modelo estatístico](#o-que-é-um-modelo-estatístico)
    - [Por que modelar?](#por-que-modelar)
    - [Etapas da modelagem estatística](#etapas-da-modelagem-estatística)
    - [Regressão linear](#regressão-linear)
        - [Correlação](#correlação)
        - [Modelos de regressão](#modelos-de-regressão)
        - [Escolhendo o tipo de regressão](#escolhendo-o-tipo-de-regressão)
        - [Regressão linear simples](#regressão-linear-simples)

## UNIDADE 01

### TEMAS ABORDADOS ATÉ O MOMENTO

1. Objetivos e etapas da modelagem estatística.
2. Principais modelos estatísticos.
3. Conceito de modelo estatístico.
4. Regressão linear e correlação.
5. Tipos de regressão e escolha do modelo.
6. Regressão linear simples e seus componentes.

### OBJETIVOS DA MODELAGEM ESTATÍSTICA

Os modelos estatísticos ajudam a transformar dados em informações úteis para análise e tomada de decisões. Eles permitem estudar relações entre variáveis, identificar padrões e fazer previsões com base em evidências.

Os principais objetivos são:

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

- *Representação simplificada e abstrata de um fenômeno* ou sistema real que se baseia em princípios estatísticos e matemáticos.
- *Descreve a relação entre variáveis* e fornece uma estrutura para *entender*, *analisar* e *prever* dados.
- São amplamente utilizados em ciências de dados para *compreender padrões, explorar relações e tomar decisões* informadas com base em evidências quantitativas.

### POR QUE MODELAR?

- **Compreensão do fenômeno:** entender como as variáveis se relacionam.
- **Previsão:** estimar valores futuros ou desconhecidos.
- **Teste de hipóteses:** verificar se uma ideia sobre os dados possui evidências estatísticas.

### ETAPAS DA MODELAGEM ESTATÍSTICA

1. Formulação do problema
2. Coleta de dados
3. Exploração de dados
4. Seleção do modelo
5. Estimação dos parâmetros
6. Validação do modelo
7. Interpretação dos resultados

### REGRESSÃO LINEAR

- A regressão linear é uma técnica estatística que modela a relação entre uma **variável dependente** (ou resposta) e uma ou mais **variáveis independentes** (ou preditoras).
- Ela é usada para explicar relações e prever valores numéricos, como preço, temperatura, renda ou nota.
- O termo “linear” indica que a relação média entre as variáveis pode ser representada por uma reta ou por uma combinação linear de variáveis.

Por exemplo, podemos perguntar: “como a nota muda quando aumentamos as horas de estudo?”. A regressão tenta encontrar a reta que melhor representa essa tendência nos dados.

#### CORRELAÇÃO

**Correlação linear** é uma medida da direção e da intensidade da relação linear entre duas variáveis quantitativas. Ela pode ser avaliada por um gráfico de dispersão e pelo coeficiente de correlação.

![Força da Correlação](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/06%20-%20Modelos%20Estatísticos/images/forcaCorrelacao.png)

![Equação da Correlação](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/06%20-%20Modelos%20Estatísticos/images/equacaoCorrelacao.png)

![Força da Correlação 2](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/06%20-%20Modelos%20Estatísticos/images/forcaCorrelacao2.png)

O coeficiente de correlação de Pearson, representado por $r$, é calculado por:

$$
r = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i - \bar{x})^2}\sqrt{\sum_{i=1}^{n}(y_i - \bar{y})^2}}
$$

Ele assume valores entre $-1$ e $1$:

- Quando $r > 0$, existe uma associação linear positiva: em geral, quando uma variável aumenta, a outra também aumenta.
- Quando $r < 0$, existe uma associação linear negativa: em geral, quando uma variável aumenta, a outra diminui.
- Quando $r = 0$, não há evidência de uma associação linear.

Quanto mais próximo de $1$ ou de $-1$, mais forte é a relação linear. Quanto mais próximo de $0$, mais fraca é essa relação. Correlação não significa, por si só, que uma variável causa a outra.

> Existem também as correlações de Kendall e de Spearman, que são alternativas não paramétricas e podem ser úteis quando os dados não atendem às condições da correlação de Pearson.

#### MODELOS DE REGRESSÃO

![Principais modelos de regressão](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/06%20-%20Modelos%20Estatísticos/images/principaisModelosRegressao.png)

Exemplos:
- Regressão Linear Simples:
    - Uma variável dependente $Y$.
    - Uma variável independente $X$.
- Regressão Linear Múltipla:
    - Uma variável dependente $Y$.
    - Duas ou mais variáveis independentes, como $X_1$, $X_2$ e $X_3$.


#### ESCOLHENDO O TIPO DE REGRESSÃO

O que deve ser analisado antes de escolher:

![Escolhendo o modelo de regressão](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/06%20-%20Modelos%20Estatísticos/images/escolhendoModeloRegressao.png)

![Under X Over X Balanceado](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/06%20-%20Modelos%20Estatísticos/images/UnderXOverXBalanceado.png)

#### REGRESSÃO LINEAR SIMPLES

A regressão linear simples relaciona uma variável dependente $Y$ a uma única variável independente $X$. Seu modelo é:

$$
Y_i = \beta_0 + \beta_1X_i + \varepsilon_i
$$

Onde:

- $Y_i$ é o valor observado da variável dependente para a observação $i$.
- $X_i$ é o valor da variável independente para a observação $i$.
- $\beta_0$ é o **intercepto** ou coeficiente linear: o valor médio esperado de $Y$ quando $X = 0$.
- $\beta_1$ é a **inclinação** ou coeficiente angular: a mudança média esperada em $Y$ para cada aumento de uma unidade em $X$.
- $\varepsilon_i$ é o **erro aleatório**: a parte de $Y$ que o modelo não consegue explicar, incluindo variações naturais e fatores não observados.

Depois de estimar os coeficientes, obtemos a reta prevista:

$$
\hat{Y}_i = \hat{\beta}_0 + \hat{\beta}_1X_i
$$

O acento circunflexo indica um valor estimado pelo modelo. A diferença entre o valor observado e o valor previsto é chamada de **resíduo**:

$$
e_i = Y_i - \hat{Y}_i
$$

Se o resíduo for positivo, o modelo subestimou o valor observado. Se for negativo, o modelo superestimou esse valor. No método dos mínimos quadrados, escolhemos a reta que minimiza a soma dos resíduos ao quadrado:

$$
\sum_{i=1}^{n} e_i^2 = \sum_{i=1}^{n}(Y_i - \hat{Y}_i)^2
$$

O quadrado evita que resíduos positivos e negativos se anulem e dá mais peso aos erros maiores.

Para que esse modelo seja adequado, é importante verificar se:

- o relacionamento médio entre $X$ e $Y$ é aproximadamente linear;
- há uma quantidade razoável de informação para estimar a relação;
- os resíduos não apresentam padrões evidentes;
- a correlação é uma evidência inicial compatível com a relação estudada, mas não é uma exigência de causalidade.