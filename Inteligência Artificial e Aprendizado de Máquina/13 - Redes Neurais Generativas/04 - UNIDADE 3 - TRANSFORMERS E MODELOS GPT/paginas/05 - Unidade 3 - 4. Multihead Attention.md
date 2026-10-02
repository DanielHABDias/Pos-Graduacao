# Unidade 3 - 4. Multihead Attention

- Origem: [Canvas](https://pucminas.instructure.com/courses/230806/pages/unidade-3-4-multihead-attention)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar o seguinte tópico:**

- Multihead Attention e Captura de Múltiplas Relações.

**Ao final, você será capaz de:**

- Compreender como o multihead attention amplia a capacidade do modelo de representar diferentes padrões de dependência em uma sequência.

---

#### **Multi-head attention**

Na videoaula a seguir, você irá entender como o mecanismo de Multi‑Head Attention expande o poder do self‑attention tradicional, permitindo que o modelo capture múltiplos tipos de relações e contextos simultaneamente. Em vez de utilizar apenas um único attention head, a arquitetura Transformer executa vários heads em paralelo, cada um aprendendo um padrão distinto de dependências entre as palavras. Isso torna o modelo muito mais expressivo e capaz de compreender nuances complexas da linguagem, já que diferentes heads podem focar em diferentes aspectos: sintaxe, relações de longo alcance, associações semânticas ou detalhes locais.

Além disso, você verá como o modelo, após processar a entrada em vários heads, concatena todas as saídas e aplica uma projeção linear final por meio de uma matriz de pesos aprendida durante o treinamento. Esse passo unifica a contribuição de cada head em um único vetor de contexto, mais rico e informativo. A aula também mostra um exemplo prático com a implementação da camada MultiHeadAttention do Keras, explicando como definir o número de heads, o tamanho dos vetores de query, key e value, e como isso se traduz em uma saída robusta. Preparado(a) para entender como essa técnica tornou os Transformers tão poderosos e precisos? Então, vamos começar!
