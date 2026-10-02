# 03 - UNIDADE 2 - APRENDIZADO SUPERVISIONADO

[← Voltar à disciplina](../README.md)

## Resumo da unidade

A unidade cobre classificação e regressão supervisionadas, separação de dados, seleção de atributos, árvores e avaliação. A métrica deve refletir o custo de falso positivo e falso negativo.

### Exemplo

Em detecção de fraude, acurácia pode ser alta mesmo se o modelo ignorar todas as fraudes. Precisão, revocação e matriz de confusão mostram o comportamento real.

## Fórmulas essenciais

### Precisão

$$
\mathrm{Precisão}=\frac{VP}{VP+FP}
$$

Entre os casos previstos como positivos, mede quantos estavam corretos.

### Revocação

$$
\mathrm{Revocação}=\frac{VP}{VP+FN}
$$

Entre os positivos reais, mede quantos foram encontrados.

### F1

$$
F_1=2\frac{\mathrm{Precisão}\cdot\mathrm{Revocação}}{\mathrm{Precisão}+\mathrm{Revocação}}
$$

Resume precisão e revocação pela média harmônica.


## Conteúdo da unidade

- [Unidade 2 - Orientações de Estudo](paginas/01%20-%20Unidade%202%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md)
- [Unidade 2 - 1. Aprendizado supervisionado - Processo](paginas/04%20-%20Unidade%202%20-%201.%20Aprendizado%20supervisionado%20-%20Processo.md)
- [Unidade 2 - 2. Aprendizado supervisionado - Separação da base de dados](paginas/06%20-%20Unidade%202%20-%202.%20Aprendizado%20supervisionado%20-%20Separa%C3%A7%C3%A3o%20da%20base%20de%20dados.md)
- [Unidade 2 - 3. Seleção de registros e atributos](paginas/08%20-%20Unidade%202%20-%203.%20Sele%C3%A7%C3%A3o%20de%20registros%20e%20atributos.md)
- [Unidade 2 - 4. Escolha do Algoritmo](paginas/10%20-%20Unidade%202%20-%204.%20Escolha%20do%20Algoritmo.md)
- [Unidade 2 - 5. Avaliação do modelo - Matriz de confusão](paginas/12%20-%20Unidade%202%20-%205.%20Avalia%C3%A7%C3%A3o%20do%20modelo%20-%20Matriz%20de%20confus%C3%A3o.md)
- [Unidade 2 - 6. Avaliação do modelo - Medidas de qualidade](paginas/13%20-%20Unidade%202%20-%206.%20Avalia%C3%A7%C3%A3o%20do%20modelo%20-%20Medidas%20de%20qualidade.md)
- [Unidade 2 - 7. Árvore de decisão: Princípios](paginas/17%20-%20Unidade%202%20-%207.%20%C3%81rvore%20de%20decis%C3%A3o_%20Princ%C3%ADpios.md)
- [Unidade 2 - 8. Árvore de decisão: ID3](paginas/19%20-%20Unidade%202%20-%208.%20%C3%81rvore%20de%20decis%C3%A3o_%20ID3.md)
- [Unidade 2 - 9. Árvore de decisão: overfitting](paginas/23%20-%20Unidade%202%20-%209.%20%C3%81rvore%20de%20decis%C3%A3o_%20overfitting.md)
- [Unidade 2 - 10. Árvore de decisão: Atributos Contínuos](paginas/25%20-%20Unidade%202%20-%2010.%20%C3%81rvore%20de%20decis%C3%A3o_%20Atributos%20Cont%C3%ADnuos.md)
- [Unidade 2 - Aula Prática 1: Árvore de Decisão](paginas/27%20-%20Unidade%202%20-%20Aula%20Pr%C3%A1tica%201_%20%C3%81rvore%20de%20Decis%C3%A3o.md)
- [Unidade 2 - Aula Prática 2: Colab - Árvore de Decisão - Iris](paginas/30%20-%20Unidade%202%20-%20Aula%20Pr%C3%A1tica%202_%20Colab%20-%20%C3%81rvore%20de%20Decis%C3%A3o%20-%20Iris.md)
- [Unidade 2 - 11. Classificação Bayesiana](paginas/32%20-%20Unidade%202%20-%2011.%20Classifica%C3%A7%C3%A3o%20Bayesiana.md)
- [Unidade 2 - Aula Prática 3: Colab - Naïve Bayes - Iris](paginas/34%20-%20Unidade%202%20-%20Aula%20Pr%C3%A1tica%203_%20Colab%20-%20Na%C3%AFve%20Bayes%20-%20Iris.md)
- [Unidade 2 - 12. Redes Neurais Artificiais](paginas/38%20-%20Unidade%202%20-%2012.%20Redes%20Neurais%20Artificiais.md)
- [Unidade 2 - 13. Regressão Linear, Rigde e Lasso](paginas/41%20-%20Unidade%202%20-%2013.%20Regress%C3%A3o%20Linear%2C%20Rigde%20e%20Lasso.md)
- [Unidade 2 - Aula Prática 4: Colab - Regressão linear, Ridge e LASSO](paginas/44%20-%20Unidade%202%20-%20Aula%20Pr%C3%A1tica%204_%20Colab%20-%20Regress%C3%A3o%20linear%2C%20Ridge%20e%20LASSO.md)
- [Unidade 2 - 14. Boosting](paginas/48%20-%20Unidade%202%20-%2014.%20Boosting.md)
- [Unidade 2 - 15. Aprendizado supervisionado - Busca por hiperparâmetros](paginas/52%20-%20Unidade%202%20-%2015.%20Aprendizado%20supervisionado%20-%20Busca%20por%20hiperpar%C3%A2metros.md)
- [Unidade 2 - Aula Prática 5: Grid Search](paginas/54%20-%20Unidade%202%20-%20Aula%20Pr%C3%A1tica%205_%20Grid%20Search.md)

