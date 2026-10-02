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
  - [UNIDADE 03 – INFERÊNCIA ESTATÍSTICA E ESTIMAÇÃO DE PARÂMETROS](#unidade-03--inferência-estatística-e-estimação-de-parâmetros)
    - [1. INFERÊNCIA ESTATÍSTICA](#1-inferência-estatística)
      - [1.1 O que é](#11-o-que-é)
      - [1.2 Por que usar?](#12-por-que-usar)
      - [1.3 Tipos de Inferência](#13-tipos-de-inferência)
    - [2. ESTIMAÇÃO DE PARÂMETROS ESTATÍSTICOS](#2-estimação-de-parâmetros-estatísticos)
      - [2.1 O que é](#21-o-que-é)
      - [2.2 Tipos de Estimação](#22-tipos-de-estimação)
    - [3. ESTIMAÇÃO PONTUAL](#3-estimação-pontual)
      - [3.1 O que é](#31-o-que-é)
      - [3.2 Estimadores Comuns](#32-estimadores-comuns)
        - [3.2.1 Estimador da Média Populacional](#321-estimador-da-média-populacional)
        - [3.2.2 Estimador da Proporção Populacional](#322-estimador-da-proporção-populacional)
        - [3.2.3 Estimador da Variância Populacional](#323-estimador-da-variância-populacional)
      - [3.3 Propriedades dos Estimadores](#33-propriedades-dos-estimadores)
      - [3.4 Exemplo Resolvido](#34-exemplo-resolvido)
    - [4. INTERVALOS DE CONFIANÇA](#4-intervalos-de-confiança)
      - [4.1 O que é](#41-o-que-é)
      - [4.2 Interpretação](#42-interpretação)
      - [4.3 Intervalo de Confiança para a Média Populacional (σ Conhecido)](#43-intervalo-de-confiança-para-a-média-populacional-σ-conhecido)
        - [4.3.1 Fórmula](#431-fórmula)
        - [4.3.2 Exemplo Resolvido](#432-exemplo-resolvido)
      - [4.4 Intervalo de Confiança para a Média Populacional (σ Desconhecido)](#44-intervalo-de-confiança-para-a-média-populacional-σ-desconhecido)
        - [4.4.1 Fórmula](#441-fórmula)
        - [4.4.2 Exemplo Resolvido](#442-exemplo-resolvido)
      - [4.5 Intervalo de Confiança para a Proporção Populacional](#45-intervalo-de-confiança-para-a-proporção-populacional)
        - [4.5.1 Fórmula](#451-fórmula)
        - [4.5.2 Exemplo Resolvido](#452-exemplo-resolvido)
      - [4.6 Fatores que Afetam a Amplitude do Intervalo](#46-fatores-que-afetam-a-amplitude-do-intervalo)
    - [5. GRAU DE CONFIANÇA](#5-grau-de-confiança)
      - [5.1 O que é](#51-o-que-é)
      - [5.2 Interpretação](#52-interpretação)
      - [5.3 Valores Comuns](#53-valores-comuns)
      - [5.4 Relação com o Nível de Significância](#54-relação-com-o-nível-de-significância)
    - [6. CÁLCULO DO TAMANHO AMOSTRAL](#6-cálculo-do-tamanho-amostral)
      - [6.1 O que é](#61-o-que-é)
      - [6.2 Por que é Importante?](#62-por-que-é-importante)
      - [6.3 Tamanho Amostral para a Média Populacional](#63-tamanho-amostral-para-a-média-populacional)
        - [6.3.1 Fórmula (σ Conhecido)](#631-fórmula-σ-conhecido)
        - [6.3.2 Exemplo Resolvido](#632-exemplo-resolvido)
      - [6.4 Tamanho Amostral para a Proporção Populacional](#64-tamanho-amostral-para-a-proporção-populacional)
        - [6.4.1 Fórmula](#641-fórmula)
        - [6.4.2 Exemplo Resolvido](#642-exemplo-resolvido)
      - [6.5 Considerações Finais](#65-considerações-finais)
    - [CONCLUSÃO DA UNIDADE 03](#conclusão-da-unidade-03)
  - [UNIDADE 04 — INFERÊNCIA ESTATÍSTICA E TESTES DE HIPÓTESES](#unidade-04--inferência-estatística-e-testes-de-hipóteses)
    - [1. Inferência Estatística](#1-inferência-estatística-1)
      - [O que é Inferência Estatística?](#o-que-é-inferência-estatística)
      - [Exemplo](#exemplo-5)
    - [2. Testes de Hipóteses](#2-testes-de-hipóteses)
      - [O que é um Teste de Hipóteses?](#o-que-é-um-teste-de-hipóteses)
    - [3. Hipótese Nula (H₀)](#3-hipótese-nula-h)
      - [O que é a Hipótese Nula?](#o-que-é-a-hipótese-nula)
      - [Exemplos](#exemplos-1)
    - [4. Hipótese Alternativa (H₁)](#4-hipótese-alternativa-h)
      - [O que é a Hipótese Alternativa?](#o-que-é-a-hipótese-alternativa)
      - [Exemplos](#exemplos-2)
    - [5. Hipótese Bilateral](#5-hipótese-bilateral)
      - [O que é uma Hipótese Bilateral?](#o-que-é-uma-hipótese-bilateral)
      - [Forma matemática](#forma-matemática)
      - [Exemplo](#exemplo-6)
    - [6. Hipótese Unilateral](#6-hipótese-unilateral)
      - [O que é uma Hipótese Unilateral?](#o-que-é-uma-hipótese-unilateral)
      - [Tipos](#tipos)
        - [Unilateral à direita](#unilateral-à-direita)
        - [Unilateral à esquerda](#unilateral-à-esquerda)
      - [Exemplo](#exemplo-7)
    - [7. Nível de Significância (α)](#7-nível-de-significância-α)
      - [O que é o Nível de Significância?](#o-que-é-o-nível-de-significância)
      - [Valores comuns](#valores-comuns)
    - [8. Estatística de Teste](#8-estatística-de-teste)
      - [O que é Estatística de Teste?](#o-que-é-estatística-de-teste)
      - [Exemplo (Teste Z)](#exemplo-teste-z)
    - [9. Decisão em Testes de Hipóteses](#9-decisão-em-testes-de-hipóteses)
      - [Métodos de decisão](#métodos-de-decisão)
        - [Região crítica](#região-crítica)
        - [p-valor](#p-valor)
    - [10. Comparação de Duas Variâncias](#10-comparação-de-duas-variâncias)
      - [Para que serve?](#para-que-serve)
      - [Hipóteses](#hipóteses)
      - [Estatística de Teste (Distribuição F)](#estatística-de-teste-distribuição-f)
      - [Exemplo](#exemplo-8)
    - [11. Importância dos Testes de Hipóteses](#11-importância-dos-testes-de-hipóteses)
    - [Conclusão da Unidade 04](#conclusão-da-unidade-04)
  
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

## UNIDADE 03 – INFERÊNCIA ESTATÍSTICA E ESTIMAÇÃO DE PARÂMETROS

---

### 1. INFERÊNCIA ESTATÍSTICA

#### 1.1 O que é
A **Inferência Estatística** é o ramo da Estatística que permite **generalizar resultados de uma amostra para a população** da qual ela foi retirada. Em vez de analisar toda a população (o que muitas vezes é impraticável), usamos amostras para fazer inferências sobre parâmetros populacionais, como média, proporção ou variância.

#### 1.2 Por que usar?
- Populações são frequentemente grandes ou infinitas, tornando impossível coletar dados de todos os elementos.
- Permite estimar parâmetros desconhecidos e testar hipóteses com base em dados amostrais.
- Apoia decisões em áreas como medicina, economia, engenharia e ciência de dados.

#### 1.3 Tipos de Inferência
- **Estimação**: Estimar valores de parâmetros populacionais (ex.: média ou proporção).
- **Testes de Hipóteses**: Verificar se uma afirmação sobre a população é verdadeira ou não.

Esta unidade foca na estimação de parâmetros.

---

### 2. ESTIMAÇÃO DE PARÂMETROS ESTATÍSTICOS

#### 2.1 O que é
A **estimação de parâmetros** envolve o uso de dados amostrais para aproximar valores desconhecidos da população, como a média (\$\mu\$), proporção (\$p\$) ou variância (\$\sigma^2\$).

#### 2.2 Tipos de Estimação
- **Pontual**: Fornece um único valor como estimativa (ex.: \$\bar{x}\$ para \$\mu\$).
- **Intervalar**: Fornece um intervalo de valores plausíveis, com um nível de confiança associado.

---

### 3. ESTIMAÇÃO PONTUAL

#### 3.1 O que é
A **estimação pontual** fornece um **único valor** como estimativa do parâmetro populacional. É simples, mas não indica a precisão ou incerteza da estimativa.

#### 3.2 Estimadores Comuns

##### 3.2.1 Estimador da Média Populacional
\$
\hat{\mu} = \bar{x} = \frac{\sum x_i}{n}
\$
Onde:
- \$\bar{x}\$: média amostral
- \$n\$: tamanho da amostra

##### 3.2.2 Estimador da Proporção Populacional
\$
\hat{p} = \frac{x}{n}
\$
Onde:
- \$x\$: número de sucessos na amostra
- \$n\$: tamanho da amostra

##### 3.2.3 Estimador da Variância Populacional
\$
\hat{\sigma}^2 = s^2 = \frac{\sum (x_i - \bar{x})^2}{n-1}
\$
Onde:
- \$s^2\$: variância amostral
- \$n-1\$: graus de liberdade

#### 3.3 Propriedades dos Estimadores
- **Não viesado**: A média dos valores estimados ao longo de muitas amostras é igual ao parâmetro verdadeiro.
- **Consistente**: À medida que \$n\$ aumenta, o estimador se aproxima do parâmetro verdadeiro.
- **Eficiente**: Tem a menor variância possível entre estimadores não viesados.

#### 3.4 Exemplo Resolvido
Uma amostra de 10 funcionários de uma empresa tem salários médios de R$ 3.500. Qual é a estimativa pontual da média salarial da empresa?

\$
\hat{\mu} = 3500
\$

Essa é uma estimativa simples, mas não indica quão precisa ela é.

---

### 4. INTERVALOS DE CONFIANÇA

#### 4.1 O que é
Um **intervalo de confiança** fornece um **intervalo de valores** dentro do qual o parâmetro populacional provavelmente se encontra, com um determinado nível de confiança (ex.: 95%). Ele quantifica a incerteza associada à estimação.

#### 4.2 Interpretação
- Não significa que o parâmetro está dentro do intervalo com 95% de probabilidade (o parâmetro é fixo).
- Significa que, se repetirmos o processo de amostragem muitas vezes, 95% dos intervalos calculados conterão o parâmetro verdadeiro.

#### 4.3 Intervalo de Confiança para a Média Populacional (σ Conhecido)
Usado quando o desvio padrão populacional (\$\sigma\$) é conhecido. Baseia-se na distribuição normal.

##### 4.3.1 Fórmula
\$
\bar{x} \pm z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}
\$
Onde:
- \$\bar{x}\$: média amostral
- \$z_{\alpha/2}\$: valor crítico da distribuição normal (ex.: 1,96 para 95% de confiança)
- \$\sigma\$: desvio padrão populacional
- \$n\$: tamanho da amostra

##### 4.3.2 Exemplo Resolvido
Uma amostra de 100 produtos tem peso médio de 500g, com \$\sigma = 20g\$. Construa um IC de 95% para a média populacional.

\$
z_{0.025} = 1.96
\$

\$
500 \pm 1.96 \cdot \frac{20}{\sqrt{100}} = 500 \pm 3.92
\$

Intervalo: (496.08, 503.92)

#### 4.4 Intervalo de Confiança para a Média Populacional (σ Desconhecido)
Usado quando \$\sigma\$ é desconhecido. Baseia-se na distribuição t de Student.

##### 4.4.1 Fórmula
\$
\bar{x} \pm t_{\alpha/2, n-1} \cdot \frac{s}{\sqrt{n}}
\$
Onde:
- \$t_{\alpha/2, n-1}\$: valor crítico da distribuição t (graus de liberdade = n-1)
- \$s\$: desvio padrão amostral

##### 4.4.2 Exemplo Resolvido
Uma amostra de 29 pacientes tem tempo médio de consulta de 30 minutos, com \$s = 7\$ minutos. Construa um IC de 95%.

Graus de liberdade = 28, \$t_{0.025, 28} \approx 2.048\$

\$
30 \pm 2.048 \cdot \frac{7}{\sqrt{29}} \approx 30 \pm 2.66
\$

Intervalo: (27.34, 32.66)

#### 4.5 Intervalo de Confiança para a Proporção Populacional
Usado para estimar proporções (ex.: porcentagem de sucesso).

##### 4.5.1 Fórmula
\$
\hat{p} \pm z_{\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
\$
Onde:
- \$\hat{p}\$: proporção amostral
- \$z_{\alpha/2}\$: valor crítico da distribuição normal

##### 4.5.2 Exemplo Resolvido
Em uma amostra de 200 pessoas, 120 aprovaram uma política. Construa um IC de 95% para a proporção populacional.

\$\hat{p} = 120/200 = 0.6\$, \$z_{0.025} = 1.96\$

\$
0.6 \pm 1.96 \sqrt{\frac{0.6 \cdot 0.4}{200}} = 0.6 \pm 0.068
\$

Intervalo: (0.532, 0.668) ou (53.2%, 66.8%)

#### 4.6 Fatores que Afetam a Amplitude do Intervalo
- **Nível de confiança**: Maior confiança aumenta a amplitude.
- **Tamanho da amostra (n)**: Maior n reduz a amplitude.
- **Variabilidade dos dados**: Maior variância aumenta a amplitude.

---

### 5. GRAU DE CONFIANÇA

#### 5.1 O que é
O **grau de confiança** (ou nível de confiança) indica a probabilidade de que o intervalo de confiança contenha o parâmetro verdadeiro. É expresso em porcentagem (ex.: 95%).

#### 5.2 Interpretação
- Um IC de 95% significa que, em 95% das vezes, o intervalo cobrirá o parâmetro verdadeiro se o experimento for repetido.
- Não é uma probabilidade para um intervalo específico.

#### 5.3 Valores Comuns
- 90%: \$z = 1.645\$
- 95%: \$z = 1.96\$
- 99%: \$z = 2.576\$

#### 5.4 Relação com o Nível de Significância
- Nível de confiança = 1 - nível de significância (\$\alpha\$).
- Ex.: Para 95% de confiança, \$\alpha = 0.05\$.

---

### 6. CÁLCULO DO TAMANHO AMOSTRAL

#### 6.1 O que é
O **tamanho amostral** é o número mínimo de observações necessárias para estimar um parâmetro com uma precisão desejada, considerando o nível de confiança e a margem de erro.

#### 6.2 Por que é Importante?
- Evita amostras muito pequenas (baixa precisão) ou grandes (custos desnecessários).
- Baseia-se em fórmulas matemáticas derivadas da teoria estatística.

#### 6.3 Tamanho Amostral para a Média Populacional
Usado quando estimamos a média (\$\mu\$).

##### 6.3.1 Fórmula (σ Conhecido)
\$
n = \left( \frac{z_{\alpha/2} \cdot \sigma}{E} \right)^2
\$
Onde:
- \$E\$: margem de erro desejada
- \$\sigma\$: desvio padrão populacional

##### 6.3.2 Exemplo Resolvido
Queremos estimar a média de salários com erro máximo de R$ 100, confiança de 95% e \$\sigma = 500\$.

\$z_{0.025} = 1.96\$, \$E = 100\$

\$
n = \left( \frac{1.96 \cdot 500}{100} \right)^2 = (9.8)^2 = 96.04 \approx 97
\$

#### 6.4 Tamanho Amostral para a Proporção Populacional
Usado quando estimamos proporções (\$p\$).

##### 6.4.1 Fórmula
\$
n = \frac{z_{\alpha/2}^2 \cdot p(1-p)}{E^2}
\$
Onde:
- \$p\$: estimativa da proporção (use 0.5 se desconhecida para maximizar n)
- \$E\$: margem de erro

##### 6.4.2 Exemplo Resolvido
Para estimar a proporção de satisfeitos com erro de 2.5%, confiança de 90%, sem estimativa prévia.

\$z_{0.05} = 1.645\$, \$p = 0.5\$, \$E = 0.025\$

\$
n = \frac{(1.645)^2 \cdot 0.5 \cdot 0.5}{(0.025)^2} = \frac{2.706 \cdot 0.25}{0.000625} = \frac{0.6765}{0.000625} \approx 1082
\$

#### 6.5 Considerações Finais
- Sempre arredonde n para cima.
- Se \$\sigma\$ ou \$p\$ forem desconhecidos, use estimativas ou valores conservadores.
- Considere fatores práticos como custo e acessibilidade.

---

### CONCLUSÃO DA UNIDADE 03

A Unidade 03 apresentou os fundamentos da Inferência Estatística, com foco na estimação de parâmetros populacionais por meio de amostras. A estimação pontual oferece simplicidade, mas os intervalos de confiança fornecem uma visão mais robusta da incerteza, essencial para decisões informadas. O cálculo do tamanho amostral garante eficiência e precisão, evitando desperdícios ou imprecisões. Esses conceitos são pilares para aplicações em pesquisa, negócios e ciência de dados, permitindo transformar dados limitados em insights confiáveis sobre populações maiores.

## UNIDADE 04 — INFERÊNCIA ESTATÍSTICA E TESTES DE HIPÓTESES

### 1. Inferência Estatística

#### O que é Inferência Estatística?

A inferência estatística é o ramo da estatística que permite **tirar conclusões sobre uma população** a partir de **informações obtidas em uma amostra**.

Como, na prática, quase nunca é possível analisar toda a população, utilizamos amostras e técnicas estatísticas para:
- Estimar parâmetros populacionais
- Testar suposições
- Apoiar a tomada de decisões

#### Exemplo

Uma empresa deseja saber o tempo médio de atendimento ao cliente.  
Em vez de analisar todos os atendimentos, coleta-se uma amostra e, a partir dela, faz-se uma inferência sobre a população.

---

### 2. Testes de Hipóteses

#### O que é um Teste de Hipóteses?

Um teste de hipóteses é um procedimento estatístico utilizado para **avaliar afirmações sobre parâmetros populacionais**, com base em dados amostrais.

Em essência, trata-se de decidir se os dados fornecem **evidências suficientes** para rejeitar uma suposição inicial.

---

### 3. Hipótese Nula (H₀)

#### O que é a Hipótese Nula?

A hipótese nula representa a **situação padrão**, aquilo que se assume como verdadeiro até que haja evidência em contrário.

📌 A hipótese nula **sempre contém igualdade**.

#### Exemplos

- H₀: μ = 30  
- H₀: p = 0,40  
- H₀: σ₁² = σ₂²  

O objetivo do teste é verificar se existem evidências para **rejeitar H₀**.

---

### 4. Hipótese Alternativa (H₁)

#### O que é a Hipótese Alternativa?

A hipótese alternativa é a afirmação que **contradiz a hipótese nula**.  
Ela representa aquilo que se deseja investigar ou comprovar.

📌 Nunca possui sinal de igualdade.

#### Exemplos

- H₁: μ ≠ 30  
- H₁: μ > 30  
- H₁: μ < 30  

---

### 5. Hipótese Bilateral

#### O que é uma Hipótese Bilateral?

É utilizada quando se deseja verificar se o parâmetro é **diferente**, sem especificar se é maior ou menor.

#### Forma matemática

H₀: μ = μ₀  
H₁: μ ≠ μ₀  

#### Exemplo

Verificar se o tempo médio de atendimento **mudou**, sem saber se aumentou ou diminuiu.

---

### 6. Hipótese Unilateral

#### O que é uma Hipótese Unilateral?

É utilizada quando o interesse está **apenas em um sentido da variação**.

#### Tipos

##### Unilateral à direita
H₁: μ > μ₀  

##### Unilateral à esquerda
H₁: μ < μ₀  

#### Exemplo

Uma empresa quer saber se um novo método **reduziu** o tempo médio de produção.

---

### 7. Nível de Significância (α)

#### O que é o Nível de Significância?

O nível de significância representa a **probabilidade de rejeitar a hipótese nula quando ela é verdadeira**.

Em outras palavras, é o **risco de cometer erro** ao rejeitar H₀.

#### Valores comuns

- α = 0,10 (10%)
- α = 0,05 (5%)
- α = 0,01 (1%)

Quanto menor o valor de α, **mais rigoroso** é o teste.

---

### 8. Estatística de Teste

#### O que é Estatística de Teste?

A estatística de teste é um valor calculado a partir da amostra que indica **o quão distante o resultado observado está do valor assumido em H₀**.

Ela permite comparar o resultado com valores críticos ou calcular o p-valor.

#### Exemplo (Teste Z)

Z = (x̄ − μ₀) / (σ / √n)

Onde:
- x̄: média amostral  
- μ₀: média hipotética  
- σ: desvio padrão populacional  
- n: tamanho da amostra  

---

### 9. Decisão em Testes de Hipóteses

#### Métodos de decisão

##### Região crítica
Compara-se a estatística de teste com valores críticos da tabela.

##### p-valor
- Se p ≤ α → rejeita-se H₀  
- Se p > α → não se rejeita H₀  

---

### 10. Comparação de Duas Variâncias

#### Para que serve?

Serve para verificar se **duas populações possuem a mesma variabilidade**.

É um passo importante antes de comparar médias.

---

#### Hipóteses

H₀: σ₁² = σ₂²  
H₁: σ₁² ≠ σ₂²  

---

#### Estatística de Teste (Distribuição F)

F = s₁² / s₂²  

Onde:
- s₁²: maior variância amostral  
- s₂²: menor variância amostral  

📌 A maior variância deve sempre ficar no numerador.

---

#### Exemplo

- Variância A: 16  
- Variância B: 9  

F = 16 / 9 ≈ 1,78  

O valor calculado é comparado com o valor crítico da distribuição F.

---

### 11. Importância dos Testes de Hipóteses

Os testes de hipóteses são fundamentais porque:
- Permitem decisões baseadas em dados
- Reduzem erros de julgamento
- São amplamente utilizados em ciência, economia, engenharia e análise de dados

Eles formam a base da **inferência estatística moderna**.

### Conclusão da Unidade 04

Nesta unidade, foram apresentados os principais conceitos da **Inferência Estatística** e dos **Testes de Hipóteses**, que têm como objetivo permitir a tomada de decisões sobre uma população a partir de informações obtidas em amostras. Esse processo é fundamental, pois na prática raramente é possível analisar todos os elementos de uma população.

Inicialmente, compreendeu-se que a inferência estatística utiliza métodos formais para avaliar suposições e estimar parâmetros populacionais, reduzindo a incerteza por meio de critérios probabilísticos. Em seguida, foi introduzido o conceito de **teste de hipóteses**, no qual se estabelece uma hipótese nula, representando a situação padrão, e uma hipótese alternativa, que expressa a possibilidade de mudança ou diferença.

Foram discutidos os diferentes tipos de hipóteses, destacando-se os testes **bilaterais**, utilizados quando se deseja verificar qualquer diferença, e os testes **unilaterais**, aplicados quando há interesse específico em apenas um sentido da variação. Também foi apresentado o **nível de significância (α)**, que define o risco máximo aceitável de rejeitar a hipótese nula quando ela é verdadeira, sendo um elemento central no processo de decisão.

A unidade abordou ainda a **estatística de teste**, responsável por transformar os dados amostrais em um valor numérico que pode ser comparado com valores críticos ou utilizado no cálculo do p-valor. Esse mecanismo torna o processo decisório objetivo e fundamentado matematicamente.

Por fim, foi estudada a **comparação de duas variâncias**, etapa importante para avaliar a homogeneidade da dispersão entre populações e frequentemente utilizada como pré-requisito para outros testes estatísticos. O uso da distribuição F foi apresentado como ferramenta adequada para esse tipo de análise.

Assim, esta unidade fornece a base necessária para compreender como decisões estatísticas são construídas de forma racional e confiável, preparando o estudante para a análise crítica de dados, a validação de hipóteses e a aplicação desses conceitos em contextos acadêmicos, profissionais e científicos.
