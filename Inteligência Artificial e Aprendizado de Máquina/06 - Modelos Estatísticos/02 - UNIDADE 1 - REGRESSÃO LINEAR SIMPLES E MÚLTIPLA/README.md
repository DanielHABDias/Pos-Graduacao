# 02 - UNIDADE 1 - REGRESSÃO LINEAR SIMPLES E MÚLTIPLA

[← Voltar à disciplina](../README.md)

## Resumo da unidade

A unidade modela uma variável quantitativa com regressão linear simples e múltipla. A interpretação depende dos coeficientes e da análise dos resíduos, não apenas do valor de R².

### Exemplo

Em um modelo de preço por área e idade, o coeficiente da área representa a variação média esperada no preço ao aumentar uma unidade de área, mantendo a idade constante.

## Fórmulas essenciais

### Regressão linear múltipla

$$
Y_i=\beta_0+\beta_1X_{i1}+\cdots+\beta_pX_{ip}+\varepsilon_i
$$

Relaciona a resposta a vários preditores.

### Coeficiente de determinação

$$
R^2=1-\frac{\sum_i(y_i-\hat{y}_i)^2}{\sum_i(y_i-\bar{y})^2}
$$

Compara o erro do modelo com a variação total da resposta.


## Conteúdo da unidade

- [Unidade 1 - Orientações de Estudo](paginas/01%20-%20Unidade%201%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md) — Bem-vindo à Unidade sobre Regressão Linear Simples e Múltipla! Nesta seção do seu curso, mergulharemos no fascinante mundo da análise de regressão. A regressão linear é uma ferramenta poderosa para modelar e entender a relação entre duas ou mais variáveis, permitindo prever ou explicar o comportamento de uma com base na outra. 1. Fundamentos da regressão linear: equação da reta de regressão, método dos mínimos…
- [Unidade 1 - 1. Modelos Estatísticos](paginas/02%20-%20Unidade%201%20-%201.%20Modelos%20Estat%C3%ADsticos.md)
- [Unidade 1 - 2. Fundamentos para modelos de regressão linear](paginas/03%20-%20Unidade%201%20-%202.%20Fundamentos%20para%20modelos%20de%20regress%C3%A3o%20linear.md)
- [Unidade 1 - 2.1 Medidas de Associação com R](paginas/04%20-%20Unidade%201%20-%202.1%20Medidas%20de%20Associa%C3%A7%C3%A3o%20com%20R.md)
- [Unidade 1 - 2.2 Medidas de Associação com Python](paginas/05%20-%20Unidade%201%20-%202.2%20Medidas%20de%20Associa%C3%A7%C3%A3o%20com%20Python.md)
- [Unidade 1 - 3. Regressão linear](paginas/06%20-%20Unidade%201%20-%203.%20Regress%C3%A3o%20linear.md)
- [Unidade 1 - 4. Estimativa de coeficientes de regressão linear simples](paginas/07%20-%20Unidade%201%20-%204.%20Estimativa%20de%20coeficientes%20de%20regress%C3%A3o%20linear%20simples.md)
- [Unidade 1 - 5. Premissas de Regressão linear simples](paginas/08%20-%20Unidade%201%20-%205.%20Premissas%20de%20Regress%C3%A3o%20linear%20simples.md)
- [Unidade 1 - 6. Regressão linear múltipla](paginas/09%20-%20Unidade%201%20-%206.%20Regress%C3%A3o%20linear%20m%C3%BAltipla.md)
- [Unidade 1 - 7. Premissas da Regressão linear múltipla](paginas/10%20-%20Unidade%201%20-%207.%20Premissas%20da%20Regress%C3%A3o%20linear%20m%C3%BAltipla.md)
- [Unidade 1 - 8. Regressão Linear múltipla com Python](paginas/11%20-%20Unidade%201%20-%208.%20Regress%C3%A3o%20Linear%20m%C3%BAltipla%20com%20Python.md)
- [Unidade 1 - 9. Comparação de modelos da Regressão linear múltipla](paginas/12%20-%20Unidade%201%20-%209.%20Compara%C3%A7%C3%A3o%20de%20modelos%20da%20Regress%C3%A3o%20linear%20m%C3%BAltipla.md)
- [Unidade 1 - 10. Comparação de modelos de Regressão linear com Python](paginas/13%20-%20Unidade%201%20-%2010.%20Compara%C3%A7%C3%A3o%20de%20modelos%20de%20Regress%C3%A3o%20linear%20com%20Python.md)
- [Unidade 1 - 11. Comparação de modelos - Atividade - com Python](paginas/14%20-%20Unidade%201%20-%2011.%20Compara%C3%A7%C3%A3o%20de%20modelos%20-%20Atividade%20-%20com%20Python.md)
- [Unidade 1 - 12. Transformação de variáveis](paginas/15%20-%20Unidade%201%20-%2012.%20Transforma%C3%A7%C3%A3o%20de%20vari%C3%A1veis.md)
- [Unidade 1 - 12.1 Transformação de variáveis com Python](paginas/16%20-%20Unidade%201%20-%2012.1%20Transforma%C3%A7%C3%A3o%20de%20vari%C3%A1veis%20com%20Python.md)
- [Unidade 1 - 12.2 Transformação de variáveis com R](paginas/17%20-%20Unidade%201%20-%2012.2%20Transforma%C3%A7%C3%A3o%20de%20vari%C3%A1veis%20com%20R.md)
- [Unidade 1 - 13.1 Seleção de variáveis - Stepwise](paginas/18%20-%20Unidade%201%20-%2013.1%20Sele%C3%A7%C3%A3o%20de%20vari%C3%A1veis%20-%20Stepwise.md)
- [Unidade 1 - 13.2 Seleção de variáveis - Lasso](paginas/19%20-%20Unidade%201%20-%2013.2%20Sele%C3%A7%C3%A3o%20de%20vari%C3%A1veis%20-%20Lasso.md)
- [Unidade 1 - 13.1 Seleção de variáveis com Python](paginas/20%20-%20Unidade%201%20-%2013.1%20Sele%C3%A7%C3%A3o%20de%20vari%C3%A1veis%20com%20Python.md)
- [Unidade 1 - 13.2 Seleção de variáveis com R](paginas/21%20-%20Unidade%201%20-%2013.2%20Sele%C3%A7%C3%A3o%20de%20vari%C3%A1veis%20com%20R.md)
- [Unidade 1 - Material Complementar](paginas/22%20-%20Unidade%201%20-%20Material%20Complementar.md) — 04 - Estimacao dos parametros da regressao linear simples.pdf 05 - Premissas da Regressao linear simples.pdf 5.2 - Python - Regressão Linear Simples Propaganda.ipynb 07 - Premissas da Regressão linear mútipla.pdf 08 - Comparação de modelos - regressão linear mútipla.pdf 09.2 - Python - Transformação de variáveis com Pyhton.ipynb

