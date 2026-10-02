# 02 - UNIDADE 1 - REDES NEURAIS RECORRENTES

[← Voltar à disciplina](../README.md)

## Resumo da unidade

A unidade modela sequências com RNNs, LSTMs e GRUs. Portas controlam que informação entra, permanece ou sai do estado, reduzindo o problema de dependências longas.

### Exemplo

Em previsão de texto, o estado resume o contexto anterior. Sequências muito longas ainda podem exigir atenção ou Transformers.

## Conteúdo da unidade

- [Unidade 1 - Orientações de Estudo](paginas/01%20-%20Unidade%201%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md) — Você já parou para pensar em como os sistemas inteligentes conseguem lidar com informações que chegam em sequência, como frases, músicas ou séries temporais? Esse é um desafio fascinante, pois envolve compreender padrões que não estão isolados, mas conectados ao longo do tempo. Nesta unidade, você vai descobrir como as Redes Neurais Recorrentes (RNNs) tornam isso possível, permitindo que modelos aprendam relações…
- [Unidade 1 - 1. Fundamentos de RNNs](paginas/02%20-%20Unidade%201%20-%201.%20Fundamentos%20de%20RNNs.md) — Nesta aula, vamos abordar os seguintes tópicos: - Introdução às Redes Neurais Recorrentes; - Diferenças entre RNNs e Redes Feedforward; - Processamento sequencial e estados ocultos. - Identificar os conceitos fundamentais das RNNs. - Reconhecer as diferenças entre arquiteturas recorrentes e feedforward. No vídeo a seguir, você irá aprofundar seus conhecimentos sobre redes neurais recorrentes e entender por que elas…
- [Unidade 1 - 2. Problemas de dependência temporal e gradientes](paginas/03%20-%20Unidade%201%20-%202.%20Problemas%20de%20depend%C3%AAncia%20temporal%20e%20gradientes.md) — - Compreender problemas de gradientes em RNNs. No vídeo a seguir, você irá compreender os principais problemas de gradiente no treinamento de redes neurais recorrentes, analisando por que eles podem desaparecer ou explodir ao longo do tempo e como isso compromete o aprendizado de dependências temporais em sequências longas. A aula apresenta o papel dos gradientes no ajuste dos pesos, as causas dessas instabilidades…
- [Unidade 1 - 3. Arquiteturas avançadas – LSTM (Long Short-Term Memory)](paginas/04%20-%20Unidade%201%20-%203.%20Arquiteturas%20avan%C3%A7adas%20%E2%80%93%20LSTM%20%28Long%20Short-Term%20Memory%29.md) — Nesta aula, vamos abordar os seguintes tópicos: - Descrever os componentes da arquitetura LSTM. No vídeo a seguir, você irá conhecer a arquitetura das redes LSTM e entender por que elas foram desenvolvidas para superar as limitações das redes neurais recorrentes tradicionais. A aula apresenta como essa arquitetura permite preservar informações relevantes por longos períodos, explicando o papel da célula de memória e
- [Unidade 1 - 4. Arquiteturas avançadas – GRU (Gated Recurrent Unit)](paginas/05%20-%20Unidade%201%20-%204.%20Arquiteturas%20avan%C3%A7adas%20%E2%80%93%20GRU%20%28Gated%20Recurrent%20Unit%29.md) — - Descrever os componentes da arquitetura GRU. No vídeo a seguir, você irá conhecer a arquitetura GRU (Gated Recurrent Unit) e entender por que ela surge como uma alternativa mais simples e eficiente para o processamento de dados sequenciais. A aula apresenta como essa arquitetura controla o fluxo de informações por meio das portas de atualização e de reset, explicando de que forma esses mecanismos decidem o que…
- [Unidade 1 - 5. Treinamento e avaliação de RNNs](paginas/06%20-%20Unidade%201%20-%205.%20Treinamento%20e%20avalia%C3%A7%C3%A3o%20de%20RNNs.md) — Nesta aula, vamos abordar os seguintes tópicos: - Backpropagation Through Time (BPTT); - Técnicas de regularização e otimização em RNNs; - Avaliação de Modelos RNN. - Compreender estratégias de treinamento de RNNs; - Compreender estratégias de avaliação de RNNs. No vídeo a seguir, você irá compreender o funcionamento do algoritmo Backpropagation Through Time (BPTT) e sua importância no treinamento de redes neurais…
- [Unidade 1 - 6. Aplicações de RNNs](paginas/07%20-%20Unidade%201%20-%206.%20Aplica%C3%A7%C3%B5es%20de%20RNNs.md) — No vídeo a seguir, você irá conhecer as principais aplicações das redes neurais recorrentes e entender por que esses modelos são especialmente adequados para lidar com dados sequenciais e temporais. A aula apresenta como as redes recorrentes são utilizadas em áreas como processamento de linguagem natural, séries temporais e análise de dados dinâmicos, permitindo capturar dependências ao longo do tempo e antecipar…
- [Unidade 1 - Material Complementar](paginas/08%20-%20Unidade%201%20-%20Material%20Complementar.md) — Unidade 1 - Tema 1 - Processamento Sequencial RNNs.pptx Unidade 1 - Tema 2 - Problemas Gradientes.pptx Unidade 1 - Tema 5 - Regularização Otimização RNNs.pptx - IPTON, Z. C.; BERKOWITZ, J.; ELKAN, C. A critical review of recurrent neural networks for sequence learning . arXiv, 2015. Disponível em: <https://arxiv.org/pdf/1506.00019 . Acesso em: 2 dez. 2025. Este artigo apresenta uma síntese clara dos desafios das…

