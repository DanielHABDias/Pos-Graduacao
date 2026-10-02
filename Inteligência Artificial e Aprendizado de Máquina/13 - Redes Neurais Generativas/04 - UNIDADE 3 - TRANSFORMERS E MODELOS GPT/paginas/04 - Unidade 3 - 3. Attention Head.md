# Unidade 3 - 3. Attention Head

- Origem: [Canvas](https://pucminas.instructure.com/courses/230806/pages/unidade-3-3-attention-head)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar o seguinte tópico:**

- Funcionamento de uma Attention Head.

**Ao final, você será capaz de:**

- Identificar o papel de uma attention head no cálculo das relações entre consultas, chaves e valores.

---

#### **Attention Is All You Need**

Em nossa próxima videoaula, você irá compreender com profundidade o funcionamento interno do mecanismo de atenção introduzido no artigo "Attention Is All You Need", que deu origem à arquitetura Transformer. A aula mostra como, para prever a próxima palavra, o modelo não trata o texto como uma sequência fixa, mas como um conjunto de informações que podem ser consultadas dinamicamente. Isso é feito por meio do cálculo entre queries (consultas), keys (chaves) e values (valores). Assim, o modelo aprende a determinar quais palavras anteriores são relevantes para a próxima predição, atribuindo pesos maiores às que realmente moldam o contexto e ignorando as que têm pouca influência.

Além disso, você verá passo a passo como ocorre esse processo matemático: desde a tokenização inicial e a conversão das palavras em vetores de embedding, até a multiplicação entre queries e keys que produz as pontuações de atenção, posteriormente normalizadas pelo softmax. A aula também explica como o vetor de contexto é construído ao combinar os valores ponderados e por que esse vetor carrega a “opinião” de toda a frase sobre a próxima palavra a ser gerada. Com exemplos visuais, como a frase do elefante tentando entrar no carro, você perceberá como certas palavras recebem alta atenção e outras quase nenhuma. Preparado(a) para entender, de forma clara e acessível, o componente central que permitiu o surgimento dos Transformers e dos modelos GPT? Então, assista à videoaula!
