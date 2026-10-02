# 02 - UNIDADE 1 - FUNDAMENTOS DO APRENDIZADO POR REFORÇO

[← Voltar à disciplina](../README.md)

## Resumo da unidade

A unidade formaliza agente, ambiente, estado, ação, recompensa e processo de decisão de Markov. A recompensa acumulada representa consequências imediatas e futuras.

### Exemplo

Em controle de estoque, o estado inclui nível atual e demanda observada. A ação decide reposição e a recompensa combina venda, falta e custo de armazenagem.

## Fórmulas essenciais

### Retorno descontado

$$
G_t=\sum_{k=0}^{\infty}\gamma^kR_{t+k+1}
$$

Combina recompensas futuras e reduz o peso das mais distantes.

### Equação de Bellman

$$
V^{\pi}(s)=\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)[r+\gamma V^{\pi}(s')]
$$

Decompõe o valor entre recompensa imediata e valor futuro.


## Conteúdo da unidade

- [Unidade 1 - Orientações de Estudo](paginas/01%20-%20Unidade%201%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md) — Nesta unidade, você vai conhecer os princípios que definem o Aprendizado por Reforço (Reinforcement Learning – RL) e compreender em que ele se diferencia de outros tipos de aprendizado de máquina. O estudo começa apresentando o contexto e as aplicações práticas desse campo, que já estão presentes em sistemas de jogos, robótica, veículos autônomos e em diversas soluções utilizadas no cotidiano. Em seguida, serão…
- [Unidade 1 - 1. Introdução ao Aprendizado por Reforço](paginas/02%20-%20Unidade%201%20-%201.%20Introdu%C3%A7%C3%A3o%20ao%20Aprendizado%20por%20Refor%C3%A7o.md) — Nesta aula, vamos abordar os seguintes tópicos: - Paradigmas de Machine Learning. - Definição de Aprendizado por Reforço. - Características principais do RL. - Casos reais de RL. - Impactos do RL em jogos. - indústria e mobilidade. - Lembrar os três paradigmas de aprendizado de máquina. - Compreender a definição de RL como problema de tomada de decisão sequencial. - Identificar as características que diferenciam o…
- [Unidade 1 - 2. Agente, Ambiente, Estados, Ações e Recompensas](paginas/03%20-%20Unidade%201%20-%202.%20Agente%2C%20Ambiente%2C%20Estados%2C%20A%C3%A7%C3%B5es%20e%20Recompensas.md) — Nesta aula, vamos abordar os seguintes tópicos: - Termos fundamentais: agente, ambiente, estado, observação, ação, recompensa, episódio. - Objetivo do agente: maximizar a recompensa acumulada. - Definir os principais termos do RL. - Diferenciar os conceitos de estado, observação, ação, recompensa e episódio em um problema de RL. - Identificar exemplos que representem corretamente os conceitos de agente, ambiente,…
- [Unidade 1 - 3. Processo de Decisão de Markov (MDP)](paginas/04%20-%20Unidade%201%20-%203.%20Processo%20de%20Decis%C3%A3o%20de%20Markov%20%28MDP%29.md) — Nesta aula, vamos abordar os seguintes tópicos: - Processos de Decisão de Markov. - Propriedade de Markov. - Formalização do problema de decisão sequencial – MDP. - Conceitos fundamentais para estratégia de tomada de decisão. - Estratégias de decisão adotadas por agentes em diferentes contextos de aprendizado. - O papel do tempo e da incerteza na avaliação de recompensas e resultados. - Desafios práticos do…
- [Unidade 1 - Material Complementar](paginas/05%20-%20Unidade%201%20-%20Material%20Complementar.md) — Unidade 1 - Definicoes do RL continuação.pptx ÁTILA IAMARINO. Precisamos falar sobre dopamina . YouTube, 30 set. 2025. Disponível em: <https://www.youtube.com/watch?v=8-nrgPRHOoY . Acesso em: 15 out. 2025. GOOGLE DEEPMIND. AlphaStar : The inside story. YouTube, 24 jan. 2019. Disponível em: <https://www.youtube.com/watch?v=UuhECwm31dM . Acesso em: 15 out. 2025.

## Materiais

### Apresentações (5)

- [Unidade 1 - Definicoes do RL continuação.pptx](documentos/Unidade%201%20-%20Definicoes%20do%20RL%20continua%C3%A7%C3%A3o.pptx)
- [Unidade 1 - Definicoes do RL.pptx](documentos/Unidade%201%20-%20Definicoes%20do%20RL.pptx)
- [Unidade 1 - Exemplos.pptx](documentos/Unidade%201%20-%20Exemplos.pptx)
- [Unidade 1 - Introdução ao RL.pptx](documentos/Unidade%201%20-%20Introdu%C3%A7%C3%A3o%20ao%20RL.pptx)
- [Unidade 1 - MDP.pptx](documentos/Unidade%201%20-%20MDP.pptx)

### Páginas e textos (5)

- [01 - Unidade 1 - Orientações de Estudo.md](paginas/01%20-%20Unidade%201%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md)
- [02 - Unidade 1 - 1. Introdução ao Aprendizado por Reforço.md](paginas/02%20-%20Unidade%201%20-%201.%20Introdu%C3%A7%C3%A3o%20ao%20Aprendizado%20por%20Refor%C3%A7o.md)
- [03 - Unidade 1 - 2. Agente, Ambiente, Estados, Ações e Recompensas.md](paginas/03%20-%20Unidade%201%20-%202.%20Agente%2C%20Ambiente%2C%20Estados%2C%20A%C3%A7%C3%B5es%20e%20Recompensas.md)
- [04 - Unidade 1 - 3. Processo de Decisão de Markov (MDP).md](paginas/04%20-%20Unidade%201%20-%203.%20Processo%20de%20Decis%C3%A3o%20de%20Markov%20%28MDP%29.md)
- [05 - Unidade 1 - Material Complementar.md](paginas/05%20-%20Unidade%201%20-%20Material%20Complementar.md)

### Imagens (6)

- [banner-pos-2022-1.jpg](images/banner-pos-2022-1.jpg)
- [banner-pos-2022.jpg](images/banner-pos-2022.jpg)
- [icone-bussola.png](images/icone-bussola.png)
- [Leitura (2).png](images/Leitura%20%282%29.png)
- [material-b.png](images/material-b.png)
- [Play (1).png](images/Play%20%281%29.png)

### HTML original (5)

- [01 - Unidade 1 - Orientações de Estudo.html](html/01%20-%20Unidade%201%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.html)
- [02 - Unidade 1 - 1. Introdução ao Aprendizado por Reforço.html](html/02%20-%20Unidade%201%20-%201.%20Introdu%C3%A7%C3%A3o%20ao%20Aprendizado%20por%20Refor%C3%A7o.html)
- [03 - Unidade 1 - 2. Agente, Ambiente, Estados, Ações e Recompensas.html](html/03%20-%20Unidade%201%20-%202.%20Agente%2C%20Ambiente%2C%20Estados%2C%20A%C3%A7%C3%B5es%20e%20Recompensas.html)
- [04 - Unidade 1 - 3. Processo de Decisão de Markov (MDP).html](html/04%20-%20Unidade%201%20-%203.%20Processo%20de%20Decis%C3%A3o%20de%20Markov%20%28MDP%29.html)
- [05 - Unidade 1 - Material Complementar.html](html/05%20-%20Unidade%201%20-%20Material%20Complementar.html)

## Roteiro de estudo

1. Leia as páginas na ordem apresentada pelo módulo.
2. Consulte os PDFs e apresentações enquanto registra definições, hipóteses e exemplos.
3. Execute notebooks e códigos, verificando entradas, saídas e limitações.
4. Ao final, responda:

   - Como você explicaria **Unidade 1 - Orientações de Estudo** sem consultar o material?
   - Como você explicaria **Unidade 1 - 1. Introdução ao Aprendizado por Reforço** sem consultar o material?
   - Como você explicaria **Unidade 1 - 2. Agente, Ambiente, Estados, Ações e Recompensas** sem consultar o material?
   - Como você explicaria **Unidade 1 - 3. Processo de Decisão de Markov (MDP)** sem consultar o material?
   - Como você explicaria **Unidade 1 - Material Complementar** sem consultar o material?
