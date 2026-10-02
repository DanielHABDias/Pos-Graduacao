# Unidade 3 - 2. Estratégias de Recomendação Híbrida e Tendências

- Origem: [Canvas](https://pucminas.instructure.com/courses/230809/pages/unidade-3-2-estrategias-de-recomendacao-hibrida-e-tendencias)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar os seguintes tópicos:**

- Sistemas de recomendação híbridos.

**Ao final, você será capaz de:**

- Compreender o funcionamento de sistemas de recomendação híbridos, analisando como a integração de diferentes abordagens permite superar limitações intrínsecas de modelos operando de forma isolada.
- Identificar as principais estratégias de hibridização, reconhecendo métodos para combinar filtragem colaborativa, baseada em conteúdo e outras técnicas para otimizar a assertividade do sistema.
- Identificar aplicações práticas da recomendação híbrida, relacionando os conceitos teóricos com a implementação de soluções eficientes em cenários reais de mercado.

---

#### **Recomendação hibrida**

Nesta videoaula, você vai conhecer a recomendação híbrida, uma das estratégias mais poderosas e utilizadas em sistemas modernos. A aula explica como combinar diferentes abordagens — como filtragem colaborativa, recomendação baseada em conteúdo e técnicas baseadas em conhecimento — para superar limitações de cada método isolado. Essa combinação permite lidar com problemas comuns, como *cold start*, aumentar a precisão das sugestões e oferecer listas mais diversas e robustas. Você também aprenderá por que sistemas reais, como plataformas de streaming e e-commerce, adotam modelos híbridos para melhorar continuamente a experiência do usuário.

A videoaula apresenta ainda três formas principais de implementar sistemas híbridos: **monolíticos**, nos quais a saída de um método serve como entrada para outro; **mixed**, que mesclam listas de recomendação geradas de forma independente; e **ensemble**, que combinam as predições de modelos distintos por meio de pesos ou metamodelos. Esses mecanismos possibilitam unir pontos fortes de cada abordagem e gerar recomendações mais personalizadas, diversas e surpreendentes. É uma introdução essencial para entender como arquiteturas híbridas formam o “estado da arte” da recomendação hoje.

#### **Recomendação hibrida - Prática**

Nesta videoaula prática, você vai implementar três estratégias híbridas usando Python e Google Colab: a abordagem **monolítica**, a abordagem **mixed** e o método **ensemble**. A aula começa construindo funções de recomendação baseadas em conteúdo e em filtragem colaborativa, normalizando escores e criando perfis personalizados para diferentes usuários. Em seguida, você aprende a integrar esses componentes — seja filtrando candidatos com uma técnica e ordenando com outra, seja mesclando listas independentes, seja combinando escores com pesos ajustáveis.

A videoaula demonstra como cada abordagem produz resultados com características distintas: versões monolíticas podem priorizar fidelidade ao perfil ou diversidade, dependendo da ordem e do filtro inicial; a versão *mixed* combina diferentes listas para ampliar possibilidades; e a versão *ensemble* permite modular o comportamento do recomendador, dando mais peso ao conteúdo, à colaboração ou ao equilíbrio entre ambos. Com exemplos reais para usuários diferentes, você verá como ajustar pesos, selecionar candidatos e montar listas híbridas capazes de proporcionar recomendações mais ricas e úteis. Vamos colocar a hibridização em prática?
