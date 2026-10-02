# Unidade 2 - 3. Algoritmos Avançados

- Origem: [Canvas](https://pucminas.instructure.com/courses/230807/pages/unidade-2-3-algoritmos-avancados)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar os seguintes tópicos:**

- SARSA: controle on-policy: aprendizado considerando exploração.
- Q-Learning: controle off-policy: aprendizado voltado ao ótimo global.
- Comparação direta: comportamento conservador (SARSA) vs. agressivo (Q-Learning).
- Síntese geral Model-Based vs. Model-Free.

**Ao final, você será capaz de:**

- Distinguir algoritmos on-policy e off-policy, interpretando o papel da exploração no aprendizado.
- Reconhecer os elementos essenciais dos algoritmos SARSA e Q-Learning, compreendendo suas diferenças na forma de atualização e política adotada.
- Analisar diferenças comportamentais entre políticas conservadoras e arrojadas.
- Relacionar métodos Model-Free com suas bases Model-Based para compreender cenários de uso.

---

#### **SARSA**

Na videoaula a seguir, você irá conhecer o algoritmo SARSA, um dos métodos fundamentais de aprendizado por reforço baseados em diferença temporal. A aula destaca a filosofia on-policy do SARSA, mostrando como o agente aprende a partir das ações que realmente executa, incluindo aquelas tomadas durante a exploração. Ao longo da explicação, você verá como o aprendizado acontece passo a passo, sem esperar o fim do episódio, e por que a exploração faz parte direta do processo de aprendizado.

Você também irá entender por que o SARSA tende a aprender políticas mais cautelosas e estáveis, sendo especialmente indicado para ambientes onde erros durante a exploração podem ser custosos ou perigosos. Quer compreender como aprender levando em conta o comportamento real do agente? Então, acompanhe o vídeo!

#### **Q-Learning**

No vídeo a seguir, você irá explorar o Q-Learning, um dos algoritmos mais populares e influentes do aprendizado por reforço. A aula explica como esse método adota uma abordagem off-policy, aprendendo como se o agente sempre tomasse a melhor ação possível no futuro, independentemente das escolhas exploratórias feitas durante o treinamento. Essa ideia simples, baseada no uso do valor máximo das ações futuras, é o que torna o Q-Learning tão poderoso.

Você também verá como o Q-Learning tende a aprender políticas mais agressivas e eficientes, sendo a base conceitual de muitos algoritmos modernos, como o Deep Q-Learning. Quer entender por que esse método se tornou referência no aprendizado por reforço? Então, dê o play e siga com a aula!

#### **Comparação Geral**

No vídeo a seguir, você irá consolidar tudo o que foi estudado até aqui por meio de uma comparação geral dos principais algoritmos de aprendizado por reforço. A aula organiza os métodos em grandes categorias, como *model-based* e *model-free*, *prediction* e *control*, ajudando você a construir um mapa mental que facilita entender de onde cada algoritmo surge e qual problema ele busca resolver.

Além disso, você irá comparar abordagens como Monte Carlo, TD Learning, SARSA e Q-Learning, compreendendo suas diferenças filosóficas, vantagens, limitações e cenários de aplicação. Pronto para enxergar o aprendizado por reforço como um conjunto organizado de ferramentas? Então, acompanhe o vídeo e feche esse ciclo com uma visão integrada do conteúdo!
