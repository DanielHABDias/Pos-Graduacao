# Unidade 2 - Orientações de Estudo

- Origem: [Canvas](https://pucminas.instructure.com/courses/230807/pages/unidade-2-orientacoes-de-estudo)

![](../images/banner-pos-2022.jpg)

**ALGORITMOS CLÁSSICOS E AVANÇOS EM APRENDIZADO POR REFORÇO**

Nesta unidade, exploraremos alguns dos algoritmos mais importantes e influentes do Aprendizado por Reforço, entendendo como agentes podem aprender a tomar decisões em ambientes dinâmicos, incertos e muitas vezes complexos. Vamos começar revisitando o dilema central entre explorar novas possibilidades e aproveitar o que já se sabe, usando estratégias como ε-greedy, Softmax e UCB para equilibrar essas escolhas. Em seguida, avançaremos para dois pilares fundamentais da estimativa de valor: os métodos de Monte Carlo, que aprendem a partir de episódios completos, e o TD Learning, que aprende de forma incremental a cada passo. Essa comparação é essencial para entendermos quando priorizar velocidade, precisão ou estabilidade no aprendizado.

Na sequência, estudaremos como lidar com ambientes de alta dimensionalidade por meio de Funções de Aproximação, saindo da representação tabular para modelos capazes de generalizar, incluindo aproximação linear e, futuramente, redes neurais como no DQN. Depois, investigaremos mais a fundo os algoritmos de controle SARSA (on-policy) e Q-Learning (off-policy), compreendendo como eles influenciam o comportamento final do agente — seja mais conservador ou mais agressivo na busca pelo ótimo. Finalizaremos conhecendo o universo de Multi-Agent Reinforcement Learning (MARL), no qual vários agentes aprendem simultaneamente, exigindo coordenação, comunicação e adaptação constante.

A unidade está organizada de forma progressiva, partindo de conceitos mais intuitivos para aplicações mais complexas. Ao final, você será capaz de comparar algoritmos, selecionar abordagens adequadas para diferentes contextos, aplicar funções de aproximação para generalização e compreender os desafios de ambientes multiagente. Detalhadamente, os objetivos específicos desta unidade são:

- Identificar o dilema exploração vs. exploitação, selecionando estratégias adequadas para diferentes cenários.
- Diferenciar métodos de Monte Carlo e TD Learning, reconhecendo suas vantagens e limitações.
- Aplicar algoritmos de MC Prediction e TD(0) para estimar valores de estados em ambientes simples.
- Comparar a abordagem por retorno completo (MC) com a abordagem incremental (TD), reconhecendo o impacto na estabilidade e velocidade de aprendizado.
- Reconhecer quando métodos tabulares se tornam inviáveis.
- Reconhecer como funções de aproximação representam valores e reduzem a dimensionalidade em espaços grandes.
- Compreender o processo de atualização por gradiente em um modelo linear simples, reconhecendo seus impactos na estabilidade do aprendizado.
- Distinguir algoritmos on-policy e off-policy, interpretando o papel da exploração no aprendizado.
- Reconhecer os elementos essenciais dos algoritmos SARSA e Q-Learning, compreendendo suas diferenças na forma de atualização e política adotada.
- Analisar diferenças comportamentais entre políticas conservadoras e arrojadas.
- Relacionar métodos Model-Free com suas bases Model-Based para compreender cenários de uso.
- Reconhecer como o aprendizado multiagente difere do agente único.
- Identificar os desafios de coordenação, comunicação e competição em cenários multiagente.
- Compreender o paradigma CTDE e sua importância para a estabilidade e eficiência do aprendizado em sistemas multiagente.
- Relacionar MARL com aplicações reais em cenários cooperativos e competitivos.

O objetivo é que você desenvolva um olhar crítico e fundamentado, capaz de entender não apenas como os algoritmos funcionam, mas por que e quando utilizá-los. Prepare-se para conectar teoria, prática e intuição de maneira integrada — essa unidade é um passo essencial para se tornar um profissional capaz de aplicar RL com eficiência e clareza em problemas reais.

Não se esqueça de acessar os materiais complementares e de realizar a atividade avaliativa.

---

**Temáticas da Unidade 2**

- Métodos de Monte Carlo e TD Learning.
- Funções de Aproximação.
- Algoritmos Avançados.
- Multi-Agent Reinforcement Learning (MARL).

---
