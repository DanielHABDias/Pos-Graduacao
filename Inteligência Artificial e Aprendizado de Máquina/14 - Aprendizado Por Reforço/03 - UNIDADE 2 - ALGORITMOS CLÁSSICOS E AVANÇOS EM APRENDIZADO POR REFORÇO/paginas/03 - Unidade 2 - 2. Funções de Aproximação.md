# Unidade 2 - 2. Funções de Aproximação

- Origem: [Canvas](https://pucminas.instructure.com/courses/230807/pages/unidade-2-2-funcoes-de-aproximacao)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar os seguintes tópicos:**

- Limitações dos métodos tabulares em grandes espaços de estado.
- Ideia central da Função de Aproximação (generalização).
- Aproximação Linear e atualização por gradiente.
- Aproximação para Q(s, a).
- Generalização vs. Overfitting.

**Ao final, você será capaz de:**

- Reconhecer quando métodos tabulares se tornam inviáveis.
- Reconhecer como funções de aproximação representam valores e reduzem a dimensionalidade em espaços grandes.
- Compreender o processo de atualização por gradiente em um modelo linear simples, reconhecendo seus impactos na estabilidade do aprendizado.

---

#### **Funções de Aproximação**

No vídeo a seguir, você irá entender por que as funções de aproximação representam um ponto de virada no aprendizado por reforço, permitindo que os algoritmos deixem de funcionar apenas em ambientes simples e passem a lidar com problemas reais e complexos. A aula explica as limitações dos métodos tabulares e mostra como, em espaços de estado grandes ou contínuos, o agente precisa aprender uma função geral para estimar valores, em vez de memorizar cada estado individualmente, utilizando características relevantes do ambiente.

Além disso, você irá conhecer como essas funções são ajustadas por meio do aprendizado por diferença temporal, possibilitando generalização entre estados semelhantes e abrindo caminho para o uso de modelos mais sofisticados, como redes neurais. Essa abordagem é a base do aprendizado por reforço profundo e conecta os conceitos clássicos da área aos avanços mais modernos. Quer descobrir como o aprendizado por reforço escala para problemas do mundo real? Então, acompanhe o vídeo!
