# 03 - UNIDADE 2 - MODELOS LINEARES GENERALIZADOS

[← Voltar à disciplina](../README.md)

## Resumo da unidade

Modelos lineares generalizados ligam uma distribuição da família exponencial a um preditor linear. Isso permite tratar respostas binárias, contagens e outros dados que não seguem uma normal.

### Exemplo

A regressão logística estima a probabilidade de inadimplência, enquanto uma regressão de Poisson pode modelar a quantidade de chamados por dia.

## Fórmulas essenciais

### Estrutura de um GLM

$$
g(\mu_i)=\eta_i=\mathbf{x}_i^\top\boldsymbol{\beta}
$$

A função de ligação conecta a média da resposta ao preditor linear.


## Conteúdo da unidade

- [Unidade 2 - Orientações de Estudo](paginas/01%20-%20Unidade%202%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md) — Bem-vindo à Unidade sobre Modelos Lineares Generalizados (GLM)! Nesta seção do seu curso, você será apresentado a uma extensão dos modelos lineares tradicionais, que permite a análise de uma ampla gama de tipos de dados. Os GLMs são uma ferramenta versátil e poderosa para lidar com situações onde os pressupostos da regressão linear clássica não se aplicam, proporcionando maior flexibilidade na modelagem de relações…
- [Unidade 2 - 1. Introdução aos Modelos lineares Generalizados](paginas/02%20-%20Unidade%202%20-%201.%20Introdu%C3%A7%C3%A3o%20aos%20Modelos%20lineares%20Generalizados.md)
- [Unidade 2 - 2.1. Famílias exponenciais - parte 1](paginas/03%20-%20Unidade%202%20-%202.1.%20Fam%C3%ADlias%20exponenciais%20-%20parte%201.md)
- [Unidade 2 - 2.2. Família Exponencial - parte 2](paginas/04%20-%20Unidade%202%20-%202.2.%20Fam%C3%ADlia%20Exponencial%20-%20parte%202.md)
- [Unidade 2 - 3. Definição de um GLM](paginas/05%20-%20Unidade%202%20-%203.%20Defini%C3%A7%C3%A3o%20de%20um%20GLM.md)
- [Unidade 2 - 4. Especificação de um GLM](paginas/06%20-%20Unidade%202%20-%204.%20Especifica%C3%A7%C3%A3o%20de%20um%20GLM.md)
- [Unidade 2 - 5.1. Estimação de parâmetros](paginas/07%20-%20Unidade%202%20-%205.1.%20Estima%C3%A7%C3%A3o%20de%20par%C3%A2metros.md)
- [Unidade 2 - 5.2 Estimação de Parâmetros - Parte 2](paginas/08%20-%20Unidade%202%20-%205.2%20Estima%C3%A7%C3%A3o%20de%20Par%C3%A2metros%20-%20Parte%202.md)
- [Unidade 2 - 5.3 Estimação de Parâmetros - Método Escore de Fisher](paginas/09%20-%20Unidade%202%20-%205.3%20Estima%C3%A7%C3%A3o%20de%20Par%C3%A2metros%20-%20M%C3%A9todo%20Escore%20de%20Fisher.md)
- [Unidade 2 - 6. Inferência Aplicada aos GLM's](paginas/10%20-%20Unidade%202%20-%206.%20Infer%C3%AAncia%20Aplicada%20aos%20GLM%27s.md)
- [Unidade 2 - 7.1. Medidas de Discrepância - Deviance](paginas/11%20-%20Unidade%202%20-%207.1.%20Medidas%20de%20Discrep%C3%A2ncia%20-%20Deviance.md)
- [Unidade 2 - 7.2 Medidas de Discrepância - Pearson](paginas/12%20-%20Unidade%202%20-%207.2%20Medidas%20de%20Discrep%C3%A2ncia%20-%20Pearson.md)
- [Unidade 2 - 8.1 Teste de Hipóteses para os GLMs - Parte 1](paginas/13%20-%20Unidade%202%20-%208.1%20Teste%20de%20Hip%C3%B3teses%20para%20os%20GLMs%20-%20Parte%201.md)
- [Unidade 2 - 8.2. Teste de Hipóteses para os GLMs - Parte 2](paginas/14%20-%20Unidade%202%20-%208.2.%20Teste%20de%20Hip%C3%B3teses%20para%20os%20GLMs%20-%20Parte%202.md)
- [Unidade 2 - 9. Introdução a analise de resíduos e diagnósticos](paginas/15%20-%20Unidade%202%20-%209.%20Introdu%C3%A7%C3%A3o%20a%20analise%20de%20res%C3%ADduos%20e%20diagn%C3%B3sticos.md)
- [Unidade 2 - 10. Tipos de resíduos - GLM](paginas/16%20-%20Unidade%202%20-%2010.%20Tipos%20de%20res%C3%ADduos%20-%20GLM.md)
- [Unidade 2 - 11. Análise de resíduos](paginas/17%20-%20Unidade%202%20-%2011.%20An%C3%A1lise%20de%20res%C3%ADduos.md)
- [Unidade 2 - 12.1 Análise de resíduos no R](paginas/18%20-%20Unidade%202%20-%2012.1%20An%C3%A1lise%20de%20res%C3%ADduos%20no%20R.md)
- [Unidade 2 - 12.2 Análise de resíduos no Python](paginas/19%20-%20Unidade%202%20-%2012.2%20An%C3%A1lise%20de%20res%C3%ADduos%20no%20Python.md)
- [Unidade 2 - 13. Síntese dos método](paginas/20%20-%20Unidade%202%20-%2013.%20S%C3%ADntese%20dos%20m%C3%A9todo.md)
- [Unidade 2 - 14. GLM para Dados Binários ou Proporções](paginas/21%20-%20Unidade%202%20-%2014.%20GLM%20para%20Dados%20Bin%C3%A1rios%20ou%20Propor%C3%A7%C3%B5es.md)
- [Unidade 2 - 15. Regressão logística](paginas/22%20-%20Unidade%202%20-%2015.%20Regress%C3%A3o%20log%C3%ADstica.md)
- [Unidade 2 - 16. Interpretação dos parâmetros da Regressão logística](paginas/23%20-%20Unidade%202%20-%2016.%20Interpreta%C3%A7%C3%A3o%20dos%20par%C3%A2metros%20da%20Regress%C3%A3o%20log%C3%ADstica.md)
- [Unidade 2 - 17. Pressupostos e análises diagnósticos da Regressão logística](paginas/24%20-%20Unidade%202%20-%2017.%20Pressupostos%20e%20an%C3%A1lises%20diagn%C3%B3sticos%20da%20Regress%C3%A3o%20log%C3%ADstica.md)
- [Unidade 2 - 17.1 Regressão Binária no R](paginas/25%20-%20Unidade%202%20-%2017.1%20Regress%C3%A3o%20Bin%C3%A1ria%20no%20R.md)
- [Unidade 2 - 17.2 Regressão binária com Python - Parte 1](paginas/26%20-%20Unidade%202%20-%2017.2%20Regress%C3%A3o%20bin%C3%A1ria%20com%20Python%20-%20Parte%201.md)
- [Unidade 2 - 17.3 Regressão binária com Python - Parte 2](paginas/27%20-%20Unidade%202%20-%2017.3%20Regress%C3%A3o%20bin%C3%A1ria%20com%20Python%20-%20Parte%202.md)
- [Unidade 2 - 17.4 Estudo de Caso - Regressão logística com Python - Pré-Processamento - Parte 1](paginas/28%20-%20Unidade%202%20-%2017.4%20Estudo%20de%20Caso%20-%20Regress%C3%A3o%20log%C3%ADstica%20com%20Python%20-%20Pr%C3%A9-Processamento%20-%20Parte%201.md)
- [Unidade 2 - 17.5 Estudo de Caso - Regressão logística com Python - Pré-Processamento - Parte 2](paginas/29%20-%20Unidade%202%20-%2017.5%20Estudo%20de%20Caso%20-%20Regress%C3%A3o%20log%C3%ADstica%20com%20Python%20-%20Pr%C3%A9-Processamento%20-%20Parte%202.md)
- [Unidade 2 - 18. Regressão Multinomial](paginas/30%20-%20Unidade%202%20-%2018.%20Regress%C3%A3o%20Multinomial.md)
- [Unidade 2 - 19 Interpretação dos parâmentros da Regressão Multinomial](paginas/31%20-%20Unidade%202%20-%2019%20Interpreta%C3%A7%C3%A3o%20dos%20par%C3%A2mentros%20da%20Regress%C3%A3o%20Multinomial.md)
- [Unidade 2 - 20.1 Regressão Multinomial no R - Parte 1](paginas/32%20-%20Unidade%202%20-%2020.1%20Regress%C3%A3o%20Multinomial%20no%20R%20-%20Parte%201.md)
- [Unidade 2 - 20.2 Regressão Multinomial no R - Parte 2](paginas/33%20-%20Unidade%202%20-%2020.2%20Regress%C3%A3o%20Multinomial%20no%20R%20-%20Parte%202.md)
- [Unidade 2 - 20.1 Regressão Multinomial com Python - Parte 1](paginas/34%20-%20Unidade%202%20-%2020.1%20Regress%C3%A3o%20Multinomial%20com%20Python%20-%20Parte%201.md)
- [Unidade 2 - 20.2 Regressão Multinomial com Python - Parte 2](paginas/35%20-%20Unidade%202%20-%2020.2%20Regress%C3%A3o%20Multinomial%20com%20Python%20-%20Parte%202.md)
- [Unidade 2 - Material Complementar](paginas/36%20-%20Unidade%202%20-%20Material%20Complementar.md) — 01 - Introducao aos modelos lineares generalizados.pdf 03 - Familia exponencial de distribuicao - parte 2.pdf 14 - Teste de Hipóteses para os GLMs - parte 2.pdf 15 - Introdução a análise de resíduos e diagnósticos.pdf 21 - Interpretação dos Parâmetros da Regressão Logistica.pdf.pdf "Link") 22 - Pressupostos e análise de diagnósticos da Regressão Logística .pdf.pdf "Link")