## Materiais

### PDFs (15)

- [Slides - Aprendizado supervisionado - Busca por Hiperparâmetros.pdf](documentos/Slides%20-%20Aprendizado%20supervisionado%20-%20Busca%20por%20Hiperpar%C3%A2metros.pdf) (arquivo indisponível ou ainda em processamento no Canvas)
- [Slides - Aprendizado supervisionado - Processo.pdf](documentos/Slides%20-%20Aprendizado%20supervisionado%20-%20Processo.pdf) (arquivo indisponível ou ainda em processamento no Canvas)
- [Slides - Aprendizado supervisionado - Separação da base de dados.pdf](documentos/Slides%20-%20Aprendizado%20supervisionado%20-%20Separa%C3%A7%C3%A3o%20da%20base%20de%20dados.pdf) (arquivo indisponível ou ainda em processamento no Canvas)
- [Slides - Boosting.pdf](documentos/Slides%20-%20Boosting.pdf) (arquivo indisponível ou ainda em processamento no Canvas)
- [Slides - Classificação Bayesiana.pdf](documentos/Slides%20-%20Classifica%C3%A7%C3%A3o%20Bayesiana.pdf) (arquivo indisponível ou ainda em processamento no Canvas)
- [Slides - Classificação e previsão - avaliação do modelo.pdf](documentos/Slides%20-%20Classifica%C3%A7%C3%A3o%20e%20previs%C3%A3o%20-%20avalia%C3%A7%C3%A3o%20do%20modelo.pdf) (arquivo indisponível ou ainda em processamento no Canvas)
- [Slides - Escolha do algoritmo.pdf](documentos/Slides%20-%20Escolha%20do%20algoritmo.pdf) (arquivo indisponível ou ainda em processamento no Canvas)
- [Slides - Redes Neurais Artificiais.pdf](documentos/Slides%20-%20Redes%20Neurais%20Artificiais.pdf) (arquivo indisponível ou ainda em processamento no Canvas)
- [Slides - Regressão Linear - Ridge e Lasso.pdf](documentos/Slides%20-%20Regress%C3%A3o%20Linear%20-%20Ridge%20e%20Lasso.pdf) (arquivo indisponível ou ainda em processamento no Canvas)
- [Slides - Regressão Linear.pdf](documentos/Slides%20-%20Regress%C3%A3o%20Linear.pdf) (arquivo indisponível ou ainda em processamento no Canvas)
- [Slides - Seleção de atributos e registros.pdf](documentos/Slides%20-%20Sele%C3%A7%C3%A3o%20de%20atributos%20e%20registros.pdf) (arquivo indisponível ou ainda em processamento no Canvas)
- [Slides - Árvore de decisão - atributos contínuos.pdf](documentos/Slides%20-%20%C3%81rvore%20de%20decis%C3%A3o%20-%20atributos%20cont%C3%ADnuos.pdf) (arquivo indisponível ou ainda em processamento no Canvas)
- [Slides - Árvore de decisão - ID3.pdf](documentos/Slides%20-%20%C3%81rvore%20de%20decis%C3%A3o%20-%20ID3.pdf) (arquivo indisponível ou ainda em processamento no Canvas)
- [Slides - Árvore de decisão - overfitting.pdf](documentos/Slides%20-%20%C3%81rvore%20de%20decis%C3%A3o%20-%20overfitting.pdf) (arquivo indisponível ou ainda em processamento no Canvas)
- [Slides - Árvore de decisão - principios.pdf](documentos/Slides%20-%20%C3%81rvore%20de%20decis%C3%A3o%20-%20principios.pdf) (arquivo indisponível ou ainda em processamento no Canvas)

