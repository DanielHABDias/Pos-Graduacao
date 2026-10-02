# Unidade 2 - 1. Fundamentos de Sistemas de Recomendação: Conceitos e Abordagens

- Origem: [Canvas](https://pucminas.instructure.com/courses/230809/pages/unidade-2-1-fundamentos-de-sistemas-de-recomendacao-conceitos-e-abordagens)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar os seguintes tópicos:**

- Introdução aos sistemas de recomendação;
- Técnicas de recomendação pelo nível de personalização;
- Abordagens de sistemas de recomendação;
- Recomendação não personalizada.

**Ao final, você será capaz de:**

- Identificar o conceito de sistemas de recomendação;
- Reconhecer as diferenças entre recomendações não personalizadas e recomendações personalizadas;
- Compreender os requisitos fundamentais e os tipos de dados aplicados, diferenciando o uso de feedback explícito e feedback implícito;
- Compreender os principais desafios técnicos de implementação, como o problema de cold start e a escalabilidade em grandes volumes de dados.

---

#### **Introdução aos sistemas de recomendação**

Nesta videoaula, você vai entender o que são os sistemas de recomendação, por que eles se tornaram essenciais no mundo digital e como ajudam a mitigar desafios como a sobrecarga de informação e o paradoxo da escolha. A aula explica como esses algoritmos analisam preferências, comportamentos e interações para conectar cada usuário aos itens mais relevantes — seja um filme, produto, notícia, vídeo ou serviço. Também mostra como a recomendação está presente no nosso cotidiano, sustentando experiências personalizadas em plataformas de streaming, e‑commerce e redes sociais.

Além disso, você vai descobrir como esses sistemas lidam com a “cauda longa”, revelando conteúdos menos populares, mas altamente relevantes para nichos específicos. A aula percorre a evolução histórica da área, desde os primeiros experimentos acadêmicos até os modelos modernos impulsionados por inteligência artificial, e ilustra sua importância estratégica com métricas reais de impacto em empresas como Amazon, Netflix, YouTube e TikTok. É uma porta de entrada essencial para compreender como esses algoritmos moldam a experiência digital contemporânea. Assista!

#### **Técnicas de recomendação pelo nível de personalização**

Nesta videoaula, você vai explorar como sistemas de recomendação variam conforme o nível de personalização oferecido: não personalizada, semipersonalizada e personalizada. A aula explica como cada abordagem equilibra simplicidade, escalabilidade e relevância, indo desde sugestões globais iguais para todos até recomendações altamente individualizadas, moldadas pelo histórico, perfil e comportamento de cada usuário. Essa diferenciação nos ajuda a compreender como serviços como plataformas de streaming, e-commerce e ambientes educacionais adaptam suas recomendações ao público.

Você também verá como dados explícitos (como avaliações) e implícitos (como tempo de visualização e cliques) se combinam com informações contextuais para tornar as recomendações mais assertivas. A aula evidencia como, ao aumentar o nível de personalização, cresce também a complexidade técnica — mas o ganho em engajamento e relevância costuma compensar. Vamos nos aprofundar nesses modelos?

#### **Abordagens sistemas de recomendação**

Nesta videoaula, você vai conhecer as quatro principais abordagens usadas para implementar sistemas de recomendação: baseada em conhecimento, baseada em conteúdo, filtragem colaborativa e abordagem híbrida. A aula detalha como cada técnica funciona, quais informações utiliza — como características dos itens, perfis de usuários, regras de negócio ou padrões coletivos — e em quais cenários cada uma delas é mais adequada. Você também aprenderá por que essas estratégias são fundamentais para gerar recomendações relevantes, variadas e funcionais.

Além disso, você verá como os sistemas híbridos combinam pontos fortes de mais de uma abordagem, oferecendo precisão maior e lidando melhor com desafios como usuários novos, itens novos e ausência de dados suficientes. A aula apresenta exemplos práticos, como sugestões em plataformas de streaming, e-commerce e portais educacionais, para mostrar como essas técnicas se traduzem em soluções reais. Vamos explorar essas abordagens em profundidade?

#### **Recomendação não personalizada**

Nesta videoaula, você vai compreender como funcionam as recomendações não personalizadas — a forma mais simples e direta de sugerir itens em sistemas de recomendação. A aula mostra como listas de “Top 10”, produtos mais vendidos, filmes mais assistidos e itens frequentemente comprados juntos são gerados a partir de métricas globais, como popularidade, volume de compras ou avaliações agregadas. Como essas estratégias não utilizam o histórico individual do usuário, funcionam de forma escalável, rápida e aplicável mesmo quando não há dados suficientes sobre quem está navegando.

Você também verá que, apesar de úteis em vários cenários, recomendações não personalizadas têm limitações importantes, como baixa relevância individual e incapacidade de capturar preferências específicas. A aula ainda ilustra como técnicas de associação — como regras “quem comprou X também comprou Y” — podem enriquecer as sugestões sem precisar de personalização. Essa é a porta de entrada para entender abordagens mais avançadas de recomendação. Vamos começar?

#### **Recomendação não personalizada - Prática**

Nesta videoaula, você vai aprender, na prática, como construir dois tipos fundamentais de recomendações não personalizadas: listas Top 10 e recomendações associativas, como “quem comprou X também comprou Y”. A aula guia você pelo uso do dataset MovieLens, muito utilizado em pesquisas acadêmicas, mostrando de que forma carregar, explorar e agregar informações — como número de avaliações e notas médias — para gerar listas ordenadas. Você também verá por que métricas simples podem distorcer resultados e como técnicas como filtros por número mínimo de votos e o IMDB Weighted Rating tornam as listas mais confiáveis e significativas.

Além disso, a videoaula introduz recomendações por regras de associação, aplicadas a um dataset de transações simuladas de uma lanchonete. Usando a biblioteca mlxtend e o algoritmo Apriori, você aprenderá a identificar itens frequentes, gerar regras com métricas como support, confidence e lift, e transformar essas descobertas em sugestões automáticas úteis — como “quem comprou chocolate quente também comprou café e torta”. Com isso, a aula mostra como técnicas simples, mas eficazes, podem oferecer recomendações imediatamente aplicáveis em cenários reais. Acompanhe!
