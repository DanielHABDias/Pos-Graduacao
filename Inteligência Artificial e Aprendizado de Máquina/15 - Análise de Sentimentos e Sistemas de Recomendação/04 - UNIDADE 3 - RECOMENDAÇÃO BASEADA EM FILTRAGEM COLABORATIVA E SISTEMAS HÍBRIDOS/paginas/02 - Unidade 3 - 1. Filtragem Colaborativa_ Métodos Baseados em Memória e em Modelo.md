# Unidade 3 - 1. Filtragem Colaborativa: Métodos Baseados em Memória e em Modelo

- Origem: [Canvas](https://pucminas.instructure.com/courses/230809/pages/unidade-3-1-filtragem-colaborativa-metodos-baseados-em-memoria-e-em-modelo)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar os seguintes tópicos:**

- Introdução a recomendação colaborativa.
- Recomendação colaborativa baseada em memória.
- Recomendação colaborativa baseada em modelo.
- Avaliação da recomendação colaborativa.

**Ao final, você será capaz de:**

- Compreender o conceito fundamental de filtragem colaborativa.
- Diferenciar os métodos baseados em memória (User-User e Item-Item) dos métodos baseados em modelo.
- Identificar a lógica de similaridade no contexto colaborativo, analisando como as interações históricas fundamentam o cálculo de proximidade entre perfis de usuários ou características de itens.
- Analisar os critérios de avaliação da recomendação colaborativa, compreendendo como mensurar a eficácia das previsões e a qualidade das sugestões.
- Reconhecer as características essenciais da filtragem colaborativa, compreendendo seu papel estratégico na construção de sistemas de recomendação.

---

#### **Introdução a recomendação colaborativa**

Nesta videoaula, você vai descobrir como funciona a recomendação colaborativa, uma das técnicas mais utilizadas em plataformas modernas, como serviços de streaming e e‑commerce. A aula apresenta o princípio central dessa abordagem: **usuários semelhantes tendem a gostar de itens semelhantes**. A partir do histórico de interações — como filmes assistidos, notas atribuídas, produtos comprados — o sistema identifica padrões de comportamento para prever o que um usuário provavelmente iria gostar. Você também entenderá problemas clássicos, como o *cold start*, e a diferença entre métodos que predizem notas (rating‑based) e métodos que geram rankings de preferência.

A videoaula mostra como os sistemas colaborativos usam a sabedoria da multidão, aproveitando o gosto coletivo para gerar recomendações relevantes e personalizadas. A aula introduz ainda os dois grandes grupos de técnicas colaborativas: **memory‑based**, que usam diretamente a matriz de interações entre usuários e itens, e **model‑based**, que empregam machine learning e técnicas como fatoração de matrizes. É uma introdução essencial para compreender como plataformas conseguem sugerir conteúdos com alta precisão, mesmo sem analisar diretamente características dos itens.

#### **Recomendação colaborativa baseada em memória**

Nesta videoaula, você vai entender em profundidade como funcionam as técnicas de recomendação colaborativa baseadas em memória, também chamadas de estratégias de vizinhança (*neighborhood-based*). A aula apresenta os dois métodos principais — **user‑user** e **item‑item** — explicando como encontrar usuários parecidos entre si ou itens avaliados de forma semelhante. A partir dessas similaridades, você aprende a estimar a nota que um usuário daria a um item não consumido, utilizando métricas como correlação de Pearson e similaridade do cosseno.

Além disso, a videoaula compara as abordagens user‑user e item‑item, destacando vantagens e limitações de cada uma. Enquanto user‑user tende a trazer mais diversidade e novidade, item‑item é geralmente mais estável e escalável, sendo amplamente usado em sistemas reais — como “itens frequentemente comprados juntos” ou sugestões após assistir a um filme. A aula demonstra, passo a passo, o processo de cálculo de similaridade, seleção de vizinhos, predição de notas e geração final das recomendações. É a base conceitual para as implementações que serão vistas na aula prática.

#### **Recomendação colaborativa baseada em memória - Prática**

Nesta videoaula prática, você vai implementar recomendações colaborativas baseadas em memória usando Python e Google Colab. A aula começa com um exemplo didático simples, onde você calcula similaridades entre usuários, estima notas ausentes e compreende matematicamente como a predição colaborativa funciona. Em seguida, avança para exemplos reais, utilizando bibliotecas como **Surprise**, que já implementam algoritmos user‑user, item‑item e vizinhança baseada em similaridade.

A videoaula mostra como construir recomendações do tipo “usuários semelhantes também gostaram” e “itens semelhantes ao que você acabou de assistir”, usando similaridade entre itens para sugerir filmes como *Toy Story 2*, *Aladdin* ou *The Godfather Part II*. Você aprende a carregar datasets de filmes e avaliações, treinar modelos de vizinhança, recuperar vizinhos mais próximos e gerar recomendações personalizadas de forma reproduzível. É uma etapa prática completa, que conecta conceitos teóricos com aplicações reais de recomendação colaborativa.

#### **Recomendação colaborativa baseada em modelo**

Nesta videoaula, você vai aprender como funcionam as recomendações colaborativas baseadas em modelo — uma classe de técnicas mais sofisticadas, que utilizam algoritmos de aprendizado de máquina para prever avaliações de usuários. Em vez de depender diretamente das similaridades entre usuários ou entre itens, essa abordagem busca identificar **fatores latentes** que explicam padrões de interação, permitindo estimar notas para itens nunca vistos por um usuário. O conteúdo apresenta a etapa offline de treinamento do modelo, seguida pela fase online em que o sistema gera recomendações em tempo real a partir das predições aprendidas.

A videoaula destaca especialmente a **fatoração de matrizes (SVD)** como técnica central, além de mencionar métodos probabilísticos e redes neurais profundas. Esses modelos conseguem representar usuários e itens em espaços de baixa dimensionalidade, capturando informações implícitas — como preferências por gênero, estilo narrativo ou duração — sem que essas características estejam explícitas nos dados. Esse é o fundamento matemático por trás de sistemas modernos como Netflix, Amazon e Spotify, que usam aprendizado de máquina para gerar recomendações altamente eficazes. Vamos explorar como essa “mágica matemática” acontece?

#### **Recomendação colaborativa baseada em modelo - Prática**

Nesta videoaula prática, você vai implementar modelos colaborativos baseados em modelo utilizando Python e a biblioteca **LibRecommender**. A aula demonstra duas estratégias: **modelos de rating**, que estimam notas numéricas com técnicas como SVD; e **modelos de ranking**, que usam algoritmos de *learning to rank* para ordenar itens com base na sua probabilidade de relevância. Você aprenderá a treinar cada modelo, gerar predições, comparar resultados e observar como diferentes métodos influenciam o comportamento das recomendações.

Além disso, a videoaula mostra como conectar o modelo ao perfil real de usuários, analisando recomendações por meio de gêneros, características e padrões individuais de consumo. Exemplos práticos incluem sugestões para usuários com preferências por drama, comédia, ação e suspense; bem como situações em que o modelo surpreende ao trazer diversidade para além do perfil declarado — característica típica da recomendação colaborativa. Ao final, você verá também a aplicação de algoritmos de ranking avançados, como o **LightGCN**, que conseguem identificar títulos populares e relevantes, demonstrando um comportamento bastante alinhado ao que é usado em plataformas de grande escala.

#### **Avaliação da recomendação colaborativa**

Nesta videoaula, você vai aprender como **avaliar a qualidade de um sistema de recomendação**, tanto para modelos baseados em rating quanto para modelos baseados em ranking. A aula apresenta métricas fundamentais de erro — como **MAE** e **RMSE** — para comparar predições de notas com avaliações reais e determinar quão distante o modelo está do comportamento verdadeiro dos usuários. Esse tipo de métricas é essencial quando o objetivo é prever avaliações numéricas de forma precisa.

Para métodos baseados em ranking, a videoaula introduz métricas próprias de ordenação, como **Precisão**, **Revocação (Recall)**, **Average Precision (AP)** e **Mean Average Precision (MAP)**. Esses indicadores medem qualidade e cobertura das sugestões, analisando se os itens relevantes aparecem no topo da lista e se o modelo recupera uma boa parte dos conteúdos desejados. Com diagramas intuitivos e exemplos simples, a aula mostra como interpretar resultados e como essas métricas ajudam a validar, comparar e aprimorar diferentes modelos de recomendação.

#### **Avaliação da recomendação colaborativa - Prática**

Nesta videoaula, você vai aprender a comparar, na prática, diferentes estratégias de recomendação colaborativa usando métricas específicas para avaliar seu desempenho. A aula mostra como dividir o conjunto de avaliações em partes de treino e teste, treinar modelos em 80% das interações e avaliar sua eficácia nos 20% restantes. Para os modelos baseados em rating — como SVD, SVD++ e fatoração de matrizes — você aprende a medir erros usando RMSE e MAE, identificando qual abordagem produz as estimativas mais próximas das notas reais dos usuários.

Em seguida, a videoaula aborda a avaliação de modelos baseados em ranking, que não estimam notas, mas ordenam sugestões buscando colocar os itens mais relevantes no topo da lista. Você verá como treinar algoritmos específicos para ranqueamento e como interpretá‑los usando métricas como Precisão, Recall, NDCG e MAP, analisando a qualidade da ordenação das recomendações. Essa prática oferece uma visão completa e aplicada de como validar sistemas colaborativos de forma rigorosa, comparando múltiplos modelos e identificando quais estratégias são mais adequadas para uso real. Vamos colocar a avaliação em ação?
