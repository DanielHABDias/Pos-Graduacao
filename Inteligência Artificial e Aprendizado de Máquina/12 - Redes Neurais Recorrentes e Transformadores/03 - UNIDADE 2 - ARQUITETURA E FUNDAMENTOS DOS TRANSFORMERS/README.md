# 03 - UNIDADE 2 - ARQUITETURA E FUNDAMENTOS DOS TRANSFORMERS

[← Voltar à disciplina](../README.md)

## Resumo da unidade

A unidade apresenta atenção e a arquitetura Transformer. Cada token combina informação dos demais tokens em paralelo, com codificação de posição para representar ordem.

### Exemplo

Na frase “o banco aprovou o crédito”, a atenção pode relacionar “banco” a “crédito” e distinguir o sentido financeiro de outros usos.

## Fórmulas essenciais

### Atenção escalada

$$
\mathrm{Attention}(Q,K,V)=\mathrm{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
$$

Calcula quanto cada consulta deve combinar os valores associados às chaves.


## Conteúdo da unidade

- [Unidade 2 - Orientações de Estudo](paginas/01%20-%20Unidade%202%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md) — Os modelos modernos de inteligência artificial são capazes de traduzir textos, responder perguntas e até gerar conteúdo com uma precisão impressionante. Essa evolução é possível graças aos Transformers , uma arquitetura que revolucionou a forma como tratamos dados sequenciais e se tornou a base dos sistemas de IA mais avançados da atualidade. Nesta unidade, você vai conhecer os fundamentos dos Transformers e…
- [Unidade 2 - 1. Fundamentos dos Transformers](paginas/02%20-%20Unidade%202%20-%201.%20Fundamentos%20dos%20Transformers.md) — - Limitações das RNNs e surgimento dos Transformers. - Identificar os conceitos fundamentais dos Transformers. No vídeo a seguir, você irá compreender as principais limitações das redes neurais recorrentes e os desafios que surgem quando esses modelos são aplicados a sequências longas e complexas. A aula aborda questões como o desaparecimento e a explosão de gradientes, as dificuldades de manter informações…
- [Unidade 2 - 2. Mecanismos de Atenção](paginas/03%20-%20Unidade%202%20-%202.%20Mecanismos%20de%20Aten%C3%A7%C3%A3o.md) — Nesta aula, vamos abordar os seguintes tópicos: - Fundamentos do mecanismo de atenção; - Atenção por Produto Interno Escalado; - Atenção Multi-Cabeça; - Codificação Posicional. - Compreender os mecanismos de atenção e sua importância nos Transformers. Você já parou para pensar como um modelo consegue identificar quais partes de uma sequência são mais importantes para a compreensão do contexto? Na videoaula a seguir,
- [Unidade 2 - 3. Arquitetura Transformer](paginas/04%20-%20Unidade%202%20-%203.%20Arquitetura%20Transformer.md) — Nesta aula, vamos abordar os seguintes tópicos: - Arquitetura do codificador; - Arquitetura do decodificador; - Atenção mascarada e integração encoder-decoder. - Descrever os componentes da arquitetura Transformer. No vídeo a seguir, você irá conhecer a arquitetura do codificador nos modelos Transformer e entender como ele processa a entrada para gerar representações contextuais ricas. A aula mostra como os blocos…
- [Unidade 2 - 4. Treinamento de modelos baseados em Transformers](paginas/05%20-%20Unidade%202%20-%204.%20Treinamento%20de%20modelos%20baseados%20em%20Transformers.md) — - Compreender estratégias de treinamento de Transformers. No vídeo a seguir, você irá compreender como funciona o treinamento de modelos Transformers e quais são as principais etapas envolvidas nesse processo. A aula aborda desde o pré-processamento dos dados, tokenização, construção do vocabulário e codificação posicional até aspectos fundamentais como inicialização de pesos, funções de perda, otimizadores e…
- [Unidade 2 - 5. Comparação entre RNNs e Transformers](paginas/06%20-%20Unidade%202%20-%205.%20Compara%C3%A7%C3%A3o%20entre%20RNNs%20e%20Transformers.md) — - Reconhecer as diferenças entre arquiteturas recorrentes e baseadas em atenção. No vídeo a seguir, você irá comparar as principais características das redes neurais recorrentes e dos Transformers, compreendendo como cada arquitetura processa dados sequenciais e quais impactos isso traz para desempenho, escalabilidade e aplicações práticas. A aula apresenta as diferenças entre o processamento sequencial das redes…
- [Unidade 2 - 6. Aplicações de Transformers](paginas/07%20-%20Unidade%202%20-%206.%20Aplica%C3%A7%C3%B5es%20de%20Transformers.md) — No vídeo a seguir, você irá conhecer as principais aplicações dos Transformers e entender por que essa arquitetura se tornou central em soluções modernas de inteligência artificial. A aula apresenta como esses modelos são utilizados em tarefas como tradução automática, sumarização de textos, geração de conteúdo, sistemas de perguntas e respostas, análise de sentimentos e chatbots, destacando o papel do mecanismo de…
- [Unidade 2 - Material Complementar](paginas/08%20-%20Unidade%202%20-%20Material%20Complementar.md) — Unidade 2 - Tema 2 - Atenção por Produto Interno Escalado.pptx Unidade 2 - Tema 2 - Atenção Multi Cabeca.pptx Unidade 2 - Tema 2 - Codificação Posicional.pptx Unidade 2 - Tema 3 - Arquitetura Codificador.pptx Unidade 2 - Tema 3 - Arquitetura Decodificador.pptx Unidade 2 - Tema 3 - Atenção Mascarada Integração CD.pptx Unidade 2 - Tema 4 - Treinamento Transformers.pptx

## Materiais

### Apresentações (11)

- [Unidade2-Tema1-Topico1 - Limitacoes RNNs.pptx](documentos/Unidade2-Tema1-Topico1%20-%20Limitacoes%20RNNs.pptx)
- [Unidade2-Tema2-Topico1 - Mecanismo Atenção.pptx](documentos/Unidade2-Tema2-Topico1%20-%20Mecanismo%20Aten%C3%A7%C3%A3o.pptx)
- [Unidade2-Tema2-Topico2 - Atenção por Produto Interno Escalado.pptx](documentos/Unidade2-Tema2-Topico2%20-%20Aten%C3%A7%C3%A3o%20por%20Produto%20Interno%20Escalado.pptx)
- [Unidade2-Tema2-Topico3 - Atenção Multi Cabeca.pptx](documentos/Unidade2-Tema2-Topico3%20-%20Aten%C3%A7%C3%A3o%20Multi%20Cabeca.pptx)
- [Unidade2-Tema2-Topico4 - Codificação Posicional.pptx](documentos/Unidade2-Tema2-Topico4%20-%20Codifica%C3%A7%C3%A3o%20Posicional.pptx)
- [Unidade2-Tema3-Topico1 - Arquitetura Codificador.pptx](documentos/Unidade2-Tema3-Topico1%20-%20Arquitetura%20Codificador.pptx)
- [Unidade2-Tema3-Topico2 - Arquitetura Decodificador.pptx](documentos/Unidade2-Tema3-Topico2%20-%20Arquitetura%20Decodificador.pptx)
- [Unidade2-Tema3-Topico3 - Atenção Mascarada Integração CD.pptx](documentos/Unidade2-Tema3-Topico3%20-%20Aten%C3%A7%C3%A3o%20Mascarada%20Integra%C3%A7%C3%A3o%20CD.pptx)
- [Unidade2-Tema4-Topico1 - Treinamento Transformers.pptx](documentos/Unidade2-Tema4-Topico1%20-%20Treinamento%20Transformers.pptx)
- [Unidade2-Tema5-Topico1 - Comparação RNNs Transformers.pptx](documentos/Unidade2-Tema5-Topico1%20-%20Compara%C3%A7%C3%A3o%20RNNs%20Transformers.pptx)
- [Unidade2-Tema6-Topico1 - Aplicações Transformers.pptx](documentos/Unidade2-Tema6-Topico1%20-%20Aplica%C3%A7%C3%B5es%20Transformers.pptx)

### Páginas e textos (8)

- [01 - Unidade 2 - Orientações de Estudo.md](paginas/01%20-%20Unidade%202%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md)
- [02 - Unidade 2 - 1. Fundamentos dos Transformers.md](paginas/02%20-%20Unidade%202%20-%201.%20Fundamentos%20dos%20Transformers.md)
- [03 - Unidade 2 - 2. Mecanismos de Atenção.md](paginas/03%20-%20Unidade%202%20-%202.%20Mecanismos%20de%20Aten%C3%A7%C3%A3o.md)
- [04 - Unidade 2 - 3. Arquitetura Transformer.md](paginas/04%20-%20Unidade%202%20-%203.%20Arquitetura%20Transformer.md)
- [05 - Unidade 2 - 4. Treinamento de modelos baseados em Transformers.md](paginas/05%20-%20Unidade%202%20-%204.%20Treinamento%20de%20modelos%20baseados%20em%20Transformers.md)
- [06 - Unidade 2 - 5. Comparação entre RNNs e Transformers.md](paginas/06%20-%20Unidade%202%20-%205.%20Compara%C3%A7%C3%A3o%20entre%20RNNs%20e%20Transformers.md)
- [07 - Unidade 2 - 6. Aplicações de Transformers.md](paginas/07%20-%20Unidade%202%20-%206.%20Aplica%C3%A7%C3%B5es%20de%20Transformers.md)
- [08 - Unidade 2 - Material Complementar.md](paginas/08%20-%20Unidade%202%20-%20Material%20Complementar.md)

### Imagens (5)

- [banner-pos-2022-1.jpg](images/banner-pos-2022-1.jpg)
- [banner-pos-2022.jpg](images/banner-pos-2022.jpg)
- [icone-bussola.png](images/icone-bussola.png)
- [Leitura (2).png](images/Leitura%20%282%29.png)
- [material-b.png](images/material-b.png)

### HTML original (8)

- [01 - Unidade 2 - Orientações de Estudo.html](html/01%20-%20Unidade%202%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.html)
- [02 - Unidade 2 - 1. Fundamentos dos Transformers.html](html/02%20-%20Unidade%202%20-%201.%20Fundamentos%20dos%20Transformers.html)
- [03 - Unidade 2 - 2. Mecanismos de Atenção.html](html/03%20-%20Unidade%202%20-%202.%20Mecanismos%20de%20Aten%C3%A7%C3%A3o.html)
- [04 - Unidade 2 - 3. Arquitetura Transformer.html](html/04%20-%20Unidade%202%20-%203.%20Arquitetura%20Transformer.html)
- [05 - Unidade 2 - 4. Treinamento de modelos baseados em Transformers.html](html/05%20-%20Unidade%202%20-%204.%20Treinamento%20de%20modelos%20baseados%20em%20Transformers.html)
- [06 - Unidade 2 - 5. Comparação entre RNNs e Transformers.html](html/06%20-%20Unidade%202%20-%205.%20Compara%C3%A7%C3%A3o%20entre%20RNNs%20e%20Transformers.html)
- [07 - Unidade 2 - 6. Aplicações de Transformers.html](html/07%20-%20Unidade%202%20-%206.%20Aplica%C3%A7%C3%B5es%20de%20Transformers.html)
- [08 - Unidade 2 - Material Complementar.html](html/08%20-%20Unidade%202%20-%20Material%20Complementar.html)

## Roteiro de estudo

1. Leia as páginas na ordem apresentada pelo módulo.
2. Consulte os PDFs e apresentações enquanto registra definições, hipóteses e exemplos.
3. Execute notebooks e códigos, verificando entradas, saídas e limitações.
4. Ao final, responda:

   - Como você explicaria **Unidade 2 - Orientações de Estudo** sem consultar o material?
   - Como você explicaria **Unidade 2 - 1. Fundamentos dos Transformers** sem consultar o material?
   - Como você explicaria **Unidade 2 - 2. Mecanismos de Atenção** sem consultar o material?
   - Como você explicaria **Unidade 2 - 3. Arquitetura Transformer** sem consultar o material?
   - Como você explicaria **Unidade 2 - 4. Treinamento de modelos baseados em Transformers** sem consultar o material?
