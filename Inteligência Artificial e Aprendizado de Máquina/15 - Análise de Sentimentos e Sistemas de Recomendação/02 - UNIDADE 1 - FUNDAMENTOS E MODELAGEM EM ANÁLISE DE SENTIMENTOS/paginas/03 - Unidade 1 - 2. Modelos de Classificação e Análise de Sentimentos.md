# Unidade 1 - 2. Modelos de Classificação e Análise de Sentimentos

- Origem: [Canvas](https://pucminas.instructure.com/courses/230809/pages/unidade-1-2-modelos-de-classificacao-e-analise-de-sentimentos)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar os seguintes tópicos:**

- Abordagens de análise de sentimento;
- Abordagens baseadas em léxico;
- Abordagens baseadas em machine learning;
- Abordagens baseadas em deep learning.

**Ao final, você será capaz de:**

- Identificar as principais categorias de modelos utilizados na análise de sentimentos: léxico, aprendizado de máquina e híbrido;
- Compreender como funciona a classificação baseada em léxico e o papel dos dicionários de sentimentos;
- Reconhecer as etapas necessárias para implementar um fluxo de aprendizado de máquina supervisionado aplicado a textos;
- Compreender os algoritmos de classificação clássicos e as formas básicas de representação textual;
- Reconhecer a aplicação de aprendizado profundo (deep learning) e arquiteturas modernas na detecção de sentimentos.

---

#### **Abordagens de análise de sentimentos**

Nesta videoaula, você vai conhecer o panorama completo das principais estratégias utilizadas na análise de sentimentos, entendendo como elas evoluíram desde os primeiros métodos baseados em regras até os modelos mais modernos de deep learning. A aula apresenta três grandes abordagens: métodos baseados em léxico, modelos clássicos de machine learning e arquiteturas avançadas como transformers. Também mostra suas diferenças quanto à necessidade de dados, complexidade computacional e capacidade de interpretar nuances da linguagem.

Além disso, você verá exemplos que ilustram como cada técnica processa um mesmo texto, permitindo compreender por que métodos mais simples são rápidos, porém limitados, enquanto os mais avançados capturam contexto e significado com muito mais precisão. A aula oferece uma visão clara da trajetória histórica da área e prepara você para identificar qual abordagem é a mais adequada para cada cenário de aplicação. Vamos começar?

#### **Abordagens de análise de sentimentos - Prática**

Nesta videoaula, você vai acompanhar a aplicação prática das principais técnicas de análise de sentimentos, utilizando Python e o Google Colab para demonstrar passo a passo como cada abordagem funciona. A aula parte de listas simples de palavras positivas e negativas, avança para léxicos com pontuações e chega aos métodos de machine learning e deep learning, mostrando seus resultados sobre um conjunto de frases reais. Você verá como pré‑processar textos, representar dados numericamente e treinar modelos classificadores.

A videoaula também demonstra o uso de bibliotecas modernas, como pysentimiento, para aplicações baseadas em transformers já pré‑treinados. Assim, você visualiza na prática como diferentes métodos geram resultados distintos e compreende os limites e vantagens de cada abordagem. É uma aula essencial para quem deseja sair da teoria e vivenciar a análise de sentimentos em execução. Vamos lá?

#### **Abordagens baseada em léxico**

Nesta videoaula, você irá aprender como funcionam as abordagens baseadas em léxico, uma das formas mais intuitivas e tradicionais de análise automática de sentimentos. A aula explica como dicionários especiais atribuem pontuações positivas, negativas ou neutras a cada palavra, e como essas pontuações são combinadas para gerar uma classificação final de sentimento. Tal aula também mostra o papel de modificadores — como “muito”, “pouco”, “jamais” ou uso de caixa alta — que podem intensificar ou inverter polaridades.

Você também verá os passos fundamentais desse tipo de abordagem: tokenização, consulta ao léxico, atribuição de pontuações, agregação e decisão final. A aula apresenta ainda variações mais robustas, como léxicos com regras linguísticas e métodos híbridos que combinam dicionários e estatística. É uma introdução prática e acessível para entender como sistemas simples conseguem classificar textos sem depender de grandes volumes de dados. Podemos avançar?

#### **Abordagens baseada em léxico - Prática**

Nesta videoaula, você vai acompanhar a aplicação prática das abordagens baseadas em léxico para análise de sentimentos, explorando diferentes dicionários já existentes — como VADER, sua adaptação em português (LEIA) e TextBlob. A aula demonstra, passo a passo, como pré‑processar textos, consultar pontuações de polaridade, interpretar intensificadores, negações e outros modificadores, além de observar como essas ferramentas estimam sentimentos positivos, negativos ou neutros. Exemplos reais em português e inglês ajudam a visualizar claramente como cada léxico funciona e quais limitações apresentam.

Você também verá como medir a acurácia desses modelos, ajustar funções de decisão e comparar desempenhos entre diferentes léxicos. A videoaula destaca que, embora simples e rápidos, esses métodos ainda enfrentam desafios com nuances linguísticas, contexto e ambiguidades. Ainda assim, são ótimos pontos de partida para estudos em PLN e uma excelente base para entender métodos mais avançados. Vamos experimentar na prática?

#### **Abordagens baseadas em machine learning**

Nesta videoaula, você vai compreender os fundamentos das abordagens de análise de sentimentos baseadas em machine learning, que representam um avanço importante sobre métodos puramente lexicais. A aula explica como grandes volumes de textos rotulados — como avaliações de produtos e comentários de redes sociais — permitem treinar modelos capazes de aprender padrões e regras a partir dos próprios dados. Você conhecerá conceitos essenciais como coleta de dados, engenharia de features, representações vetoriais (Bag of Words, TF‑IDF e n‑gramas), além de entender como funciona o processo de treino, validação e predição.

A videoaula também apresenta os principais tipos de classificadores, como regressão logística, Naive Bayes, KNN, árvores de decisão, Random Forest, SVM e redes neurais, discutindo suas forças, limitações e níveis de interpretabilidade. O conteúdo evidencia que não existe um algoritmo melhor em todos os casos, mas sim escolhas adequadas para diferentes domínios, volumes de dados e necessidades do problema. Vamos avançar nessa segunda geração de técnicas?

#### **Abordagens baseada em machine learning - Prática**

Na videoaula a seguir, você vai colocar em prática a teoria aprendida sobre machine learning, utilizando Python e Google Colab para treinar e testar modelos de classificação de sentimentos. A aula demonstra como dividir o dataset, pré‑processar textos, transformar frases em vetores (Bag of Words e TF‑IDF) e aplicar diversos algoritmos — como regressão logística, Naive Bayes, SVM, árvores de decisão e Random Forest. Verá como cada técnica produz desempenhos diferentes e  medir acurácia para comparar resultados.

Além disso, a prática destaca pontos importantes do mundo real: a necessidade de grandes volumes de dados, o papel crucial da engenharia de features e a importância de ajuste fino de hiperparâmetros para melhorar resultados. A aula termina mostrando como diferentes representações vetoriais impactam o desempenho e de que maneira escolhas metodológicas moldam a eficácia do modelo final. Vamos explorar essas estratégias na prática?

#### **Abordagens baseada em deep learning**

Nesta videoaula, você vai conhecer como o deep learning revolucionou a análise de sentimentos, superando limitações dos métodos lexicais e de machine learning clássico. A aula apresenta conceitos essenciais como embeddings, explicando como essas representações vetoriais capturam significado e semântica das palavras, permitindo interpretações muito mais precisas do que simples contagens ou frequências. Também é explorada a diferença entre modelos pré‑transformers e pós‑transformers, mostrando como o mecanismo de autoatenção possibilitou interpretar frases completas, detectar contexto, lidar com polissemia e compreender nuances como sarcasmo, negação e dependências de longo alcance.

Você verá ainda como modelos pré‑treinados — BERT e GPT, por exemplo— aprenderam padrões linguísticos a partir de enormes volumes de textos, permitindo que tarefas como análise de sentimento sejam resolvidas com enorme precisão, mesmo em textos complexos. A aula te ajuda a entender por que os transformers se tornaram o estado da arte e como essa tecnologia impacta aplicações reais que envolvem texto, áudio, imagem e multimodalidade. Vamos explorar essa nova era do PLN?

#### **Abordagens baseada em deep learning - Prática**

Nesta videoaula, você colocará em prática o uso de modelos de deep learning para análise de sentimentos, aplicando embeddings e transformers em exemplos reais por meio de scripts em Python. A aula mostra como converter frases em vetores semânticos que preservam significado contextual e como treinar classificadores simples usando essas representações. Em seguida, você experimenta modelos pré‑treinados — especializados em inglês e português — capazes de classificar sentimentos com alta acurácia, além de explorar classificações em estrelas e análise de emoções com bibliotecas como pysentimiento.

Você também verá como modelos treinados em grandes bases superam facilmente abordagens tradicionais, detectando emoções como raiva, admiração, desapontamento etc. A aula reforça, de forma prática e acessível, o salto de desempenho que o deep learning proporciona e como essas ferramentas podem ser aplicadas em cenários reais, desde avaliações de produtos até monitoramento de redes sociais. Veremos a seguir uma experimentação desses modelos avançados.
