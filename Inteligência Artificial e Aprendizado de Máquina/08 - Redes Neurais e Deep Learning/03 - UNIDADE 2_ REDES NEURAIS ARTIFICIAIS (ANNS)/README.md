# 03 - UNIDADE 2_ REDES NEURAIS ARTIFICIAIS (ANNS)

[← Voltar à disciplina](../README.md)

## Resumo da unidade

A unidade explica camadas, ativações, descida do gradiente e retropropagação. A regra da cadeia transporta o efeito do erro da saída até cada peso da rede.

### Exemplo

Se a taxa de aprendizado for alta, a otimização pode oscilar. Se for muito baixa, o treinamento avança devagar ou fica preso em uma região ruim.

## Fórmulas essenciais

### Atualização por gradiente

$$
\theta_{t+1}=\theta_t-\eta\nabla_{\theta}L(\theta_t)
$$

Move os parâmetros na direção que reduz a perda localmente.


## Conteúdo da unidade

- [Unidade 2 - Orientações de Estudo](paginas/01%20-%20Unidade%202%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md) — Nessa unidade, você será apresentado ao conteúdo necessário para compreender o funcionamento de redes neurais artificiais, bem como entender aspectos relevantes sobre a inspiração biológica por detrás delas. Em seguida, vai se examinar como a otimização da função de perda pode conduzir a obtenção de um bom modelo de rede neural, juntamente com uma descrição detalhada do método de gradiente e de uma de suas variações
- [Unidade 2 - 1. Redes Neurais Artificiais - Introdução](paginas/03%20-%20Unidade%202%20-%201.%20Redes%20Neurais%20Artificiais%20-%20Introdu%C3%A7%C3%A3o.md) — Nessa videoaula vai se realizar uma breve introdução sobre as redes neurais artificiais e aspectos relativos a inspiração biológica por detrás de seu funcionamento. - Apresentar uma breve introdução às redes neurais artificiais - Explorar aspectos sobre a inspiração biológica por detrás das redes neurais artificiais
- [Unidade 2 - 2. Redes Neurais Artificiais - Detalhes de Arquitetura & Histórico](paginas/04%20-%20Unidade%202%20-%202.%20Redes%20Neurais%20Artificiais%20-%20Detalhes%20de%20Arquitetura%20%26%20Hist%C3%B3rico.md) — Nessa videoaula vai se discutir detalhes sobre arquitetura de redes neurais artificiais e fatos relevantes de sua história. - Apresentar um detalhamento sobre arquitetura de redes neurais artificiais - Abordar alguns fatos relevantes da história das redes neurais artificiais
- [Unidade 2 - 3. Redes Neurais Artificiais - Otimização da Função de Perda](paginas/05%20-%20Unidade%202%20-%203.%20Redes%20Neurais%20Artificiais%20-%20Otimiza%C3%A7%C3%A3o%20da%20Fun%C3%A7%C3%A3o%20de%20Perda.md) — Nessa videoaula vai se discutir duas estratégias para a otimização da função de perda de uma rede neural artificial. - Discutir a otimização da função de perda como método para obtenção de um "bom" modelo de rede neural artificial - Abordar duas estratégias distintas para otimização da função de perda: (i) busca randômica; e (ii) uso de derivadas
- [Unidade 2 - 4. Redes Neurais Artificiais - Método do Gradiente](paginas/06%20-%20Unidade%202%20-%204.%20Redes%20Neurais%20Artificiais%20-%20M%C3%A9todo%20do%20Gradiente.md) — Nessa videoaula vai se apresentar o método do gradiente. - Apresentar o método do gradiente (ou método de descida mais íngreme)
- [Unidade 2 - 5. Redes Neurais Artificiais - Gradiente Descendente Estocástico (SGD)](paginas/07%20-%20Unidade%202%20-%205.%20Redes%20Neurais%20Artificiais%20-%20Gradiente%20Descendente%20Estoc%C3%A1stico%20%28SGD%29.md) — Nessa videoaula vai se apresentar o método do gradiente descendente estocástico (SGD - Stochastic gradient descent ). - Discutir algumas ressalvas sobre o método do gradiente - Apresentar o método do gradiente descendente estocástico ( SGD - Stochastic gradient descent )
- [Unidade 2 - 6. Redes Neurais Artificiais - Propagação Retrógrada (I)](paginas/08%20-%20Unidade%202%20-%206.%20Redes%20Neurais%20Artificiais%20-%20Propaga%C3%A7%C3%A3o%20Retr%C3%B3grada%20%28I%29.md) — Nessa videoaula vai se apresentar a propagação retrógrada (ou backpropagation ) como ferramenta para cálculo de gradiente em um grafo de computação. - Apresentar como a propagação retrógrada (ou backpropagation ) pode ser utilizada para cálculo de gradiente em um grafo de computação
- [Unidade 2 - 7. Redes Neurais Artificiais - Propagação Retrógrada (II)](paginas/09%20-%20Unidade%202%20-%207.%20Redes%20Neurais%20Artificiais%20-%20Propaga%C3%A7%C3%A3o%20Retr%C3%B3grada%20%28II%29.md) — Nessa videoaula vai se apresentar como explorar blocos funcionais durante a propagação retrógrada (ou backpropagation ), bem como os padrões existentes no fluxo de gradientes. - Apresentar como blocos funcionais podem ser explorados na propagação retrógrada (ou backpropagation ) para melhoria de performance - Abordar os padrões existentes no fluxo de gradientes durante a propagação retrógrada (ou backpropagation )
- [Unidade 2 - 8. Redes Neurais Artificiais - Propagação Retrógrada (III)](paginas/10%20-%20Unidade%202%20-%208.%20Redes%20Neurais%20Artificiais%20-%20Propaga%C3%A7%C3%A3o%20Retr%C3%B3grada%20%28III%29.md) — Nessa videoaula vai se apresentar detalhes sobre o cálculo de gradientes para dados multidimensionais, bem como alguns detalhes sobre implementação e construção de bibliotecas de componentes/camadas. - Apresentar detalhes sobre o cálculo de gradientes para dados multidimensionais - Abordar alguns detalhes sobre implementação e construção de bibliotecas de componentes/camadas
- [Unidade 2 - 9. Redes Neurais Artificiais - Função de Ativação](paginas/11%20-%20Unidade%202%20-%209.%20Redes%20Neurais%20Artificiais%20-%20Fun%C3%A7%C3%A3o%20de%20Ativa%C3%A7%C3%A3o.md) — Nessa videoaula vai se descrever o uso e funcionamento de uma função de ativação, além de apresentar detalhes sobre algumas das principais funções de ativação utilizadas em redes neurais artificiais. - Descrever o uso e funcionamento de uma função de ativação - Apresentar detalhes sobre algumas das principais funções de ativação utilizadas em redes neurais artificiais
- [Unidade 2 - 10. Redes Neurais Artificiais - Preparação de Dados & Inicialização](paginas/12%20-%20Unidade%202%20-%2010.%20Redes%20Neurais%20Artificiais%20-%20Prepara%C3%A7%C3%A3o%20de%20Dados%20%26%20Inicializa%C3%A7%C3%A3o.md) — Nessa videoaula vai se abordar a preparação de dados, além de apresentar estratégias para inicialização dos pesos utilizadas em redes neurais artificiais. - Abordar a preparação de dados a serem utilizados em uma rede neural artificial - Apresentar estratégias para inicialização dos pesos utilizadas em redes neurais artificiais
- [Unidade 2 - Resolução da Atividade Prática](paginas/26%20-%20Unidade%202%20-%20Resolu%C3%A7%C3%A3o%20da%20Atividade%20Pr%C3%A1tica.md) — Nesse vídeo vai se discutir a resolução da Atividade Prática 2. Material adicional sobre ajuste de hiperparâmetros usando busca randômica Artigo demonstrando superioridade da busca randômica sobre busca em grade - BERGSTRA, James; BENGIO, Yoshua. Random search for hyper-parameter optimization. The Journal of Machine Learning Research , v. 13, n. 1, p. 281-305, 2012.

