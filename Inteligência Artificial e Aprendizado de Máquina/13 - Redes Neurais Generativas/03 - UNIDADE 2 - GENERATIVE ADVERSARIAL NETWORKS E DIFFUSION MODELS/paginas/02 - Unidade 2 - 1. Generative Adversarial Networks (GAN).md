# Unidade 2 - 1. Generative Adversarial Networks (GAN)

- Origem: [Canvas](https://pucminas.instructure.com/courses/230806/pages/unidade-2-1-generative-adversarial-networks-gan)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar o seguinte tópico:**

- Fundamentos das GANs.

**Ao final, você será capaz de:**

- Compreender o funcionamento básico das GANs, incluindo o papel do gerador e do discriminador dentro do processo adversarial.

---

#### **Variational Autoencoders**

Na videoaula a seguir, você compreenderá de forma intuitiva e prática o conceito de Variational Autoencoders, entendendo por que eles representam um avanço significativo em relação aos autoencoders tradicionais. Em vez de mapear cada imagem para um único ponto fixo no espaço latente, os VAEs aprendem uma distribuição inteira, geralmente uma normal multivariada, representando a região onde é mais provável que a imagem esteja. Essa mudança de perspectiva permite gerar representações mais estáveis, contínuas e flexíveis, evitando distorções bruscas quando pequenas variações são feitas no espaço latente. A videoaula também explica como essa abordagem funciona como uma forma de regularização, forçando o modelo a organizar o espaço latente de maneira mais suave e consistente.

Além disso, você verá como essa estrutura possibilita uma geração muito mais rica de dados, já que o modelo pode navegar aleatoriamente dentro da região de probabilidade associada a cada entrada e produzir múltiplas variações realistas. Enquanto o encoder tradicional aprende apenas uma representação compacta, o encoder variacional aprende não só a representação, mas também a incerteza associada a ela. O decoder continua exercendo o mesmo papel: receber o vetor latente e reconstruir a imagem. Porém, como agora ele trabalha com amostras probabilísticas, consegue gerar resultados mais suaves, coerentes e diversificados. Pronto(a) para mergulhar em uma das arquiteturas mais elegantes e poderosas do deep learning generativo? Então, assista à videoaula!

#### **Criando um VAE**

Em nossa próxima videoaula, você irá entender como transformar um autoencoder tradicional em um Variational Autoencoder (VAE), um dos modelos generativos mais importantes e influentes do deep learning moderno. Você verá por que, diferentemente dos autoencoders comuns, que produzem um único ponto fixo no espaço latente, o VAE aprende uma distribuição probabilística, representada por média e variância, capaz de descrever uma região inteira no espaço latente. Isso permite que o modelo gere múltiplas variações realistas a partir de uma mesma entrada, ampliando enormemente sua capacidade criativa. Para possibilitar esse comportamento, o VAE inclui uma nova etapa fundamental: a camada de amostragem, responsável por gerar pontos aleatórios dentro da distribuição aprendida, seguindo uma normal multivariada.

Além disso, você irá compreender como o treinamento do VAE ajusta simultaneamente dois objetivos: reconstruir bem as imagens originais e manter a distribuição latente próxima de uma normal padrão, por meio do termo de divergência KL. Essa combinação garante que o modelo aprenda representações suaves, contínuas e navegáveis, características que permitem interpolar entre imagens, gerar exemplos inéditos e manipular atributos no espaço latente. A videoaula também mostrará como o encoder passa a calcular mean e log-variance, como o decoder permanece responsável por transformar uma amostra latente de volta em uma imagem, e como toda essa estrutura forma uma poderosa arquitetura generativa. Preparado(a) para explorar um dos modelos mais elegantes e versáteis da IA moderna? Então, vamos começar!

#### **Gerando imagens com VAE**

Na videoaula a seguir, você descobrirá como gerar novas imagens utilizando um Variational Autoencoder após o seu treinamento. Vamos explorar duas etapas fundamentais: primeiro, a codificação das imagens reais do conjunto de teste, permitindo visualizar como o modelo organiza esses exemplos no espaço latente; e segundo, a amostragem de novos pontos desse espaço para criar imagens completamente inéditas. Essa visualização do espaço latente ajuda a compreender como o VAE distribui diferentes padrões visuais e revela se o modelo conseguiu formar uma estrutura organizada e coerente entre os tipos de imagens.

Além disso, você verá na prática como pontos aleatórios amostrados de uma distribuição normal padrão são convertidos em representações visuais pelo decoder, mostrando a verdadeira capacidade generativa do VAE. Mesmo sem utilizar rótulos durante o treinamento, o modelo aprende, por conta própria, a agrupar padrões semelhantes e gerar versões realistas de diferentes categorias. Ao observar as imagens sintetizadas, você entenderá como o VAE captura estilos, texturas e formas, produzindo resultados que não estavam presentes no conjunto original, mas que ainda assim parecem plausíveis. Preparado(a) para visualizar o espaço latente ganhando vida e ver o VAE criando novas imagens? Então, assista à videoaula a seguir!
