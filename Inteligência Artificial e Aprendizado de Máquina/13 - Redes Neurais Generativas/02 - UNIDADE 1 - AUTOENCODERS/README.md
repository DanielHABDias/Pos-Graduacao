# 02 - UNIDADE 1 - AUTOENCODERS

[← Voltar à disciplina](../README.md)

## Resumo da unidade

A unidade usa autoencoders para comprimir e reconstruir dados. VAEs aprendem uma distribuição latente regularizada, o que permite amostrar novas representações.

### Exemplo

Um denoising autoencoder recebe uma imagem corrompida e aprende a reconstruir a versão limpa, evitando apenas copiar a entrada.

## Fórmulas essenciais

### Objetivo de um VAE

$$
\mathcal{L}=\mathbb{E}_{q(z\mid x)}[\log p(x\mid z)]-D_{KL}(q(z\mid x)\Vert p(z))
$$

Equilibra reconstrução e organização do espaço latente.


## Conteúdo da unidade

- [Unidade 1 - Orientações de Estudo](paginas/01%20-%20Unidade%201%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md) — Seja muito bem-vindo e bem-vinda à Unidade 1! Vamos iniciar explorando os fundamentos que sustentam os modelos capazes de criar, reconstruir e transformar dados. Esta unidade foi planejada para apresentar a você os conceitos essenciais que permitem compreender como as máquinas aprendem a gerar novas informações a partir de padrões aprendidos. Você conhecerá o que são redes neurais generativas, por que elas se…
- [Unidade 1 - 1. Introdução às Redes Neurais Generativas](paginas/02%20-%20Unidade%201%20-%201.%20Introdu%C3%A7%C3%A3o%20%C3%A0s%20Redes%20Neurais%20Generativas.md) — - Conceitos de IA generativa e dirença para outros tipos de aprendizagem de máquina. - Compreender o conceito de redes neurais generativas e seu papel dentro do campo de aprendizado profundo. - Conhecer as diferenças conceituais entre modelos generativos e discriminativos. Na videoaula a seguir, você compreenderá os fundamentos da modelagem generativa dentro do deep learning, explorando como esses modelos são…
- [Unidade 1 - 2. Autoencoders](paginas/03%20-%20Unidade%201%20-%202.%20Autoencoders.md) — - Principais tipos de modelos generativos (Autoencoders VAEs e GANs). - Reconhecer os principais tipos de modelos generativos, como Autoencoders. Na videoaula a seguir, você irá compreender como funcionam os autoencoders, uma das arquiteturas fundamentais dentro do deep learning para redução de dimensionalidade, aprendizado de representações e geração de novos dados. Você conhecerá como esse modelo é dividido: o…
- [Unidade 1 - 3. Stacked Autoencoders](paginas/04%20-%20Unidade%201%20-%203.%20Stacked%20Autoencoders.md) — - Representação latente e sua importância no processo generativo. - Entender o papel da representação latente e sua importância no processo de geração de dados. Na videoaula a seguir, você compreenderá como funcionam os stacked autoencoders, uma evolução dos autoencoders tradicionais que permite aprender representações muito mais profundas e complexas dos dados. Você verá como, ao empilhar múltiplas camadas no…
- [Unidade 1 - 4. Convolutional Autoencoders](paginas/05%20-%20Unidade%201%20-%204.%20Convolutional%20Autoencoders.md) — - Modelos generativos autoencoders com redes convolucionais. - Identificar os elementos fundamentais do funcionamento de modelos convolucionais, incluindo arquitetura básica e fluxo de treinamento. Na videoaula a seguir, você irá compreender como funcionam os convolutional autoencoders, uma variação dos autoencoders tradicionais especialmente projetada para trabalhar com imagens. Você verá por que arquiteturas…
- [Unidade 1 - 5. Denoising Autoencoders](paginas/06%20-%20Unidade%201%20-%205.%20Denoising%20Autoencoders.md) — - Modelos generativos autoencoders para remoção de ruído. - Compreender aplicações usuais de modelos generativos em diferentes domínios, como remoção de ruído de imagens. Na videoaula a seguir, você irá compreender como funcionam os Denoising Autoencoders, uma variação poderosa dos autoencoders tradicionais projetada para remover ruído de imagens e aprender representações mais robustas dos dados. Você verá como, ao…
- [Unidade 1 - 6. Variational Autoencoders](paginas/07%20-%20Unidade%201%20-%206.%20Variational%20Autoencoders.md) — - Tipos de arquiteturas de autoenconders e aplicação prática. - Reconhecer os principais tipos de modelos generativos. Na videoaula a seguir, você irá compreender qual será o desafio prático desta unidade: desenvolver um denoising autoencoder capaz de remover ruídos de imagens e reconstruir versões mais limpas e realistas. Você verá como esse tipo de modelo aprende a partir de pares de imagens ruidosas e suas…
- [Unidade 1 - 7. Autoencoders para Eliminação de Ruído em Imagens](paginas/08%20-%20Unidade%201%20-%207.%20Autoencoders%20para%20Elimina%C3%A7%C3%A3o%20de%20Ru%C3%ADdo%20em%20Imagens.md) — - Reconhecer os desafios iniciais associados ao treinamento de modelos generativos. Na videoaula a seguir, você irá acompanhar o processo completo de treinamento de um denoising autoencoder aplicado ao dataset Fashion‑MNIST, observando como o modelo aprende a remover ruídos e reconstruir imagens de forma mais limpa e fiel. Vamos analisar desde o carregamento e preparação dos dados até a construção das partes…
- [Unidade 1 - Material Complementar](paginas/09%20-%20Unidade%201%20-%20Material%20Complementar.md) — Para aprofundar os conhecimentos apresentados nesta unidade, recomendamos a leitura do livro abaixo, que oferece uma visão prática e acessível de Processamento de Linguagem Natural: LANE, Hobson; HOWARD, Cole; HAPKE, Hannes. Natural Language Processing in Action . 1st edition. 2019. 1 online resource (544 pages). Disponível em:…

