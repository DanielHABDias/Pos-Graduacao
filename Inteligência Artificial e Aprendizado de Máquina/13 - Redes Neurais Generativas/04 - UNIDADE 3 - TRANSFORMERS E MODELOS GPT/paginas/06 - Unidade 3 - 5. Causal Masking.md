# Unidade 3 - 5. Causal Masking

- Origem: [Canvas](https://pucminas.instructure.com/courses/230806/pages/unidade-3-5-causal-masking)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar o seguinte tópico:**

- Causal Masking em Modelos Autorregressivos.

**Ao final, você será capaz de:**

- Reconhecer a função do causal masking no controle do acesso à informação futura durante a geração de texto.

---

#### **Causal Masking**

Na próxima videoaula, você irá entender o conceito de Causal Masking, um dos componentes essenciais para que modelos como o GPT consigam gerar texto de maneira coerente e sequencial. Embora o mecanismo de atenção analise todas as palavras em paralelo, durante o treinamento é fundamental que cada posição da sequência não enxergue tokens futuros, garantindo que o modelo aprenda a prever a próxima palavra apenas com base no que já foi escrito. O causal mask faz exatamente isso: bloqueia, na matriz de atenção, qualquer acesso a posições futuras, assegurando que o modelo respeite a direção temporal da linguagem, simulando fielmente a forma como escrevemos e pensamos.

Além disso, você verá por que esse mascaramento é indispensável para tarefas de geração de texto, mas não é utilizado em outros tipos de aplicação baseadas em Transformers, como tradução automática, em que o modelo pode acessar tokens anteriores e posteriores para entender corretamente o significado. A videoaula também ilustra, de forma clara, como o masking é aplicado em paralelo a todas as palavras da sequência, garantindo eficiência no treinamento ao mesmo tempo que preserva a causalidade. Com isso, o modelo aprende a gerar texto de maneira fluida, sem “trapacear” olhando o futuro. Pronto(a) para compreender uma das engrenagens mais importantes por trás do GPT? Então, assista à videoaula!
