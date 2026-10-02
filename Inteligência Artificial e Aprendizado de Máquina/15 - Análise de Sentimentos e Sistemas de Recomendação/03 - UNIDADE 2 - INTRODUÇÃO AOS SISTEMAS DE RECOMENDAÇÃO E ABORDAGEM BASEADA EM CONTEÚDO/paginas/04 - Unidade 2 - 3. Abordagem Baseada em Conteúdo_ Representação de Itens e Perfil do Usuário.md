# Unidade 2 - 3. Abordagem Baseada em Conteúdo: Representação de Itens e Perfil do Usuário

- Origem: [Canvas](https://pucminas.instructure.com/courses/230809/pages/unidade-2-3-abordagem-baseada-em-conteudo-representacao-de-itens-e-perfil-do-usuario)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar os seguintes tópicos:**

- Recomendação baseada em conteúdo;
- Recomendação baseada em conteúdo personalizada e perfil do usuário.

**Ao final, você será capaz de:**

- Compreender a lógica da filtragem baseada em conteúdo;
- Identificar métodos de representação de itens, reconhecendo a importância do uso de metadados, tags e descritores textuais;
- Compreender o processo de construção do perfil do usuário;
- Diferenciar recomendações baseadas em conteúdo genéricas de personalizadas.

---

#### **Recomendação baseada em conteúdo**

Nesta videoaula, você vai entender como funcionam as recomendações baseadas em conteúdo, uma das abordagens mais importantes dentro dos sistemas de recomendação. A aula explica como esse método utiliza as características dos itens — como gênero, atores, tags, categorias ou descrições — para identificar outros itens semelhantes e oferecê‑los ao usuário. Mesmo quando não há um perfil pessoal previamente construído, é possível recomendar títulos parecidos com aquilo que o usuário acabou de assistir, buscou ou demonstrou interesse.

A videoaula também diferencia as versões personalizada e não personalizada dessa abordagem. Na forma personalizada, o sistema considera o histórico do usuário para montar um perfil único que orienta novas sugestões; já na forma não personalizada, as recomendações são iguais para todos que interagiram com um item específico — como “títulos semelhantes a este”. Esse conteúdo estabelece a base conceitual para compreender como plataformas de streaming e e‑commerce conseguem sugerir itens relacionados de maneira rápida e eficiente. Vamos começar?

#### **Recomendação baseada em conteúdo - Prática**

Nesta videoaula prática, você vai implementar um sistema de recomendação baseado em conteúdo usando Python, embeddings e busca por similaridade. A aula mostra como preparar dados de filmes, limpar textos, combinar título, gêneros e tags em um único documento e transformar tudo em representações vetoriais ricas utilizando modelos comoSentence-BERT*.* Com esses vetores, o sistema passa a ser capaz de comparar itens matematicamente, identificando quais são mais semelhantes entre si.

Em seguida, você aprende a usar estruturas eficientes de indexação, como HNSW, para realizar buscas rápidas e oferecer recomendações mesmo em catálogos com milhares de itens. A videoaula demonstra consultas reais — como sugerir filmes semelhantes a *Toy Story*, *The Lego Movie* ou *O Poderoso Chefão* — e como encontrar títulos relacionados sem depender de perfis individuais. Essa prática oferece uma visão clara e aplicada de como sistemas reais usam similaridade semântica para gerar recomendações de forma instantânea e precisa. Assista!

#### **Recomendação baseada em conteúdo personalizada**

Nesta videoaula, você vai aprender como construir recomendações baseadas em conteúdo de forma totalmente personalizada, criando perfis individuais a partir do histórico de interações do usuário. A aula apresenta o conceito de **user profile**, uma representação que consolida características dos itens que o usuário avaliou positivamente, assistiu, comprou ou consumiu com frequência. A partir desse perfil, é possível identificar padrões — como preferência por gêneros específicos, temas recorrentes ou estilos de narrativa — e transformar isso em uma estrutura numérica usada para recuperar itens compatíveis no catálogo.

Com esse perfil consolidado, o sistema é capaz de buscar itens que compartilham das mesmas características, calcular relevância, ordenar resultados e entregar recomendações realmente alinhadas ao gosto do usuário. A videoaula mostra exemplos visuais de como esses perfis se tornam mapas de preferências e explicam recomendações (como “recomendado para você”). Assim, você descobre como essa técnica é capaz de entregar sugestões altamente precisas e individualizadas — um dos fatores mais valorizados em serviços modernos de recomendação digital.

#### **Recomendação baseada em conteúdo personalizada - Prática**

Nesta videoaula, você aprende a implementar um sistema de recomendação baseada em conteúdo totalmente personalizado, construindo perfis individuais a partir das avaliações que cada usuário fez. A aula mostra, passo a passo, como transformar gêneros e características dos filmes em uma matriz estruturada, como ponderar essas informações pelas notas que o usuário atribuiu e como gerar um user profile que representa matematicamente o gosto desse usuário — destacando preferências por gênero, intensidade dos interesses e padrões únicos de consumo. Esse perfil permite visualizar, de forma clara, quais categorias têm maior peso e como elas diferenciam um usuário do outro.

Depois, a videoaula ensina a utilizar esse perfil para calcular similaridade entre o usuário e todos os filmes do catálogo, produzindo recomendações altamente assertivas. A partir da combinação entre os gostos do usuário e as características dos filmes, você verá como o algoritmo retorna sugestões alinhadas ao que cada pessoa realmente tende a apreciar — como drama, comédia, ação, fantasia ou romance, dependendo do perfil. Ao final, fica evidente como a personalização transforma a experiência, tornando as recomendações únicas para cada indivíduo. Vamos ao código?
