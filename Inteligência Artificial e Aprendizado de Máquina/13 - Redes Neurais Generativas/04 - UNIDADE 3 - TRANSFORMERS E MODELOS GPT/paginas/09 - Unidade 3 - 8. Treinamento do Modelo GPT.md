# Unidade 3 - 8. Treinamento do Modelo GPT

- Origem: [Canvas](https://pucminas.instructure.com/courses/230806/pages/unidade-3-8-treinamento-do-modelo-gpt)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar o seguinte tópico:**

- Etapas do Treinamento de Modelos GPT.

**Ao final, você será capaz de:**

- Reconhecer as principais etapas envolvidas no treinamento de um modelo GPT, desde a preparação dos dados até o ajuste dos parâmetros.

---

#### **Treinamento do modelo GPT**

Na videoaula a seguir, você irá entender de forma clara como ocorre o treinamento de um modelo GPT, explorando o processo pelo qual a rede aprende a prever a próxima palavra de um texto. A videoaula destaca que, ao final de toda a arquitetura Transformer o modelo utiliza uma camada densa com ativação Softmax para calcular a probabilidade de cada palavra do vocabulário ser a próxima na sequência. Assim, se o vocabulário possui 10.000 palavras, o GPT precisa gerar uma distribuição de probabilidade para todas elas, selecionando aquela mais coerente de acordo com o contexto já processado. Esse comportamento é o que torna o GPT capaz de manter fluidez e consistência ao longo de um texto.

Além disso, você verá como essa lógica se conecta ao pré‑treinamento em larga escala, no qual o objetivo é simplesmente aprender a tarefa de language modeling: prever o próximo token com base nos anteriores. Durante o treinamento, milhões de exemplos fazem com que a rede ajuste continuamente suas matrizes internas para que, a cada etapa, ela fique mais precisa em capturar relações de contexto, estilo e coerência semântica. A videoaula também explica como, durante a inferência, o modelo repete esse processo palavra por palavra, consultando o contexto acumulado para gerar a sequência final. Vamos entender como o GPT realmente “aprende a escrever”? Dê o play no vídeo a seguir!

#### **Transformer Models (GPT Models)**

Em nossa próxima videoaula, você irá compreender como os modelos Transformer se desdobram em diferentes arquiteturas e como cada uma delas atende a um tipo específico de tarefa em processamento de linguagem natural. Você verá que o GPT é um modelo decoder‑only, projetado para geração de texto sequencial a partir de mecanismos como causal masking, analisando apenas os tokens anteriores para prever o próximo. Por outro lado, modelos como BERT, baseados apenas em encoder, são usados para tarefas de compreensão, como classificação, análise semântica e resposta a perguntas. Já arquiteturas encoder‑decoder, como o T5, combinam ambos os lados para resolver tarefas de transformação de texto, como tradução, resumo e reformulação. Essa distinção permite entender por que diferentes modelos prosperam em tarefas diferentes, apesar de todos compartilharem a mesma base Transformer.

Além disso, a aula faz um panorama evolutivo dos modelos GPT, desde o lançamento do GPT‑1, em 2018, com 120 milhões de parâmetros, passando pelo GPT‑2, com 1,5 bilhão, até o salto monumental do GPT‑3, lançado em 2020 com 175 bilhões de parâmetros. Também é abordada a chegada do GPT‑4, em 2023, cuja arquitetura completa permanece fechada, mas que introduziu capacidades multimodais e melhorias significativas no desempenho. Você irá entender ainda como surgiu o ChatGPT, baseado inicialmente no GPT‑3.5, e como seu treinamento envolve supervised fine‑tuning, reward modeling e reinforcement learning from human feedback (RLHF). Essa combinação fez do ChatGPT uma ferramenta extremamente robusta, capaz de interagir de forma natural, coerente e contextual. Pronto(a) para entender como esses modelos revolucionaram o processamento de linguagem? Então, assista à videoaula!

#### **Enunciado do Projeto (winemag-data)**

Na videoaula a seguir, você irá conhecer o projeto final desta unidade, que consiste em utilizar um conjunto real de reviews de vinhos para treinar um modelo generativo baseado na arquitetura Transformer. O dataset escolhido contém aproximadamente 130 mil avaliações, incluindo descrições detalhadas dos vinhos, informações de região, variedade, país de origem e outros atributos relevantes. A ideia central é aproveitar o campo description, que traz textos ricos e bem estruturados, para ensinar o modelo a capturar o estilo e o vocabulário característico dessas avaliações profissionais.  
Além disso, você verá como o objetivo do projeto não é criar um grande modelo generalista como GPT, mas sim um gerador especializado, capaz de produzir novas descrições de vinhos seguindo o estilo presente no dataset. Embora a quantidade de textos seja relativamente pequena para padrões de modelos de linguagem de grande escala, ela é suficiente para treinar um modelo especializado que gera frases coerentes, estruturadas e com vocabulário típico do universo enológico. Ao final, você irá testar o modelo produzindo novas avaliações e analisando o quanto elas se aproximam do padrão aprendido. Preparado(a) para unir NLP, Transformers e criatividade em um único projeto? Então, vamos começar!

#### **Preparando e Treinando o Modelo**

Em nossa próxima videoaula, você irá acompanhar passo a passo como preparar o dataset de reviews de vinhos e construir um modelo Transformer capaz de gerar novos textos no estilo das descrições originais. A videoaula começa mostrando como organizar o ambiente de trabalho no Google Colab, criando pastas para checkpoints e módulos, além de carregar o arquivo JSON com as avaliações. Você verá a importância de usar GPU sempre que possível, já que o treinamento de modelos baseados em Transformers pode ser bem mais demorado em CPU. Também será apresentado um conjunto de parâmetros essenciais que determinam tanto a capacidade quanto a eficiência do modelo durante o aprendizado.

Além disso, você verá como ocorre a tokenização dos textos, convertendo as descrições dos vinhos em sequências de índices numéricos dentro de um vocabulário limitado a 10.000 palavras. A videoaula também apresenta a criação do conjunto de treinamento com entrada e saída deslocadas (input e target), permitindo que o modelo aprenda a prever o próximo token. Em seguida, são incluídos todos os componentes aprendidos ao longo das aulas teóricas: causal masking, bloco Transformer completo, embeddings de palavras e embeddings posicionais. Por fim, o notebook constrói o modelo final, instala callbacks para salvar checkpoints e inicia o processo de treinamento. Ao final dessa etapa, seu modelo estará pronto para gerar novas avaliações de vinhos baseadas no estilo do dataset original. Assista à videoaula para aprender como transformar teoria em prática e ver seu próprio modelo generativo ganhar vida!

#### **Analisando o GPT**

Na videoaula a seguir, você irá analisar o comportamento do modelo GPT que foi treinado no dataset de reviews de vinhos, observando como ele gera texto e como utiliza o mecanismo de atenção para escolher cada próxima palavra. Após completar cinco épocas de treinamento, o modelo passa a produzir descrições inéditas, mas fortemente inspiradas no padrão do corpus. A videoaula também demonstra o impacto da temperatura, parâmetro que controla o nível de criatividade do modelo: valores altos geram textos mais aventureiros e variados, enquanto valores baixos resultam em escolhas mais determinísticas e previsíveis. Isso permite comparar estilos de geração e avaliar o quanto o modelo aprendeu as estruturas e o vocabulário característicos das avaliações de vinho.

Além disso, você verá uma análise visual do mecanismo de atenção, identificando quais palavras dentro da sequência gerada recebem maior peso na hora de prever o próximo token. O modelo destaca termos fundamentais do contexto e utiliza essas pistas para continuar a construção da descrição. A videoaula explora como essas atenções variam ao longo da frase, como a probabilidade de escolha muda conforme os tokens anteriores e como diferentes palavras se influenciam mutuamente. Essa visualização torna evidente o funcionamento interno do Transformer: mesmo em um modelo pequeno, treinado com um dataset limitado, ele consegue capturar padrões semânticos e sintáticos de maneira impressionante. Ao final, você compreenderá como o GPT aprende, como decide e como pode ser adaptado para gerar textos em qualquer domínio. Vamos começar?
