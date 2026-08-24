# 04 - Python para Ciência de Dados

## SUMÁRIO

- [UNIDADE 01](#unidade-01)
	- [TEMAS ABORDADOS](#temas-abordados)
	- [Por que Python?](#por-que-python)
	- [Variáveis e tipos de dados](#variáveis-e-tipos-de-dados)
	- [Operadores e estruturas de controle](#operadores-e-estruturas-de-controle)
	- [Funções e módulos](#funções-e-módulos)
- [UNIDADE 02](#unidade-02)
	- [Estruturas de dados](#estruturas-de-dados)
	- [Listas](#listas)
	- [Tuplas](#tuplas)
	- [Conjuntos](#conjuntos)
	- [Dicionários](#dicionários)
- [UNIDADE 03](#unidade-03)
	- [NumPy](#numpy)
	- [Pandas](#pandas)
	- [Series e DataFrames](#series-e-dataframes)
	- [Importação e inspeção de datasets](#importação-e-inspeção-de-datasets)
	- [Seleção e filtragem](#seleção-e-filtragem)
	- [Limpeza e transformação](#limpeza-e-transformação)
- [UNIDADE 04](#unidade-04)
	- [Visualização de dados](#visualização-de-dados)
	- [Gráficos com Matplotlib](#gráficos-com-matplotlib)
	- [Gráficos com Seaborn](#gráficos-com-seaborn)
	- [Boas práticas](#boas-práticas)

## UNIDADE 01

### TEMAS ABORDADOS

- Sintaxe básica e principais características da linguagem Python.
- Variáveis, tipos de dados, operadores e conversões.
- Estruturas condicionais e de repetição.
- Funções, módulos e tratamento de exceções.
- Organização de scripts e notebooks para análise de dados.

### Por que Python?

Python é uma linguagem de programação de alto nível, interpretada e de propósito geral. Sua sintaxe simples, a grande comunidade e o ecossistema de bibliotecas voltadas para dados fazem dela uma das principais ferramentas para ciência de dados.

Em um projeto de dados, Python pode ser usado para:

- Coletar dados de arquivos, bancos de dados e APIs;
- Preparar, limpar e transformar informações;
- Explorar dados e identificar padrões;
- Criar visualizações e modelos estatísticos;
- Automatizar tarefas repetitivas.

### Variáveis e tipos de dados

Variáveis associam nomes a valores. Python identifica o tipo do valor automaticamente, mas é importante compreender os tipos mais comuns:

```python
nome = "Ana"             # str: texto
idade = 30               # int: número inteiro
altura = 1.68            # float: número decimal
aprovado = True          # bool: verdadeiro ou falso
ausente = None           # ausência de valor
```

Os tipos podem ser consultados com `type()` e convertidos quando necessário:

```python
valor = "42"
numero = int(valor)
texto = str(numero)
```

### Operadores e estruturas de controle

Os operadores aritméticos mais utilizados são `+`, `-`, `*`, `/`, `//`, `%` e `**`. Operadores relacionais (`==`, `!=`, `>`, `<`, `>=` e `<=`) produzem valores booleanos. Os operadores lógicos `and`, `or` e `not` combinam condições.

```python
nota = 8.5

if nota >= 7:
		situacao = "aprovado"
else:
		situacao = "reprovado"

for valor in [10, 20, 30]:
		print(valor * 2)
```

Use `while` quando a repetição depender de uma condição e `for` quando for necessário percorrer uma sequência. `break` encerra um laço e `continue` pula para a próxima iteração.

### Funções e módulos

Funções agrupam uma tarefa e podem receber parâmetros e retornar resultados:

```python
def media(valores):
		return sum(valores) / len(valores)

resultado = media([7, 8, 9])
```

Módulos permitem reutilizar código. Bibliotecas podem ser importadas com `import` ou com a seleção de um recurso específico:

```python
import math
from datetime import date

raiz = math.sqrt(25)
hoje = date.today()
```

Erros esperados devem ser tratados sem esconder problemas de programação:

```python
try:
		valor = float(input("Digite um número: "))
except ValueError:
		print("Entrada inválida")
```

## UNIDADE 02

### Estruturas de dados

Estruturas de dados organizam valores para que possam ser consultados e modificados. A escolha depende da necessidade de ordem, mutabilidade e unicidade:

| Estrutura | Ordenada | Mutável | Permite repetição | Uso comum |
| --- | --- | --- | --- | --- |
| Lista | Sim | Sim | Sim | Coleções que mudam |
| Tupla | Sim | Não | Sim | Registros imutáveis |
| Conjunto | Não | Sim | Não | Valores únicos |
| Dicionário | Por inserção | Sim | Chaves únicas | Dados por chave |

### Listas

Listas são sequências mutáveis e indexadas a partir de zero. Os métodos mais utilizados são `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `sort()` e `reverse()`.

```python
notas = [7.0, 8.5, 6.0]
notas.append(9.0)
notas.sort()

primeira = notas[0]
ultimas = notas[-2:]
aprovados = [nota for nota in notas if nota >= 7]
```

### Tuplas

Tuplas são sequências imutáveis, adequadas para representar um conjunto fixo de valores:

```python
coordenada = (-19.92, -43.94)
latitude, longitude = coordenada
```

### Conjuntos

Conjuntos armazenam valores únicos e são úteis para eliminar duplicidades e realizar operações de conjunto:

```python
categorias = {"livro", "curso", "livro"}
outras = {"curso", "evento"}

uniao = categorias | outras
intersecao = categorias & outras
```

### Dicionários

Dicionários armazenam pares de chave e valor. As chaves devem ser únicas e permitem acesso direto à informação:

```python
aluno = {"nome": "Ana", "nota": 8.5}
aluno["aprovado"] = aluno["nota"] >= 7

nome = aluno.get("nome")
for chave, valor in aluno.items():
		print(chave, valor)
```

## UNIDADE 03

### NumPy

NumPy fornece arrays multidimensionais e operações numéricas eficientes. Diferentemente de listas, seus arrays são adequados para cálculos vetorizados e trabalham com um tipo de dado homogêneo.

```python
import numpy as np

valores = np.array([10, 20, 30, 40])
media = valores.mean()
normalizados = (valores - valores.mean()) / valores.std()
```

### Pandas

Pandas é uma biblioteca para manipulação e análise de dados tabulares. Seus objetos principais são `Series` e `DataFrame`.

### Series e DataFrames

Uma `Series` é uma sequência unidimensional rotulada. Um `DataFrame` é uma tabela composta por linhas e colunas, semelhante a uma planilha ou tabela de banco de dados.

```python
import pandas as pd

dados = {
		"produto": ["A", "B", "C"],
		"vendas": [120, 85, 150],
		"regiao": ["Sul", "Norte", "Sul"],
}
df = pd.DataFrame(dados)
```

### Importação e inspeção de datasets

Datasets podem ser carregados de CSV, Excel, JSON e outras fontes:

```python
df = pd.read_csv("vendas.csv")

df.head()
df.shape
df.info()
df.describe(numeric_only=True)
df.dtypes
```

Antes de analisar, verifique dimensões, tipos, valores ausentes, duplicidades e possíveis inconsistências. Essa etapa evita conclusões baseadas em dados incompletos ou interpretados incorretamente.

### Seleção e filtragem

Colunas podem ser selecionadas pelo nome e linhas podem ser filtradas por condições. `loc` trabalha com rótulos e `iloc` trabalha com posições inteiras.

```python
vendas_sul = df.loc[df["regiao"] == "Sul", ["produto", "vendas"]]
primeiras_linhas = df.iloc[:2]
```

### Limpeza e transformação

Operações comuns incluem renomear colunas, converter tipos, tratar valores ausentes, remover duplicidades e criar novas variáveis:

```python
df = df.drop_duplicates()
df["vendas"] = pd.to_numeric(df["vendas"], errors="coerce")
df["vendas"] = df["vendas"].fillna(0)
df["vendas_milhares"] = df["vendas"] / 1000
```

Para resumir dados, use `groupby()` e agregações:

```python
resumo = (
		df.groupby("regiao", as_index=False)["vendas"]
			.agg(total="sum", media="mean")
			.sort_values("total", ascending=False)
)
```

## UNIDADE 04

### Visualização de dados

Gráficos ajudam a comunicar distribuições, comparações, relações e tendências. A escolha deve acompanhar a pergunta da análise:

- **Barras**: comparar categorias;
- **Linhas**: acompanhar evolução ao longo do tempo;
- **Histograma**: observar a distribuição de uma variável numérica;
- **Dispersão**: investigar a relação entre duas variáveis;
- **Boxplot**: comparar distribuição e identificar possíveis outliers.

### Gráficos com Matplotlib

Matplotlib oferece controle detalhado sobre figuras, eixos, títulos, rótulos e legendas:

```python
import matplotlib.pyplot as plt

plt.bar(resumo["regiao"], resumo["total"])
plt.title("Vendas por região")
plt.xlabel("Região")
plt.ylabel("Total de vendas")
plt.tight_layout()
plt.show()
```

### Gráficos com Seaborn

Seaborn complementa o Matplotlib com uma interface orientada a datasets e estilos adequados à análise estatística:

```python
import seaborn as sns

sns.set_theme(style="whitegrid")
sns.scatterplot(data=df, x="vendas", y="produto", hue="regiao")
plt.tight_layout()
plt.show()
```

### Boas práticas

- Defina a pergunta antes de escolher o gráfico;
- Use títulos, rótulos de eixos e unidades claras;
- Evite distorções de escala e excesso de elementos decorativos;
- Preserve a consistência das cores entre gráficos;
- Destaque somente a informação relevante;
- Salve figuras com resolução e formato adequados ao destino.

## CONCLUSÃO

Python oferece a base de programação, enquanto NumPy, Pandas e as bibliotecas de visualização fornecem as ferramentas para transformar datasets em análises reproduzíveis. Um fluxo de trabalho típico é: carregar os dados, inspecionar sua qualidade, limpar e transformar as colunas, resumir os resultados e comunicar os achados por meio de visualizações adequadas.