### Notebooks (6)

- [Arvore_de_decisao_clima.ipynb](documentos/Arvore_de_decisao_clima.ipynb) (arquivo indisponível ou ainda em processamento no Canvas)
- [Arvore_de_decisao_iris.ipynb](documentos/Arvore_de_decisao_iris.ipynb) (arquivo indisponível ou ainda em processamento no Canvas)
- [Arvore_de_decisao_sonar.ipynb](documentos/Arvore_de_decisao_sonar.ipynb) (arquivo indisponível ou ainda em processamento no Canvas)
- [Naive_Bayes_iris.ipynb](documentos/Naive_Bayes_iris.ipynb) (arquivo indisponível ou ainda em processamento no Canvas)
- [Rede Neurais-sonar.ipynb](documentos/Rede%20Neurais-sonar.ipynb) (arquivo indisponível ou ainda em processamento no Canvas)
- [Regressao_Linear_Boston.ipynb](documentos/Regressao_Linear_Boston.ipynb) (arquivo indisponível ou ainda em processamento no Canvas)

### Dados e artefatos (2)

- [clima.csv](documentos/clima.csv) (arquivo indisponível ou ainda em processamento no Canvas)
- [sonar.csv](documentos/sonar.csv) (arquivo indisponível ou ainda em processamento no Canvas)

### Páginas e textos (21)