## Materiais

### PDFs (24)

- [01 - Introducao aos modelos lineares generalizados.pdf](documentos/01%20-%20Introducao%20aos%20modelos%20lineares%20generalizados.pdf) (18 páginas)
- [02 - Familia exponencial.pdf](documentos/02%20-%20Familia%20exponencial.pdf) (12 páginas)
- [03 - Familia exponencial de distribuicao - parte 2.pdf](documentos/03%20-%20Familia%20exponencial%20de%20distribuicao%20-%20parte%202.pdf) (9 páginas)
- [04 - Definindo um GLM.pdf](documentos/04%20-%20Definindo%20um%20GLM.pdf) (9 páginas)
- [05 - Especificacao de um GLM.pdf](documentos/05%20-%20Especificacao%20de%20um%20GLM.pdf) (13 páginas)
- [06 - Estimacao de parametros.pdf](documentos/06%20-%20Estimacao%20de%20parametros.pdf) (16 páginas)
- [07 - Estimacao de parametros - parte 2.pdf](documentos/07%20-%20Estimacao%20de%20parametros%20-%20parte%202.pdf) (8 páginas)
- [08 - Estimacao de parametros - parte 3.pdf](documentos/08%20-%20Estimacao%20de%20parametros%20-%20parte%203.pdf) (14 páginas)
- [09 - Inferencia aplicada aos GLMs.pdf](documentos/09%20-%20Inferencia%20aplicada%20aos%20GLMs.pdf) (11 páginas)
- [10 - Medidas de Discrepancia - Deviance.pdf](documentos/10%20-%20Medidas%20de%20Discrepancia%20-%20Deviance.pdf) (12 páginas)
- [11 - Medidas de Discrepancia - Pearson.pdf](documentos/11%20-%20Medidas%20de%20Discrepancia%20-%20Pearson.pdf) (4 páginas)
- [12 - Estimacao do parametro de dispersao.pdf](documentos/12%20-%20Estimacao%20do%20parametro%20de%20dispersao.pdf) (6 páginas)
- [13 - Teste de Hipóteses para os GLMs.pdf](documentos/13%20-%20Teste%20de%20Hip%C3%B3teses%20para%20os%20GLMs.pdf) (8 páginas)
- [14 - Teste de Hipóteses para os GLMs - parte 2.pdf](documentos/14%20-%20Teste%20de%20Hip%C3%B3teses%20para%20os%20GLMs%20-%20parte%202.pdf) (9 páginas)
- [15 - Introdução a análise de resíduos e diagnósticos.pdf](documentos/15%20-%20Introdu%C3%A7%C3%A3o%20a%20an%C3%A1lise%20de%20res%C3%ADduos%20e%20diagn%C3%B3sticos.pdf) (9 páginas)
- [16 - Tipos de resíduos.pdf](documentos/16%20-%20Tipos%20de%20res%C3%ADduos.pdf) (9 páginas)
- [17 - Análise de Resíduos.pdf](documentos/17%20-%20An%C3%A1lise%20de%20Res%C3%ADduos.pdf) (9 páginas)
- [17 - GLM para dados binários.pdf](documentos/17%20-%20GLM%20para%20dados%20bin%C3%A1rios.pdf) (11 páginas)
- [18 - Síntese do método.pdf](documentos/18%20-%20S%C3%ADntese%20do%20m%C3%A9todo.pdf) (12 páginas)
- [20 - Regressão logística (1).pdf](documentos/20%20-%20Regress%C3%A3o%20log%C3%ADstica%20%281%29.pdf) (12 páginas)
- [21 - Interpretação dos Parâmetros da Regressão Logistica (1).pdf](documentos/21%20-%20Interpreta%C3%A7%C3%A3o%20dos%20Par%C3%A2metros%20da%20Regress%C3%A3o%20Logistica%20%281%29.pdf) (8 páginas)
- [22 - Pressupostos e análise de diagnósticos da Regressão Logística (1).pdf](documentos/22%20-%20Pressupostos%20e%20an%C3%A1lise%20de%20diagn%C3%B3sticos%20da%20Regress%C3%A3o%20Log%C3%ADstica%20%281%29.pdf) (16 páginas)
- [23 - regressao multinomial (1).pdf](documentos/23%20-%20regressao%20multinomial%20%281%29.pdf) (12 páginas)
- [24 - Interpretação dos Parâmetros Regressão Multinomial (1).pdf](documentos/24%20-%20Interpreta%C3%A7%C3%A3o%20dos%20Par%C3%A2metros%20Regress%C3%A3o%20Multinomial%20%281%29.pdf) (17 páginas)

