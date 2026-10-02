# Unidade 1 - 5. Treinamento e avaliação de RNNs

- Origem: [Canvas](https://pucminas.instructure.com/courses/230805/pages/unidade-1-5-treinamento-e-avaliacao-de-rnns)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar os seguintes tópicos:**

- Backpropagation Through Time (BPTT);
- Técnicas de regularização e otimização em RNNs;
- Avaliação de Modelos RNN.

**Ao final, você será capaz de:**

- Compreender estratégias de treinamento de RNNs;
- Compreender estratégias de avaliação de RNNs.

---

#### **Backpropagation Through Time - BPTT**

No vídeo a seguir, você irá compreender o funcionamento do algoritmo Backpropagation Through Time (BPTT) e sua importância no treinamento de redes neurais recorrentes. A aula apresenta o conceito de desdobramento da rede no tempo, explicando como os estados ocultos e as saídas são utilizados para calcular e propagar o erro ao longo da sequência, permitindo o aprendizado de dependências temporais.

Além disso, você irá conhecer os desafios associados ao BPTT, como o alto custo computacional e os problemas de explosão e desaparecimento dos gradientes, bem como estratégias para mitigá-los, como truncamento, clipping, regularização e o uso de arquiteturas mais robustas. Pronto para aprofundar esse tema fundamental? Então, siga para a videoaula e bons estudos!

#### **Regularização e Otimização**

No vídeo a seguir, você irá explorar as principais técnicas de regularização e otimização aplicadas às redes neurais recorrentes, compreendendo como essas estratégias ajudam a evitar o overfitting e a tornar o treinamento mais estável e eficiente. A aula aborda conceitos como dropout, penalização de pesos e inicialização adequada, destacando seu papel no controle da complexidade do modelo e na melhoria da generalização.

Você também irá conhecer os principais algoritmos de otimização, como SGD, RMSprop e Adam, analisando suas vantagens, limitações e contextos de aplicação, além de estratégias como validação cruzada, ajuste de taxa de aprendizado e busca de hiperparâmetros. Que tal entender como essas escolhas impactam diretamente o desempenho do modelo? Vamos em frente!

#### **Avaliação de RNN**

No vídeo a seguir, você irá compreender a importância da avaliação de redes neurais recorrentes e como esse processo contribui para garantir que o modelo aprenda padrões relevantes, evitando a simples memorização dos dados de treino. A aula apresenta os principais objetivos da avaliação, como a escolha da arquitetura mais adequada, a identificação de instabilidades no aprendizado e o ajuste fino de hiperparâmetros para melhorar a generalização e o desempenho do modelo.

Além disso, você irá conhecer as métricas mais utilizadas em tarefas de classificação, regressão e modelos de linguagem, entendendo quando usar acurácia, precisão, recall, F-score, erro médio, R² e perplexidade. Preparado para aprofundar sua análise sobre o desempenho de modelos sequenciais? Então, acompanhe a videoaula!