- [01 - Unidade 2 - Orientações de Estudo.md](paginas/01%20-%20Unidade%202%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md)
- [04 - Unidade 2 - 1. Aprendizado supervisionado - Processo.md](paginas/04%20-%20Unidade%202%20-%201.%20Aprendizado%20supervisionado%20-%20Processo.md)
- [06 - Unidade 2 - 2. Aprendizado supervisionado - Separação da base de dados.md](paginas/06%20-%20Unidade%202%20-%202.%20Aprendizado%20supervisionado%20-%20Separa%C3%A7%C3%A3o%20da%20base%20de%20dados.md)
- [08 - Unidade 2 - 3. Seleção de registros e atributos.md](paginas/08%20-%20Unidade%202%20-%203.%20Sele%C3%A7%C3%A3o%20de%20registros%20e%20atributos.md)
- [10 - Unidade 2 - 4. Escolha do Algoritmo.md](paginas/10%20-%20Unidade%202%20-%204.%20Escolha%20do%20Algoritmo.md)
- [12 - Unidade 2 - 5. Avaliação do modelo - Matriz de confusão.md](paginas/12%20-%20Unidade%202%20-%205.%20Avalia%C3%A7%C3%A3o%20do%20modelo%20-%20Matriz%20de%20confus%C3%A3o.md)
- [13 - Unidade 2 - 6. Avaliação do modelo - Medidas de qualidade.md](paginas/13%20-%20Unidade%202%20-%206.%20Avalia%C3%A7%C3%A3o%20do%20modelo%20-%20Medidas%20de%20qualidade.md)
- [17 - Unidade 2 - 7. Árvore de decisão_ Princípios.md](paginas/17%20-%20Unidade%202%20-%207.%20%C3%81rvore%20de%20decis%C3%A3o_%20Princ%C3%ADpios.md)
- [19 - Unidade 2 - 8. Árvore de decisão_ ID3.md](paginas/19%20-%20Unidade%202%20-%208.%20%C3%81rvore%20de%20decis%C3%A3o_%20ID3.md)
- [23 - Unidade 2 - 9. Árvore de decisão_ overfitting.md](paginas/23%20-%20Unidade%202%20-%209.%20%C3%81rvore%20de%20decis%C3%A3o_%20overfitting.md)
- [25 - Unidade 2 - 10. Árvore de decisão_ Atributos Contínuos.md](paginas/25%20-%20Unidade%202%20-%2010.%20%C3%81rvore%20de%20decis%C3%A3o_%20Atributos%20Cont%C3%ADnuos.md)
- [27 - Unidade 2 - Aula Prática 1_ Árvore de Decisão.md](paginas/27%20-%20Unidade%202%20-%20Aula%20Pr%C3%A1tica%201_%20%C3%81rvore%20de%20Decis%C3%A3o.md)
- [30 - Unidade 2 - Aula Prática 2_ Colab - Árvore de Decisão - Iris.md](paginas/30%20-%20Unidade%202%20-%20Aula%20Pr%C3%A1tica%202_%20Colab%20-%20%C3%81rvore%20de%20Decis%C3%A3o%20-%20Iris.md)
- [32 - Unidade 2 - 11. Classificação Bayesiana.md](paginas/32%20-%20Unidade%202%20-%2011.%20Classifica%C3%A7%C3%A3o%20Bayesiana.md)
- [34 - Unidade 2 - Aula Prática 3_ Colab - Naïve Bayes - Iris.md](paginas/34%20-%20Unidade%202%20-%20Aula%20Pr%C3%A1tica%203_%20Colab%20-%20Na%C3%AFve%20Bayes%20-%20Iris.md)
- [38 - Unidade 2 - 12. Redes Neurais Artificiais.md](paginas/38%20-%20Unidade%202%20-%2012.%20Redes%20Neurais%20Artificiais.md)
- [41 - Unidade 2 - 13. Regressão Linear, Rigde e Lasso.md](paginas/41%20-%20Unidade%202%20-%2013.%20Regress%C3%A3o%20Linear%2C%20Rigde%20e%20Lasso.md)
- [44 - Unidade 2 - Aula Prática 4_ Colab - Regressão linear, Ridge e LASSO.md](paginas/44%20-%20Unidade%202%20-%20Aula%20Pr%C3%A1tica%204_%20Colab%20-%20Regress%C3%A3o%20linear%2C%20Ridge%20e%20LASSO.md)
- [48 - Unidade 2 - 14. Boosting.md](paginas/48%20-%20Unidade%202%20-%2014.%20Boosting.md)
- [52 - Unidade 2 - 15. Aprendizado supervisionado - Busca por hiperparâmetros.md](paginas/52%20-%20Unidade%202%20-%2015.%20Aprendizado%20supervisionado%20-%20Busca%20por%20hiperpar%C3%A2metros.md)
- [54 - Unidade 2 - Aula Prática 5_ Grid Search.md](paginas/54%20-%20Unidade%202%20-%20Aula%20Pr%C3%A1tica%205_%20Grid%20Search.md)

### HTML original (21)

