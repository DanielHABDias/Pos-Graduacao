# Unidade 1 - 7. Autoencoders para Eliminação de Ruído em Imagens

- Origem: [Canvas](https://pucminas.instructure.com/courses/230806/pages/unidade-1-7-autoencoders-para-eliminacao-de-ruido-em-imagens)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar o seguinte tópico:**

- Prática de implementação de autoenconders.

**Ao final, você será capaz de:**

- Reconhecer os desafios iniciais associados ao treinamento de modelos generativos.

---

#### **Treinamento do modelo**

Na videoaula a seguir, você irá acompanhar o processo completo de treinamento de um denoising autoencoder aplicado ao dataset Fashion‑MNIST, observando como o modelo aprende a remover ruídos e reconstruir imagens de forma mais limpa e fiel. Vamos analisar desde o carregamento e preparação dos dados até a construção das partes essenciais do modelo: encoder e decoder. Você verá como o encoder aplica ruído gaussiano, extrai padrões com convoluções e reduz dimensionalidade com max pooling, enquanto o decoder executa o caminho inverso, reconstruindo a imagem original por meio de camadas densas, reshaping e convoluções transpostas.

Além disso, será possível entender como o treinamento é configurado, quantas épocas são utilizadas e por que, mesmo com um número relativamente pequeno de iterações, o modelo já pode apresentar resultados satisfatórios. Você também perceberá como ajustar o número de épocas pode influenciar a qualidade final das reconstruções e por que balancear tempo de treinamento e desempenho é uma etapa importante do processo. Preparado(a) para ver o modelo ganhar vida, aprender padrões e transformar imagens ruidosas em versões mais nítidas? Então, vamos começar!

#### **Visualizando o Resultado**

Em nossa próxima videoaula, você analisará visualmente o desempenho do denoising autoencoder após o processo de treinamento, avaliando se o modelo realmente aprendeu a remover ruídos das imagens do dataset. Você verá como são selecionadas amostras reais do conjunto de teste, como o ruído é aplicado propositalmente a essas imagens e de que forma o autoencoder, já treinado, tenta reconstruir versões mais limpas. A comparação lado a lado permite observar claramente o quanto o modelo foi capaz de recuperar detalhes e eliminar imperfeições introduzidas artificialmente.

Além disso, você irá interpretar os gráficos de loss exibidos durante o treinamento e entender por que, apesar de a queda na função de erro ter sido relativamente pequena e lenta, os resultados visuais ainda podem ser bastante satisfatórios. A videoaula também destaca que diferentes datasets oferecem níveis distintos de dificuldade, podendo exigir mais épocas ou arquiteturas mais robustas para alcançar reconstruções de alta qualidade. Com essas observações, você perceberá como avaliar não apenas métricas numéricas, mas principalmente a qualidade perceptual das imagens produzidas. Pronto(a) para ver, na prática, como o modelo transforma ruído em clareza? Dê o play e assista à videoaula!