## Materiais

### PDFs (10)

- [Nota de aula - Unidade 2 - Videoaula 01.pdf](documentos/Nota%20de%20aula%20-%20Unidade%202%20-%20Videoaula%2001.pdf) (35 páginas)
- [Nota de aula - Unidade 2 - Videoaula 02.pdf](documentos/Nota%20de%20aula%20-%20Unidade%202%20-%20Videoaula%2002.pdf) (24 páginas)
- [Nota de aula - Unidade 2 - Videoaula 03.pdf](documentos/Nota%20de%20aula%20-%20Unidade%202%20-%20Videoaula%2003.pdf) (27 páginas)
- [Nota de aula - Unidade 2 - Videoaula 04.pdf](documentos/Nota%20de%20aula%20-%20Unidade%202%20-%20Videoaula%2004.pdf) (16 páginas)
- [Nota de aula - Unidade 2 - Videoaula 05.pdf](documentos/Nota%20de%20aula%20-%20Unidade%202%20-%20Videoaula%2005.pdf) (29 páginas)
- [Nota de aula - Unidade 2 - Videoaula 06.pdf](documentos/Nota%20de%20aula%20-%20Unidade%202%20-%20Videoaula%2006.pdf) (40 páginas)
- [Nota de aula - Unidade 2 - Videoaula 07.pdf](documentos/Nota%20de%20aula%20-%20Unidade%202%20-%20Videoaula%2007.pdf) (30 páginas)
- [Nota de aula - Unidade 2 - Videoaula 08.pdf](documentos/Nota%20de%20aula%20-%20Unidade%202%20-%20Videoaula%2008.pdf) (22 páginas)
- [Nota de aula - Unidade 2 - Videoaula 09.pdf](documentos/Nota%20de%20aula%20-%20Unidade%202%20-%20Videoaula%2009.pdf) (38 páginas)
- [Nota de aula - Unidade 2 - Videoaula 10.pdf](documentos/Nota%20de%20aula%20-%20Unidade%202%20-%20Videoaula%2010.pdf) (15 páginas)