## Materiais

### Apresentações (11)

- [Unidade1-Tema1-Topico1 - Introducao RNNs.pptx](documentos/Unidade1-Tema1-Topico1%20-%20Introducao%20RNNs.pptx)
- [Unidade1-Tema1-Topico2 - RNN vs Feedforward.pptx](documentos/Unidade1-Tema1-Topico2%20-%20RNN%20vs%20Feedforward.pptx)
- [Unidade1-Tema1-Topico3 - Processamento Sequencial RNNs.pptx](documentos/Unidade1-Tema1-Topico3%20-%20Processamento%20Sequencial%20RNNs.pptx)
- [Unidade1-Tema2-Topico1 - Problemas Gradientes.pptx](documentos/Unidade1-Tema2-Topico1%20-%20Problemas%20Gradientes.pptx)
- [Unidade1-Tema3-Topico1 - Arquitetura LSTM.pptx](documentos/Unidade1-Tema3-Topico1%20-%20Arquitetura%20LSTM.pptx)
- [Unidade1-Tema3-Topico2 - Portas LSTM.pptx](documentos/Unidade1-Tema3-Topico2%20-%20Portas%20LSTM.pptx)
- [Unidade1-Tema4-Topico1 - Arquitetura GRU.pptx](documentos/Unidade1-Tema4-Topico1%20-%20Arquitetura%20GRU.pptx)
- [Unidade1-Tema5-Topico1 - BPTT.pptx](documentos/Unidade1-Tema5-Topico1%20-%20BPTT.pptx)
- [Unidade1-Tema5-Topico2 - Regularização Otimização RNNs.pptx](documentos/Unidade1-Tema5-Topico2%20-%20Regulariza%C3%A7%C3%A3o%20Otimiza%C3%A7%C3%A3o%20RNNs.pptx)
- [Unidade1-Tema5-Topico3 - Avaliação RNN.pptx](documentos/Unidade1-Tema5-Topico3%20-%20Avalia%C3%A7%C3%A3o%20RNN.pptx)
- [Unidade1-Tema6-Topico1- Aplicações RNNs.pptx](documentos/Unidade1-Tema6-Topico1-%20Aplica%C3%A7%C3%B5es%20RNNs.pptx)

### Páginas e textos (8)

