# Unidade 1 - 4. Convolutional Autoencoders

- Origem: [Canvas](https://pucminas.instructure.com/courses/230806/pages/unidade-1-4-convolutional-autoencoders)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar o seguinte tópico:**

- Modelos generativos autoencoders com redes convolucionais.

**Ao final, você será capaz de:**

- Identificar os elementos fundamentais do funcionamento de modelos convolucionais, incluindo arquitetura básica e fluxo de treinamento.

---

#### **Convolutional Autoencoders**

Na videoaula a seguir, você irá compreender como funcionam os convolutional autoencoders, uma variação dos autoencoders tradicionais especialmente projetada para trabalhar com imagens. Você verá por que arquiteturas totalmente densas perdem desempenho quando aplicadas a dados visuais, principalmente porque transformam a imagem em um vetor e, com isso, descartam relações espaciais fundamentais entre pixels. Ao explorar esse conceito, ficará claro que, em problemas envolvendo visão computacional, preservar a estrutura bidimensional da imagem e o relacionamento local entre pixels é essencial para capturar formas, texturas e padrões relevantes.

Além disso, a aula mostrará como o encoder baseado em convolução utiliza filtros e camadas de pooling para extrair características locais e reduzir progressivamente a dimensionalidade espacial, enquanto aumenta a profundidade da representação. Em seguida, você acompanhará como o decoder executa o processo inverso, utilizando camadas convolucionais transpostas ou técnicas de upsampling para reconstruir a imagem. Essa combinação torna os convolutional autoencoders muito mais eficazes para compressão, reconstrução e aprendizado de representações visuais em comparação com modelos densos tradicionais. Preparado(a) para entender uma das arquiteturas mais poderosas para manipular imagens em deep learning? Então, dê o play!
