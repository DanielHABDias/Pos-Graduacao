# 04 - UNIDADE 3 - TRANSFORMERS E MODELOS GPT

[← Voltar à disciplina](../README.md)

## Resumo da unidade

A unidade detalha atenção causal, múltiplas cabeças, posição e treinamento de GPT. A máscara causal impede que o modelo consulte tokens futuros durante a previsão.

### Exemplo

Ao prever a próxima palavra, o token na posição t pode usar apenas as posições anteriores e a própria posição, nunca o restante da resposta.

## Conteúdo da unidade

- [Unidade 3 - Orientações de Estudo](paginas/01%20-%20Unidade%203%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md) — Seja muito bem-vindo e bem-vinda à Unidade 3! Nesta etapa, você estudará sobre Transformers e os modelos GPT, arquiteturas que revolucionaram a forma como lidamos com dados sequenciais e tornaram-se centrais em tarefas de geração e compreensão de texto. Após estudar, nas unidades anteriores, modelos generativos baseados em autoencoders, adversarial training e difusão, agora avançaremos para arquiteturas capazes de…
- [Unidade 3 - 1. Transformers e Modelos GPT](paginas/02%20-%20Unidade%203%20-%201.%20Transformers%20e%20Modelos%20GPT.md) — - Visão Geral dos Transformers e dos Modelos GPT. - Compreender os princípios gerais da arquitetura Transformer e o papel dos modelos GPT no contexto dos modelos generativos. Na primeira videoaula desta unidade, você irá conhecer os fundamentos da arquitetura Transformer e entender por que ela revolucionou o campo de processamento de linguagem natural, visão computacional e modelos generativos. Partindo do artigo…
- [Unidade 3 - 2. Mecanismo de Atenção](paginas/03%20-%20Unidade%203%20-%202.%20Mecanismo%20de%20Aten%C3%A7%C3%A3o.md) — - Entender como o mecanismo de atenção permite ao modelo identificar relações de dependência entre diferentes partes de uma sequência. Na videoaula a seguir, você irá compreender de forma clara e intuitiva como funcionam os mecanismos de atenção, o componente central que tornou os Transformers tão poderosos e eficientes. A aula começa mostrando um ponto essencial: quando escrevemos uma frase, a escolha da próxima…
- [Unidade 3 - 3. Attention Head](paginas/04%20-%20Unidade%203%20-%203.%20Attention%20Head.md) — - Identificar o papel de uma attention head no cálculo das relações entre consultas, chaves e valores. Em nossa próxima videoaula, você irá compreender com profundidade o funcionamento interno do mecanismo de atenção introduzido no artigo "Attention Is All You Need", que deu origem à arquitetura Transformer. A aula mostra como, para prever a próxima palavra, o modelo não trata o texto como uma sequência fixa, mas…
- [Unidade 3 - 4. Multihead Attention](paginas/05%20-%20Unidade%203%20-%204.%20Multihead%20Attention.md) — - Multihead Attention e Captura de Múltiplas Relações. - Compreender como o multihead attention amplia a capacidade do modelo de representar diferentes padrões de dependência em uma sequência. Na videoaula a seguir, você irá entender como o mecanismo de Multi‑Head Attention expande o poder do self‑attention tradicional, permitindo que o modelo capture múltiplos tipos de relações e contextos simultaneamente. Em vez…
- [Unidade 3 - 5. Causal Masking](paginas/06%20-%20Unidade%203%20-%205.%20Causal%20Masking.md) — - Causal Masking em Modelos Autorregressivos. - Reconhecer a função do causal masking no controle do acesso à informação futura durante a geração de texto. Na próxima videoaula, você irá entender o conceito de Causal Masking, um dos componentes essenciais para que modelos como o GPT consigam gerar texto de maneira coerente e sequencial. Embora o mecanismo de atenção analise todas as palavras em paralelo, durante o…
- [Unidade 3 - 6. Bloco Transformer](paginas/07%20-%20Unidade%203%20-%206.%20Bloco%20Transformer.md) — - Estrutura e Componentes do Bloco Transformer. - Identificar os principais componentes de um bloco Transformer e compreender sua organização funcional. Na videoaula a seguir, você irá compreender como funciona o bloco Transformer, a unidade fundamental que compõe toda a arquitetura dos modelos baseados em Transformers, como GPT, BERT e muitos outros. O bloco combina diversos elementos vistos em aulas anteriores em…
- [Unidade 3 - 7. Positional Encoding](paginas/08%20-%20Unidade%203%20-%207.%20Positional%20Encoding.md) — - Compreender a necessidade do positional encoding para representar a ordem dos tokens em sequências textuais. Em nossa próxima videoaula, você irá entender por que os Transformers precisam de um componente adicional chamado Positional Encoding para funcionar corretamente. Embora o mecanismo de atenção seja extremamente poderoso e processado completamente em paralelo, ele possui uma limitação fundamental: ele não…
- [Unidade 3 - 8. Treinamento do Modelo GPT](paginas/09%20-%20Unidade%203%20-%208.%20Treinamento%20do%20Modelo%20GPT.md) — - Reconhecer as principais etapas envolvidas no treinamento de um modelo GPT, desde a preparação dos dados até o ajuste dos parâmetros. Na videoaula a seguir, você irá entender de forma clara como ocorre o treinamento de um modelo GPT, explorando o processo pelo qual a rede aprende a prever a próxima palavra de um texto. A videoaula destaca que, ao final de toda a arquitetura Transformer o modelo utiliza uma camada…
- [Unidade 3 - Material Complementar](paginas/10%20-%20Unidade%203%20-%20Material%20Complementar.md) — Para aprofundar os conhecimentos apresentados nesta unidade, recomendamos a leitura do livro abaixo, que oferece uma visão prática e acessível de Processamento de Linguagem Natural: LANE, Hobson; HOWARD, Cole; HAPKE, Hannes. Natural Language Processing in Action . 1st edition. 2019. 1 online resource (544 pages). Disponível em:…