- [01 - Unidade 1 - Orientações de Estudo.md](paginas/01%20-%20Unidade%201%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md)
- [02 - Unidade 1 - 1. Fundamentos de RNNs.md](paginas/02%20-%20Unidade%201%20-%201.%20Fundamentos%20de%20RNNs.md)
- [03 - Unidade 1 - 2. Problemas de dependência temporal e gradientes.md](paginas/03%20-%20Unidade%201%20-%202.%20Problemas%20de%20depend%C3%AAncia%20temporal%20e%20gradientes.md)
- [04 - Unidade 1 - 3. Arquiteturas avançadas – LSTM (Long Short-Term Memory).md](paginas/04%20-%20Unidade%201%20-%203.%20Arquiteturas%20avan%C3%A7adas%20%E2%80%93%20LSTM%20%28Long%20Short-Term%20Memory%29.md)
- [05 - Unidade 1 - 4. Arquiteturas avançadas – GRU (Gated Recurrent Unit).md](paginas/05%20-%20Unidade%201%20-%204.%20Arquiteturas%20avan%C3%A7adas%20%E2%80%93%20GRU%20%28Gated%20Recurrent%20Unit%29.md)
- [06 - Unidade 1 - 5. Treinamento e avaliação de RNNs.md](paginas/06%20-%20Unidade%201%20-%205.%20Treinamento%20e%20avalia%C3%A7%C3%A3o%20de%20RNNs.md)
- [07 - Unidade 1 - 6. Aplicações de RNNs.md](paginas/07%20-%20Unidade%201%20-%206.%20Aplica%C3%A7%C3%B5es%20de%20RNNs.md)
- [08 - Unidade 1 - Material Complementar.md](paginas/08%20-%20Unidade%201%20-%20Material%20Complementar.md)

### Imagens (5)

- [banner-pos-2022-1.jpg](images/banner-pos-2022-1.jpg)
- [banner-pos-2022.jpg](images/banner-pos-2022.jpg)
- [icone-bussola.png](images/icone-bussola.png)
- [Leitura (2).png](images/Leitura%20%282%29.png)
- [material-b.png](images/material-b.png)

### HTML original (8)

- [01 - Unidade 1 - Orientações de Estudo.html](html/01%20-%20Unidade%201%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.html)
- [02 - Unidade 1 - 1. Fundamentos de RNNs.html](html/02%20-%20Unidade%201%20-%201.%20Fundamentos%20de%20RNNs.html)
- [03 - Unidade 1 - 2. Problemas de dependência temporal e gradientes.html](html/03%20-%20Unidade%201%20-%202.%20Problemas%20de%20depend%C3%AAncia%20temporal%20e%20gradientes.html)
- [04 - Unidade 1 - 3. Arquiteturas avançadas – LSTM (Long Short-Term Memory).html](html/04%20-%20Unidade%201%20-%203.%20Arquiteturas%20avan%C3%A7adas%20%E2%80%93%20LSTM%20%28Long%20Short-Term%20Memory%29.html)
- [05 - Unidade 1 - 4. Arquiteturas avançadas – GRU (Gated Recurrent Unit).html](html/05%20-%20Unidade%201%20-%204.%20Arquiteturas%20avan%C3%A7adas%20%E2%80%93%20GRU%20%28Gated%20Recurrent%20Unit%29.html)
- [06 - Unidade 1 - 5. Treinamento e avaliação de RNNs.html](html/06%20-%20Unidade%201%20-%205.%20Treinamento%20e%20avalia%C3%A7%C3%A3o%20de%20RNNs.html)
- [07 - Unidade 1 - 6. Aplicações de RNNs.html](html/07%20-%20Unidade%201%20-%206.%20Aplica%C3%A7%C3%B5es%20de%20RNNs.html)
- [08 - Unidade 1 - Material Complementar.html](html/08%20-%20Unidade%201%20-%20Material%20Complementar.html)

## Roteiro de estudo

1. Leia as páginas na ordem apresentada pelo módulo.
2. Consulte os PDFs e apresentações enquanto registra definições, hipóteses e exemplos.
3. Execute notebooks e códigos, verificando entradas, saídas e limitações.
4. Ao final, responda:

   - Como você explicaria **Unidade 1 - Orientações de Estudo** sem consultar o material?
   - Como você explicaria **Unidade 1 - 1. Fundamentos de RNNs** sem consultar o material?
   - Como você explicaria **Unidade 1 - 2. Problemas de dependência temporal e gradientes** sem consultar o material?
   - Como você explicaria **Unidade 1 - 3. Arquiteturas avançadas – LSTM (Long Short-Term Memory)** sem consultar o material?
   - Como você explicaria **Unidade 1 - 4. Arquiteturas avançadas – GRU (Gated Recurrent Unit)** sem consultar o material?
