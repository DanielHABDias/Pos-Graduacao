# Unidade 2 - 2. Técnicas de Recuperação de Informação e Similaridade

- Origem: [Canvas](https://pucminas.instructure.com/courses/230809/pages/unidade-2-2-tecnicas-de-recuperacao-de-informacao-e-similaridade)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar os seguintes tópicos:**

- Recuperação de informação;
- Modelo vetorial e cálculo de similaridade.

**Ao final, você será capaz de:**

- Compreender os conceitos fundamentais de Recuperação de Informação (RI);
- Compreender os métodos de cálculo de similaridade, com foco na Similaridade de Cosseno;
- Reconhecer a aplicação prática do modelo vetorial, distinguindo os desafios de implementação técnica entre a teoria e o processamento de similaridade em cenários reais.

---

#### **Recuperação de informação**

Nesta videoaula, você vai entender o que é um sistema de recuperação de informação e por que ele é essencial para buscas em plataformas como serviços de streaming e e‑commerce. A aula explica como esses sistemas conectam a necessidade expressa pelo usuário — por meio de palavras‑chave ou frases — aos itens mais relevantes de um catálogo possivelmente enorme. Você também verá como a busca depende de processos prévios de indexação, normalização e criação de representações adequadas, para que o algoritmo consiga localizar rapidamente os itens mais compatíveis com a consulta.

A videoaula introduz o fluxo completo de uma busca: da entrada da consulta ao ranqueamento final, mostrando como textos são convertidos em vetores numéricos e comparados matematicamente no espaço vetorial. Esse processo permite que consultas como “filmes de drama” ou “romances antigos” retornem resultados ordenados pela relevância. É uma base fundamental para compreender mecanismos de busca e também estruturas mais avançadas usadas em sistemas de recomendação. Vamos começar?

#### **Modelo vetorial e similaridade**

Nesta videoaula, você vai explorar o modelo vetorial, uma das bases mais importantes para sistemas de busca e de recomendação. A aula explica como itens (como filmes) e consultas são convertidos em vetores multidimensionais, permitindo o cálculo da similaridade entre eles. Você verá como métricas como a **similaridade do cosseno** medem quão próximos dois vetores estão, identificando assim quais itens melhor atendem ao que o usuário procura.

Além disso, a videoaula apresenta diferentes formas de representar textos — Bag of Words, TF‑IDF e embeddings — mostrando as vantagens e limitações de cada abordagem. Representações simples capturam frequência literal de palavras, enquanto embeddings conseguem compreender semântica, contexto e relações profundas entre termos. Esse conteúdo é essencial para entender por que buscas podem ser cada vez mais inteligentes e alinhadas ao significado real da consulta. Vamos avançar?

#### **Modelo vetorial e similaridade - Prática**

Nesta videoaula prática, você vai implementar um sistema completo de recuperação de informação usando o modelo vetorial. A aula mostra como pré‑processar textos, gerar representações TF‑IDF para milhares de filmes e calcular similaridades para responder consultas como “filmes de drama” ou "*Toy Story*", produzindo um ranking ordenado automaticamente pela proximidade vetorial. Você verá como converter tanto o catálogo quanto a consulta para representações compatíveis e como a similaridade do cosseno atua na recuperação final.

A videoaula também apresenta uma implementação mais avançada, usando Sentence‑BERT e embeddings, além de um índice eficiente via HNSW, para buscas semânticas de alta performance. Essa abordagem permite identificar filmes relacionados não apenas por palavras idênticas, mas pelo significado contextual do termo buscado — por exemplo, encontrando toda a trilogia de *O Poderoso Chefão* ou animações próximas a *Toy Story*. É uma etapa prática fundamental para construir buscadores modernos e inteligentes. Vamos ao código?
