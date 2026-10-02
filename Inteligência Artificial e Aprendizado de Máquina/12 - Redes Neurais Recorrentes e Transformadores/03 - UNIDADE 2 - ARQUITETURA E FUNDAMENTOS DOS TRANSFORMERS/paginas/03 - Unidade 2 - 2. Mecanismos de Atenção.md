# Unidade 2 - 2. Mecanismos de Atenção

- Origem: [Canvas](https://pucminas.instructure.com/courses/230805/pages/unidade-2-2-mecanismos-de-atencao)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar os seguintes tópicos:**

- Fundamentos do mecanismo de atenção;
- Atenção por Produto Interno Escalado;
- Atenção Multi-Cabeça;
- Codificação Posicional.

**Ao final, você será capaz de:**

- Compreender os mecanismos de atenção e sua importância nos Transformers.

---

#### **Mecanismo de Atenção**

Você já parou para pensar como um modelo consegue identificar quais partes de uma sequência são mais importantes para a compreensão do contexto? Na videoaula a seguir, você conhecerá o mecanismo de atenção e entenderá como ele permite que modelos atribuam pesos diferentes aos elementos da entrada, priorizando informações relevantes e melhorando a qualidade das representações geradas.

A aula também apresenta exemplos práticos de desambiguação em linguagem natural, mostrando como a atenção ajuda a resolver ambiguidades e a capturar dependências de longo prazo, além de discutir seus benefícios e desafios computacionais. Vamos entender como esse mecanismo se tornou a base das arquiteturas modernas? Então, siga para o vídeo!

#### **Atenção por Produto Interno Escalado**

No vídeo a seguir, você irá entender o funcionamento da atenção por produto interno escalado, um dos principais componentes da arquitetura Transformer. A aula apresenta como esse mecanismo calcula pesos de atenção a partir da similaridade entre consultas e chaves, utilizando normalização para garantir estabilidade numérica e permitir o foco seletivo em partes relevantes da entrada.

Além disso, você irá conhecer o papel das consultas, chaves e valores, o uso de máscaras de atenção e a aplicação desse mecanismo em tarefas como tradução automática e sumarização de textos. Preparado para compreender a base do funcionamento dos Transformers? Então, acompanhe a videoaula!

#### **Atenção Multi-Cabeça**

No vídeo a seguir, você irá explorar o mecanismo de atenção multi-cabeça e entender como ele amplia a capacidade dos modelos Transformer de capturar diferentes padrões simultaneamente. A aula mostra como múltiplas cabeças de atenção operam em paralelo, permitindo que o modelo analise diversas relações entre tokens a partir de subespaços distintos, enriquecendo a representação contextual da sequência.

Você também irá compreender como as projeções independentes de consultas, chaves e valores são combinadas para formar uma visão mais robusta da entrada, além de conhecer aplicações desse mecanismo em modelos como BERT e GPT. Que tal descobrir como essa abordagem contribui para um desempenho mais expressivo e eficiente? Vamos lá!

#### **Codificação Posicional**

No vídeo a seguir, você irá compreender o papel da codificação posicional nos modelos Transformer e por que esse mecanismo é essencial para o processamento de dados sequenciais. A aula apresenta como a inserção de informações de posição nos embeddings permite que o modelo preserve a ordem dos tokens, mesmo operando de forma paralela e sem recorrência, garantindo a interpretação correta das relações temporais entre os elementos da sequência.

Além disso, você conhecerá os principais tipos de codificação posicional, como a senoidal e a aprendida, entendendo suas diferenças, vantagens e limitações, bem como sua aplicação em modelos como BERT, GPT e em tarefas visuais. Pronto para aprofundar esse conceito fundamental? Então, siga para a videoaula!
