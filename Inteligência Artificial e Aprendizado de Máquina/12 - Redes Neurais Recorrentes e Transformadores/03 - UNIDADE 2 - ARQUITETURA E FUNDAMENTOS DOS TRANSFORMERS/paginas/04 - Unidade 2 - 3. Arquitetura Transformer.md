# Unidade 2 - 3. Arquitetura Transformer

- Origem: [Canvas](https://pucminas.instructure.com/courses/230805/pages/unidade-2-3-arquitetura-transformer)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar os seguintes tópicos:**

- Arquitetura do codificador;
- Arquitetura do decodificador;
- Atenção mascarada e integração encoder-decoder.

**Ao final, você será capaz de:**

- Descrever os componentes da arquitetura Transformer.

---

#### **Arquitetura do Codificador**

No vídeo a seguir, você irá conhecer a arquitetura do codificador nos modelos Transformer e entender como ele processa a entrada para gerar representações contextuais ricas. A aula mostra como os blocos empilhados combinam atenção multi-cabeça, camadas feedforward, normalização e conexões residuais para capturar relações complexas entre os elementos da sequência.

Além disso, você irá compreender o papel da codificação posicional e como o codificador permite a paralelização do processamento, sendo amplamente utilizado em tarefas de compreensão de linguagem, como classificação e análise contextual. Preparado para entender a base da interpretação nos Transformers? Então, acompanhe a videoaula!

#### **Arquitetura do Decodificador**

Nesta videoaula, você irá explorar a arquitetura do decodificador nos modelos Transformer e compreender o papel de cada um de seus componentes. A aula apresenta como a atenção mascarada controla o acesso à sequência gerada, enquanto a atenção cruzada permite integrar o contexto produzido pelo codificador, garantindo coerência e alinhamento entre entrada e saída.

Você também irá conhecer a função das camadas feedforward, das conexões residuais e da normalização, entendendo como esses elementos contribuem para a estabilidade do treinamento e para a geração de textos mais consistentes. Vamos aprofundar o funcionamento dessa parte fundamental do modelo? Siga para o vídeo!

#### **Atenção Mascarada e Integração CD**

No vídeo a seguir, você irá compreender como funciona a atenção mascarada e por que esse mecanismo é essencial para a geração sequencial de texto nos modelos Transformer. A aula explica como a máscara impede que o decodificador acesse informações futuras, garantindo previsões passo a passo e preservando a coerência durante o treinamento e a geração de sequências.

Além disso, você irá entender a integração entre codificador e decodificador por meio da atenção cruzada, analisando como esse mecanismo conecta a entrada à saída em tarefas como tradução e sumarização. Pronto para entender como esses componentes trabalham juntos para gerar resultados mais precisos? Então, vamos começar!