## Materiais

### PDFs (9)

- [01 - Modelos estatísticos.pdf](documentos/01%20-%20Modelos%20estat%C3%ADsticos.pdf) (9 páginas)
- [02 - Fundamentos de regressao.pdf](documentos/02%20-%20Fundamentos%20de%20regressao.pdf) (17 páginas)
- [03- Regressao Linear.pdf](documentos/03-%20Regressao%20Linear.pdf) (12 páginas)
- [04 - Estimacao dos parametros da regressao linear simples.pdf](documentos/04%20-%20Estimacao%20dos%20parametros%20da%20regressao%20linear%20simples.pdf) (14 páginas)
- [05 - Premissas da Regressao linear simples.pdf](documentos/05%20-%20Premissas%20da%20Regressao%20linear%20simples.pdf) (19 páginas)
- [06 - Regressao linear multipla.pdf](documentos/06%20-%20Regressao%20linear%20multipla.pdf) (9 páginas)
- [07 - Premissas da Regressão linear mútipla.pdf](documentos/07%20-%20Premissas%20da%20Regress%C3%A3o%20linear%20m%C3%BAtipla.pdf) (17 páginas)
- [08 - Comparação de modelos - regressão linear mútipla.pdf](documentos/08%20-%20Compara%C3%A7%C3%A3o%20de%20modelos%20-%20regress%C3%A3o%20linear%20m%C3%BAtipla.pdf) (14 páginas)
- [09 - transformação de variáveis.pdf](documentos/09%20-%20transforma%C3%A7%C3%A3o%20de%20vari%C3%A1veis.pdf) (17 páginas)

