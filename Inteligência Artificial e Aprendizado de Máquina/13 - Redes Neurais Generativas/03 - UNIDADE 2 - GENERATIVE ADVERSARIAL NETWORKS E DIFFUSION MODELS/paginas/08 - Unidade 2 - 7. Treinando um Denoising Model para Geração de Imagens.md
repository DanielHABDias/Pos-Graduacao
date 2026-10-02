# Unidade 2 - 7. Treinando um Denoising Model para Geração de Imagens

- Origem: [Canvas](https://pucminas.instructure.com/courses/230806/pages/unidade-2-7-treinando-um-denoising-model-para-geracao-de-imagens)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar o seguinte tópico:**

- Etapas do Treinamento de um Modelo de Denoising.

**Ao final, você será capaz de:**

- Reconhecer as etapas necessárias para treinar um modelo de denoising.

---

#### **Treinando um Denoising Model**

Na última videoaula desta unidade, você irá entender em detalhes como funciona o treinamento de um Denoising Model, base essencial dos modernos modelos de difusão utilizados na geração de imagens. A aula mostra que, durante a fase de treinamento, o modelo aprende a prever o ruído presente em uma imagem ruidosa em diferentes etapas do processo de difusão. Isso significa que o modelo não tenta restaurar tudo de uma vez, mas sim aprender pequenas correções progressivas. Essa abordagem é o que possibilita, posteriormente, transformar uma imagem completamente aleatória (ruído puro) em uma imagem coerente e realista ao longo de vários passos de denoising.

Além disso, você verá como o processo reverso de difusão é executado passo a passo: a rede neural prevê o ruído da imagem atual, estima uma versão menos ruidosa e avança para o próximo estágio até que reste apenas a imagem final. A aula também explica por que esse método permite criar imagens inéditas: ao começar sempre de um ruído aleatório, cada trajetória no processo reverso leva a um resultado único, ainda que siga o estilo aprendido no conjunto de treinamento. Isso significa que, treinado com imagens de gatos, por exemplo, o modelo será capaz de gerar gatos completamente novos. Preparado(a) para entender a lógica por trás da tecnologia usada no Stable Diffusion, DALL·E e outros modelos de ponta? Então, assista à videoaula!