- [01 - Unidade 2 - Orientações de Estudo.html](html/01%20-%20Unidade%202%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.html)
- [04 - Unidade 2 - 1. Aprendizado supervisionado - Processo.html](html/04%20-%20Unidade%202%20-%201.%20Aprendizado%20supervisionado%20-%20Processo.html)
- [06 - Unidade 2 - 2. Aprendizado supervisionado - Separação da base de dados.html](html/06%20-%20Unidade%202%20-%202.%20Aprendizado%20supervisionado%20-%20Separa%C3%A7%C3%A3o%20da%20base%20de%20dados.html)
- [08 - Unidade 2 - 3. Seleção de registros e atributos.html](html/08%20-%20Unidade%202%20-%203.%20Sele%C3%A7%C3%A3o%20de%20registros%20e%20atributos.html)
- [10 - Unidade 2 - 4. Escolha do Algoritmo.html](html/10%20-%20Unidade%202%20-%204.%20Escolha%20do%20Algoritmo.html)
- [12 - Unidade 2 - 5. Avaliação do modelo - Matriz de confusão.html](html/12%20-%20Unidade%202%20-%205.%20Avalia%C3%A7%C3%A3o%20do%20modelo%20-%20Matriz%20de%20confus%C3%A3o.html)
- [13 - Unidade 2 - 6. Avaliação do modelo - Medidas de qualidade.html](html/13%20-%20Unidade%202%20-%206.%20Avalia%C3%A7%C3%A3o%20do%20modelo%20-%20Medidas%20de%20qualidade.html)
- [17 - Unidade 2 - 7. Árvore de decisão_ Princípios.html](html/17%20-%20Unidade%202%20-%207.%20%C3%81rvore%20de%20decis%C3%A3o_%20Princ%C3%ADpios.html)
- [19 - Unidade 2 - 8. Árvore de decisão_ ID3.html](html/19%20-%20Unidade%202%20-%208.%20%C3%81rvore%20de%20decis%C3%A3o_%20ID3.html)
- [23 - Unidade 2 - 9. Árvore de decisão_ overfitting.html](html/23%20-%20Unidade%202%20-%209.%20%C3%81rvore%20de%20decis%C3%A3o_%20overfitting.html)
- [25 - Unidade 2 - 10. Árvore de decisão_ Atributos Contínuos.html](html/25%20-%20Unidade%202%20-%2010.%20%C3%81rvore%20de%20decis%C3%A3o_%20Atributos%20Cont%C3%ADnuos.html)
- [27 - Unidade 2 - Aula Prática 1_ Árvore de Decisão.html](html/27%20-%20Unidade%202%20-%20Aula%20Pr%C3%A1tica%201_%20%C3%81rvore%20de%20Decis%C3%A3o.html)
- [30 - Unidade 2 - Aula Prática 2_ Colab - Árvore de Decisão - Iris.html](html/30%20-%20Unidade%202%20-%20Aula%20Pr%C3%A1tica%202_%20Colab%20-%20%C3%81rvore%20de%20Decis%C3%A3o%20-%20Iris.html)
- [32 - Unidade 2 - 11. Classificação Bayesiana.html](html/32%20-%20Unidade%202%20-%2011.%20Classifica%C3%A7%C3%A3o%20Bayesiana.html)
- [34 - Unidade 2 - Aula Prática 3_ Colab - Naïve Bayes - Iris.html](html/34%20-%20Unidade%202%20-%20Aula%20Pr%C3%A1tica%203_%20Colab%20-%20Na%C3%AFve%20Bayes%20-%20Iris.html)
- [38 - Unidade 2 - 12. Redes Neurais Artificiais.html](html/38%20-%20Unidade%202%20-%2012.%20Redes%20Neurais%20Artificiais.html)
- [41 - Unidade 2 - 13. Regressão Linear, Rigde e Lasso.html](html/41%20-%20Unidade%202%20-%2013.%20Regress%C3%A3o%20Linear%2C%20Rigde%20e%20Lasso.html)
- [44 - Unidade 2 - Aula Prática 4_ Colab - Regressão linear, Ridge e LASSO.html](html/44%20-%20Unidade%202%20-%20Aula%20Pr%C3%A1tica%204_%20Colab%20-%20Regress%C3%A3o%20linear%2C%20Ridge%20e%20LASSO.html)
- [48 - Unidade 2 - 14. Boosting.html](html/48%20-%20Unidade%202%20-%2014.%20Boosting.html)
- [52 - Unidade 2 - 15. Aprendizado supervisionado - Busca por hiperparâmetros.html](html/52%20-%20Unidade%202%20-%2015.%20Aprendizado%20supervisionado%20-%20Busca%20por%20hiperpar%C3%A2metros.html)
- … e mais 1 arquivos em [html/](html/)

## Roteiro de estudo

1. Leia as páginas na ordem apresentada pelo módulo.
2. Consulte os PDFs e apresentações enquanto registra definições, hipóteses e exemplos.
3. Execute notebooks e códigos, verificando entradas, saídas e limitações.
4. Ao final, responda:

   - Como você explicaria **Unidade 2 - Orientações de Estudo** sem consultar o material?
   - Como você explicaria **Unidade 2 - 1. Aprendizado supervisionado - Processo** sem consultar o material?
   - Como você explicaria **Unidade 2 - 2. Aprendizado supervisionado - Separação da base de dados** sem consultar o material?
   - Como você explicaria **Unidade 2 - 3. Seleção de registros e atributos** sem consultar o material?
   - Como você explicaria **Unidade 2 - 4. Escolha do Algoritmo** sem consultar o material?