### Notebooks (6)

- [Aula_2_comparacao_de_modelos.ipynb](documentos/Aula_2_comparacao_de_modelos.ipynb)
- [Aula_2_regressao_linear_multipla.ipynb](documentos/Aula_2_regressao_linear_multipla.ipynb)
- [Medidas_correlacao.ipynb](documentos/Medidas_correlacao.ipynb)
- [regressao_linear_simples_propaganda.ipynb](documentos/regressao_linear_simples_propaganda.ipynb)
- [Selecao_variaveis.ipynb](documentos/Selecao_variaveis.ipynb)
- [Transformação de variáveis com Pyhton.ipynb](documentos/Transforma%C3%A7%C3%A3o%20de%20vari%C3%A1veis%20com%20Pyhton.ipynb)

### Código e configuração (2)

- [Selecao de variaveis com R.Rmd](documentos/Selecao%20de%20variaveis%20com%20R.Rmd)
- [transformação de variáveis com R.Rmd](documentos/transforma%C3%A7%C3%A3o%20de%20vari%C3%A1veis%20com%20R.Rmd)

### Dados e artefatos (5)

- [adult.data.csv](documentos/adult.data.csv)
- [Consumo_cerveja_1.csv](documentos/Consumo_cerveja_1.csv)
- [diabetes_dataset.xlsx](documentos/diabetes_dataset.xlsx)
- [enem_tratado.csv](documentos/enem_tratado.csv)
- [propaganda.csv](documentos/propaganda.csv)

### Páginas e textos (22)