## Materiais

### Apresentações (1)

- [Unidade 1 - Autoencoders.pptx](documentos/Unidade%201%20-%20Autoencoders.pptx)

### Notebooks (1)

- [RNG_Unidade_I_Autoencoders,_GANs,_e_Diffusion_Models_projeto.ipynb](documentos/RNG_Unidade_I_Autoencoders%2C_GANs%2C_e_Diffusion_Models_projeto.ipynb)

### Páginas e textos (9)

- [01 - Unidade 1 - Orientações de Estudo.md](paginas/01%20-%20Unidade%201%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md)
- [02 - Unidade 1 - 1. Introdução às Redes Neurais Generativas.md](paginas/02%20-%20Unidade%201%20-%201.%20Introdu%C3%A7%C3%A3o%20%C3%A0s%20Redes%20Neurais%20Generativas.md)
- [03 - Unidade 1 - 2. Autoencoders.md](paginas/03%20-%20Unidade%201%20-%202.%20Autoencoders.md)
- [04 - Unidade 1 - 3. Stacked Autoencoders.md](paginas/04%20-%20Unidade%201%20-%203.%20Stacked%20Autoencoders.md)
- [05 - Unidade 1 - 4. Convolutional Autoencoders.md](paginas/05%20-%20Unidade%201%20-%204.%20Convolutional%20Autoencoders.md)
- [06 - Unidade 1 - 5. Denoising Autoencoders.md](paginas/06%20-%20Unidade%201%20-%205.%20Denoising%20Autoencoders.md)
- [07 - Unidade 1 - 6. Variational Autoencoders.md](paginas/07%20-%20Unidade%201%20-%206.%20Variational%20Autoencoders.md)
- [08 - Unidade 1 - 7. Autoencoders para Eliminação de Ruído em Imagens.md](paginas/08%20-%20Unidade%201%20-%207.%20Autoencoders%20para%20Elimina%C3%A7%C3%A3o%20de%20Ru%C3%ADdo%20em%20Imagens.md)
- [09 - Unidade 1 - Material Complementar.md](paginas/09%20-%20Unidade%201%20-%20Material%20Complementar.md)

### Imagens (5)

- [banner-pos-2022-1.jpg](images/banner-pos-2022-1.jpg)
- [banner-pos-2022.jpg](images/banner-pos-2022.jpg)
- [icone-bussola.png](images/icone-bussola.png)
- [Leitura.png](images/Leitura.png)
- [material-b.png](images/material-b.png)

### HTML original (9)

- [01 - Unidade 1 - Orientações de Estudo.html](html/01%20-%20Unidade%201%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.html)
- [02 - Unidade 1 - 1. Introdução às Redes Neurais Generativas.html](html/02%20-%20Unidade%201%20-%201.%20Introdu%C3%A7%C3%A3o%20%C3%A0s%20Redes%20Neurais%20Generativas.html)
- [03 - Unidade 1 - 2. Autoencoders.html](html/03%20-%20Unidade%201%20-%202.%20Autoencoders.html)
- [04 - Unidade 1 - 3. Stacked Autoencoders.html](html/04%20-%20Unidade%201%20-%203.%20Stacked%20Autoencoders.html)
- [05 - Unidade 1 - 4. Convolutional Autoencoders.html](html/05%20-%20Unidade%201%20-%204.%20Convolutional%20Autoencoders.html)
- [06 - Unidade 1 - 5. Denoising Autoencoders.html](html/06%20-%20Unidade%201%20-%205.%20Denoising%20Autoencoders.html)
- [07 - Unidade 1 - 6. Variational Autoencoders.html](html/07%20-%20Unidade%201%20-%206.%20Variational%20Autoencoders.html)
- [08 - Unidade 1 - 7. Autoencoders para Eliminação de Ruído em Imagens.html](html/08%20-%20Unidade%201%20-%207.%20Autoencoders%20para%20Elimina%C3%A7%C3%A3o%20de%20Ru%C3%ADdo%20em%20Imagens.html)
- [09 - Unidade 1 - Material Complementar.html](html/09%20-%20Unidade%201%20-%20Material%20Complementar.html)

## Roteiro de estudo

1. Leia as páginas na ordem apresentada pelo módulo.
2. Consulte os PDFs e apresentações enquanto registra definições, hipóteses e exemplos.
3. Execute notebooks e códigos, verificando entradas, saídas e limitações.
4. Ao final, responda:

   - Como você explicaria **Unidade 1 - Orientações de Estudo** sem consultar o material?
   - Como você explicaria **Unidade 1 - 1. Introdução às Redes Neurais Generativas** sem consultar o material?
   - Como você explicaria **Unidade 1 - 2. Autoencoders** sem consultar o material?
   - Como você explicaria **Unidade 1 - 3. Stacked Autoencoders** sem consultar o material?
   - Como você explicaria **Unidade 1 - 4. Convolutional Autoencoders** sem consultar o material?
