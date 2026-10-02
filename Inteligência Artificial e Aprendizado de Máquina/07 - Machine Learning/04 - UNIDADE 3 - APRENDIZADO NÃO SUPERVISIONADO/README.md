# 04 - UNIDADE 3 - APRENDIZADO NÃO SUPERVISIONADO

[← Voltar à disciplina](../README.md)

## Resumo da unidade

A unidade estuda regras de associação, agrupamento, medidas de distância e detecção de observações atípicas. Como não existe rótulo de resposta, a validação combina métricas internas e utilidade no domínio.

### Exemplo

Em uma cesta de compras, suporte mede frequência conjunta. Confiança mede com que frequência B aparece quando A aparece. Lift compara essa relação com o acaso.

## Fórmulas essenciais

### Lift de uma regra

$$
\mathrm{lift}(A\to B)=\frac{P(A\cap B)}{P(A)P(B)}
$$

Valores acima de 1 indicam ocorrência conjunta maior que a esperada sob independência.

### Distância euclidiana

$$
d(\mathbf{x},\mathbf{y})=\sqrt{\sum_{j=1}^{p}(x_j-y_j)^2}
$$

Compara vetores numéricos na mesma escala.


## Conteúdo da unidade

- [Unidade 3 - Orientações de Estudo](paginas/01%20-%20Unidade%203%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md)
- [Unidade 3 - 1. Regras de Associação: definições](paginas/04%20-%20Unidade%203%20-%201.%20Regras%20de%20Associa%C3%A7%C3%A3o_%20defini%C3%A7%C3%B5es.md)
- [Unidade 3 - 2. Regras de Associação: suporte e confiança](paginas/06%20-%20Unidade%203%20-%202.%20Regras%20de%20Associa%C3%A7%C3%A3o_%20suporte%20e%20confian%C3%A7a.md)
- [Unidade 3 - 3. Regras de associação: conjuntos de itens frequentes](paginas/08%20-%20Unidade%203%20-%203.%20Regras%20de%20associa%C3%A7%C3%A3o_%20conjuntos%20de%20itens%20frequentes.md)
- [Unidade 3 - 4. Regras de Associação: algoritmos](paginas/10%20-%20Unidade%203%20-%204.%20Regras%20de%20Associa%C3%A7%C3%A3o_%20algoritmos.md)
- [Unidade 3 - 5. Regras de Associação: avaliação das regras](paginas/12%20-%20Unidade%203%20-%205.%20Regras%20de%20Associa%C3%A7%C3%A3o_%20avalia%C3%A7%C3%A3o%20das%20regras.md)
- [Unidade 3 - Aula Prática 1: Colab - Regras de Associação](paginas/14%20-%20Unidade%203%20-%20Aula%20Pr%C3%A1tica%201_%20Colab%20-%20Regras%20de%20Associa%C3%A7%C3%A3o.md)
- [Unidade 3 - 6. Clustering](paginas/18%20-%20Unidade%203%20-%206.%20Clustering.md)
- [Unidade 3 - 7. Estruturas de dados para aprendizado não supervisionado](paginas/20%20-%20Unidade%203%20-%207.%20Estruturas%20de%20dados%20para%20aprendizado%20n%C3%A3o%20supervisionado.md)
- [Unidade 3 - 8. Medidas de distância de variáveis qualitativas](paginas/22%20-%20Unidade%203%20-%208.%20Medidas%20de%20dist%C3%A2ncia%20de%20vari%C3%A1veis%20qualitativas.md)
- [Unidade 3 - 9. Medidas de distância de variáveis quantitativas](paginas/24%20-%20Unidade%203%20-%209.%20Medidas%20de%20dist%C3%A2ncia%20de%20vari%C3%A1veis%20quantitativas.md)
- [Unidade 3 - 10. Métodos de agrupamento](paginas/28%20-%20Unidade%203%20-%2010.%20M%C3%A9todos%20de%20agrupamento.md)
- [Unidade 3 - 11. Algoritmos hierárquicos](paginas/30%20-%20Unidade%203%20-%2011.%20Algoritmos%20hier%C3%A1rquicos.md)
- [Unidade 3 - 12. DB-outlier](paginas/34%20-%20Unidade%203%20-%2012.%20DB-outlier.md)

## Materiais

### PDFs (12)