### Páginas e textos (12)

- [01 - Unidade 2 - Orientações de Estudo.md](paginas/01%20-%20Unidade%202%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md)
- [03 - Unidade 2 - 1. Redes Neurais Artificiais - Introdução.md](paginas/03%20-%20Unidade%202%20-%201.%20Redes%20Neurais%20Artificiais%20-%20Introdu%C3%A7%C3%A3o.md)
- [04 - Unidade 2 - 2. Redes Neurais Artificiais - Detalhes de Arquitetura & Histórico.md](paginas/04%20-%20Unidade%202%20-%202.%20Redes%20Neurais%20Artificiais%20-%20Detalhes%20de%20Arquitetura%20%26%20Hist%C3%B3rico.md)
- [05 - Unidade 2 - 3. Redes Neurais Artificiais - Otimização da Função de Perda.md](paginas/05%20-%20Unidade%202%20-%203.%20Redes%20Neurais%20Artificiais%20-%20Otimiza%C3%A7%C3%A3o%20da%20Fun%C3%A7%C3%A3o%20de%20Perda.md)
- [06 - Unidade 2 - 4. Redes Neurais Artificiais - Método do Gradiente.md](paginas/06%20-%20Unidade%202%20-%204.%20Redes%20Neurais%20Artificiais%20-%20M%C3%A9todo%20do%20Gradiente.md)
- [07 - Unidade 2 - 5. Redes Neurais Artificiais - Gradiente Descendente Estocástico (SGD).md](paginas/07%20-%20Unidade%202%20-%205.%20Redes%20Neurais%20Artificiais%20-%20Gradiente%20Descendente%20Estoc%C3%A1stico%20%28SGD%29.md)
- [08 - Unidade 2 - 6. Redes Neurais Artificiais - Propagação Retrógrada (I).md](paginas/08%20-%20Unidade%202%20-%206.%20Redes%20Neurais%20Artificiais%20-%20Propaga%C3%A7%C3%A3o%20Retr%C3%B3grada%20%28I%29.md)
- [09 - Unidade 2 - 7. Redes Neurais Artificiais - Propagação Retrógrada (II).md](paginas/09%20-%20Unidade%202%20-%207.%20Redes%20Neurais%20Artificiais%20-%20Propaga%C3%A7%C3%A3o%20Retr%C3%B3grada%20%28II%29.md)
- [10 - Unidade 2 - 8. Redes Neurais Artificiais - Propagação Retrógrada (III).md](paginas/10%20-%20Unidade%202%20-%208.%20Redes%20Neurais%20Artificiais%20-%20Propaga%C3%A7%C3%A3o%20Retr%C3%B3grada%20%28III%29.md)
- [11 - Unidade 2 - 9. Redes Neurais Artificiais - Função de Ativação.md](paginas/11%20-%20Unidade%202%20-%209.%20Redes%20Neurais%20Artificiais%20-%20Fun%C3%A7%C3%A3o%20de%20Ativa%C3%A7%C3%A3o.md)
- [12 - Unidade 2 - 10. Redes Neurais Artificiais - Preparação de Dados & Inicialização.md](paginas/12%20-%20Unidade%202%20-%2010.%20Redes%20Neurais%20Artificiais%20-%20Prepara%C3%A7%C3%A3o%20de%20Dados%20%26%20Inicializa%C3%A7%C3%A3o.md)
- [26 - Unidade 2 - Resolução da Atividade Prática.md](paginas/26%20-%20Unidade%202%20-%20Resolu%C3%A7%C3%A3o%20da%20Atividade%20Pr%C3%A1tica.md)

