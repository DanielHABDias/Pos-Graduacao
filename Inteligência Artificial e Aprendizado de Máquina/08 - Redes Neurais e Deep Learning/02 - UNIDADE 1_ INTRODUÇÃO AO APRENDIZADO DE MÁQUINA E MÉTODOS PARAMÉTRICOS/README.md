# 02 - UNIDADE 1_ INTRODUÇÃO AO APRENDIZADO DE MÁQUINA E MÉTODOS PARAMÉTRICOS

[← Voltar à disciplina](../README.md)

## Resumo da unidade

A unidade introduz predição, funções de perda, Softmax e regularização. Treinar significa ajustar parâmetros para reduzir uma medida de erro em dados de treino sem perder capacidade de generalização.

### Exemplo

Em classificação de imagens, Softmax transforma escores em probabilidades que somam 1. A entropia cruzada penaliza baixa probabilidade atribuída à classe correta.

## Fórmulas essenciais

### Entropia cruzada

$$
L=-\sum_{k=1}^{K}y_k\log(\hat{p}_k)
$$

Penaliza probabilidade baixa atribuída à classe correta.


## Conteúdo da unidade

- [Unidade 1 - Orientações de Estudo](paginas/01%20-%20Unidade%201%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md) — INTRODUÇÃO AO APRENDIZADO DE MÁQUINA E MÉTODOS PARAMÉTRICOS Nessa unidade, será realizada uma introdução às redes neurais e à aprendizagem profunda, além de se apresentar um breve histórico sobre as redes neurais (profundas ou não). Além disso, será feita uma introdução a conceitos sobre visão computacional, uma vez que a aprendizagem profunda tem demonstrado bons resultados quando aplicada a diversas tarefas da…
- [Unidade 1 - 1. Introdução](paginas/03%20-%20Unidade%201%20-%201.%20Introdu%C3%A7%C3%A3o.md) — Nessa videoaula vai se realizar uma introdução à aprendizagem profunda. - Introduzir a aprendizagem profunda - Destacar alguns marcos relevantes relacionados à aprendizagem profunda, bem como mencionar críticas e riscos aos associados a ela
- [Unidade 1 - 2. Breve Histórico](paginas/04%20-%20Unidade%201%20-%202.%20Breve%20Hist%C3%B3rico.md) — Nessa videoaula vai se realizar um breve histórico sobre redes neurais e aprendizagem profunda. - Apresentar um breve histórico sobre redes neurais e aprendizagem profunda - Explorar a relacão entre IA, aprendizado de máquina, aprendizagem de representação e aprendizagem produnda - Destacar algumas razões para o sucesso da utilização de redes neurais e de abordagens profundas
- [Unidade 1 - 3. Visão Computacional - Introdução](paginas/05%20-%20Unidade%201%20-%203.%20Vis%C3%A3o%20Computacional%20-%20Introdu%C3%A7%C3%A3o.md) — Nessa videoaula vai se realizar uma breve introdução sobre a área de visão computacional. - Apresentar uma breve introdução à área de visão computacional - Descrever a evolução das abordagens da área de visão até a recente utilização de redes neurais profundas
- [Unidade 1 - 4. Visão Computacional - Classificação de Imagens](paginas/06%20-%20Unidade%201%20-%204.%20Vis%C3%A3o%20Computacional%20-%20Classifica%C3%A7%C3%A3o%20de%20Imagens.md) — Nessa videoaula vai se apresentar a tarefa de classificação de imagens como uma das mais relevantes na área de visão computacional. - Apresentar a tarefa de classificação de imagens como uma das mais relevantes na área de visão computacional - Descrever os principais desafios na resolução do problema de classificação de imagens - Comparar o uso de uma abordagem tradicional de IA à uma abordagem de aprendizado de…
- [Unidade 1 - 5. Visão Computacional - Classificador Simples](paginas/07%20-%20Unidade%201%20-%205.%20Vis%C3%A3o%20Computacional%20-%20Classificador%20Simples.md) — Nessa videoaula vai se apresentar um exemplo de classificador simples para a tarefa de classificação de imagens. - Apresentar um exemplo de classificador simples para a tarefa de classificação de imagens - Descrever detalhes sobre treinamento e predição relacionados ao um classificador baseado no vizinho mais próximo
- [Unidade 1 - 6. Aprendizado de Máquina - Introdução](paginas/08%20-%20Unidade%201%20-%206.%20Aprendizado%20de%20M%C3%A1quina%20-%20Introdu%C3%A7%C3%A3o.md) — Nessa videoaula vai se realizar uma breve introdução ao aprendizado de máquina e, em especial, ao aprendizado estatístico. - Apresentar uma breve introdução ao aprendizado de máquina - Descrever o aprendizado de máquina estatístico e sua aplicação em problemas de predição
- [Unidade 1 - 7. Aprendizado de Máquina - Função de Predição](paginas/09%20-%20Unidade%201%20-%207.%20Aprendizado%20de%20M%C3%A1quina%20-%20Fun%C3%A7%C3%A3o%20de%20Predi%C3%A7%C3%A3o.md) — Nessa videoaula vai se explorar o conceito de função de predição e sua utilização em uma abordagem paramétrica de aprendizado de máquina. - Apresentar o conceito de função de predição e seu uso em uma abordagem paramétrica de aprendizado de máquina - Explorar um exemplo de função de predição para um simples classificador linear - Discutir a interpretação dos resultados de predição de um simples classificador linear
- [Unidade 1 - 8. Aprendizado de Máquina - Função de Perda (I)](paginas/10%20-%20Unidade%201%20-%208.%20Aprendizado%20de%20M%C3%A1quina%20-%20Fun%C3%A7%C3%A3o%20de%20Perda%20%28I%29.md) — Nessa videoaula vai se explorar o conceito de função de perda e sua utilização para obtenção de um bom modelo de aprendizado de máquina. - Apresentar o conceito de função de perda e seu uso na obtenção de um bom modelo por meio da minimização do risco empírico - Explorar um exemplo com base na função de perda quadrática unidimensional
- [Unidade 1 - 9. Aprendizado de Máquina - Função de Perda (II)](paginas/11%20-%20Unidade%201%20-%209.%20Aprendizado%20de%20M%C3%A1quina%20-%20Fun%C3%A7%C3%A3o%20de%20Perda%20%28II%29.md) — Nessa videoaula vai se explorar o conceito de função de perda para dados multidimensionais, bem como examinar a função de perda de entropia cruzada (ou cross-entropy loss ). - Discutir o conceito de função de perda para dados multidimensionais - Explorar a função de perda de entropia cruzada (ou cross-entropy loss ) que é muito utilizada em redes neurais profundas
- [Unidade 1 - 10. Aprendizado de Máquina - Função de Perda (III)](paginas/12%20-%20Unidade%201%20-%2010.%20Aprendizado%20de%20M%C3%A1quina%20-%20Fun%C3%A7%C3%A3o%20de%20Perda%20%28III%29.md) — Nessa videoaula vai se explorar a função de perda de articulação (ou hinge loss ). - Explorar a função de perda de articulação (ou hinge loss ) muito usual em modelos de "margem máxima"
- [Unidade 1 - 11. Aprendizado de Máquina - Função Softmax & Regularização](paginas/13%20-%20Unidade%201%20-%2011.%20Aprendizado%20de%20M%C3%A1quina%20-%20Fun%C3%A7%C3%A3o%20Softmax%20%26%20Regulariza%C3%A7%C3%A3o.md) — Nessa videoaula vai se examinar a função softmax , bem como explorar o conceito de regularização. - Explorar a função softmax utilizada em redes neurais para obtenção de uma distribuição de probabilidades - Discutir o conceito de regularização
- [Unidade 1 - 12. Aprendizado de Máquina - Ajuste de Hiperparâmetros](paginas/14%20-%20Unidade%201%20-%2012.%20Aprendizado%20de%20M%C3%A1quina%20-%20Ajuste%20de%20Hiperpar%C3%A2metros.md) — Nessa videoaula vai se explorar o conceito de hiperparâmetros no aprendizado supervisionado, bem como examinar algumas estratégias para ajustes de hiperparâmetros de um modelo de aprendizado de máquina. - Discutir o conceito de hiperparâmetros no aprendizado supervisionado - Explorar algumas estratégias para ajuste de hiperparâmetros
- [Unidade 1 - Resolução da Atividade Prática](paginas/30%20-%20Unidade%201%20-%20Resolu%C3%A7%C3%A3o%20da%20Atividade%20Pr%C3%A1tica.md) — Nesse vídeo vai se discutir a resolução da Atividade Prática 1.