- [01 - Unidade 1 - Orientações de Estudo.md](paginas/01%20-%20Unidade%201%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md)
- [02 - Unidade 1 - 1. Modelos Estatísticos.md](paginas/02%20-%20Unidade%201%20-%201.%20Modelos%20Estat%C3%ADsticos.md)
- [03 - Unidade 1 - 2. Fundamentos para modelos de regressão linear.md](paginas/03%20-%20Unidade%201%20-%202.%20Fundamentos%20para%20modelos%20de%20regress%C3%A3o%20linear.md)
- [04 - Unidade 1 - 2.1 Medidas de Associação com R.md](paginas/04%20-%20Unidade%201%20-%202.1%20Medidas%20de%20Associa%C3%A7%C3%A3o%20com%20R.md)
- [05 - Unidade 1 - 2.2 Medidas de Associação com Python.md](paginas/05%20-%20Unidade%201%20-%202.2%20Medidas%20de%20Associa%C3%A7%C3%A3o%20com%20Python.md)
- [06 - Unidade 1 - 3. Regressão linear.md](paginas/06%20-%20Unidade%201%20-%203.%20Regress%C3%A3o%20linear.md)
- [07 - Unidade 1 - 4. Estimativa de coeficientes de regressão linear simples.md](paginas/07%20-%20Unidade%201%20-%204.%20Estimativa%20de%20coeficientes%20de%20regress%C3%A3o%20linear%20simples.md)
- [08 - Unidade 1 - 5. Premissas de Regressão linear simples.md](paginas/08%20-%20Unidade%201%20-%205.%20Premissas%20de%20Regress%C3%A3o%20linear%20simples.md)
- [09 - Unidade 1 - 6. Regressão linear múltipla.md](paginas/09%20-%20Unidade%201%20-%206.%20Regress%C3%A3o%20linear%20m%C3%BAltipla.md)
- [10 - Unidade 1 - 7. Premissas da Regressão linear múltipla.md](paginas/10%20-%20Unidade%201%20-%207.%20Premissas%20da%20Regress%C3%A3o%20linear%20m%C3%BAltipla.md)
- [11 - Unidade 1 - 8. Regressão Linear múltipla com Python.md](paginas/11%20-%20Unidade%201%20-%208.%20Regress%C3%A3o%20Linear%20m%C3%BAltipla%20com%20Python.md)
- [12 - Unidade 1 - 9. Comparação de modelos da Regressão linear múltipla.md](paginas/12%20-%20Unidade%201%20-%209.%20Compara%C3%A7%C3%A3o%20de%20modelos%20da%20Regress%C3%A3o%20linear%20m%C3%BAltipla.md)
- [13 - Unidade 1 - 10. Comparação de modelos de Regressão linear com Python.md](paginas/13%20-%20Unidade%201%20-%2010.%20Compara%C3%A7%C3%A3o%20de%20modelos%20de%20Regress%C3%A3o%20linear%20com%20Python.md)
- [14 - Unidade 1 - 11. Comparação de modelos - Atividade - com Python.md](paginas/14%20-%20Unidade%201%20-%2011.%20Compara%C3%A7%C3%A3o%20de%20modelos%20-%20Atividade%20-%20com%20Python.md)
- [15 - Unidade 1 - 12. Transformação de variáveis.md](paginas/15%20-%20Unidade%201%20-%2012.%20Transforma%C3%A7%C3%A3o%20de%20vari%C3%A1veis.md)
- [16 - Unidade 1 - 12.1 Transformação de variáveis com Python.md](paginas/16%20-%20Unidade%201%20-%2012.1%20Transforma%C3%A7%C3%A3o%20de%20vari%C3%A1veis%20com%20Python.md)
- [17 - Unidade 1 - 12.2 Transformação de variáveis com R.md](paginas/17%20-%20Unidade%201%20-%2012.2%20Transforma%C3%A7%C3%A3o%20de%20vari%C3%A1veis%20com%20R.md)
- [18 - Unidade 1 - 13.1 Seleção de variáveis - Stepwise.md](paginas/18%20-%20Unidade%201%20-%2013.1%20Sele%C3%A7%C3%A3o%20de%20vari%C3%A1veis%20-%20Stepwise.md)
- [19 - Unidade 1 - 13.2 Seleção de variáveis - Lasso.md](paginas/19%20-%20Unidade%201%20-%2013.2%20Sele%C3%A7%C3%A3o%20de%20vari%C3%A1veis%20-%20Lasso.md)
- [20 - Unidade 1 - 13.1 Seleção de variáveis com Python.md](paginas/20%20-%20Unidade%201%20-%2013.1%20Sele%C3%A7%C3%A3o%20de%20vari%C3%A1veis%20com%20Python.md)
- [21 - Unidade 1 - 13.2 Seleção de variáveis com R.md](paginas/21%20-%20Unidade%201%20-%2013.2%20Sele%C3%A7%C3%A3o%20de%20vari%C3%A1veis%20com%20R.md)
- [22 - Unidade 1 - Material Complementar.md](paginas/22%20-%20Unidade%201%20-%20Material%20Complementar.md)

### Imagens (5)

- [banner-pos-2022-1.jpg](images/banner-pos-2022-1.jpg)
- [banner-pos-2022-3-1.jpg](images/banner-pos-2022-3-1.jpg)
- [banner-pos-2022-4.jpg](images/banner-pos-2022-4.jpg)
- [icone-bussola-1.png](images/icone-bussola-1.png)
- [material-b-1.png](images/material-b-1.png)

### HTML original (24)

