# Unidade 3 - 7. Positional Encoding

- Origem: [Canvas](https://pucminas.instructure.com/courses/230806/pages/unidade-3-7-positional-encoding)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar o seguinte tópico:**

- Codificação Posicional em Transformers.

**Ao final, você será capaz de:**

- Compreender a necessidade do positional encoding para representar a ordem dos tokens em sequências textuais.

---

#### **Positional Encoding**

Em nossa próxima videoaula, você irá entender por que os Transformers precisam de um componente adicional chamado Positional Encoding para funcionar corretamente. Embora o mecanismo de atenção seja extremamente poderoso e processado completamente em paralelo, ele possui uma limitação fundamental: ele não sabe, por si só, a ordem das palavras na frase. Como as operações de atenção tratam as entradas como um conjunto e não como uma sequência, informações como “quem veio antes” ou “quem veio depois” seriam totalmente perdidas, o que prejudicaria a interpretação correta do contexto. A videoaula ilustra isso com clareza usando exemplos simples, mostrando como frases com as mesmas palavras, mas em ordem diferente, têm significados completamente distintos.

Além disso, você verá como o Positional Encoding soluciona esse problema ao incorporar, no vetor de cada token, informações sobre sua posição na sequência. Essa codificação posicional é gerada matematicamente e somada ao embedding da palavra antes que os tokens entrem no bloco Transformer. Dessa forma, cada vetor final carrega não apenas o significado semântico da palavra, mas também sua localização relativa na frase. A videoaula também apresenta o funcionamento dessa soma entre token embedding e positional embedding, mostrando que ambos os vetores são aprendidos pelo modelo e combinados no início da arquitetura. Vamos entender como os Transformers “aprendem” a noção de ordem mesmo processando tudo em paralelo? Então, dê o play!