### Notebooks (5)

- [01 - Análise de Resíduos.ipynb](documentos/01%20-%20An%C3%A1lise%20de%20Res%C3%ADduos.ipynb)
- [04 - Regressão Binária com Python-canvas-14887846.ipynb](documentos/04%20-%20Regress%C3%A3o%20Bin%C3%A1ria%20com%20Python-canvas-14887846.ipynb)
- [04 - Regressão Binária com Python.ipynb](documentos/04%20-%20Regress%C3%A3o%20Bin%C3%A1ria%20com%20Python.ipynb)
- [Regressao_logistica_multinomial.ipynb](documentos/Regressao_logistica_multinomial.ipynb)
- [Regressao_logistica_stroke.ipynb](documentos/Regressao_logistica_stroke.ipynb)

### Código e configuração (3)

- [02 - Analise de residuos - R.Rmd](documentos/02%20-%20Analise%20de%20residuos%20-%20R.Rmd)
- [03 - Regressão Logística com R.Rmd](documentos/03%20-%20Regress%C3%A3o%20Log%C3%ADstica%20com%20R.Rmd)
- [05 - Regressao_multinomial.Rmd](documentos/05%20-%20Regressao_multinomial.Rmd)

### Dados e artefatos (5)

- [covid_doencas_preexistentes-canvas-14887837.csv](documentos/covid_doencas_preexistentes-canvas-14887837.csv)
- [covid_doencas_preexistentes.csv](documentos/covid_doencas_preexistentes.csv)
- [dados_covid19_vacinas.xlsx](documentos/dados_covid19_vacinas.xlsx)
- [dados_exemplo_multinomial.xlsx](documentos/dados_exemplo_multinomial.xlsx)
- [stroke.csv](documentos/stroke.csv)

