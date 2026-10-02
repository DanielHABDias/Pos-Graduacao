# Unidade 2 - 2. GAN para geração de imagens

- Origem: [Canvas](https://pucminas.instructure.com/courses/230806/pages/unidade-2-2-gan-para-geracao-de-imagens)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar o seguinte tópico:**

- Aplicação de GANs na síntese de imagens.

**Ao final, você será capaz de:**

- Reconhecer como as GANs são utilizadas para gerar imagens, entendendo o fluxo de treinamento voltado à criação de exemplos visuais realistas.

---

#### **Generative Adversarial Networks**

Na videoaula a seguir, você compreenderá o funcionamento das Generative Adversarial Networks (GANs), uma das arquiteturas mais revolucionárias já desenvolvidas para geração de dados sintéticos. Criadas por Ian Goodfellow, as GANs se destacam pela capacidade de produzir imagens, vídeos e outros tipos de conteúdo extremamente realistas, impulsionando áreas como super‑resolução, colorização automática, síntese de quadros em vídeos, criação de artes e até expansão de datasets médicos. Você verá exemplos práticos dessas aplicações, como TVs que ampliam resoluções para 4K, placas de vídeo que usam IA para prever quadros futuros em jogos e sistemas capazes de transformar esboços simples em imagens altamente detalhadas.

Além disso, você entenderá em profundidade o mecanismo adversarial que torna as GANs tão poderosas: a interação competitiva entre gerador e discriminador. O gerador tenta produzir imagens sintéticas convincentes, enquanto o discriminador busca diferenciar imagens reais das produzidas artificialmente. Durante o treinamento, esses dois modelos se enfrentam em um processo contínuo, levando o gerador a criar resultados cada vez mais realistas. Ao longo da videoaula, essa dinâmica será ilustrada com exemplos visuais, mostrando como o ruído inicial é transformado em uma imagem plausível e como toda a rede evolui para entregar resultados impressionantes. Preparado(a) para conhecer uma das bases da IA moderna que impulsiona grande parte das tecnologias visuais que você vê hoje? Então, vamos começar!

#### **Criando uma GAN**

Em nossa próxima videoaula, você aprenderá passo a passo como construir uma GAN — Generative Adversarial Network, entendendo na prática como seus dois componentes principais trabalham juntos em um processo competitivo e cooperativo ao mesmo tempo. O gerador, funcionando de forma semelhante ao decoder de um autoencoder, recebe um vetor de ruído e tenta transformá-lo em uma imagem convincente. Já o discriminador, atuando como um classificador binário tradicional, avalia essas imagens e decide se elas são reais (oriundas do dataset) ou falsas (produzidas pelo gerador). Ao longo da aula, você verá como essas duas redes neurais são estruturadas, como o gerador transforma representações densas em matrizes de pixels e como o discriminador utiliza camadas densas e ativação sigmoide para distinguir padrões reais de padrões artificiais.

Além disso, você compreenderá detalhadamente como ocorre o treinamento adversarial: na primeira fase, o discriminador aprende a separar imagens verdadeiras das produzidas pelo gerador; na segunda fase, o gerador é treinado para enganar o discriminador, recebendo rótulos que o incentivam a produzir imagens cada vez mais realistas. Esse ciclo cria uma dinâmica de jogo de soma zero, em que o avanço de um representa momentaneamente a derrota do outro, até que idealmente se atinja um equilíbrio, ponto em que o discriminador já não consegue diferenciar real de falso com mais do que 50% de acerto. A videoaula também discute desafios comuns, como instabilidade no treinamento e dificuldade em alcançar esse equilíbrio, reforçando a importância de experimentar diferentes arquiteturas e hiperparâmetros. Pronto(a) para ver na prática como uma GAN evolui de ruído aleatório para imagens cada vez mais convincentes? Então, assista à videoaula!

#### **Prática - GAN**

Na videoaula a seguir, você acompanhará a implementação prática de uma rede GAN utilizando o dataset Fashion‑MNIST, um conjunto simples e amplamente utilizado para experimentação em visão computacional. Vamos iniciar carregando as imagens diretamente da biblioteca Keras, que já fornece o dataset dividido entre treino e teste, contendo peças de roupas em formato monocromático 28×28. A partir disso, você verá como estruturamos os dois componentes fundamentais de uma GAN: o gerador, responsável por transformar um vetor de ruído em uma imagem sintética, e o discriminador, uma rede totalmente conectada que aprende a classificar se cada imagem apresentada é real ou falsa. A videoaula mostrará como essas arquiteturas se complementam e como o gerador utiliza operações densas e reshape para produzir imagens completas a partir de ruído aleatório.

Além disso, você acompanhará visualmente o processo de treinamento adversarial, observando como a GAN evolui ao longo das épocas. Mesmo com apenas cinco épocas, será possível perceber como as imagens produzidas pelo gerador começam a ganhar forma, passando de ruído puro para contornos reconhecíveis de roupas. A comparação entre as primeiras e últimas épocas revela claramente o aprendizado progressivo do modelo. Você também entenderá por que treinamentos mais longos tendem a produzir resultados muito melhores e como o gerador aprende, gradualmente, a enganar o discriminador, criando imagens cada vez mais semelhantes às reais. Preparado(a) para ver esse processo acontecer na prática e observar uma GAN “aprender a desenhar”? Então, vamos começar!

#### **Prática - Deep Convolutional GAN**

Na última videoaula deste tópico, você acompanhará a implementação prática de uma Deep Convolutional GAN (DCGAN), uma das arquiteturas mais eficazes para geração de imagens realistas. Diferentemente das GANs densas tradicionais, aqui o gerador e o discriminador utilizam camadas convolucionais, tornando o modelo muito mais adequado para lidar com estruturas espaciais presentes em imagens. Você verá como o gerador parte de um vetor de ruído, passa por camadas densas e depois utiliza camadas convolucionais transpostas para transformar gradualmente essa representação em uma imagem completa de 28×28 pixels. Em contrapartida, o discriminador funciona como uma CNN clássica: recebe uma imagem (real ou gerada), extrai padrões através de convoluções e, ao final, classifica se ela é autêntica ou falsa usando uma camada densa com ativação sigmoide.

Além disso, você poderá observar o impacto direto da arquitetura convolucional na qualidade das imagens produzidas. Mesmo com apenas cinco épocas de treinamento, o modelo já é capaz de gerar peças de roupa que se parecem significativamente mais com o dataset original quando comparado à GAN densa tradicional. À medida que as épocas avançam, as imagens deixam de ser borrões pouco definidos e começam a assumir contornos e texturas reconhecíveis, demonstrando como as camadas convolucionais permitem ao gerador aprender padrões visuais muito mais complexos. Essa evolução deixa claro por que as DCGANs se tornaram padrão na geração de imagens de maior fidelidade. Preparado(a) para ver a potência das convoluções na criação de imagens sintéticas? Então, assista à videoaula a seguir!