## Materiais

### Apresentações (1)

- [Unidade 3 - Transformers e modelos GPT.pptx](documentos/Unidade%203%20-%20Transformers%20e%20modelos%20GPT.pptx)

### Notebooks (1)

- [nlp_unidade_III_winemag_data_with_transformers.ipynb](documentos/nlp_unidade_III_winemag_data_with_transformers.ipynb)

### Páginas e textos (10)

- [01 - Unidade 3 - Orientações de Estudo.md](paginas/01%20-%20Unidade%203%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md)
- [02 - Unidade 3 - 1. Transformers e Modelos GPT.md](paginas/02%20-%20Unidade%203%20-%201.%20Transformers%20e%20Modelos%20GPT.md)
- [03 - Unidade 3 - 2. Mecanismo de Atenção.md](paginas/03%20-%20Unidade%203%20-%202.%20Mecanismo%20de%20Aten%C3%A7%C3%A3o.md)
- [04 - Unidade 3 - 3. Attention Head.md](paginas/04%20-%20Unidade%203%20-%203.%20Attention%20Head.md)
- [05 - Unidade 3 - 4. Multihead Attention.md](paginas/05%20-%20Unidade%203%20-%204.%20Multihead%20Attention.md)
- [06 - Unidade 3 - 5. Causal Masking.md](paginas/06%20-%20Unidade%203%20-%205.%20Causal%20Masking.md)
- [07 - Unidade 3 - 6. Bloco Transformer.md](paginas/07%20-%20Unidade%203%20-%206.%20Bloco%20Transformer.md)
- [08 - Unidade 3 - 7. Positional Encoding.md](paginas/08%20-%20Unidade%203%20-%207.%20Positional%20Encoding.md)
- [09 - Unidade 3 - 8. Treinamento do Modelo GPT.md](paginas/09%20-%20Unidade%203%20-%208.%20Treinamento%20do%20Modelo%20GPT.md)
- [10 - Unidade 3 - Material Complementar.md](paginas/10%20-%20Unidade%203%20-%20Material%20Complementar.md)

### Imagens (5)

- [banner-pos-2022-1.jpg](images/banner-pos-2022-1.jpg)
- [banner-pos-2022.jpg](images/banner-pos-2022.jpg)
- [icone-bussola.png](images/icone-bussola.png)
- [Leitura.png](images/Leitura.png)
- [material-b.png](images/material-b.png)

### HTML original (10)

- [01 - Unidade 3 - Orientações de Estudo.html](html/01%20-%20Unidade%203%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.html)
- [02 - Unidade 3 - 1. Transformers e Modelos GPT.html](html/02%20-%20Unidade%203%20-%201.%20Transformers%20e%20Modelos%20GPT.html)
- [03 - Unidade 3 - 2. Mecanismo de Atenção.html](html/03%20-%20Unidade%203%20-%202.%20Mecanismo%20de%20Aten%C3%A7%C3%A3o.html)
- [04 - Unidade 3 - 3. Attention Head.html](html/04%20-%20Unidade%203%20-%203.%20Attention%20Head.html)
- [05 - Unidade 3 - 4. Multihead Attention.html](html/05%20-%20Unidade%203%20-%204.%20Multihead%20Attention.html)
- [06 - Unidade 3 - 5. Causal Masking.html](html/06%20-%20Unidade%203%20-%205.%20Causal%20Masking.html)
- [07 - Unidade 3 - 6. Bloco Transformer.html](html/07%20-%20Unidade%203%20-%206.%20Bloco%20Transformer.html)
- [08 - Unidade 3 - 7. Positional Encoding.html](html/08%20-%20Unidade%203%20-%207.%20Positional%20Encoding.html)
- [09 - Unidade 3 - 8. Treinamento do Modelo GPT.html](html/09%20-%20Unidade%203%20-%208.%20Treinamento%20do%20Modelo%20GPT.html)
- [10 - Unidade 3 - Material Complementar.html](html/10%20-%20Unidade%203%20-%20Material%20Complementar.html)

## Roteiro de estudo

1. Leia as páginas na ordem apresentada pelo módulo.
2. Consulte os PDFs e apresentações enquanto registra definições, hipóteses e exemplos.
3. Execute notebooks e códigos, verificando entradas, saídas e limitações.
4. Ao final, responda:

   - Como você explicaria **Unidade 3 - Orientações de Estudo** sem consultar o material?
   - Como você explicaria **Unidade 3 - 1. Transformers e Modelos GPT** sem consultar o material?
   - Como você explicaria **Unidade 3 - 2. Mecanismo de Atenção** sem consultar o material?
   - Como você explicaria **Unidade 3 - 3. Attention Head** sem consultar o material?
   - Como você explicaria **Unidade 3 - 4. Multihead Attention** sem consultar o material?