## Materiais

### PDFs (13)

- [01-cb-teoria-decisao.pdf](documentos/01-cb-teoria-decisao.pdf) (149 páginas)
- [Nota de aula - Unidade 1 - VIdeoaula 01.pdf](documentos/Nota%20de%20aula%20-%20Unidade%201%20-%20VIdeoaula%2001.pdf) (18 páginas)
- [Nota de aula - Unidade 1 - Videoaula 02.pdf](documentos/Nota%20de%20aula%20-%20Unidade%201%20-%20Videoaula%2002.pdf) (39 páginas)
- [Nota de aula - Unidade 1 - VIdeoaula 03.pdf](documentos/Nota%20de%20aula%20-%20Unidade%201%20-%20VIdeoaula%2003.pdf) (24 páginas)
- [Nota de aula - Unidade 1 - VIdeoaula 04.pdf](documentos/Nota%20de%20aula%20-%20Unidade%201%20-%20VIdeoaula%2004.pdf) (17 páginas)
- [Nota de aula - Unidade 1 - VIdeoaula 05.pdf](documentos/Nota%20de%20aula%20-%20Unidade%201%20-%20VIdeoaula%2005.pdf) (16 páginas)
- [Nota de aula - Unidade 1 - VIdeoaula 06.pdf](documentos/Nota%20de%20aula%20-%20Unidade%201%20-%20VIdeoaula%2006.pdf) (16 páginas)
- [Nota de aula - Unidade 1 - VIdeoaula 07.pdf](documentos/Nota%20de%20aula%20-%20Unidade%201%20-%20VIdeoaula%2007.pdf) (28 páginas)
- [Nota de aula - Unidade 1 - VIdeoaula 08.pdf](documentos/Nota%20de%20aula%20-%20Unidade%201%20-%20VIdeoaula%2008.pdf) (23 páginas)
- [Nota de aula - Unidade 1 - VIdeoaula 09.pdf](documentos/Nota%20de%20aula%20-%20Unidade%201%20-%20VIdeoaula%2009.pdf) (21 páginas)
- [Nota de aula - Unidade 1 - VIdeoaula 10.pdf](documentos/Nota%20de%20aula%20-%20Unidade%201%20-%20VIdeoaula%2010.pdf) (28 páginas)
- [Nota de aula - Unidade 1 - VIdeoaula 11.pdf](documentos/Nota%20de%20aula%20-%20Unidade%201%20-%20VIdeoaula%2011.pdf) (25 páginas)
- [Nota de aula - Unidade 1 - VIdeoaula 12.pdf](documentos/Nota%20de%20aula%20-%20Unidade%201%20-%20VIdeoaula%2012.pdf) (23 páginas)

