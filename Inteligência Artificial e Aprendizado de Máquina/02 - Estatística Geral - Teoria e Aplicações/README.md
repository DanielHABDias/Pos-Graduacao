# 02 - Estatística Geral - Teoria e Aplicações

## SUMÁRIO
- [02 - Estatística Geral - Teoria e Aplicações](#02---estatística-geral---teoria-e-aplicações)
  - [SUMÁRIO](#sumário)
  - [UNIDADE 01](#unidade-01)
    - [CONCEITOS BÁSICOS](#conceitos-básicos)
      - [O QUE É POPULAÇÃO?](#o-que-é-população)
      - [O QUE É AMOSTRA?](#o-que-é-amostra)
      - [O QUE SÃO PARÂMETROS?](#o-que-são-parâmetros)
      - [O QUE SÃO ESTATÍSTICAS?](#o-que-são-estatísticas)
    - [TIPOS DE DADOS (VARIÁVEIS)](#tipos-de-dados-variáveis)
      - [TIPO QUALITATIVO OU CATEGÓRICO](#tipo-qualitativo-ou-categórico)
      - [TIPO QUANTITATIVO OU NÚMERICO](#tipo-quantitativo-ou-númerico)
    - [MEDIDAS DE TENDÊNCIA CENTRAL](#medidas-de-tendência-central)
      - [O QUE SÃO MEDIDAS DE TENDÊNCIA CENTRAL?](#o-que-são-medidas-de-tendência-central)
      - [MEDIA ARITIMÉTICA SIMPLES](#media-aritimética-simples)
      - [MEDIANA ARITIMÉTICA](#mediana-aritimética)
      - [MODA](#moda)
      - [OUTLIER (VALOR DISCREPANTE)](#outlier-valor-discrepante)
    - [MEDIDAS DE POSIÇÃO RELATIVA](#medidas-de-posição-relativa)
      - [O QUE SÃO MEDIDAS DE POSIÇÃO RELATIVA?](#o-que-são-medidas-de-posição-relativa)
      - [QUARTIS](#quartis)
      - [DECIS](#decis)
      - [PERCENTIS](#percentis)
      - [EXEMPLO](#exemplo)
      - [ESCORE (Z-SCORE)](#escore-z-score)
    - [MEDIDAS DE DISPERSÃO](#medidas-de-dispersão)
      - [AMPLITUDE](#amplitude)
        - [FÓRMULA](#fórmula)
        - [EXEMPLO](#exemplo-1)
      - [VARIÂNCIA E DESVIO PADRÃO](#variância-e-desvio-padrão)
        - [VARIÂNCIA POPULACIONAL](#variância-populacional)
        - [VARIÂNCIA AMOSTRAL](#variância-amostral)
        - [DESVIO PADRÃO POPULACIONAL](#desvio-padrão-populacional)
        - [DESVIO PADRÃO AMOSTRAL](#desvio-padrão-amostral)
        - [EXEMPLO](#exemplo-2)
      - [COEFICIENTE DE VARIAÇÃO (CV)](#coeficiente-de-variação-cv)
        - [FÓRMULA](#fórmula-1)
        - [EXEMPLO 1](#exemplo-1)
        - [EXEMPLO 2](#exemplo-2)
      - [TABELA DE VARIAVÉIS](#tabela-de-variavéis)
    - [REPRESENTAÇÃO GRÁFICA DOS DADOS](#representação-gráfica-dos-dados)
      - [Gráfico de Barras](#gráfico-de-barras)
      - [Gráfico de Colunas](#gráfico-de-colunas)
      - [Gráfico de Setores (Pizza)](#gráfico-de-setores-pizza)
      - [Histograma](#histograma)
      - [Gráfico de Linhas](#gráfico-de-linhas)
      - [Boxplot (Diagrama de Caixa)](#boxplot-diagrama-de-caixa)
    - [CONCLUSÃO DA UNIDADE 01](#conclusão-da-unidade-01)
  - [UNIDADE 02 – PROBABILIDADE E VARIÁVEIS ALEATÓRIAS](#unidade-02--probabilidade-e-variáveis-aleatórias)
    - [1. PROBABILIDADE](#1-probabilidade)
      - [1.1 Interpretação Numérica da Probabilidade](#11-interpretação-numérica-da-probabilidade)
      - [1.2 Definição Clássica de Probabilidade (Laplace)](#12-definição-clássica-de-probabilidade-laplace)
        - [Onde:](#onde)
        - [Quando usar?](#quando-usar)
        - [Exemplo resolvido](#exemplo-resolvido)
    - [2. EXPERIMENTO ALEATÓRIO](#2-experimento-aleatório)
        - [Exemplos:](#exemplos)
    - [3. ESPAÇO AMOSTRAL (Ω)](#3-espaço-amostral-ω)
        - [Exemplo](#exemplo-3)
    - [4. EVENTO](#4-evento)
        - [Exemplo](#exemplo-4)
    - [5. AXIOMAS DA PROBABILIDADE](#5-axiomas-da-probabilidade)
      - [5.1 Não negatividade](#51-não-negatividade)
      - [5.2 Normalização](#52-normalização)
      - [5.3 Aditividade](#53-aditividade)
    - [6. PROBABILIDADE CONDICIONAL](#6-probabilidade-condicional)
        - [Onde:](#onde-1)
        - [Por que usar?](#por-que-usar)
    - [7. TEOREMA DE BAYES](#7-teorema-de-bayes)
        - [Significado dos termos:](#significado-dos-termos)
    - [8. VARIÁVEIS ALEATÓRIAS](#8-variáveis-aleatórias)
      - [8.1 Variável Aleatória Discreta](#81-variável-aleatória-discreta)
      - [8.2 Variável Aleatória Contínua](#82-variável-aleatória-contínua)
    - [9. DISTRIBUIÇÕES DE PROBABILIDADE](#9-distribuições-de-probabilidade)
    - [10. DISTRIBUIÇÃO BINOMIAL](#10-distribuição-binomial)
      - [10.1 O que é](#101-o-que-é)
      - [10.2 Condições obrigatórias](#102-condições-obrigatórias)
      - [10.3 Função de probabilidade](#103-função-de-probabilidade)
        - [Onde:](#onde-2)
    - [11. DISTRIBUIÇÃO POISSON](#11-distribuição-poisson)
        - [Onde:](#onde-3)
    - [12. DISTRIBUIÇÃO NORMAL](#12-distribuição-normal)
      - [12.1 O que é](#121-o-que-é)
      - [12.2 Por que é tão importante?](#122-por-que-é-tão-importante)
      - [12.3 Função densidade](#123-função-densidade)
        - [Onde:](#onde-4)
    - [13. DISTRIBUIÇÃO EXPONENCIAL](#13-distribuição-exponencial)
        - [Onde:](#onde-5)
    - [CONCLUSÃO DA UNIDADE 02](#conclusão-da-unidade-02)
  
## UNIDADE 01

### CONCEITOS BÁSICOS

#### O QUE É POPULAÇÃO?

- É o nosso **principal alvo** quando vamos fazer uma pesquisa.
- Quando definimos um objetivo, escolhemos a população que será avaliada.

#### O QUE É AMOSTRA?

- Existem populações muito grandes, sendo impossivel trabalhar com elas, e quando for o caso é preciso ter uma amostra.
- Com isso tiramos uma amostra, sendo um **subconjunto de itens da nossa população.**
- Fazemos nossa seleção amostral para definir a amostra.

#### O QUE SÃO PARÂMETROS?

- Quando utilizamos dos dados de uma **população** e assim criamos nossas analises, podemos chamar os **resultados** de parâmtros.
- Parâmtros são resultados de analises como: média, percentuais e etc...

#### O QUE SÃO ESTATÍSTICAS?

- É basicamente o **mesmo conceito de parâmetros**, entretanto a única **diferença é a origem dos dados**, que agora vêm de uma **amostra** e não de uma população.

### TIPOS DE DADOS (VARIÁVEIS)

#### TIPO QUALITATIVO OU CATEGÓRICO

Consistem em **atributos**, **qualidades** ou **características**.

- Se dividem em **duas subcategorias**:
    - **Nominais**: Representam **nomes**, **rótulos** ou **categorias** que **não têm ordem ou hierarquia.**
      - Exemplo: Meio de transporte utilizado por uma pessoa
    - **Ordinais**: Mantêm uma **relação de ordem do menor para o maior.**
      - Exemplo: Nível de satisfação do cliente (carinhas felizes)

#### TIPO QUANTITATIVO OU NÚMERICO

Consistem em **medidas** ou **contagens númericas.**

- Se dividem em **duas subcategorias**:
    - **Discretos**: Resultam de um conjunto **finito** ou enumerável de valores possíveis (**Contagens**).
      - Exemplo: Número de ventiladores
    - **Contínuos**: Resultam em um número **infinito** de valores possíveis (**Mensurações**).
      - Exemplo: Altura de um prédio

> **ATENÇÃO: Não é só por que um número está representado como inteiro, que é necessariamente discreto, é preciso analisar a natureza do dado.**

### MEDIDAS DE TENDÊNCIA CENTRAL

#### O QUE SÃO MEDIDAS DE TENDÊNCIA CENTRAL?

São valores que têm o **objetivo de resumir a nossa amostra.** Principal exemplo é a **Média**.

#### MEDIA ARITIMÉTICA SIMPLES

![Fórmula da Média Aritimética](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/02%20-%20Estatística%20Geral%20-%20Teoria%20e%20Aplicações/images/MediaAritimetica_Formula.png)

> Quando a média é calculada com base em uma **amostra**, é representada pelo símbolo **"x̄"** (x barra). Já quando a média é calculada com base em toda a **população**, é representada pelo símbolo **"μ"** (micro).

#### MEDIANA ARITIMÉTICA

- É o valor que **divide a amostra em duas partes iguais**, o valor que está **exatamente no meio.**
- É preciso que amostra esteja **ordenada do menor para o maior**.

Quando o número de elementos é **ímpar**:
![Fórmula da Média Aritimética Impar](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/02%20-%20Estatística%20Geral%20-%20Teoria%20e%20Aplicações/images/MedianaAritimetica_Formula_Impar.png)

Quando o número de elementos é **par**:
![Fórmula da Média Aritimética Par](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/02%20-%20Estatística%20Geral%20-%20Teoria%20e%20Aplicações/images/MedianaAritimetica_Formula_Par.png)

#### MODA

- É o **valor** que aparece com **maior frequência** dentro da amostra. 
- Única media que **pode ser utilizada** para **medir dados categoricos** (Qualitativos).
- É possivel ter mais de uma moda, caso as maiores ocorrências empatem.

#### OUTLIER (VALOR DISCREPANTE)

- Valores **muito diferentes do restante dos valores da amostra.**

Ex: 1, 2, 3, 4, **50**

- **Afeta muito a média**, entretanto a **mediana continua a mesma**.
- Se a **média** e a **mediana** forem muito **próximas**, quer dizer que **não temos valor discrepantes**, nesse caso é **melhor utilizar a média**.
- Se a **média** e a **mediana** forem muito **diferentes**, bem possível de **termos valores discrepantes**, ou seja, utilizar a **média não é a melhor opção**, pois ela pode estar muito distorcida, **necessitando de uma avaliação.**

### MEDIDAS DE POSIÇÃO RELATIVA

#### O QUE SÃO MEDIDAS DE POSIÇÃO RELATIVA?

As medidas de posição relativa indicam a posição de um valor dentro da distribuição de dados. Incluem quartis, decis, percentis e o escore padrão (z-score).

#### QUARTIS
Os **quartis** dividem a distribuição em **quatro partes iguais** (**25% cada**):
- Q1: 25% dos dados
- Q2: 50% (mediana)
- Q3: 75%

#### DECIS
Os **decis** dividem os dados em **dez partes iguais** (**10% cada**):
- D1: 10%
- D5: 50%
- D9: 90%

#### PERCENTIS
Os **percentis** dividem a distribuição em **100 partes iguais.**  
Exemplo de interpretação:  
- P20 = valor abaixo do qual estão 20% dos dados  
- P80 = valor abaixo do qual estão 80% dos dados  

#### EXEMPLO
Considere a lista de valores ordenados:  
10, 15, 20, 25, 30, 35, 40, 45  
Se P75 = 37, então 75% dos valores são menores que 37.

#### ESCORE (Z-SCORE)
O **z-score** indica quantos **desvios-padrão um valor está distante da média. ** 
Fórmula:  
z = (x − média) / desvio-padrão  

Ele **permite comparar valores em diferentes escalas** e **identificar pontos fora do padrão (outliers)**.

### MEDIDAS DE DISPERSÃO

As medidas de dispersão q**uantificam o quanto os dados variam em relação à média**. Incluem **amplitude**, **variância**, **desvio padrão** e **coeficiente de variação**.

#### AMPLITUDE
A amplitude é a **diferença entre o maior e o menor valor** de um **conjunto de dados**.

##### FÓRMULA
**Amplitude = X_max − X_min**

##### EXEMPLO
Dados: 50, 60, 70, 85, 90  
Amplitude = 90 − 50 = 40

#### VARIÂNCIA E DESVIO PADRÃO

A **variância** mede o **quanto os valores se afastam da média**.  
O **desvio padrão** é a **raiz quadrada da variância** e expressa a **dispersão na mesma unidade dos dados**.

##### VARIÂNCIA POPULACIONAL
σ² = Σ(xᵢ − μ)² / N

##### VARIÂNCIA AMOSTRAL
s² = Σ(xᵢ − x̄)² / (n − 1)

##### DESVIO PADRÃO POPULACIONAL
σ = √σ²

##### DESVIO PADRÃO AMOSTRAL
s = √s²

##### EXEMPLO
Dados: 10, 12, 15  
Média = 12.33  

Cálculos dos desvios ao quadrado:  
(10 − 12.33)² = 5.43  
(12 − 12.33)² = 0.11  
(15 − 12.33)² = 7.11  

Variância amostral:  
s² = (5.43 + 0.11 + 7.11) / 2 = 6.325  

Desvio padrão amostral:  
s = √6.325 ≈ 2.51

#### COEFICIENTE DE VARIAÇÃO (CV)

O coeficiente de variação mede a **dispersão relativa**, indicando **quanto o desvio padrão representa em relação à média**.

##### FÓRMULA
CV = (Desvio Padrão / Média) × 100

##### EXEMPLO 1
Média = 100  
Desvio padrão = 5  
CV = 5%

##### EXEMPLO 2
Média = 20  
Desvio padrão = 3  
CV = 15%

#### TABELA DE VARIAVÉIS

| Conceito        | População | Amostra |
|-----------------|-----------|---------|
| Média           | μ         | x̄       |
| Tamanho         | N         | n       |
| Variância       | σ²        | s²      |
| Desvio padrão   | σ         | s       |
| Denominador     | N         | n − 1   |

### REPRESENTAÇÃO GRÁFICA DOS DADOS

A representação gráfica dos dados tem como objetivo facilitar a interpretação das informações, permitindo visualizar padrões, tendências, comparações e possíveis anomalias.

#### Gráfico de Barras
Indicado para:
- Dados qualitativos (nominais ou ordinais)
- Comparação entre categorias

Exemplos:
- Quantidade de vendas por produto
- Número de alunos por curso

#### Gráfico de Colunas
Indicado para:
- Comparações ao longo do tempo (dados discretos)
- Análise de evolução por períodos

Exemplo:
- Faturamento mensal

#### Gráfico de Setores (Pizza)
Indicado para:
- Análise de participação percentual
- Situações em que o total representa 100%

Exemplo:
- Distribuição de mercado por empresa

Não é recomendado quando há muitas categorias.

#### Histograma
Indicado para:
- Dados quantitativos contínuos
- Análise da distribuição dos dados

Exemplo:
- Distribuição de alturas, pesos ou salários

Permite identificar assimetria, dispersão e concentração dos dados.

#### Gráfico de Linhas
Indicado para:
- Séries temporais
- Análise de tendência ao longo do tempo

Exemplo:
- Crescimento populacional ao longo dos anos

#### Boxplot (Diagrama de Caixa)
Indicado para:
- Identificação de mediana, quartis e outliers
- Comparação entre distribuições

Exemplo:
- Comparação salarial entre setores ou empresas
  
### CONCLUSÃO DA UNIDADE 01

A Unidade 01 apresentou os fundamentos essenciais da Estatística Geral, com foco na Estatística Descritiva, fornecendo a base conceitual necessária para a análise e interpretação de dados.

Inicialmente, foram definidos os conceitos de população e amostra, permitindo compreender a origem dos dados analisados e a diferença entre parâmetros populacionais e estatísticas amostrais. Em seguida, a classificação das variáveis em qualitativas e quantitativas possibilitou identificar a natureza dos dados e selecionar métodos adequados de análise.

As medidas de tendência central demonstraram como resumir um conjunto de dados por meio de valores representativos, enquanto as medidas de posição relativa permitiram localizar observações dentro da distribuição, destacando a importância de quartis, decis, percentis e do escore padronizado. As medidas de dispersão complementaram essa análise ao quantificar a variabilidade dos dados, mostrando o quanto os valores se afastam da média.

Por fim, a representação gráfica dos dados reforçou o papel da visualização como instrumento essencial na análise estatística, facilitando a comunicação dos resultados e auxiliando na tomada de decisões. Dessa forma, esta unidade estabelece um alicerce sólido para o avanço em conteúdos mais complexos, como inferência estatística, análise preditiva e aplicações em ciência de dados e aprendizado de máquina.



## UNIDADE 02 – PROBABILIDADE E VARIÁVEIS ALEATÓRIAS

---

### 1. PROBABILIDADE

A **Probabilidade** é o ramo da Estatística que estuda fenômenos **aleatórios**, ou seja, situações em que o resultado individual não pode ser previsto com certeza, mesmo quando o experimento é repetido sob as mesmas condições.

Seu principal objetivo é **quantificar a incerteza**, permitindo avaliar riscos, expectativas e apoiar a tomada de decisões baseadas em dados.

---

#### 1.1 Interpretação Numérica da Probabilidade

- \(P(A) = 0\): evento impossível  
- \(P(A) = 1\): evento certo  
- \(0 < P(A) < 1\): evento aleatório  

---

#### 1.2 Definição Clássica de Probabilidade (Laplace)

\[
P(A) = \frac{n(A)}{n(\Omega)}
\]

##### Onde:
- \(P(A)\): probabilidade do evento A
- \(n(A)\): número de resultados favoráveis ao evento A
- \(n(\Omega)\): número total de resultados possíveis no espaço amostral

##### Quando usar?
Quando **todos os resultados possíveis têm a mesma chance de ocorrer**.

---

##### Exemplo resolvido

Um dado honesto é lançado. Qual a probabilidade de sair um número maior que 4?

Espaço amostral:
\[
\Omega = \{1,2,3,4,5,6\}
\]

Evento A:
\[
A = \{5,6\}
\]

\[
P(A) = \frac{2}{6} = \frac{1}{3}
\]

---

### 2. EXPERIMENTO ALEATÓRIO

Um **experimento aleatório** é aquele cujo resultado individual **não pode ser previsto com certeza**, embora o conjunto de resultados possíveis seja conhecido.

##### Exemplos:
- Lançamento de moedas ou dados
- Número de clientes que chegam a um banco
- Tempo de vida de um equipamento

A Estatística não busca prever o resultado individual, mas **o comportamento médio e probabilístico**.

---

### 3. ESPAÇO AMOSTRAL (Ω)

O **espaço amostral**, representado por \(\Omega\), é o conjunto formado por **todos os resultados possíveis** de um experimento aleatório.

##### Exemplo

Lançamento de duas moedas:

\[
\Omega = \{(C,C),(C,K),(K,C),(K,K)\}
\]

---

### 4. EVENTO

Um **evento** é qualquer **subconjunto do espaço amostral**.

- Evento simples: um único resultado
- Evento composto: mais de um resultado

##### Exemplo

Evento A = “ocorrer exatamente uma cara”:

\[
A = \{(C,K),(K,C)\}
\]

\[
P(A) = \frac{2}{4} = 0{,}5
\]

---

### 5. AXIOMAS DA PROBABILIDADE

Os axiomas garantem que os cálculos probabilísticos sejam matematicamente coerentes.

#### 5.1 Não negatividade
\[
P(A) \ge 0
\]

#### 5.2 Normalização
\[
P(\Omega) = 1
\]

#### 5.3 Aditividade
Se A e B são mutuamente exclusivos:
\[
P(A \cup B) = P(A) + P(B)
\]

---

### 6. PROBABILIDADE CONDICIONAL

A probabilidade condicional mede a chance de um evento ocorrer **sabendo que outro evento já ocorreu**.

\[
P(A|B) = \frac{P(A \cap B)}{P(B)}
\]

##### Onde:
- \(P(A|B)\): probabilidade de A dado B
- \(P(A \cap B)\): probabilidade de A e B ocorrerem juntos
- \(P(B)\): probabilidade de B

##### Por que usar?
Porque **informações adicionais alteram as probabilidades**.

---

### 7. TEOREMA DE BAYES

O Teorema de Bayes permite **atualizar probabilidades iniciais** quando novas evidências são observadas.

\[
P(A|B) = \frac{P(B|A)\cdot P(A)}{P(B)}
\]

##### Significado dos termos:
- \(P(A)\): probabilidade inicial (priori)
- \(P(B|A)\): verossimilhança
- \(P(A|B)\): probabilidade atualizada (posteriori)

---

### 8. VARIÁVEIS ALEATÓRIAS

Uma **variável aleatória** associa um valor numérico a cada resultado do experimento aleatório.

#### 8.1 Variável Aleatória Discreta
Assume valores **contáveis** (0, 1, 2, …)

Exemplos:
- Número de filhos
- Número de defeitos

#### 8.2 Variável Aleatória Contínua
Assume valores em **intervalos reais**

Exemplos:
- Tempo
- Altura
- Peso

---

### 9. DISTRIBUIÇÕES DE PROBABILIDADE

Uma **distribuição de probabilidade** descreve como os valores de uma variável aleatória estão distribuídos.

---

### 10. DISTRIBUIÇÃO BINOMIAL

#### 10.1 O que é
Modela o **número de sucessos** em um número fixo de tentativas independentes.

#### 10.2 Condições obrigatórias
1. Número fixo de tentativas (\(n\))
2. Dois resultados possíveis
3. Probabilidade constante (\(p\))
4. Independência

#### 10.3 Função de probabilidade
\[
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
\]

##### Onde:
- \(X\): variável aleatória
- \(k\): número de sucessos desejados
- \(n\): número total de tentativas
- \(p\): probabilidade de sucesso em uma tentativa
- \(1-p\): probabilidade de fracasso
- \(\binom{n}{k}\): número de combinações possíveis

---

### 11. DISTRIBUIÇÃO POISSON

Modela o **número de ocorrências** de um evento em um intervalo fixo.

\[
P(X = k) = \frac{e^{-\lambda}\lambda^k}{k!}
\]

##### Onde:
- \(k\): número de ocorrências
- \(\lambda\): média de ocorrências no intervalo
- \(e\): constante de Euler

---

### 12. DISTRIBUIÇÃO NORMAL

#### 12.1 O que é
Distribuição contínua que surge naturalmente em fenômenos reais devido ao **Teorema Central do Limite**.

#### 12.2 Por que é tão importante?
- Modela erros de medição
- Base da inferência estatística
- Aproxima muitas distribuições reais

#### 12.3 Função densidade
\[
f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}
\]

##### Onde:
- \(\mu\): média
- \(\sigma\): desvio padrão

---

### 13. DISTRIBUIÇÃO EXPONENCIAL

Modela o **tempo até a ocorrência de um evento**.

\[
f(x)=\lambda e^{-\lambda x}
\]

##### Onde:
- \(\lambda\): taxa média de ocorrência
- \(x\): tempo

Propriedade importante: **ausência de memória**.

---

### CONCLUSÃO DA UNIDADE 02

A Unidade 02 apresentou os fundamentos da Probabilidade e das Variáveis Aleatórias, explicando não apenas como calcular probabilidades, mas principalmente **por que cada conceito e distribuição existe**. A correta compreensão das variáveis, parâmetros e condições de aplicação é essencial para evitar erros de modelagem e interpretação.

As distribuições Binomial, Poisson, Normal e Exponencial representam diferentes tipos de fenômenos reais e constituem a base da Estatística Inferencial, da Ciência de Dados e do Aprendizado de Máquina. O domínio desses conceitos permite transformar incerteza em informação quantitativa confiável, apoiando decisões fundamentadas em dados.