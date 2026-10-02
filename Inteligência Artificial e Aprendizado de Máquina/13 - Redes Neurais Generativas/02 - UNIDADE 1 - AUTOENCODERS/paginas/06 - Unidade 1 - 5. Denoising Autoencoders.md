# Unidade 1 - 5. Denoising Autoencoders

- Origem: [Canvas](https://pucminas.instructure.com/courses/230806/pages/unidade-1-5-denoising-autoencoders)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar o seguinte tópico:**

- Modelos generativos autoencoders para remoção de ruído.

**Ao final, você será capaz de:**

- Compreender aplicações usuais de modelos generativos em diferentes domínios, como remoção de ruído de imagens.

---

#### **Denoising Autoencoders**

Na videoaula a seguir, você irá compreender como funcionam os Denoising Autoencoders, uma variação poderosa dos autoencoders tradicionais projetada para remover ruído de imagens e aprender representações mais robustas dos dados. Você verá como, ao adicionar propositalmente ruído às entradas, o modelo é forçado a aprender características realmente relevantes, evitando simplesmente memorizar os padrões originais. Durante o processo de treinamento, o encoder recebe imagens corrompidas, enquanto o decoder tenta reconstruir as versões limpas, fazendo com que o modelo aprenda a recuperar detalhes perdidos e restaurar informações essenciais.

Além disso, você acompanhará como essa abordagem não apenas melhora a capacidade de reconstrução, mas também fortalece a habilidade do modelo em lidar com variações e imperfeições do mundo real. Verá exemplos práticos em que o autoencoder é capaz de “adivinhar” partes ausentes da imagem, preenchendo falhas e reconstruindo elementos que não estão visíveis na entrada ruidosa. Essa técnica é amplamente utilizada em pré-processamento de dados, compressão robusta e até em pipelines de visão computacional para aumento de qualidade. Preparado para descobrir como ensinar uma rede neural a limpar imagens e extrair representações mais inteligentes? Então, assista à videoaula a seguir!