### Páginas e textos (14)

- [01 - Unidade 1 - Orientações de Estudo.md](paginas/01%20-%20Unidade%201%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md)
- [03 - Unidade 1 - 1. Introdução.md](paginas/03%20-%20Unidade%201%20-%201.%20Introdu%C3%A7%C3%A3o.md)
- [04 - Unidade 1 - 2. Breve Histórico.md](paginas/04%20-%20Unidade%201%20-%202.%20Breve%20Hist%C3%B3rico.md)
- [05 - Unidade 1 - 3. Visão Computacional - Introdução.md](paginas/05%20-%20Unidade%201%20-%203.%20Vis%C3%A3o%20Computacional%20-%20Introdu%C3%A7%C3%A3o.md)
- [06 - Unidade 1 - 4. Visão Computacional - Classificação de Imagens.md](paginas/06%20-%20Unidade%201%20-%204.%20Vis%C3%A3o%20Computacional%20-%20Classifica%C3%A7%C3%A3o%20de%20Imagens.md)
- [07 - Unidade 1 - 5. Visão Computacional - Classificador Simples.md](paginas/07%20-%20Unidade%201%20-%205.%20Vis%C3%A3o%20Computacional%20-%20Classificador%20Simples.md)
- [08 - Unidade 1 - 6. Aprendizado de Máquina - Introdução.md](paginas/08%20-%20Unidade%201%20-%206.%20Aprendizado%20de%20M%C3%A1quina%20-%20Introdu%C3%A7%C3%A3o.md)
- [09 - Unidade 1 - 7. Aprendizado de Máquina - Função de Predição.md](paginas/09%20-%20Unidade%201%20-%207.%20Aprendizado%20de%20M%C3%A1quina%20-%20Fun%C3%A7%C3%A3o%20de%20Predi%C3%A7%C3%A3o.md)
- [10 - Unidade 1 - 8. Aprendizado de Máquina - Função de Perda (I).md](paginas/10%20-%20Unidade%201%20-%208.%20Aprendizado%20de%20M%C3%A1quina%20-%20Fun%C3%A7%C3%A3o%20de%20Perda%20%28I%29.md)
- [11 - Unidade 1 - 9. Aprendizado de Máquina - Função de Perda (II).md](paginas/11%20-%20Unidade%201%20-%209.%20Aprendizado%20de%20M%C3%A1quina%20-%20Fun%C3%A7%C3%A3o%20de%20Perda%20%28II%29.md)
- [12 - Unidade 1 - 10. Aprendizado de Máquina - Função de Perda (III).md](paginas/12%20-%20Unidade%201%20-%2010.%20Aprendizado%20de%20M%C3%A1quina%20-%20Fun%C3%A7%C3%A3o%20de%20Perda%20%28III%29.md)
- [13 - Unidade 1 - 11. Aprendizado de Máquina - Função Softmax & Regularização.md](paginas/13%20-%20Unidade%201%20-%2011.%20Aprendizado%20de%20M%C3%A1quina%20-%20Fun%C3%A7%C3%A3o%20Softmax%20%26%20Regulariza%C3%A7%C3%A3o.md)
- [14 - Unidade 1 - 12. Aprendizado de Máquina - Ajuste de Hiperparâmetros.md](paginas/14%20-%20Unidade%201%20-%2012.%20Aprendizado%20de%20M%C3%A1quina%20-%20Ajuste%20de%20Hiperpar%C3%A2metros.md)
- [30 - Unidade 1 - Resolução da Atividade Prática.md](paginas/30%20-%20Unidade%201%20-%20Resolu%C3%A7%C3%A3o%20da%20Atividade%20Pr%C3%A1tica.md)

