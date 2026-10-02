# Unidade 2 - 1. Métodos de Monte Carlo e TD Learning

- Origem: [Canvas](https://pucminas.instructure.com/courses/230807/pages/unidade-2-1-metodos-de-monte-carlo-e-td-learning)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar os seguintes tópicos:**

- Dilema Exploração vs. Exploitação.
- Método de Monte Carlo: aprendizagem a partir de episódios completos.
- TD Learning: atualização incremental passo a passo.
- Comparação conceitual Monte Carlo × TD (viés, variância, estabilidade)
- Transição do Prediction → Control.

**Ao final, você será capaz de:**

- Identificar o dilema exploração vs. exploitação, selecionando estratégias adequadas para diferentes cenários.
- Diferenciar métodos de Monte Carlo e TD Learning, reconhecendo suas vantagens e limitações.
- Aplicar algoritmos de MC Prediction e TD(0) para estimar valores de estados em ambientes simples.
- Comparar a abordagem por retorno completo (MC) com a abordagem incremental (TD), reconhecendo o impacto na estabilidade e velocidade de aprendizado.

---

#### **Exploração vs. Exploitação**

No vídeo a seguir, você irá compreender um dos dilemas centrais do aprendizado por reforço: o equilíbrio entre explorar novas ações para aprender mais sobre o ambiente e explorar (explotar) aquilo que o agente já sabe que funciona melhor. A aula mostra por que esse dilema não é apenas um detalhe técnico, mas um problema estrutural da tomada de decisão sob incerteza, presente tanto em algoritmos quanto em decisões do cotidiano.

Além disso, você conhecerá as principais estratégias de exploração, como *epsilon-greedy*, *softmax* e *upper confidence bound (UCB)*, entendendo como cada uma lida com incerteza, desempenho e aprendizado ao longo do tempo. Quer descobrir como os agentes aprendem a decidir quando ser curiosos e quando ser eficientes? Então, acompanhe o vídeo!

#### **Monte Carlo**

No vídeo a seguir, você irá explorar os métodos de Monte Carlo, uma das abordagens mais clássicas e intuitivas do aprendizado por reforço. A aula apresenta a ideia de aprender a partir da experiência completa, explicando como o agente utiliza episódios inteiros e os retornos observados para estimar o valor dos estados, sem precisar de um modelo prévio do ambiente.

Você também verá como esses métodos funcionam especialmente bem em ambientes episódicos, como jogos, além da diferença entre *Monte Carlo Prediction* e *Monte Carlo Control*, destacando a importância da exploração para melhorar a política ao longo do tempo. Pronto(a) para entender como a experiência direta pode guiar o aprendizado por reforço? Então, dê o play e siga com a aula!

#### **TD Learning**

No vídeo a seguir, você irá conhecer o Temporal Difference Learning (TD Learning), um método central do aprendizado por reforço que transforma a forma como os agentes aprendem com a experiência. A aula apresenta a principal diferença em relação ao método de Monte Carlo: em vez de esperar o final de um episódio, o agente passa a aprender a cada passo, ajustando suas estimativas com base na diferença entre o que esperava acontecer e o que realmente observou, por meio do chamado erro TD.

Além disso, você irá entender como o uso do bootstrap permite que o aprendizado aconteça de forma contínua e online, tornando esse método especialmente adequado para ambientes contínuos e problemas do mundo real. Também será introduzida a extensão TD(λ), que equilibra aprendizado imediato e aprendizado baseado em trajetórias completas. Quer descobrir por que o TD Learning é a base dos algoritmos modernos de aprendizado por reforço? Então, acompanhe o vídeo!