- [Slides - Algoritmos hierárquicos.pdf](documentos/Slides%20-%20Algoritmos%20hier%C3%A1rquicos.pdf) (arquivo indisponível ou ainda em processamento no Canvas)
- [Slides - DB-outlier.pdf](documentos/Slides%20-%20DB-outlier.pdf) (arquivo indisponível ou ainda em processamento no Canvas)
- [Slides - Estruturas de dados para aprendizado não supervisionado.pdf](documentos/Slides%20-%20Estruturas%20de%20dados%20para%20aprendizado%20n%C3%A3o%20supervisionado.pdf) (arquivo indisponível ou ainda em processamento no Canvas)
- [Slides - K-means.pdf](documentos/Slides%20-%20K-means.pdf) (arquivo indisponível ou ainda em processamento no Canvas)
- [Slides - Medidas de distância de variáveis qualitativas.pdf](documentos/Slides%20-%20Medidas%20de%20dist%C3%A2ncia%20de%20vari%C3%A1veis%20qualitativas.pdf) (arquivo indisponível ou ainda em processamento no Canvas)
- [Slides - Medidas de distância de variáveis quantitativas.pdf](documentos/Slides%20-%20Medidas%20de%20dist%C3%A2ncia%20de%20vari%C3%A1veis%20quantitativas.pdf) (arquivo indisponível ou ainda em processamento no Canvas)
- [Slides - Métodos de agrupamento.pdf](documentos/Slides%20-%20M%C3%A9todos%20de%20agrupamento.pdf) (arquivo indisponível ou ainda em processamento no Canvas)
- [Slides - Regras de associação - algoritmos.pdf](documentos/Slides%20-%20Regras%20de%20associa%C3%A7%C3%A3o%20-%20algoritmos.pdf) (arquivo indisponível ou ainda em processamento no Canvas)
- [Slides - Regras de associação - avaliação das regras.pdf](documentos/Slides%20-%20Regras%20de%20associa%C3%A7%C3%A3o%20-%20avalia%C3%A7%C3%A3o%20das%20regras.pdf) (arquivo indisponível ou ainda em processamento no Canvas)
- [Slides - Regras de associação - conjuntos de itens frequentes.pdf](documentos/Slides%20-%20Regras%20de%20associa%C3%A7%C3%A3o%20-%20conjuntos%20de%20itens%20frequentes.pdf) (arquivo indisponível ou ainda em processamento no Canvas)
- [Slides - Regras de associação - definições.pdf](documentos/Slides%20-%20Regras%20de%20associa%C3%A7%C3%A3o%20-%20defini%C3%A7%C3%B5es.pdf) (arquivo indisponível ou ainda em processamento no Canvas)
- [Slides - Regras de associação - suporte e confiança.pdf](documentos/Slides%20-%20Regras%20de%20associa%C3%A7%C3%A3o%20-%20suporte%20e%20confian%C3%A7a.pdf) (arquivo indisponível ou ainda em processamento no Canvas)

### Notebooks (1)

- [Regras_de_associacao.ipynb](documentos/Regras_de_associacao.ipynb) (arquivo indisponível ou ainda em processamento no Canvas)

### Páginas e textos (14)

- [01 - Unidade 3 - Orientações de Estudo.md](paginas/01%20-%20Unidade%203%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md)
- [04 - Unidade 3 - 1. Regras de Associação_ definições.md](paginas/04%20-%20Unidade%203%20-%201.%20Regras%20de%20Associa%C3%A7%C3%A3o_%20defini%C3%A7%C3%B5es.md)
- [06 - Unidade 3 - 2. Regras de Associação_ suporte e confiança.md](paginas/06%20-%20Unidade%203%20-%202.%20Regras%20de%20Associa%C3%A7%C3%A3o_%20suporte%20e%20confian%C3%A7a.md)
- [08 - Unidade 3 - 3. Regras de associação_ conjuntos de itens frequentes.md](paginas/08%20-%20Unidade%203%20-%203.%20Regras%20de%20associa%C3%A7%C3%A3o_%20conjuntos%20de%20itens%20frequentes.md)
- [10 - Unidade 3 - 4. Regras de Associação_ algoritmos.md](paginas/10%20-%20Unidade%203%20-%204.%20Regras%20de%20Associa%C3%A7%C3%A3o_%20algoritmos.md)
- [12 - Unidade 3 - 5. Regras de Associação_ avaliação das regras.md](paginas/12%20-%20Unidade%203%20-%205.%20Regras%20de%20Associa%C3%A7%C3%A3o_%20avalia%C3%A7%C3%A3o%20das%20regras.md)
- [14 - Unidade 3 - Aula Prática 1_ Colab - Regras de Associação.md](paginas/14%20-%20Unidade%203%20-%20Aula%20Pr%C3%A1tica%201_%20Colab%20-%20Regras%20de%20Associa%C3%A7%C3%A3o.md)
- [18 - Unidade 3 - 6. Clustering.md](paginas/18%20-%20Unidade%203%20-%206.%20Clustering.md)
- [20 - Unidade 3 - 7. Estruturas de dados para aprendizado não supervisionado.md](paginas/20%20-%20Unidade%203%20-%207.%20Estruturas%20de%20dados%20para%20aprendizado%20n%C3%A3o%20supervisionado.md)
- [22 - Unidade 3 - 8. Medidas de distância de variáveis qualitativas.md](paginas/22%20-%20Unidade%203%20-%208.%20Medidas%20de%20dist%C3%A2ncia%20de%20vari%C3%A1veis%20qualitativas.md)
- [24 - Unidade 3 - 9. Medidas de distância de variáveis quantitativas.md](paginas/24%20-%20Unidade%203%20-%209.%20Medidas%20de%20dist%C3%A2ncia%20de%20vari%C3%A1veis%20quantitativas.md)
- [28 - Unidade 3 - 10. Métodos de agrupamento.md](paginas/28%20-%20Unidade%203%20-%2010.%20M%C3%A9todos%20de%20agrupamento.md)
- [30 - Unidade 3 - 11. Algoritmos hierárquicos.md](paginas/30%20-%20Unidade%203%20-%2011.%20Algoritmos%20hier%C3%A1rquicos.md)
- [34 - Unidade 3 - 12. DB-outlier.md](paginas/34%20-%20Unidade%203%20-%2012.%20DB-outlier.md)

