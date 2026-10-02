# Unidade 1 - 3. Stacked Autoencoders

- Origem: [Canvas](https://pucminas.instructure.com/courses/230806/pages/unidade-1-3-stacked-autoencoders)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar o seguinte tópico:**

- Representação latente e sua importância no processo generativo.

**Ao final, você será capaz de:**

- Entender o papel da representação latente e sua importância no processo de geração de dados.

---

#### **Stacked Autoencoders**

Na videoaula a seguir, você compreenderá como funcionam os stacked autoencoders, uma evolução dos autoencoders tradicionais que permite aprender representações muito mais profundas e complexas dos dados. Você verá como, ao empilhar múltiplas camadas no encoder e no decoder, o modelo se torna capaz de capturar padrões mais abstratos e refinados, algo especialmente útil quando trabalhamos com imagens ou dados de alta dimensionalidade. Também entenderá o conceito de simetria na arquitetura, em que o caminho de codificação é espelhado no processo de reconstrução, garantindo que o modelo seja capaz de transformar e recuperar as informações de forma consistente.

Além disso, a aula irá mostrar na prática como uma imagem é transformada ao longo das camadas do encoder até chegar ao espaço latente, por exemplo, convertendo uma matriz de 28×28 pixels em um vetor compacto de apenas 30 dimensões. A partir desse ponto, você verá como o decoder realiza o processo inverso, expandindo gradualmente essa representação até reconstruir a imagem original. Com esse passo a passo, ficará claro como stacked autoencoders não apenas reduzem dimensionalidade, mas também aprendem estruturas internas dos dados que facilitam tarefas de geração, visualização e compressão. Preparado(a) para aprofundar sua compreensão sobre modelos profundos de representação? Então, assista à videoaula!
