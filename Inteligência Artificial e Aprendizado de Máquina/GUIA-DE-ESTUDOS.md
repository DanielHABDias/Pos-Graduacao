# Guia integrado de estudos

[← Voltar ao curso](README.md)

Este guia conecta as disciplinas da pós-graduação em uma única trajetória. Ele não substitui o material acadêmico: serve como mapa para revisão, prática deliberada e construção de portfólio.

## Mapa de competências

### 1. Dados e decisão

Disciplinas: Data Discovery, Python e Preparação e Integração de Dados.

Ao final deste eixo, você deve conseguir transformar uma pergunta de negócio em indicadores, localizar e integrar fontes, verificar qualidade, estruturar uma análise reproduzível e comunicar resultados. O ponto central é preservar a ligação entre dado, contexto e decisão: uma visualização tecnicamente correta ainda pode induzir ao erro se a métrica ou a população estiverem mal definidas.

Projeto sugerido: construir um pipeline que ingira dados públicos, execute validações, produza uma camada analítica e publique um painel com KPIs documentados.

### 2. Probabilidade, inferência e modelagem

Disciplinas: Estatística Geral e Modelos Estatísticos.

Este eixo fornece a linguagem para lidar com incerteza. Priorize distribuição amostral, estimação, intervalos de confiança, testes de hipóteses, regressão e diagnóstico de resíduos. Mais importante que aplicar uma fórmula é declarar hipóteses, verificar condições de uso e interpretar o tamanho do efeito junto da incerteza.

Projeto sugerido: analisar um fenômeno real com exploração, modelo estatístico, diagnóstico, interpretação dos coeficientes e discussão explícita das limitações.

### 3. Machine learning confiável

Disciplinas: Machine Learning, Cultura e Práticas DataOps e MLOps.

Conecte cada experimento a uma linha de base, uma divisão de dados sem vazamento e uma métrica coerente com o custo do erro. Trate dados, código, parâmetros e modelos como artefatos versionados. Em produção, monitore não apenas disponibilidade, mas qualidade de entrada, deriva, desempenho e impacto.

Projeto sugerido: treinar um classificador com pipeline de pré-processamento, validação cruzada, rastreamento de experimentos, API de inferência, testes e monitoramento básico.

### 4. Deep learning e visão computacional

Disciplinas: Redes Neurais e Deep Learning, Frameworks para Deep Learning e Análise de Imagem e Visão Computacional.

Estude o fluxo completo: representação tensorial, propagação direta, função de perda, retropropagação, otimização, regularização e avaliação. Em visão, relacione operações clássicas — filtros, bordas, morfologia e segmentação — às representações aprendidas por CNNs.

Projeto sugerido: comparar uma solução clássica de visão com uma CNN, documentando dados, aumentação, métricas por classe, erros típicos e custo computacional.

### 5. Linguagem, sequências e modelos generativos

Disciplinas: Processamento de Linguagem Natural, Redes Neurais Recorrentes e Transformadores e Redes Neurais Generativas.

Construa a progressão conceitual: tokenização e representações vetoriais; RNN, LSTM e GRU; atenção e Transformer; pré-treinamento e adaptação; modelos generativos. Separe fluência de factualidade e avalie modelos com dados representativos, análise de erros e critérios humanos quando necessário.

Projeto sugerido: implementar uma tarefa de classificação textual, comparar uma linha de base clássica com um Transformer e criar uma pequena análise de explicabilidade e vieses.

### 6. Decisão sequencial e personalização

Disciplinas: Aprendizado por Reforço e Análise de Sentimentos e Sistemas de Recomendação.

Em recomendação, diferencie recuperação de candidatos, ranqueamento e avaliação. Em reforço, formalize estado, ação, recompensa, política e horizonte temporal antes de escolher um algoritmo. Nos dois casos, considere ciclos de feedback: a saída do sistema altera os dados futuros que serão usados para avaliá-lo.

Projeto sugerido: construir um recomendador híbrido e simular uma política simples para decidir quando explorar itens novos ou explorar preferências já conhecidas.

### 7. Ética e responsabilidade

Disciplina: Humanidades.

Use ética como parte do projeto, não como revisão posterior. Para cada sistema, registre finalidade, partes afetadas, dados sensíveis, possíveis danos, mecanismos de contestação, supervisão humana e responsáveis pelo acompanhamento. Transparência não se resume a expor código: inclui tornar compreensíveis os critérios e limites do sistema.

## Checklist para qualquer projeto de IA

1. Qual problema está sendo resolvido e para quem?
2. Qual é a linha de base sem machine learning?
3. De onde vêm os dados e quem pode estar sub-representado?
4. Há vazamento entre treino, validação e teste?
5. A métrica representa o custo real dos erros?
6. O modelo está calibrado e seus erros foram analisados por subgrupo?
7. Como reproduzir dados, ambiente, código e parâmetros?
8. Como detectar deriva e degradação depois do deployment?
9. Quem responde por uma decisão incorreta e como o usuário pode contestá-la?
10. Quando o sistema deve recusar, encaminhar ou solicitar supervisão humana?

## Método de revisão

Para cada unidade, produza quatro registros curtos:

- **Conceito:** explique a ideia central com suas próprias palavras.
- **Condições:** liste hipóteses, pré-requisitos e situações nas quais o método falha.
- **Exemplo:** implemente ou descreva um caso concreto.
- **Conexão:** relacione o tema com pelo menos uma disciplina anterior.

Use os notebooks como experimentos, não apenas como leitura. Reinicie o ambiente, execute todas as células em ordem, altere parâmetros e registre o que mudou. Em PDFs e apresentações, priorize definições, diagramas, equações, comparações e limitações.

## Referências transversais

- [scikit-learn](https://scikit-learn.org/stable/) — fundamentos e implementação de machine learning clássico.
- [Deep Learning Book](https://www.deeplearningbook.org/) — base matemática e conceitual de deep learning.
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — artigo fundador da arquitetura Transformer.
- [Reinforcement Learning: An Introduction](https://www.incompleteideas.net/book/the-book-2nd.html) — referência central de aprendizado por reforço.
- [Recomendação da UNESCO sobre Ética da IA](https://www.unesco.org/en/legal-affairs/recommendation-ethics-artificial-intelligence) — princípios de direitos humanos, transparência, supervisão e responsabilidade.
