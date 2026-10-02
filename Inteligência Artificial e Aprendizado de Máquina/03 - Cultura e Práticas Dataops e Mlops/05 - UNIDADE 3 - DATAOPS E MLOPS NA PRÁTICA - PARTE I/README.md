# 05 - UNIDADE 3 - DATAOPS E MLOPS NA PRÁTICA - PARTE I

[← Voltar à disciplina](../README.md)

## Resumo da unidade

A unidade implementa versionamento, ambientes reproduzíveis, testes e pipelines. O registro de modelos conecta uma execução experimental ao artefato que poderá ser promovido.

### Exemplo

Um teste pode verificar se o pré-processamento mantém as colunas esperadas e rejeita categorias inválidas antes do treinamento.

## Conteúdo da unidade

- [Unidade 3 - Orientações de Estudo](paginas/01%20-%20Unidade%203%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md) — Bem-vindo a um módulo emocionante e abrangente que mergulhará profundamente na integração contínua e no controle de versão, ambientes Conda, registro de modelos, e ciclo de vida completo de um projeto de Aprendizado de Máquina. Prepare-se para uma jornada prática e envolvente, onde você não apenas adquirirá habilidades essenciais DataOps e MLOps, mas também aprenderá a implementá-las de maneira eficaz em projetos do
- [Unidade 3 - 1. Integração Contínua e Versionamento](paginas/02%20-%20Unidade%203%20-%201.%20Integra%C3%A7%C3%A3o%20Cont%C3%ADnua%20e%20Versionamento.md) — Versionamento (ou Controle de Versão) é a prática de gerenciar código por meio de versões acompanhando as revisões e o histórico de alterações para facilitar a revisão e a recuperação do código. Já Integração Contínua é uma prática de desenvolvimento de software em que os desenvolvedores, com frequência, juntam suas alterações de código em um repositório central. Em outras palavras, Controle de Versão é uma forma de
- [Unidade 3 - 2. Ambientes de Desenvolvimento com Python e Anaconda](paginas/03%20-%20Unidade%203%20-%202.%20Ambientes%20de%20Desenvolvimento%20com%20Python%20e%20Anaconda.md) — Ambientes de Desenvolvimento com Python e Anaconda Um ambiente de desenvolvimento é um conjunto de ferramentas, bibliotecas e configurações que permitem que um desenvolvedor crie, teste e execute software. Esses ambientes podem ser configurados de diversas formas, dependendo das necessidades do projeto e das preferências do desenvolvedor. Alguns exemplos de ambientes de desenvolvimento são: IDEs ( Integrated…
- [Unidade 3 - 3. Registro de Modelos e Ciclo de Vida](paginas/04%20-%20Unidade%203%20-%203.%20Registro%20de%20Modelos%20e%20Ciclo%20de%20Vida.md) — Um registro de modelos de ML, também conhecido como controle de versão de modelos ou model registry , é uma ferramenta que permite centralizar todas as informações sobre modelos de Machine Learning , incluindo detalhes sobre parâmetros, métricas de desempenho e versões anteriores do modelo. Ele também permite reverter alterações feitas em modelos e escolher qual modelo é o melhor para ser utilizado em produção.…
- [Unidade 3 - 4. Testes Automatizados](paginas/05%20-%20Unidade%203%20-%204.%20Testes%20Automatizados.md) — A automatização é a utilização de tecnologias e ferramentas para automatizar processos e tarefas que antes eram realizados manualmente. Pode ser aplicada em diversas áreas, como desenvolvimento de software, infraestrutura, operações, marketing, finanças, entre outras. Tem como objetivo aumentar a eficiência e a produtividade, reduzir erros e custos, além de liberar os profissionais para se concentrarem em tarefas…
- [Unidade 3 - 5. Pipelines](paginas/06%20-%20Unidade%203%20-%205.%20Pipelines.md) — Uma pipeline é uma sequência automatizada de processos no desenvolvimento de software, composta por várias etapas. Ela automatiza e facilita o desenvolvimento e a entrega, é altamente personalizável e pode ser adaptada às necessidades específicas de uma equipe ou projeto. As pipelines ajudam a garantir a qualidade, detectar e corrigir problemas e melhorar a colaboração.
- [Unidade 3 - 6. Apresentação do Problema](paginas/07%20-%20Unidade%203%20-%206.%20Apresenta%C3%A7%C3%A3o%20do%20Problema.md) — Nesta seção será apresentado o problema que abordaremos durante as práticas da disciplina. O problema que abordaremos será o do "Sofrimento Fetal e o Exame da Cardiotocografia". O sofrimento fetal ocorre quando o feto não recebe oxigênio suficiente durante o trabalho de parto, o que pode levar a complicações graves ou até mesmo à morte fetal. A cardiotocografia é um exame que pode ajudar a detectar sinais de…
- [Unidade 3 - 7. Introdução às práticas da unidade](paginas/08%20-%20Unidade%203%20-%207.%20Introdu%C3%A7%C3%A3o%20%C3%A0s%20pr%C3%A1ticas%20da%20unidade.md) — Nesta seção você será convidado a fazer uma sequência de atividades práticas para aprofundar nos conhecimentos da disciplina. As práticas estão relacionadas aos conceitos de Integração Continua, Gerenciamento de Modelos, Automação e Testes
- [Unidade 3 - 7.1. Prática - Apresentação do Notebook](paginas/09%20-%20Unidade%203%20-%207.1.%20Pr%C3%A1tica%20-%20Apresenta%C3%A7%C3%A3o%20do%20Notebook.md) — Nesta seção será apresentado um notebook com uma rede neural para a criação e treino do modelo para o problema descrito anteriormente. Para realizar essa prática faça o download do arquivo train\ notebook.ipynb Assista a seguir o vídeo explicando o notebook:
- [Unidade 3 - 7.2. Prática - Criação do ambiente Conda](paginas/10%20-%20Unidade%203%20-%207.2.%20Pr%C3%A1tica%20-%20Cria%C3%A7%C3%A3o%20do%20ambiente%20Conda.md) — Nesta seção será apresentada a criação do ambiente conda usando os arquivos específicos para as versões das bibliotecas. Para realizar essa prática faça o download dos arquivos requirements.txt e environment.yml Assista a seguir o vídeo explicando a criação do ambiente Conda:
- [Unidade 3 - 7.3. Prática - Envio de Arquivos para o GitHub](paginas/11%20-%20Unidade%203%20-%207.3.%20Pr%C3%A1tica%20-%20Envio%20de%20Arquivos%20para%20o%20GitHub.md) — Nesta prática será apresentada uma forma de enviar os arquivos de um repositório para o GitHub. Para realizar essa prática faça o download do arquivo main.py Assista a seguir o vídeo explicando alguns comandos no Git e como enviar arquivos para o GitHub:
- [Unidade 3 - 7.4. Prática - Criação do Script e Testes com Pytest](paginas/12%20-%20Unidade%203%20-%207.4.%20Pr%C3%A1tica%20-%20Cria%C3%A7%C3%A3o%20do%20Script%20e%20Testes%20com%20Pytest.md) — Nesta prática iremos converter e refatorar o arquivo para treino, além de executarmos alguns testes unitários para o treino do modelo. Para realizar essa prática faça o download do arquivo test\ train.py
- [Unidade 3 - 7.5. Prática - Pipeline com Teste](paginas/13%20-%20Unidade%203%20-%207.5.%20Pr%C3%A1tica%20-%20Pipeline%20com%20Teste.md) — Nesta seção será apresentada a criação da pipeline para automatizar o treino do modelo. Lembrando que em um primeiro momento essa automação apenas será inicializada por alguma alteração nos códigos do repositório. Para realizar essa prática faça o download do arquivo pipeline.yml Assista a seguir o vídeo explicando a criação da pipeline:
- [Unidade 3 - 7.6. Prática - Registro de Modelos](paginas/14%20-%20Unidade%203%20-%207.6.%20Pr%C3%A1tica%20-%20Registro%20de%20Modelos.md) — Nesta seção será apresentado o registro de modelos para registrar os artefatos e modelos gerados após o treino (model\ registry.ipynb). Assista a seguir o vídeo explicando o notebook:
- [Unidade 3 - Material Complementar](paginas/15%20-%20Unidade%203%20-%20Material%20Complementar.md) — Integração Contínua, Ambientes Conda e Pipelines.pdf Registro de Modelos, Ambientes HMG, Teste e PRD.pdf Nos primeiros treinos de modelos de aprendizado de máquina, como comparava a qualidade dos modelos? Chegou a usar alguma ferramenta ou foi em uma planilha? Aula sobre CI/CD com GitHub Actions com Fabrício Veronez (Profissional de DevOps) - Aula Ci/CD Leitura do artigo - Como eu fiz o deploy do meu primeiro modelo
- [Unidade 3 - Desafio e Resolução](paginas/21%20-%20Unidade%203%20-%20Desafio%20e%20Resolu%C3%A7%C3%A3o.md) — Como podemos utilizar o pacote do MLflow em conjunto com DagsHub para monitorar o treino de um modelo de Machine Learning Para integrar um treinamento de um modelo usando MLflow com a plataforma Dagshub, é importante primeiro garantir que o pacote Dagshub esteja devidamente instalado. Isso pode ser feito através do comando pip install dagshub . Com o ambiente devidamente configurado para trabalhar com MLflow, inicie

## Materiais

### PDFs (3)

- [Definição do Problema.pdf](documentos/Defini%C3%A7%C3%A3o%20do%20Problema.pdf) (6 páginas)
- [Integração Contínua, Ambientes Conda e Pipelines.pdf](documentos/Integra%C3%A7%C3%A3o%20Cont%C3%ADnua%2C%20Ambientes%20Conda%20e%20Pipelines.pdf) (54 páginas)
- [Registro de Modelos, Ambientes HMG, Teste e PRD.pdf](documentos/Registro%20de%20Modelos%2C%20Ambientes%20HMG%2C%20Teste%20e%20PRD.pdf) (9 páginas)

### Notebooks (2)

- [model_registry.ipynb](documentos/model_registry.ipynb)
- [train_notebook.ipynb](documentos/train_notebook.ipynb)

### Código e configuração (4)

- [environment.yml](documentos/environment.yml)
- [pipeline.yml](documentos/pipeline.yml)
- [test_train.py](documentos/test_train.py)
- [train.py](documentos/train.py)

### Páginas e textos (16)

- [01 - Unidade 3 - Orientações de Estudo.md](paginas/01%20-%20Unidade%203%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md)
- [02 - Unidade 3 - 1. Integração Contínua e Versionamento.md](paginas/02%20-%20Unidade%203%20-%201.%20Integra%C3%A7%C3%A3o%20Cont%C3%ADnua%20e%20Versionamento.md)
- [03 - Unidade 3 - 2. Ambientes de Desenvolvimento com Python e Anaconda.md](paginas/03%20-%20Unidade%203%20-%202.%20Ambientes%20de%20Desenvolvimento%20com%20Python%20e%20Anaconda.md)
- [04 - Unidade 3 - 3. Registro de Modelos e Ciclo de Vida.md](paginas/04%20-%20Unidade%203%20-%203.%20Registro%20de%20Modelos%20e%20Ciclo%20de%20Vida.md)
- [05 - Unidade 3 - 4. Testes Automatizados.md](paginas/05%20-%20Unidade%203%20-%204.%20Testes%20Automatizados.md)
- [06 - Unidade 3 - 5. Pipelines.md](paginas/06%20-%20Unidade%203%20-%205.%20Pipelines.md)
- [07 - Unidade 3 - 6. Apresentação do Problema.md](paginas/07%20-%20Unidade%203%20-%206.%20Apresenta%C3%A7%C3%A3o%20do%20Problema.md)
- [08 - Unidade 3 - 7. Introdução às práticas da unidade.md](paginas/08%20-%20Unidade%203%20-%207.%20Introdu%C3%A7%C3%A3o%20%C3%A0s%20pr%C3%A1ticas%20da%20unidade.md)
- [09 - Unidade 3 - 7.1. Prática - Apresentação do Notebook.md](paginas/09%20-%20Unidade%203%20-%207.1.%20Pr%C3%A1tica%20-%20Apresenta%C3%A7%C3%A3o%20do%20Notebook.md)
- [10 - Unidade 3 - 7.2. Prática - Criação do ambiente Conda.md](paginas/10%20-%20Unidade%203%20-%207.2.%20Pr%C3%A1tica%20-%20Cria%C3%A7%C3%A3o%20do%20ambiente%20Conda.md)
- [11 - Unidade 3 - 7.3. Prática - Envio de Arquivos para o GitHub.md](paginas/11%20-%20Unidade%203%20-%207.3.%20Pr%C3%A1tica%20-%20Envio%20de%20Arquivos%20para%20o%20GitHub.md)
- [12 - Unidade 3 - 7.4. Prática - Criação do Script e Testes com Pytest.md](paginas/12%20-%20Unidade%203%20-%207.4.%20Pr%C3%A1tica%20-%20Cria%C3%A7%C3%A3o%20do%20Script%20e%20Testes%20com%20Pytest.md)
- [13 - Unidade 3 - 7.5. Prática - Pipeline com Teste.md](paginas/13%20-%20Unidade%203%20-%207.5.%20Pr%C3%A1tica%20-%20Pipeline%20com%20Teste.md)
- [14 - Unidade 3 - 7.6. Prática - Registro de Modelos.md](paginas/14%20-%20Unidade%203%20-%207.6.%20Pr%C3%A1tica%20-%20Registro%20de%20Modelos.md)
- [15 - Unidade 3 - Material Complementar.md](paginas/15%20-%20Unidade%203%20-%20Material%20Complementar.md)
- [21 - Unidade 3 - Desafio e Resolução.md](paginas/21%20-%20Unidade%203%20-%20Desafio%20e%20Resolu%C3%A7%C3%A3o.md)

### Imagens (12)

- [banner-pos-2023.jpg](images/banner-pos-2023.jpg)
- [icone-bussola-1.png](images/icone-bussola-1.png)
- [icone-coruja-1.png](images/icone-coruja-1.png)
- [icone-lampada-1.png](images/icone-lampada-1.png)
- [image-6.png](images/image-6.png)
- [image-61521910-09e0-41dd-abcf-46599f895033.png](images/image-61521910-09e0-41dd-abcf-46599f895033.png)
- [image-7.png](images/image-7.png)
- [image-778d366c-b988-4439-8dbc-bf04eb6795e9.png](images/image-778d366c-b988-4439-8dbc-bf04eb6795e9.png)
- [image-c851e0b3-8e2f-4606-b851-438e7adf7171.png](images/image-c851e0b3-8e2f-4606-b851-438e7adf7171.png)
- [image-d14a1ea2-5550-45e9-8a5b-065e00a0d497.png](images/image-d14a1ea2-5550-45e9-8a5b-065e00a0d497.png)
- [Leitura-1.png](images/Leitura-1.png)
- [material-b-1.png](images/material-b-1.png)

### HTML original (16)

- [01 - Unidade 3 - Orientações de Estudo.html](html/01%20-%20Unidade%203%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.html)
- [02 - Unidade 3 - 1. Integração Contínua e Versionamento.html](html/02%20-%20Unidade%203%20-%201.%20Integra%C3%A7%C3%A3o%20Cont%C3%ADnua%20e%20Versionamento.html)
- [03 - Unidade 3 - 2. Ambientes de Desenvolvimento com Python e Anaconda.html](html/03%20-%20Unidade%203%20-%202.%20Ambientes%20de%20Desenvolvimento%20com%20Python%20e%20Anaconda.html)
- [04 - Unidade 3 - 3. Registro de Modelos e Ciclo de Vida.html](html/04%20-%20Unidade%203%20-%203.%20Registro%20de%20Modelos%20e%20Ciclo%20de%20Vida.html)
- [05 - Unidade 3 - 4. Testes Automatizados.html](html/05%20-%20Unidade%203%20-%204.%20Testes%20Automatizados.html)
- [06 - Unidade 3 - 5. Pipelines.html](html/06%20-%20Unidade%203%20-%205.%20Pipelines.html)
- [07 - Unidade 3 - 6. Apresentação do Problema.html](html/07%20-%20Unidade%203%20-%206.%20Apresenta%C3%A7%C3%A3o%20do%20Problema.html)
- [08 - Unidade 3 - 7. Introdução às práticas da unidade.html](html/08%20-%20Unidade%203%20-%207.%20Introdu%C3%A7%C3%A3o%20%C3%A0s%20pr%C3%A1ticas%20da%20unidade.html)
- [09 - Unidade 3 - 7.1. Prática - Apresentação do Notebook.html](html/09%20-%20Unidade%203%20-%207.1.%20Pr%C3%A1tica%20-%20Apresenta%C3%A7%C3%A3o%20do%20Notebook.html)
- [10 - Unidade 3 - 7.2. Prática - Criação do ambiente Conda.html](html/10%20-%20Unidade%203%20-%207.2.%20Pr%C3%A1tica%20-%20Cria%C3%A7%C3%A3o%20do%20ambiente%20Conda.html)
- [11 - Unidade 3 - 7.3. Prática - Envio de Arquivos para o GitHub.html](html/11%20-%20Unidade%203%20-%207.3.%20Pr%C3%A1tica%20-%20Envio%20de%20Arquivos%20para%20o%20GitHub.html)
- [12 - Unidade 3 - 7.4. Prática - Criação do Script e Testes com Pytest.html](html/12%20-%20Unidade%203%20-%207.4.%20Pr%C3%A1tica%20-%20Cria%C3%A7%C3%A3o%20do%20Script%20e%20Testes%20com%20Pytest.html)
- [13 - Unidade 3 - 7.5. Prática - Pipeline com Teste.html](html/13%20-%20Unidade%203%20-%207.5.%20Pr%C3%A1tica%20-%20Pipeline%20com%20Teste.html)
- [14 - Unidade 3 - 7.6. Prática - Registro de Modelos.html](html/14%20-%20Unidade%203%20-%207.6.%20Pr%C3%A1tica%20-%20Registro%20de%20Modelos.html)
- [15 - Unidade 3 - Material Complementar.html](html/15%20-%20Unidade%203%20-%20Material%20Complementar.html)
- [21 - Unidade 3 - Desafio e Resolução.html](html/21%20-%20Unidade%203%20-%20Desafio%20e%20Resolu%C3%A7%C3%A3o.html)

### Outros materiais (1)

- [requirements.txt](documentos/requirements.txt)

## Roteiro de estudo

1. Leia as páginas na ordem apresentada pelo módulo.
2. Consulte os PDFs e apresentações enquanto registra definições, hipóteses e exemplos.
3. Execute notebooks e códigos, verificando entradas, saídas e limitações.
4. Ao final, responda:

   - Como você explicaria **Unidade 3 - Orientações de Estudo** sem consultar o material?
   - Como você explicaria **Unidade 3 - 1. Integração Contínua e Versionamento** sem consultar o material?
   - Como você explicaria **Unidade 3 - 2. Ambientes de Desenvolvimento com Python e Anaconda** sem consultar o material?
   - Como você explicaria **Unidade 3 - 3. Registro de Modelos e Ciclo de Vida** sem consultar o material?
   - Como você explicaria **Unidade 3 - 4. Testes Automatizados** sem consultar o material?