### Páginas e textos (36)

- [01 - Unidade 2 - Orientações de Estudo.md](paginas/01%20-%20Unidade%202%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md)
- [02 - Unidade 2 - 1. Introdução aos Modelos lineares Generalizados.md](paginas/02%20-%20Unidade%202%20-%201.%20Introdu%C3%A7%C3%A3o%20aos%20Modelos%20lineares%20Generalizados.md)
- [03 - Unidade 2 - 2.1. Famílias exponenciais - parte 1.md](paginas/03%20-%20Unidade%202%20-%202.1.%20Fam%C3%ADlias%20exponenciais%20-%20parte%201.md)
- [04 - Unidade 2 - 2.2. Família Exponencial - parte 2.md](paginas/04%20-%20Unidade%202%20-%202.2.%20Fam%C3%ADlia%20Exponencial%20-%20parte%202.md)
- [05 - Unidade 2 - 3. Definição de um GLM.md](paginas/05%20-%20Unidade%202%20-%203.%20Defini%C3%A7%C3%A3o%20de%20um%20GLM.md)
- [06 - Unidade 2 - 4. Especificação de um GLM.md](paginas/06%20-%20Unidade%202%20-%204.%20Especifica%C3%A7%C3%A3o%20de%20um%20GLM.md)
- [07 - Unidade 2 - 5.1. Estimação de parâmetros.md](paginas/07%20-%20Unidade%202%20-%205.1.%20Estima%C3%A7%C3%A3o%20de%20par%C3%A2metros.md)
- [08 - Unidade 2 - 5.2 Estimação de Parâmetros - Parte 2.md](paginas/08%20-%20Unidade%202%20-%205.2%20Estima%C3%A7%C3%A3o%20de%20Par%C3%A2metros%20-%20Parte%202.md)
- [09 - Unidade 2 - 5.3 Estimação de Parâmetros - Método Escore de Fisher.md](paginas/09%20-%20Unidade%202%20-%205.3%20Estima%C3%A7%C3%A3o%20de%20Par%C3%A2metros%20-%20M%C3%A9todo%20Escore%20de%20Fisher.md)
- [10 - Unidade 2 - 6. Inferência Aplicada aos GLM's.md](paginas/10%20-%20Unidade%202%20-%206.%20Infer%C3%AAncia%20Aplicada%20aos%20GLM%27s.md)
- [11 - Unidade 2 - 7.1. Medidas de Discrepância - Deviance.md](paginas/11%20-%20Unidade%202%20-%207.1.%20Medidas%20de%20Discrep%C3%A2ncia%20-%20Deviance.md)
- [12 - Unidade 2 - 7.2 Medidas de Discrepância - Pearson.md](paginas/12%20-%20Unidade%202%20-%207.2%20Medidas%20de%20Discrep%C3%A2ncia%20-%20Pearson.md)
- [13 - Unidade 2 - 8.1 Teste de Hipóteses para os GLMs - Parte 1.md](paginas/13%20-%20Unidade%202%20-%208.1%20Teste%20de%20Hip%C3%B3teses%20para%20os%20GLMs%20-%20Parte%201.md)
- [14 - Unidade 2 - 8.2. Teste de Hipóteses para os GLMs - Parte 2.md](paginas/14%20-%20Unidade%202%20-%208.2.%20Teste%20de%20Hip%C3%B3teses%20para%20os%20GLMs%20-%20Parte%202.md)
- [15 - Unidade 2 - 9. Introdução a analise de resíduos e diagnósticos.md](paginas/15%20-%20Unidade%202%20-%209.%20Introdu%C3%A7%C3%A3o%20a%20analise%20de%20res%C3%ADduos%20e%20diagn%C3%B3sticos.md)
- [16 - Unidade 2 - 10. Tipos de resíduos - GLM.md](paginas/16%20-%20Unidade%202%20-%2010.%20Tipos%20de%20res%C3%ADduos%20-%20GLM.md)
- [17 - Unidade 2 - 11. Análise de resíduos.md](paginas/17%20-%20Unidade%202%20-%2011.%20An%C3%A1lise%20de%20res%C3%ADduos.md)
- [18 - Unidade 2 - 12.1 Análise de resíduos no R.md](paginas/18%20-%20Unidade%202%20-%2012.1%20An%C3%A1lise%20de%20res%C3%ADduos%20no%20R.md)
- [19 - Unidade 2 - 12.2 Análise de resíduos no Python.md](paginas/19%20-%20Unidade%202%20-%2012.2%20An%C3%A1lise%20de%20res%C3%ADduos%20no%20Python.md)
- [20 - Unidade 2 - 13. Síntese dos método.md](paginas/20%20-%20Unidade%202%20-%2013.%20S%C3%ADntese%20dos%20m%C3%A9todo.md)
- [21 - Unidade 2 - 14. GLM para Dados Binários ou Proporções.md](paginas/21%20-%20Unidade%202%20-%2014.%20GLM%20para%20Dados%20Bin%C3%A1rios%20ou%20Propor%C3%A7%C3%B5es.md)
- [22 - Unidade 2 - 15. Regressão logística.md](paginas/22%20-%20Unidade%202%20-%2015.%20Regress%C3%A3o%20log%C3%ADstica.md)
- [23 - Unidade 2 - 16. Interpretação dos parâmetros da Regressão logística.md](paginas/23%20-%20Unidade%202%20-%2016.%20Interpreta%C3%A7%C3%A3o%20dos%20par%C3%A2metros%20da%20Regress%C3%A3o%20log%C3%ADstica.md)
- [24 - Unidade 2 - 17. Pressupostos e análises diagnósticos da Regressão logística.md](paginas/24%20-%20Unidade%202%20-%2017.%20Pressupostos%20e%20an%C3%A1lises%20diagn%C3%B3sticos%20da%20Regress%C3%A3o%20log%C3%ADstica.md)
- [25 - Unidade 2 - 17.1 Regressão Binária no R.md](paginas/25%20-%20Unidade%202%20-%2017.1%20Regress%C3%A3o%20Bin%C3%A1ria%20no%20R.md)
- [26 - Unidade 2 - 17.2 Regressão binária com Python - Parte 1.md](paginas/26%20-%20Unidade%202%20-%2017.2%20Regress%C3%A3o%20bin%C3%A1ria%20com%20Python%20-%20Parte%201.md)
- [27 - Unidade 2 - 17.3 Regressão binária com Python - Parte 2.md](paginas/27%20-%20Unidade%202%20-%2017.3%20Regress%C3%A3o%20bin%C3%A1ria%20com%20Python%20-%20Parte%202.md)
- [28 - Unidade 2 - 17.4 Estudo de Caso - Regressão logística com Python - Pré-Processamento - Parte 1.md](paginas/28%20-%20Unidade%202%20-%2017.4%20Estudo%20de%20Caso%20-%20Regress%C3%A3o%20log%C3%ADstica%20com%20Python%20-%20Pr%C3%A9-Processamento%20-%20Parte%201.md)
- [29 - Unidade 2 - 17.5 Estudo de Caso - Regressão logística com Python - Pré-Processamento - Parte 2.md](paginas/29%20-%20Unidade%202%20-%2017.5%20Estudo%20de%20Caso%20-%20Regress%C3%A3o%20log%C3%ADstica%20com%20Python%20-%20Pr%C3%A9-Processamento%20-%20Parte%202.md)
- [30 - Unidade 2 - 18. Regressão Multinomial.md](paginas/30%20-%20Unidade%202%20-%2018.%20Regress%C3%A3o%20Multinomial.md)
- [31 - Unidade 2 - 19 Interpretação dos parâmentros da Regressão Multinomial.md](paginas/31%20-%20Unidade%202%20-%2019%20Interpreta%C3%A7%C3%A3o%20dos%20par%C3%A2mentros%20da%20Regress%C3%A3o%20Multinomial.md)
- [32 - Unidade 2 - 20.1 Regressão Multinomial no R - Parte 1.md](paginas/32%20-%20Unidade%202%20-%2020.1%20Regress%C3%A3o%20Multinomial%20no%20R%20-%20Parte%201.md)
- [33 - Unidade 2 - 20.2 Regressão Multinomial no R - Parte 2.md](paginas/33%20-%20Unidade%202%20-%2020.2%20Regress%C3%A3o%20Multinomial%20no%20R%20-%20Parte%202.md)
- [34 - Unidade 2 - 20.1 Regressão Multinomial com Python - Parte 1.md](paginas/34%20-%20Unidade%202%20-%2020.1%20Regress%C3%A3o%20Multinomial%20com%20Python%20-%20Parte%201.md)
- [35 - Unidade 2 - 20.2 Regressão Multinomial com Python - Parte 2.md](paginas/35%20-%20Unidade%202%20-%2020.2%20Regress%C3%A3o%20Multinomial%20com%20Python%20-%20Parte%202.md)
- [36 - Unidade 2 - Material Complementar.md](paginas/36%20-%20Unidade%202%20-%20Material%20Complementar.md)

### Imagens (7)

- [banner-pos-2022-1-1.jpg](images/banner-pos-2022-1-1.jpg)
- [banner-pos-2022-1-2.jpg](images/banner-pos-2022-1-2.jpg)
- [banner-pos-2022-1-3.jpg](images/banner-pos-2022-1-3.jpg)
- [banner-pos-2022-1.jpg](images/banner-pos-2022-1.jpg)
- [banner-pos-2022-2.jpg](images/banner-pos-2022-2.jpg)
- [icone-bussola-1.png](images/icone-bussola-1.png)
- [material-b-1.png](images/material-b-1.png)

### HTML original (36)

- [01 - Unidade 2 - Orientações de Estudo.html](html/01%20-%20Unidade%202%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.html)
- [02 - Unidade 2 - 1. Introdução aos Modelos lineares Generalizados.html](html/02%20-%20Unidade%202%20-%201.%20Introdu%C3%A7%C3%A3o%20aos%20Modelos%20lineares%20Generalizados.html)
- [03 - Unidade 2 - 2.1. Famílias exponenciais - parte 1.html](html/03%20-%20Unidade%202%20-%202.1.%20Fam%C3%ADlias%20exponenciais%20-%20parte%201.html)
- [04 - Unidade 2 - 2.2. Família Exponencial - parte 2.html](html/04%20-%20Unidade%202%20-%202.2.%20Fam%C3%ADlia%20Exponencial%20-%20parte%202.html)
- [05 - Unidade 2 - 3. Definição de um GLM.html](html/05%20-%20Unidade%202%20-%203.%20Defini%C3%A7%C3%A3o%20de%20um%20GLM.html)
- [06 - Unidade 2 - 4. Especificação de um GLM.html](html/06%20-%20Unidade%202%20-%204.%20Especifica%C3%A7%C3%A3o%20de%20um%20GLM.html)
- [07 - Unidade 2 - 5.1. Estimação de parâmetros.html](html/07%20-%20Unidade%202%20-%205.1.%20Estima%C3%A7%C3%A3o%20de%20par%C3%A2metros.html)
- [08 - Unidade 2 - 5.2 Estimação de Parâmetros - Parte 2.html](html/08%20-%20Unidade%202%20-%205.2%20Estima%C3%A7%C3%A3o%20de%20Par%C3%A2metros%20-%20Parte%202.html)
- [09 - Unidade 2 - 5.3 Estimação de Parâmetros - Método Escore de Fisher.html](html/09%20-%20Unidade%202%20-%205.3%20Estima%C3%A7%C3%A3o%20de%20Par%C3%A2metros%20-%20M%C3%A9todo%20Escore%20de%20Fisher.html)
- [10 - Unidade 2 - 6. Inferência Aplicada aos GLM's.html](html/10%20-%20Unidade%202%20-%206.%20Infer%C3%AAncia%20Aplicada%20aos%20GLM%27s.html)
- [11 - Unidade 2 - 7.1. Medidas de Discrepância - Deviance.html](html/11%20-%20Unidade%202%20-%207.1.%20Medidas%20de%20Discrep%C3%A2ncia%20-%20Deviance.html)
- [12 - Unidade 2 - 7.2 Medidas de Discrepância - Pearson.html](html/12%20-%20Unidade%202%20-%207.2%20Medidas%20de%20Discrep%C3%A2ncia%20-%20Pearson.html)
- [13 - Unidade 2 - 8.1 Teste de Hipóteses para os GLMs - Parte 1.html](html/13%20-%20Unidade%202%20-%208.1%20Teste%20de%20Hip%C3%B3teses%20para%20os%20GLMs%20-%20Parte%201.html)
- [14 - Unidade 2 - 8.2. Teste de Hipóteses para os GLMs - Parte 2.html](html/14%20-%20Unidade%202%20-%208.2.%20Teste%20de%20Hip%C3%B3teses%20para%20os%20GLMs%20-%20Parte%202.html)
- [15 - Unidade 2 - 9. Introdução a analise de resíduos e diagnósticos.html](html/15%20-%20Unidade%202%20-%209.%20Introdu%C3%A7%C3%A3o%20a%20analise%20de%20res%C3%ADduos%20e%20diagn%C3%B3sticos.html)
- [16 - Unidade 2 - 10. Tipos de resíduos - GLM.html](html/16%20-%20Unidade%202%20-%2010.%20Tipos%20de%20res%C3%ADduos%20-%20GLM.html)
- [17 - Unidade 2 - 11. Análise de resíduos.html](html/17%20-%20Unidade%202%20-%2011.%20An%C3%A1lise%20de%20res%C3%ADduos.html)
- [18 - Unidade 2 - 12.1 Análise de resíduos no R.html](html/18%20-%20Unidade%202%20-%2012.1%20An%C3%A1lise%20de%20res%C3%ADduos%20no%20R.html)
- [19 - Unidade 2 - 12.2 Análise de resíduos no Python.html](html/19%20-%20Unidade%202%20-%2012.2%20An%C3%A1lise%20de%20res%C3%ADduos%20no%20Python.html)
- [20 - Unidade 2 - 13. Síntese dos método.html](html/20%20-%20Unidade%202%20-%2013.%20S%C3%ADntese%20dos%20m%C3%A9todo.html)
- … e mais 16 arquivos em [html/](html/)

## Roteiro de estudo

1. Leia as páginas na ordem apresentada pelo módulo.
2. Consulte os PDFs e apresentações enquanto registra definições, hipóteses e exemplos.
3. Execute notebooks e códigos, verificando entradas, saídas e limitações.
4. Ao final, responda:

   - Como você explicaria **Unidade 2 - Orientações de Estudo** sem consultar o material?
   - Como você explicaria **Unidade 2 - 1. Introdução aos Modelos lineares Generalizados** sem consultar o material?
   - Como você explicaria **Unidade 2 - 2.1. Famílias exponenciais - parte 1** sem consultar o material?
   - Como você explicaria **Unidade 2 - 2.2. Família Exponencial - parte 2** sem consultar o material?
   - Como você explicaria **Unidade 2 - 3. Definição de um GLM** sem consultar o material?