### Imagens (1)

- [banner-pos-2022.jpg](images/banner-pos-2022.jpg)

### HTML original (12)

- [01 - Unidade 2 - Orientações de Estudo.html](html/01%20-%20Unidade%202%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.html)
- [03 - Unidade 2 - 1. Redes Neurais Artificiais - Introdução.html](html/03%20-%20Unidade%202%20-%201.%20Redes%20Neurais%20Artificiais%20-%20Introdu%C3%A7%C3%A3o.html)
- [04 - Unidade 2 - 2. Redes Neurais Artificiais - Detalhes de Arquitetura & Histórico.html](html/04%20-%20Unidade%202%20-%202.%20Redes%20Neurais%20Artificiais%20-%20Detalhes%20de%20Arquitetura%20%26%20Hist%C3%B3rico.html)
- [05 - Unidade 2 - 3. Redes Neurais Artificiais - Otimização da Função de Perda.html](html/05%20-%20Unidade%202%20-%203.%20Redes%20Neurais%20Artificiais%20-%20Otimiza%C3%A7%C3%A3o%20da%20Fun%C3%A7%C3%A3o%20de%20Perda.html)
- [06 - Unidade 2 - 4. Redes Neurais Artificiais - Método do Gradiente.html](html/06%20-%20Unidade%202%20-%204.%20Redes%20Neurais%20Artificiais%20-%20M%C3%A9todo%20do%20Gradiente.html)
- [07 - Unidade 2 - 5. Redes Neurais Artificiais - Gradiente Descendente Estocástico (SGD).html](html/07%20-%20Unidade%202%20-%205.%20Redes%20Neurais%20Artificiais%20-%20Gradiente%20Descendente%20Estoc%C3%A1stico%20%28SGD%29.html)
- [08 - Unidade 2 - 6. Redes Neurais Artificiais - Propagação Retrógrada (I).html](html/08%20-%20Unidade%202%20-%206.%20Redes%20Neurais%20Artificiais%20-%20Propaga%C3%A7%C3%A3o%20Retr%C3%B3grada%20%28I%29.html)
- [09 - Unidade 2 - 7. Redes Neurais Artificiais - Propagação Retrógrada (II).html](html/09%20-%20Unidade%202%20-%207.%20Redes%20Neurais%20Artificiais%20-%20Propaga%C3%A7%C3%A3o%20Retr%C3%B3grada%20%28II%29.html)
- [10 - Unidade 2 - 8. Redes Neurais Artificiais - Propagação Retrógrada (III).html](html/10%20-%20Unidade%202%20-%208.%20Redes%20Neurais%20Artificiais%20-%20Propaga%C3%A7%C3%A3o%20Retr%C3%B3grada%20%28III%29.html)
- [11 - Unidade 2 - 9. Redes Neurais Artificiais - Função de Ativação.html](html/11%20-%20Unidade%202%20-%209.%20Redes%20Neurais%20Artificiais%20-%20Fun%C3%A7%C3%A3o%20de%20Ativa%C3%A7%C3%A3o.html)
- [12 - Unidade 2 - 10. Redes Neurais Artificiais - Preparação de Dados & Inicialização.html](html/12%20-%20Unidade%202%20-%2010.%20Redes%20Neurais%20Artificiais%20-%20Prepara%C3%A7%C3%A3o%20de%20Dados%20%26%20Inicializa%C3%A7%C3%A3o.html)
- [26 - Unidade 2 - Resolução da Atividade Prática.html](html/26%20-%20Unidade%202%20-%20Resolu%C3%A7%C3%A3o%20da%20Atividade%20Pr%C3%A1tica.html)

## Roteiro de estudo

1. Leia as páginas na ordem apresentada pelo módulo.
2. Consulte os PDFs e apresentações enquanto registra definições, hipóteses e exemplos.
3. Execute notebooks e códigos, verificando entradas, saídas e limitações.
4. Ao final, responda:

   - Como você explicaria **Unidade 2 - Orientações de Estudo** sem consultar o material?
   - Como você explicaria **Unidade 2 - 1. Redes Neurais Artificiais - Introdução** sem consultar o material?
   - Como você explicaria **Unidade 2 - 2. Redes Neurais Artificiais - Detalhes de Arquitetura & Histórico** sem consultar o material?
   - Como você explicaria **Unidade 2 - 3. Redes Neurais Artificiais - Otimização da Função de Perda** sem consultar o material?
   - Como você explicaria **Unidade 2 - 4. Redes Neurais Artificiais - Método do Gradiente** sem consultar o material?
