# 03 - UNIDADE 2 - ALGORITMOS CLÁSSICOS E AVANÇOS EM APRENDIZADO POR REFORÇO

[← Voltar à disciplina](../README.md)

## Resumo da unidade

A unidade compara Monte Carlo, diferença temporal, aproximação de funções e cenários multiagente. TD atualiza estimativas antes do episódio terminar usando outra estimativa como alvo.

### Exemplo

Q-learning aprende o valor de cada ação e pode agir com exploração epsilon-greedy para não repetir apenas a escolha conhecida.

## Fórmulas essenciais

### Atualização Q-learning

$$
Q(s,a)\leftarrow Q(s,a)+\alpha[r+\gamma\max_{a'}Q(s',a')-Q(s,a)]
$$

Atualiza o valor da ação usando o melhor valor estimado do próximo estado.


## Conteúdo da unidade

- [Unidade 2 - Orientações de Estudo](paginas/01%20-%20Unidade%202%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md) — ALGORITMOS CLÁSSICOS E AVANÇOS EM APRENDIZADO POR REFORÇO Nesta unidade, exploraremos alguns dos algoritmos mais importantes e influentes do Aprendizado por Reforço, entendendo como agentes podem aprender a tomar decisões em ambientes dinâmicos, incertos e muitas vezes complexos. Vamos começar revisitando o dilema central entre explorar novas possibilidades e aproveitar o que já se sabe, usando estratégias como…
- [Unidade 2 - 1. Métodos de Monte Carlo e TD Learning](paginas/02%20-%20Unidade%202%20-%201.%20M%C3%A9todos%20de%20Monte%20Carlo%20e%20TD%20Learning.md) — Nesta aula, vamos abordar os seguintes tópicos: - Dilema Exploração vs. Exploitação. - Método de Monte Carlo: aprendizagem a partir de episódios completos. - TD Learning: atualização incremental passo a passo. - Comparação conceitual Monte Carlo × TD (viés, variância, estabilidade) - Transição do Prediction → Control. - Identificar o dilema exploração vs. exploitação, selecionando estratégias adequadas para…
- [Unidade 2 - 2. Funções de Aproximação](paginas/03%20-%20Unidade%202%20-%202.%20Fun%C3%A7%C3%B5es%20de%20Aproxima%C3%A7%C3%A3o.md) — Nesta aula, vamos abordar os seguintes tópicos: - Limitações dos métodos tabulares em grandes espaços de estado. - Ideia central da Função de Aproximação (generalização). - Aproximação Linear e atualização por gradiente. - Aproximação para Q(s, a). - Generalização vs. Overfitting. - Reconhecer quando métodos tabulares se tornam inviáveis. - Reconhecer como funções de aproximação representam valores e reduzem a…
- [Unidade 2 - 3. Algoritmos Avançados](paginas/04%20-%20Unidade%202%20-%203.%20Algoritmos%20Avan%C3%A7ados.md) — Nesta aula, vamos abordar os seguintes tópicos: - SARSA: controle on-policy: aprendizado considerando exploração. - Q-Learning: controle off-policy: aprendizado voltado ao ótimo global. - Comparação direta: comportamento conservador (SARSA) vs. agressivo (Q-Learning). - Síntese geral Model-Based vs. Model-Free. - Distinguir algoritmos on-policy e off-policy, interpretando o papel da exploração no aprendizado. -…
- [Unidade 2 - 4. Multi-Agent Reinforcement Learning (MARL)](paginas/05%20-%20Unidade%202%20-%204.%20Multi-Agent%20Reinforcement%20Learning%20%28MARL%29.md) — Nesta aula, vamos abordar os seguintes tópicos: - Definição: múltiplos agentes aprendendo simultaneamente. - Problema da não estacionariedade. - Tipos de cenários: cooperativo, competitivo e misto. - Independent Q-Learning e suas limitações. - Paradigma CTDE (Centralized Training, Decentralized Execution). - Exemplos reais: tráfego, jogos, drones e mercados multiagentes.
- [Unidade 2 - Material Complementar](paginas/06%20-%20Unidade%202%20-%20Material%20Complementar.md) — Unidade 2 - Multi-Agent Reinforcement Learning.pptx GitHub – “Paper list of Multi-Agent Reinforcement Learning (MARL)”. Repositório público com listagem atualizada de artigos. Disponível em: <https://github.com/LantaoYu/MARL-Papers . Acesso em: 26 out. 2025. ICARL. Real-world Reinforcement Learning in Multi-Agent Systems Eugene Vinitsky. YouTube, 01 out. 2024. Disponível em:…

## Materiais

### Apresentações (8)

- [Unidade 2 - Comparação Geral.pptx](documentos/Unidade%202%20-%20Compara%C3%A7%C3%A3o%20Geral.pptx)
- [Unidade 2 - Exploracao vs Exploitação.pptx](documentos/Unidade%202%20-%20Exploracao%20vs%20Exploita%C3%A7%C3%A3o.pptx)
- [Unidade 2 - Funções de Aproximação.pptx](documentos/Unidade%202%20-%20Fun%C3%A7%C3%B5es%20de%20Aproxima%C3%A7%C3%A3o.pptx)
- [Unidade 2 - Monte Carlo.pptx](documentos/Unidade%202%20-%20Monte%20Carlo.pptx)
- [Unidade 2 - Multi-Agent Reinforcement Learning.pptx](documentos/Unidade%202%20-%20Multi-Agent%20Reinforcement%20Learning.pptx)
- [Unidade 2 - Q-Learning.pptx](documentos/Unidade%202%20-%20Q-Learning.pptx)
- [Unidade 2 - SARSA.pptx](documentos/Unidade%202%20-%20SARSA.pptx)
- [Unidade 2 - TD Learning.pptx](documentos/Unidade%202%20-%20TD%20Learning.pptx)

### Páginas e textos (6)

- [01 - Unidade 2 - Orientações de Estudo.md](paginas/01%20-%20Unidade%202%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md)
- [02 - Unidade 2 - 1. Métodos de Monte Carlo e TD Learning.md](paginas/02%20-%20Unidade%202%20-%201.%20M%C3%A9todos%20de%20Monte%20Carlo%20e%20TD%20Learning.md)
- [03 - Unidade 2 - 2. Funções de Aproximação.md](paginas/03%20-%20Unidade%202%20-%202.%20Fun%C3%A7%C3%B5es%20de%20Aproxima%C3%A7%C3%A3o.md)
- [04 - Unidade 2 - 3. Algoritmos Avançados.md](paginas/04%20-%20Unidade%202%20-%203.%20Algoritmos%20Avan%C3%A7ados.md)
- [05 - Unidade 2 - 4. Multi-Agent Reinforcement Learning (MARL).md](paginas/05%20-%20Unidade%202%20-%204.%20Multi-Agent%20Reinforcement%20Learning%20%28MARL%29.md)
- [06 - Unidade 2 - Material Complementar.md](paginas/06%20-%20Unidade%202%20-%20Material%20Complementar.md)

### Imagens (7)

- [banner-pos-2022-1.jpg](images/banner-pos-2022-1.jpg)
- [banner-pos-2022.jpg](images/banner-pos-2022.jpg)
- [icone-bussola.png](images/icone-bussola.png)
- [icone-coruja.png](images/icone-coruja.png)
- [Leitura (2).png](images/Leitura%20%282%29.png)
- [material-b.png](images/material-b.png)
- [Play (1).png](images/Play%20%281%29.png)

### HTML original (6)

- [01 - Unidade 2 - Orientações de Estudo.html](html/01%20-%20Unidade%202%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.html)
- [02 - Unidade 2 - 1. Métodos de Monte Carlo e TD Learning.html](html/02%20-%20Unidade%202%20-%201.%20M%C3%A9todos%20de%20Monte%20Carlo%20e%20TD%20Learning.html)
- [03 - Unidade 2 - 2. Funções de Aproximação.html](html/03%20-%20Unidade%202%20-%202.%20Fun%C3%A7%C3%B5es%20de%20Aproxima%C3%A7%C3%A3o.html)
- [04 - Unidade 2 - 3. Algoritmos Avançados.html](html/04%20-%20Unidade%202%20-%203.%20Algoritmos%20Avan%C3%A7ados.html)
- [05 - Unidade 2 - 4. Multi-Agent Reinforcement Learning (MARL).html](html/05%20-%20Unidade%202%20-%204.%20Multi-Agent%20Reinforcement%20Learning%20%28MARL%29.html)
- [06 - Unidade 2 - Material Complementar.html](html/06%20-%20Unidade%202%20-%20Material%20Complementar.html)

## Roteiro de estudo

1. Leia as páginas na ordem apresentada pelo módulo.
2. Consulte os PDFs e apresentações enquanto registra definições, hipóteses e exemplos.
3. Execute notebooks e códigos, verificando entradas, saídas e limitações.
4. Ao final, responda:

   - Como você explicaria **Unidade 2 - Orientações de Estudo** sem consultar o material?
   - Como você explicaria **Unidade 2 - 1. Métodos de Monte Carlo e TD Learning** sem consultar o material?
   - Como você explicaria **Unidade 2 - 2. Funções de Aproximação** sem consultar o material?
   - Como você explicaria **Unidade 2 - 3. Algoritmos Avançados** sem consultar o material?
   - Como você explicaria **Unidade 2 - 4. Multi-Agent Reinforcement Learning (MARL)** sem consultar o material?
