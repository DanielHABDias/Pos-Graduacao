# 04 - UNIDADE 3 - REPRESENTAÇÃO TEXTUAL

[← Voltar à disciplina](../README.md)

## Resumo da unidade

A unidade compara one-hot, bag of words, TF-IDF e embeddings. Representações esparsas preservam contagens explícitas, enquanto embeddings aproximam relações semânticas em vetores densos.

### Exemplo

TF-IDF reduz o peso de palavras frequentes em muitos documentos e destaca termos mais específicos de cada texto.

## Fórmulas essenciais

### TF-IDF

$$
\mathrm{tfidf}(t,d)=\mathrm{tf}(t,d)\log\left(\frac{N}{\mathrm{df}(t)}\right)
$$

Combina frequência no documento com raridade no conjunto.


## Conteúdo da unidade

- [Unidade 3 - Orientações de Estudo](paginas/01%20-%20Unidade%203%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md) — Bem-vindos à Unidade 3 de nossa jornada pelo universo do Processamento de Linguagem Natural. Aqui, mergulharemos no coração da representação textual, elemento vital para a compreensão e manipulação de textos por máquinas. Este módulo é dedicado a explorar diferentes métodos de transformar texto em formas que computadores possam processar eficientemente, pavimentando o caminho para análises mais profundas e…
- [Unidade 3 - 1. Engenharia de características](paginas/02%20-%20Unidade%203%20-%201.%20Engenharia%20de%20caracter%C3%ADsticas.md)
- [Unidade 3 - 2. One-Hot-Encoding](paginas/03%20-%20Unidade%203%20-%202.%20One-Hot-Encoding.md)
- [Unidade 3 - 3. Bag of Words](paginas/04%20-%20Unidade%203%20-%203.%20Bag%20of%20Words.md)
- [Unidade 3 - 4. TF-IDF](paginas/05%20-%20Unidade%203%20-%204.%20TF-IDF.md)
- [Unidade 3 - 4.1 Hands-on - Representação textual](paginas/06%20-%20Unidade%203%20-%204.1%20Hands-on%20-%20Representa%C3%A7%C3%A3o%20textual.md)
- [Unidade 3 - 5. Word embeddings](paginas/08%20-%20Unidade%203%20-%205.%20Word%20embeddings.md)
- [Unidade 3 - Material Complementar](paginas/09%20-%20Unidade%203%20-%20Material%20Complementar.md) — Unidade 3 - 4.2 Notebook - Representação Textual u3-02-nlp-representacao-textual-one-hot-encoding.pdf u3-03-nlp-representacao-textual-bag-of-words.pdf How to Use Tfidftransformer & Tfidfvectorizer? Quick Introduction to Bag-of-Words (BoW) and TF-IDF for Creating Features from Text Easiest explanation for Text classification in NLP using Python (Chatbot training on words)

## Materiais

### PDFs (4)

- [u3-01-nlp-engenharia-de-caracteristicas.pdf](documentos/u3-01-nlp-engenharia-de-caracteristicas.pdf) (7 páginas)
- [u3-02-nlp-representacao-textual-one-hot-encoding.pdf](documentos/u3-02-nlp-representacao-textual-one-hot-encoding.pdf) (10 páginas)
- [u3-03-nlp-representacao-textual-bag-of-words.pdf](documentos/u3-03-nlp-representacao-textual-bag-of-words.pdf) (11 páginas)
- [u3-04-nlp-representacao-textual-tf-idf.pdf](documentos/u3-04-nlp-representacao-textual-tf-idf.pdf) (16 páginas)

### Apresentações (1)

- [u3-04-nlp-representacao-textual-tf-idf.pptx](documentos/u3-04-nlp-representacao-textual-tf-idf.pptx)

### Notebooks (1)

- [03_a_representação_textual.ipynb](documentos/03_a_representa%C3%A7%C3%A3o_textual.ipynb)

### Páginas e textos (8)

- [01 - Unidade 3 - Orientações de Estudo.md](paginas/01%20-%20Unidade%203%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md)
- [02 - Unidade 3 - 1. Engenharia de características.md](paginas/02%20-%20Unidade%203%20-%201.%20Engenharia%20de%20caracter%C3%ADsticas.md)
- [03 - Unidade 3 - 2. One-Hot-Encoding.md](paginas/03%20-%20Unidade%203%20-%202.%20One-Hot-Encoding.md)
- [04 - Unidade 3 - 3. Bag of Words.md](paginas/04%20-%20Unidade%203%20-%203.%20Bag%20of%20Words.md)
- [05 - Unidade 3 - 4. TF-IDF.md](paginas/05%20-%20Unidade%203%20-%204.%20TF-IDF.md)
- [06 - Unidade 3 - 4.1 Hands-on - Representação textual.md](paginas/06%20-%20Unidade%203%20-%204.1%20Hands-on%20-%20Representa%C3%A7%C3%A3o%20textual.md)
- [08 - Unidade 3 - 5. Word embeddings.md](paginas/08%20-%20Unidade%203%20-%205.%20Word%20embeddings.md)
- [09 - Unidade 3 - Material Complementar.md](paginas/09%20-%20Unidade%203%20-%20Material%20Complementar.md)

### Imagens (4)

- [banner-pos-2022.jpg](images/banner-pos-2022.jpg)
- [icone-bussola.png](images/icone-bussola.png)
- [icone-coruja.png](images/icone-coruja.png)
- [material-b.png](images/material-b.png)

### HTML original (8)

- [01 - Unidade 3 - Orientações de Estudo.html](html/01%20-%20Unidade%203%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.html)
- [02 - Unidade 3 - 1. Engenharia de características.html](html/02%20-%20Unidade%203%20-%201.%20Engenharia%20de%20caracter%C3%ADsticas.html)
- [03 - Unidade 3 - 2. One-Hot-Encoding.html](html/03%20-%20Unidade%203%20-%202.%20One-Hot-Encoding.html)
- [04 - Unidade 3 - 3. Bag of Words.html](html/04%20-%20Unidade%203%20-%203.%20Bag%20of%20Words.html)
- [05 - Unidade 3 - 4. TF-IDF.html](html/05%20-%20Unidade%203%20-%204.%20TF-IDF.html)
- [06 - Unidade 3 - 4.1 Hands-on - Representação textual.html](html/06%20-%20Unidade%203%20-%204.1%20Hands-on%20-%20Representa%C3%A7%C3%A3o%20textual.html)
- [08 - Unidade 3 - 5. Word embeddings.html](html/08%20-%20Unidade%203%20-%205.%20Word%20embeddings.html)
- [09 - Unidade 3 - Material Complementar.html](html/09%20-%20Unidade%203%20-%20Material%20Complementar.html)

## Roteiro de estudo

1. Leia as páginas na ordem apresentada pelo módulo.
2. Consulte os PDFs e apresentações enquanto registra definições, hipóteses e exemplos.
3. Execute notebooks e códigos, verificando entradas, saídas e limitações.
4. Ao final, responda:

   - Como você explicaria **Unidade 3 - Orientações de Estudo** sem consultar o material?
   - Como você explicaria **Unidade 3 - 1. Engenharia de características** sem consultar o material?
   - Como você explicaria **Unidade 3 - 2. One-Hot-Encoding** sem consultar o material?
   - Como você explicaria **Unidade 3 - 3. Bag of Words** sem consultar o material?
   - Como você explicaria **Unidade 3 - 4. TF-IDF** sem consultar o material?