### HTML original (14)

- [01 - Unidade 3 - Orientações de Estudo.html](html/01%20-%20Unidade%203%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.html)
- [04 - Unidade 3 - 1. Regras de Associação_ definições.html](html/04%20-%20Unidade%203%20-%201.%20Regras%20de%20Associa%C3%A7%C3%A3o_%20defini%C3%A7%C3%B5es.html)
- [06 - Unidade 3 - 2. Regras de Associação_ suporte e confiança.html](html/06%20-%20Unidade%203%20-%202.%20Regras%20de%20Associa%C3%A7%C3%A3o_%20suporte%20e%20confian%C3%A7a.html)
- [08 - Unidade 3 - 3. Regras de associação_ conjuntos de itens frequentes.html](html/08%20-%20Unidade%203%20-%203.%20Regras%20de%20associa%C3%A7%C3%A3o_%20conjuntos%20de%20itens%20frequentes.html)
- [10 - Unidade 3 - 4. Regras de Associação_ algoritmos.html](html/10%20-%20Unidade%203%20-%204.%20Regras%20de%20Associa%C3%A7%C3%A3o_%20algoritmos.html)
- [12 - Unidade 3 - 5. Regras de Associação_ avaliação das regras.html](html/12%20-%20Unidade%203%20-%205.%20Regras%20de%20Associa%C3%A7%C3%A3o_%20avalia%C3%A7%C3%A3o%20das%20regras.html)
- [14 - Unidade 3 - Aula Prática 1_ Colab - Regras de Associação.html](html/14%20-%20Unidade%203%20-%20Aula%20Pr%C3%A1tica%201_%20Colab%20-%20Regras%20de%20Associa%C3%A7%C3%A3o.html)
- [18 - Unidade 3 - 6. Clustering.html](html/18%20-%20Unidade%203%20-%206.%20Clustering.html)
- [20 - Unidade 3 - 7. Estruturas de dados para aprendizado não supervisionado.html](html/20%20-%20Unidade%203%20-%207.%20Estruturas%20de%20dados%20para%20aprendizado%20n%C3%A3o%20supervisionado.html)
- [22 - Unidade 3 - 8. Medidas de distância de variáveis qualitativas.html](html/22%20-%20Unidade%203%20-%208.%20Medidas%20de%20dist%C3%A2ncia%20de%20vari%C3%A1veis%20qualitativas.html)
- [24 - Unidade 3 - 9. Medidas de distância de variáveis quantitativas.html](html/24%20-%20Unidade%203%20-%209.%20Medidas%20de%20dist%C3%A2ncia%20de%20vari%C3%A1veis%20quantitativas.html)
- [28 - Unidade 3 - 10. Métodos de agrupamento.html](html/28%20-%20Unidade%203%20-%2010.%20M%C3%A9todos%20de%20agrupamento.html)
- [30 - Unidade 3 - 11. Algoritmos hierárquicos.html](html/30%20-%20Unidade%203%20-%2011.%20Algoritmos%20hier%C3%A1rquicos.html)
- [34 - Unidade 3 - 12. DB-outlier.html](html/34%20-%20Unidade%203%20-%2012.%20DB-outlier.html)

## Roteiro de estudo

1. Leia as páginas na ordem apresentada pelo módulo.
2. Consulte os PDFs e apresentações enquanto registra definições, hipóteses e exemplos.
3. Execute notebooks e códigos, verificando entradas, saídas e limitações.
4. Ao final, responda:

   - Como você explicaria **Unidade 3 - Orientações de Estudo** sem consultar o material?
   - Como você explicaria **Unidade 3 - 1. Regras de Associação: definições** sem consultar o material?
   - Como você explicaria **Unidade 3 - 2. Regras de Associação: suporte e confiança** sem consultar o material?
   - Como você explicaria **Unidade 3 - 3. Regras de associação: conjuntos de itens frequentes** sem consultar o material?
   - Como você explicaria **Unidade 3 - 4. Regras de Associação: algoritmos** sem consultar o material?