- [Medidas_de_associacao_video.nb.html](documentos/Medidas_de_associacao_video.nb.html)
- [Regressao_linear_simples_video.nb.html](documentos/Regressao_linear_simples_video.nb.html)
- [01 - Unidade 1 - Orientações de Estudo.html](html/01%20-%20Unidade%201%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.html)
- [02 - Unidade 1 - 1. Modelos Estatísticos.html](html/02%20-%20Unidade%201%20-%201.%20Modelos%20Estat%C3%ADsticos.html)
- [03 - Unidade 1 - 2. Fundamentos para modelos de regressão linear.html](html/03%20-%20Unidade%201%20-%202.%20Fundamentos%20para%20modelos%20de%20regress%C3%A3o%20linear.html)
- [04 - Unidade 1 - 2.1 Medidas de Associação com R.html](html/04%20-%20Unidade%201%20-%202.1%20Medidas%20de%20Associa%C3%A7%C3%A3o%20com%20R.html)
- [05 - Unidade 1 - 2.2 Medidas de Associação com Python.html](html/05%20-%20Unidade%201%20-%202.2%20Medidas%20de%20Associa%C3%A7%C3%A3o%20com%20Python.html)
- [06 - Unidade 1 - 3. Regressão linear.html](html/06%20-%20Unidade%201%20-%203.%20Regress%C3%A3o%20linear.html)
- [07 - Unidade 1 - 4. Estimativa de coeficientes de regressão linear simples.html](html/07%20-%20Unidade%201%20-%204.%20Estimativa%20de%20coeficientes%20de%20regress%C3%A3o%20linear%20simples.html)
- [08 - Unidade 1 - 5. Premissas de Regressão linear simples.html](html/08%20-%20Unidade%201%20-%205.%20Premissas%20de%20Regress%C3%A3o%20linear%20simples.html)
- [09 - Unidade 1 - 6. Regressão linear múltipla.html](html/09%20-%20Unidade%201%20-%206.%20Regress%C3%A3o%20linear%20m%C3%BAltipla.html)
- [10 - Unidade 1 - 7. Premissas da Regressão linear múltipla.html](html/10%20-%20Unidade%201%20-%207.%20Premissas%20da%20Regress%C3%A3o%20linear%20m%C3%BAltipla.html)
- [11 - Unidade 1 - 8. Regressão Linear múltipla com Python.html](html/11%20-%20Unidade%201%20-%208.%20Regress%C3%A3o%20Linear%20m%C3%BAltipla%20com%20Python.html)
- [12 - Unidade 1 - 9. Comparação de modelos da Regressão linear múltipla.html](html/12%20-%20Unidade%201%20-%209.%20Compara%C3%A7%C3%A3o%20de%20modelos%20da%20Regress%C3%A3o%20linear%20m%C3%BAltipla.html)
- [13 - Unidade 1 - 10. Comparação de modelos de Regressão linear com Python.html](html/13%20-%20Unidade%201%20-%2010.%20Compara%C3%A7%C3%A3o%20de%20modelos%20de%20Regress%C3%A3o%20linear%20com%20Python.html)
- [14 - Unidade 1 - 11. Comparação de modelos - Atividade - com Python.html](html/14%20-%20Unidade%201%20-%2011.%20Compara%C3%A7%C3%A3o%20de%20modelos%20-%20Atividade%20-%20com%20Python.html)
- [15 - Unidade 1 - 12. Transformação de variáveis.html](html/15%20-%20Unidade%201%20-%2012.%20Transforma%C3%A7%C3%A3o%20de%20vari%C3%A1veis.html)
- [16 - Unidade 1 - 12.1 Transformação de variáveis com Python.html](html/16%20-%20Unidade%201%20-%2012.1%20Transforma%C3%A7%C3%A3o%20de%20vari%C3%A1veis%20com%20Python.html)
- [17 - Unidade 1 - 12.2 Transformação de variáveis com R.html](html/17%20-%20Unidade%201%20-%2012.2%20Transforma%C3%A7%C3%A3o%20de%20vari%C3%A1veis%20com%20R.html)
- [18 - Unidade 1 - 13.1 Seleção de variáveis - Stepwise.html](html/18%20-%20Unidade%201%20-%2013.1%20Sele%C3%A7%C3%A3o%20de%20vari%C3%A1veis%20-%20Stepwise.html)
- … e mais 4 arquivos em [documentos/](documentos/)

## Roteiro de estudo

1. Leia as páginas na ordem apresentada pelo módulo.
2. Consulte os PDFs e apresentações enquanto registra definições, hipóteses e exemplos.
3. Execute notebooks e códigos, verificando entradas, saídas e limitações.
4. Ao final, responda:

   - Como você explicaria **Unidade 1 - Orientações de Estudo** sem consultar o material?
   - Como você explicaria **Unidade 1 - 1. Modelos Estatísticos** sem consultar o material?
   - Como você explicaria **Unidade 1 - 2. Fundamentos para modelos de regressão linear** sem consultar o material?
   - Como você explicaria **Unidade 1 - 2.1 Medidas de Associação com R** sem consultar o material?
   - Como você explicaria **Unidade 1 - 2.2 Medidas de Associação com Python** sem consultar o material?
