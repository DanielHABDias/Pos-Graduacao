# 02 - Estatística Geral - Teoria e Aplicações

## SUMÁRIO

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
