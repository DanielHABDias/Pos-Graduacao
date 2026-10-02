# Unidade 3 - 6. Bloco Transformer

- Origem: [Canvas](https://pucminas.instructure.com/courses/230806/pages/unidade-3-6-bloco-transformer)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar o seguinte tópico:**

- Estrutura e Componentes do Bloco Transformer.

**Ao final, você será capaz de:**

- Identificar os principais componentes de um bloco Transformer e compreender sua organização funcional.

---

#### **Bloco Transformer**

Na videoaula a seguir, você irá compreender como funciona o bloco Transformer, a unidade fundamental que compõe toda a arquitetura dos modelos baseados em Transformers, como GPT, BERT e muitos outros. O bloco combina diversos elementos vistos em aulas anteriores em uma estrutura altamente eficiente, projetada para extrair e transformar representações cada vez mais ricas ao longo das camadas. Você verá como as matrizes Wq, Wk, Wv e Wo, aprendidas durante o treinamento, permitem que cada attention head capture padrões específicos da linguagem, e como a combinação paralela desses heads gera um vetor de contexto robusto, essencial para as previsões do modelo.

Além disso, a videoaula mostra como o bloco Transformer integra mecanismos cruciais de estabilidade e profundidade, como a layer normalization e as camadas feed‑forward densamente conectadas, responsáveis por expandir a capacidade de representação do modelo. O uso de skip connections preserva informações importantes ao longo do fluxo, evitando problemas como gradientes desaparecendo e garantindo que cada token carregue tanto o contexto imediato quanto transformações mais profundas aprendidas pela rede. Ao final, você verá também um exemplo de implementação do bloco Transformer em código, reunindo todos esses componentes em uma única estrutura funcional. Preparado(a) para entender o “tijolo” fundamental que compõe todos os grandes modelos da atualidade? Então, vamos começar!