### Imagens (1)

- [banner-pos-2022.jpg](images/banner-pos-2022.jpg)

### HTML original (14)

- [01 - Unidade 1 - Orientações de Estudo.html](html/01%20-%20Unidade%201%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.html)
- [03 - Unidade 1 - 1. Introdução.html](html/03%20-%20Unidade%201%20-%201.%20Introdu%C3%A7%C3%A3o.html)
- [04 - Unidade 1 - 2. Breve Histórico.html](html/04%20-%20Unidade%201%20-%202.%20Breve%20Hist%C3%B3rico.html)
- [05 - Unidade 1 - 3. Visão Computacional - Introdução.html](html/05%20-%20Unidade%201%20-%203.%20Vis%C3%A3o%20Computacional%20-%20Introdu%C3%A7%C3%A3o.html)
- [06 - Unidade 1 - 4. Visão Computacional - Classificação de Imagens.html](html/06%20-%20Unidade%201%20-%204.%20Vis%C3%A3o%20Computacional%20-%20Classifica%C3%A7%C3%A3o%20de%20Imagens.html)
- [07 - Unidade 1 - 5. Visão Computacional - Classificador Simples.html](html/07%20-%20Unidade%201%20-%205.%20Vis%C3%A3o%20Computacional%20-%20Classificador%20Simples.html)
- [08 - Unidade 1 - 6. Aprendizado de Máquina - Introdução.html](html/08%20-%20Unidade%201%20-%206.%20Aprendizado%20de%20M%C3%A1quina%20-%20Introdu%C3%A7%C3%A3o.html)
- [09 - Unidade 1 - 7. Aprendizado de Máquina - Função de Predição.html](html/09%20-%20Unidade%201%20-%207.%20Aprendizado%20de%20M%C3%A1quina%20-%20Fun%C3%A7%C3%A3o%20de%20Predi%C3%A7%C3%A3o.html)
- [10 - Unidade 1 - 8. Aprendizado de Máquina - Função de Perda (I).html](html/10%20-%20Unidade%201%20-%208.%20Aprendizado%20de%20M%C3%A1quina%20-%20Fun%C3%A7%C3%A3o%20de%20Perda%20%28I%29.html)
- [11 - Unidade 1 - 9. Aprendizado de Máquina - Função de Perda (II).html](html/11%20-%20Unidade%201%20-%209.%20Aprendizado%20de%20M%C3%A1quina%20-%20Fun%C3%A7%C3%A3o%20de%20Perda%20%28II%29.html)
- [12 - Unidade 1 - 10. Aprendizado de Máquina - Função de Perda (III).html](html/12%20-%20Unidade%201%20-%2010.%20Aprendizado%20de%20M%C3%A1quina%20-%20Fun%C3%A7%C3%A3o%20de%20Perda%20%28III%29.html)
- [13 - Unidade 1 - 11. Aprendizado de Máquina - Função Softmax & Regularização.html](html/13%20-%20Unidade%201%20-%2011.%20Aprendizado%20de%20M%C3%A1quina%20-%20Fun%C3%A7%C3%A3o%20Softmax%20%26%20Regulariza%C3%A7%C3%A3o.html)
- [14 - Unidade 1 - 12. Aprendizado de Máquina - Ajuste de Hiperparâmetros.html](html/14%20-%20Unidade%201%20-%2012.%20Aprendizado%20de%20M%C3%A1quina%20-%20Ajuste%20de%20Hiperpar%C3%A2metros.html)
- [30 - Unidade 1 - Resolução da Atividade Prática.html](html/30%20-%20Unidade%201%20-%20Resolu%C3%A7%C3%A3o%20da%20Atividade%20Pr%C3%A1tica.html)

## Roteiro de estudo

1. Leia as páginas na ordem apresentada pelo módulo.
2. Consulte os PDFs e apresentações enquanto registra definições, hipóteses e exemplos.
3. Execute notebooks e códigos, verificando entradas, saídas e limitações.
4. Ao final, responda:

   - Como você explicaria **Unidade 1 - Orientações de Estudo** sem consultar o material?
   - Como você explicaria **Unidade 1 - 1. Introdução** sem consultar o material?
   - Como você explicaria **Unidade 1 - 2. Breve Histórico** sem consultar o material?
   - Como você explicaria **Unidade 1 - 3. Visão Computacional - Introdução** sem consultar o material?
   - Como você explicaria **Unidade 1 - 4. Visão Computacional - Classificação de Imagens** sem consultar o material?
