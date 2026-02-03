#  03 - Cultura e Práticas Dataops e Mlops

## SUMÁRIO
- [03 - Cultura e Práticas Dataops e Mlops](#03---cultura-e-práticas-dataops-e-mlops)
  - [SUMÁRIO](#sumário)
  - [UNIDADE 01](#unidade-01)
    - [Conceito de Cultura](#conceito-de-cultura)
    - [Fundamentos de DevOps](#fundamentos-de-devops)
      - [O que é DevOps?](#o-que-é-devops)
      - [Ciclo de vida em DevOps](#ciclo-de-vida-em-devops)
      - [Princípios de DevOps](#princípios-de-devops)
  - [UNIDADE 02](#unidade-02)
    - [Fundamentos de DataOps - Data Operations](#fundamentos-de-dataops---data-operations)
      - [O que é DataOps?](#o-que-é-dataops)
      - [Princípios de DataOps](#princípios-de-dataops)
      - [Por que devemos aplicar DataOps?](#por-que-devemos-aplicar-dataops)
      - [O que é Data Drift?](#o-que-é-data-drift)
        - [Tipos de Drift](#tipos-de-drift)
    - [Fundamentos de MLOps - Machine Learning Operations](#fundamentos-de-mlops---machine-learning-operations)
      - [O que é MLOps?](#o-que-é-mlops)
      - [Fases de MLOps](#fases-de-mlops)
      - [Princípios de MLOps](#princípios-de-mlops)
    - [Papel do Engenheiro de Dados](#papel-do-engenheiro-de-dados)
    - [Papel do Engenheiro de Aprendizado de Máquina](#papel-do-engenheiro-de-aprendizado-de-máquina)
  - [UNIDADE 03](#unidade-03)
    - [Controle de Versão e CI](#controle-de-versão-e-ci)
      - [GIT e GITHUB](#git-e-github)
    - [Ambientes de Desenvolvimento](#ambientes-de-desenvolvimento)
      - [O que é?](#o-que-é)
      - [Python e Anaconda](#python-e-anaconda)
    - [Ambientes Virtuais](#ambientes-virtuais)
    - [Registro de Modelos e Ciclo de Vida](#registro-de-modelos-e-ciclo-de-vida)
    - [Ciclo de Vida e Ambientes](#ciclo-de-vida-e-ambientes)
    - [Automatização](#automatização)
      - [Testes automatizados](#testes-automatizados)
        - [Testes em scripts de treinamento](#testes-em-scripts-de-treinamento)
  - [UNIDADE 04](#unidade-04)

## UNIDADE 01

### Conceito de Cultura

Uma das definições mais interessantes e completas é feita por Tylor:

> "Todo aquele **complexo** que inclui o **conhecimento**, as crenças, a arte, a moral, a lei, os **costumes** e todos os outros hábitos e capacidades adquiridos pelo homem como membro de uma **sociedade**"

- **Complexo**: envolve relações complexas entre as pessoas
- **Conhecimento**: parte-se do pressuposto que existe alguma forma de conhecimento tácito (aquele que é adquirido à partir de experiências pessoais)
- **Costumes**: refere-se a um hábito ou uma prática regular/recorrente
- **Sociedade**: grupo de pessoas que compartilham de valores
  
Uma definição mais informal do que é cultura seria:

> Cultura é o **conjunto** de **hábitos**, **práticas** de forma recorrente entre **pessoas** as quais **buscam compartilhar conhecimento entre si**.

### Fundamentos de DevOps

#### O que é DevOps?

DevOps é uma **cultura**, um **conjunto de práticas** e **ferramentas** que **une** **Desenvolvimento** (Dev) e **Operações** (Ops) de TI para **automatizar** e **integrar processos**.

A partir do DevOps que **surge** **DataOps** (Focado em dados) e **MLOps** (Focado em Aprendizado de Máquina).

#### Ciclo de vida em DevOps

O ciclo de DevOps é um **ciclo infinito** que mostra o **relacionamento das fases do ciclo de vida de DevOps**. Este ciclo apresenta a **constante colaboração da equipe em conjunto** com a constante **melhoria iterativa** durante o ciclo de vida de um produto.

![Ciclo de Vida em DevOps](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/03%20-%20Cultura%20e%20Práticas%20Dataops%20e%20Mlops/images/cicloVidaDevOps.png)

Para entendermos melhor o ciclo, vamos dividi-lo nas duas fases: **desenvolvimento** e **operação**. A **fase de desenvolvimento** representa **toda** a **implementação de uma entrega** feita pela equipe. Se divide nas seguintes etapas:

- **Planejamento**: definição de qual entrega será feita;
- **Criação/Desenvolvimento**: implementação da entrega;
- **Verificação/Teste**: testes de qualidade, integração, dentre outros;
- **Empacotamento**: criação do artefato a ser entregue;

A **operação** consiste na **fase de “fazer funcionar”** a entrega feita pela equipe. Consiste em algumas etapas:
- **Release/Entrega**: realização da entrega do artefato; 
- **Configuração**: configuração do ambiente o qual vai receber o artefato desenvolvido;
- **Monitoramento/Feedback**: após a entrega feita pela equipe, entra a etapa de monitoramento da solução para coleta de feedbacks e correção preventiva de erros;

#### Princípios de DevOps

- **Integração Contínua (CI - Continuous Integration)**:  prática de integrar com grande frequência, os códigos desenvolvidos em um repositório central. O objetivo é encontrar e investigar erros mais rapidamente, melhorar a qualidade do software com redução no tempo de entrega. Esta prática busca sempre automatizar e simplificar o processo de implementação de código;
- **Controle de Versão (Version Control)**: é o processo de gerenciamento de código possuindo um histórico de alterações, podendo corrigir conflitos e reverter alterações;
- **Entrega Contínua (CD - Continuous Delivery)**: alterações de código são feitas, testadas e de forma automatizada, são liberadas para operação;
- **Microsserviços (Microservices)**: é a prática de se criar uma aplicação/software em pequenos serviços, facilitando a manutenção e escalabilidade;
- **Infraestrutura como Código (IaC - Infrastructure as Code)**: é uma forma de definir os recursos utilizados e arquiteturas dos sistemas de forma descritiva, podendo ser armazenadas e versionadas, ou seja, crie uma documentação, podendo ser versionada para podermos ter histórico;
- **Gestão de Configurações**: Gerenciamento do estado dos recursos em um sistema, incluindo servidores, máquinas virtuais e bancos de dados. Usando ferramentas de gerenciamento de configuração, as equipes podem implementar alterações de maneira controlada e sistemática, reduzindo riscos de modificar a configuração do sistema.
- **Monitoramento Contínuo (Continuous Monitoring)**: com essa prática é possível ter visibilidade em tempo real sobre o estado de uma aplicação. Esse monitoramento é feito usando coletas de telemetria, metadados, criando alarmes em casos críticos, dentre outros;
- **Comunicação & Colaboração (Agile)**: é prática de compartilhamento de informação dentro da equipe, o objetivo é facilitar a comunicação e compartilhamento de contexto, de conhecimento;
- **Automação**: possibilita um ganho de velocidade nos processos da equipe, partindo do desenvolvimento, integração até os testes.
  
## UNIDADE 02

### Fundamentos de DataOps - Data Operations

#### O que é DataOps?

É o termo que remete às **operações com dados** possuindo **origem baseada em DevOps**. O conceito tinha como proposta inicial ser um sistema de **melhores práticas com dados**, mas gradualmente amadureceu para uma **abordagem totalmente funcional** para lidar com a sua **análise**. Para sua implantação e execução com sucesso, existe uma sequência de princípio que direciona todas as práticas.

#### Princípios de DataOps

- **Satisfação contínua do cliente**: devem ser feitas entregas de valor, ou seja, que agreguem ao cliente e de forma contínua. Podem ser dados brutos para uma futura análise, dados agregados, relatórios ou até mesmo pipelines de dados;
- **Foco em análises relevantes**: quando alguma análise ou insight for solicitado, ter foco naqueles que sejam úteis para o cliente;
- **Abraçar a mudança**: é sempre importante considerar a necessidade dos clientes;
- **Ser coletivo com auto-organização**: equipes de dados com diversos papéis trazem diversidade de ideias, ferramentas, arquiteturas e novas possibilidades. Acredita-se que dando liberdade para as equipes tomarem as melhores decisões elas poderão extrair os melhores qualidades/características de cada participante;
- **Interações diárias**: interações diárias facilitam a comunicação e resolução de incidentes;
- **Redução do heroísmo**: com as possibilidades de resolução dos problemas e a diversidade de problemas, as equipes devem focar em resolver um problema por vez, evitando o heroísmo de tentar resolver todos de uma vez e acabar não conseguindo sair do lugar;
- **Ter reprodutibilidade**: é imprescindível que todos os processos sejam reprodutíveis para que em casos de falhas, o artefato de dado possa ser gerado novamente;
- **Qualidade**: a qualidade das entregas deve ser um dos grandes focos, evitando qualquer tipo de retrabalho, principalmente pelo custo - envolvido. **Exemplo**: garantindo a qualidade de um pipeline de dados, evita o reprocessamento, principalmente quando o dado em questão for de um volume elevado;
- **Aplicar monitoramento**: monitorando os processos de dados é possível corrigir alguma falha antes que o cliente perceba, garantindo a qualidade do dado entregue;
- **Melhorar o cycle time**: ao se utilizar os princípios anteriores, o tempo de entrega acaba reduzindo como consequência da qualidade das entregas e dos próprios processos.

> Embora haja algumas semelhanças entre DataOps e MLOps, como o uso de metodologias ágeis e a entrega contínua, eles têm objetivos e fluxos de trabalho diferentes. O **DataOps se concentra na gestão de dados em toda a organização**, enquanto o **MLOps se concentra na implantação e gerenciamento de modelos de aprendizado de máquina em produção**. Assista a seguir um vídeo abordando os conceitos deste módulo.

#### Por que devemos aplicar DataOps?

Existem **vários motivos** para **implantar a cultura DataOps** em uma empresa, incluindo:

- **Processos mais ágeis**: O DataOps permite que as equipes de dados trabalhem de forma mais ágil, com entregas incrementais e com valor, o que pode levar a uma maior eficiência e produtividade.
- **Insights em tempo real**: Com o DataOps, as equipes de dados podem fornecer insights em tempo real para a empresa, permitindo que ela tome decisões mais informadas e rápidas.
- **Democratização das informações**: O DataOps pode ajudar a democratizar as informações, permitindo que as equipes de negócios acessem e usem dados de forma mais eficaz.
- **Foco estratégico**: O DataOps pode ajudar a empresa a se concentrar em seus objetivos estratégicos, permitindo que as equipes de dados trabalhem em projetos que agreguem valor real à empresa.
- **Alinhamento entre negócios e TI**: O DataOps pode ajudar a alinhar as equipes de negócios e de TI, permitindo que elas trabalhem juntas de forma mais eficaz para atingir os objetivos da empresa.

#### O que é Data Drift?

Data Drift é um **fenômeno** em que os **dados usados para treinar um modelo de ML mudam com o tempo**. Isso pode **levar a uma diminuição** nas **métricas do modelo**, uma vez que o **modelo pode não ser mais capaz de generalizar bem para novos dados**. Em outras palavras, o Data Drift **ocorre quando os dados de entrada do modelo mudam ao longo do tempo**, o que pode **afetar a precisão e a eficácia do modelo**. Para **lidar com o Data Drift**, é importante **monitorar os dados usados para treinar os modelos**, **atualizar os dados regularmente** e, **se necessário, refazer os modelos completamente**.

##### Tipos de Drift

- **Data Drift**: É um fenômeno em que os dados usados para treinar um modelo de Machine Learning mudam com o tempo. Isso pode levar a uma diminuição nas métricas do modelo, uma vez que o modelo pode não ser mais capaz de generalizar bem para novos dados.
- **Concept Drift**: É um fenômeno em que a relação entre os dados e a variável alvo muda com o tempo. Isso pode levar a uma diminuição na precisão do modelo, uma vez que o modelo pode não ser mais capaz de capturar a relação entre os dados e a variável alvo de forma eficaz. O Concept Drift pode ser resolvido refazendo o modelo.

![Drift Exemplos](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/03%20-%20Cultura%20e%20Práticas%20Dataops%20e%20Mlops/images/draftExemplos.png)

### Fundamentos de MLOps - Machine Learning Operations

#### O que é MLOps?

MLOps (Machine Learning Operations) é um **conjunto de práticas** que **une** o **desenvolvimento de modelos de Machine Learning** (ML) com as **operações de TI** (DevOps) para **automatizar e gerencia**r todo o **ciclo de vida de ML**, desde a criação até a implantação e o monitoramento em produção, **garantindo** que os modelos sejam **confiáveis**, **escaláveis** e **eficientes**, **envolvendo cientistas de dados e engenheiros**.

> Agora quando mudamos o artefato entregue para um modelo de ML, o desenvolvimento e operação de modelos recebe o nome de MLOps que a junção de Machine Learning + Operations.

#### Fases de MLOps

- **Projetar o aplicativo baseado em ML**: a primeira fase é dedicada ao entendimento do negócio, entendimento dos dados e projeto do software baseado em aprendizado de máquina. Nesta etapa, é identificado o usuário em potencial, projeta-se a solução de aprendizado de máquina para resolver seu problema e avalia-se o desenvolvimento do projeto.
- **Experimentação e desenvolvimento de ML**: na segunda fase é verificada a aplicabilidade do aprendizado de máquina para o problema em questão, implementando a Prova de Conceito (POC). Nesta fase, executa-se etapas iterativamente diferentes, como identificar ou encontrar os melhores parâmetros do algoritmo adequado para o problema, engenharia de dados e/ou modelos. O objetivo principal nesta fase é fornecer um modelo de aprendizado de máquina de qualidade estável que será executado em produção.
- **Operações de ML**: o foco principal da terceira fase é entregar o modelo de aprendizado de máquina desenvolvido anteriormente em produção usando práticas de DevOps estabelecidas, como por exemplo: teste, controle de versão, entrega contínua e monitoramento;

#### Princípios de MLOps

- **Automação**: O nível de automação dos pipelines de Dados, Modelo de ML e Código determina a maturidade do processo de ML. Com o aumento da maturidade, a velocidade para o treinamento de novos modelos também aumenta. O objetivo de uma equipe de MLOps é automatizar a implantação de modelos de ML no sistema de software principal ou como um componente de serviço. Isso significa automatizar as etapas completas do fluxo de trabalho de ML sem nenhuma intervenção manual.
- **Continuous X**:
  - **Integração Contínua (CI)** estende o código e os componentes de teste e validação, adicionando dados e modelos de teste e validação.
  - **Entrega Contínua (CD)** se preocupa com a entrega de um pipeline de treinamento de ML que implanta automaticamente outro serviço de previsão do modelo de ML.
  - **Treinamento Contínuo (CT)** é exclusivo da propriedade de sistemas de ML, que retreina automaticamente os modelos de ML para reimplantação.
  - **Monitoramento Contínuo (CM)** se preocupa com o monitoramento de dados de produção e métricas de desempenho do modelo, que estão vinculados às métricas de negócios;
- **Versionamento**: O objetivo do controle de versão é tratar scripts de treinamento de ML, modelos de ML e conjuntos de dados para treinamento de modelos como cidadãos de primeira classe nos processos de DevOps. Neste caso, rastreia-se modelos de ML e conjuntos de dados com sistemas de controle de versão; 
- **Rastreio de Experimentos**: O desenvolvimento de Machine Learning é um processo altamente iterativo e centrado em pesquisa. Em contraste com o processo tradicional de desenvolvimento de software, no desenvolvimento de ML, vários experimentos de treinamento de modelos podem ser executados em paralelo antes de tomar a decisão de qual modelo será promovido para produção;
- **Teste**: é a forma de garantir a qualidade e a “saúde”, os artefatos testados são os pipelines de dados, de treino de modelo e de disponibilização da aplicação, além dos dados em si, modelo e saúde da aplicação;
- **Monitoramento**: Depois que o modelo for implantado, ele precisa ser acompanhado para garantir que o modelo funcione conforme o esperado;
- **Reprodutibilidade**: A reprodutibilidade significa que todas as fases do processamento de dados, treinamento do modelo e implantação do modelo devem produzir resultados idênticos com a mesma entrada. Se temos os mesmos dados, mesmos modelos, mesmas configurações e mesmos ambientes, temos de ser capazes de produzir os mesmos artefatos;

### Papel do Engenheiro de Dados

- Atua como principal destaque nos processos de **DataOps**
- Responsável por **projetar, implementar e manter** a infraestrutura de dados
- Garante **alta performance, escalabilidade e confiabilidade** dos processos analíticos
- Trabalha com **coleta, processamento e armazenamento de dados**
- Dá suporte a equipes de negócio, gestão e dados
- Possui perfil **técnico**, focado em infraestrutura e arquitetura de dados
- Domina **cloud computing** (AWS, Azure, GCP)
- Conhecimentos essenciais:
  - Ciência da Computação
  - Aplicações escaláveis
  - Bancos de dados relacionais e não relacionais
  - Processamento em lote e streaming
  - Configuração e uso de clusters
- Profissão **não regulamentada**, aberta a diversas formações, mas exige alto nível técnico

### Papel do Engenheiro de Aprendizado de Máquina

- Atua de forma semelhante a **programadores e cientistas de dados**
- Desenvolve sistemas capazes de **aprender com dados e gerar previsões**
- Cria e otimiza algoritmos de **Machine Learning e Inteligência Artificial**
- Avalia, organiza dados e executa testes para melhorar o desempenho dos modelos
- Responsável pela **disponibilização de modelos em produção**
- Desenvolve e mantém **pipelines de treino e deploy**
- Garante que os modelos resolvam corretamente os problemas propostos
- Conhecimentos essenciais:
  - Programação avançada
  - Frameworks de ML e Deep Learning
  - AutoML
  - MLOps
  - Engenharia de Dados
  
## UNIDADE 03

### Controle de Versão e CI

- **Controle de Versão**: É uma forma de gerenciar o histórico de alterações do código.
- **Integração Contínua**: É uma prática de colaboração entre desenvolvedores para integrar suas alterações de forma mais eficiente.

#### GIT e GITHUB

**Git** é um **sistema de controle de versão distribuído**, que permite que **várias pessoas trabalhem em um mesmo projeto ao mesmo tempo**, sem que haja conflitos entre as alterações realizadas. Já o **GitHub** é uma **plataforma de hospedagem de código-fonte baseada em Git**, que permite que **desenvolvedores colaborem em projetos e compartilhem seu código com outras pessoas**. Em resumo, **Git é uma ferramenta de controle de versão**, enquanto **GitHub é uma plataforma de hospedagem de código-fonte que utiliza o Git como base**.

**As principais características do Git são**:
- Branching e Merging;
- Pequeno e rápido;
- Distribuído;
- Staging Area;
- Gratuito e Aberto.

**Já para o GitHub, as principais características são**:
- Colaborativo;
- Automações e CI/CD;
- Segurança;
- Gerenciamento de Projetos;
- Administração de Times;
- Comunidade.

O versionamento de código com Git trabalha de seguindo basicamente o fluxo da seguinte figura:

![FluxoGit](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/03%20-%20Cultura%20e%20Práticas%20Dataops%20e%20Mlops/images/fluxoGit.png)

**Esse fluxo segue os seguintes princípios:**

- **Branch Principal (Master/Main):** Quando você cria um repositório Git, ele começa com um branch principal, geralmente chamado "master" ou "main". Este branch representa a linha de base do seu projeto e geralmente contém o código estável e pronto para produção.
- **Criação de Novas Branches**: Para desenvolver recursos, corrigir bugs ou realizar experimentos sem afetar o branch principal, você cria novas branches a partir do branch principal. Essas branches são cópias do estado atual do projeto no momento em que são criadas.
- **Trabalho em Branches Secundárias**: Os desenvolvedores trabalham em suas branches secundárias, fazendo alterações, adicionando código e realizando testes. Cada branch secundária é isolada do branch principal e de outras branches secundárias, permitindo o desenvolvimento independente.
- **Merging (Mesclagem)**: Quando um desenvolvedor conclui seu trabalho em uma branch secundária e está satisfeito com as alterações, ele pode mesclar (merge) essa branch de volta ao branch principal. Isso incorpora as alterações da branch secundária ao código principal do projeto.
- **Resolução de Conflitos**: Em algumas situações, pode ocorrer um conflito durante a mesclagem, especialmente quando duas branches alteraram a mesma parte do código. Nesse caso, os desenvolvedores precisam resolver os conflitos manualmente, decidindo qual versão das alterações será mantida.
- **Branches de Recursos e de Manutenção**: Além das branches de desenvolvimento de recursos, é comum criar branches de manutenção (como "hotfix" para correção rápida de bugs) e branches de recursos (como "feature" ou "develop" para desenvolvimento de novas funcionalidades).
- **Histórico Linear**: O Git mantém um histórico linear de commits para cada branch. Isso significa que, mesmo que você tenha várias branches de desenvolvimento, o histórico de cada branch é independente e organizado de forma linear.
- **Branches Remotas**: Além das branches locais, o Git permite criar e trabalhar com branches remotas, que estão em um repositório remoto (como no GitHub). Você pode empurrar (push) branches locais para um repositório remoto e puxar (pull) branches remotas para seu repositório local.

**Alguns comandos para serem utilizados no Git:**
- git init: inicializa um repositório Git em um diretório;
- git add: adiciona arquivos ao staging area;
- git commit: cria um novo commit com as alterações adicionadas ao staging area;
- git push: envia as alterações locais para um repositório remoto;
- git pull: baixa as alterações de um repositório remoto para o repositório local;
- git branch: lista, cria ou deleta branches;
- git merge: mescla alterações de uma branch em outra;
- git clone: clona um repositório remoto para o repositório local;
- git status: mostra o status atual do repositório (mostra o que está em staging e o que está mudado);
- git log: mostra o histórico de commits do repositório;

### Ambientes de Desenvolvimento

#### O que é?

Um ambiente de desenvolvimento é um **conjunto de ferramentas**, **bibliotecas** e **configurações** que permitem que um **desenvolvedor** **crie**, **teste** e **execute** **software**. Esses ambientes podem ser configurados de diversas formas, dependendo das necessidades do projeto e das preferências do desenvolvedor.

O **objetivo** de um ambiente de desenvolvimento é **fornecer** ao desenvolvedor as **ferramentas necessárias** para que ele possa **trabalhar de forma eficiente e produtiva.**

#### Python e Anaconda

**Anaconda** e o **Python** podem nos ajudar em **programação científica e gerenciamento de pacotes**. O **Anaconda** é uma **distribuição** de **Python** que **facilita o gerenciamento de pacotes e a implantação em múltiplos sistemas operacionais**. Ele **inclui uma série de bibliotecas e ferramentas para análise de dados, aprendizado de máquina, visualização, entre outras áreas da programação científica**. Já o Python é uma linguagem de programação de alto nível que é amplamente utilizada em diversas áreas, incluindo ciência de dados, inteligência artificial, desenvolvimento web, entre outras. Com o Python, é possível criar programas e scripts para automatizar tarefas, processar dados, criar visualizações, entre outras atividades. Em resumo, o **Anaconda e o Python são ferramentas poderosas** para quem trabalha com programação **científica e análise de dados**, permitindo que os desenvolvedores trabalhem de forma mais eficiente e produtiva.

### Ambientes Virtuais

**Ambientes virtuais** são **ambientes isolados que permitem o uso de diferentes versões de bibliotecas em um mesmo sistema**. Eles permitem que os **desenvolvedores criem ambientes de desenvolvimento específicos para cada projeto**, com suas **próprias dependências e configurações**. Isso é especialmente **útil quando se trabalha em vários projetos ao mesmo tempo**, ou quando se **precisa testar diferentes versões de bibliotecas ou pacotes**. Com os ambientes virtuais, é possível criar um ambiente de desenvolvimento limpo e isolado para cada projeto, sem interferências de outras bibliotecas ou pacotes instalados no sistema. Isso **ajuda a evitar conflitos de dependências e a garantir que o código seja executado de forma consistente em diferentes sistemas**. A figura a seguir mostra dois arquivos para criação de ambientes virtuais com o Anaconda. O arquivo à esquerda apresenta uma extensão .yml no qual é possível criar um ambiente totalmente automatizado, instalando inclusive a versão do Python. Na direita é apresentado um arquivo com a extensão .txt, geralmente denominado requirements.txt no qual apresenta apenas os pacotes e suas respectivas versões.

![ambiente virtual](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/03%20-%20Cultura%20e%20Práticas%20Dataops%20e%20Mlops/images/ambienteVirtual.png)

**Figura à esquerda**: comandos para a criação e ativação de um ambiente:
- conda env create -f environment.yml (cria o ambiente)
- conda activate mlops-env (ativa o ambiente criado)
- conda deactivate (desativa o ambiente)

**Figura à direita**: comandos para a criação de um ambiente vazio:
- conda create --name myenv python=3.9 (cria o ambiente apenas com a versão 3.9 do Python)
- conda activate myenv (ativa o ambiente)
- Ex.: pip install "tensorflow<2.11" (instala um ou vários pacotes)

### Registro de Modelos e Ciclo de Vida

Um registro de modelos de ML, também conhecido como **controle de versão de modelos** ou **model registry**, é uma ferramenta que permite **centralizar todas as informações sobre modelos de Machine Learning**, incluindo detalhes sobre **parâmetros**, **métricas de desempenho** e **versões anteriores** do modelo. Ele também **permite reverter alterações** feitas em modelos e **escolher qual modelo é o melhor para ser utilizado em produção**. **Alguma das ferramentas** que podem ser utilizadas para se registrar os modelos são o **MLflow** e **Wandb**

![Código de Registro de Modelo](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/03%20-%20Cultura%20e%20Práticas%20Dataops%20e%20Mlops/images/codigoRegistroModelo.png)

**O código faz a seguinte sequência de passos**:

- **Importação de Bibliotecas:** No início, importamos as bibliotecas necessárias para o código. O MLflow é a biblioteca principal que usamos para registrar métricas e modelos treinados. Scikit-learn é uma biblioteca popular para aprendizado de máquina em Python.
- **Inicialização da Execução do MLflow**: Inicializamos a execução do MLflow com mlflow.start_run(), garante o experimento seja inicializado.
- **Treinamento do Modelo**: Aqui, criamos um modelo de classificação chamado "RandomForestClassifier" com 100 árvores de decisão. O modelo é treinado com os dados de treinamento.
- **Fazendo Previsões e Calculando a Métrica**: Usamos o modelo treinado para fazer previsões no conjunto de teste e calculamos a métrica de acurácia. A acurácia mede a proporção de previsões corretas em relação ao total de previsões.
- **Registro da Métrica no MLflow**: Utilizamos o MLflow para registrar a métrica de acurácia. Isso nos permite acompanhar o desempenho do modelo ao longo do tempo.
- **Salvando o Modelo Treinado**: O modelo treinado é salvo no MLflow com um nome específico, "random_forest_model". Isso permite que você reutilize o modelo posteriormente.
- **Encerramento da Execução do MLflow**: Finalizamos a execução do MLflow com mlflow.end_run(), garantindo que todas as métricas e registros do modelo sejam armazenados corretamente.

No geral, este código demonstra como treinar um modelo de classificação, avaliar seu desempenho, registrar métricas e salvar o modelo treinado usando o MLflow, uma ferramenta poderosa para gerenciamento de projetos de aprendizado de máquina.

### Ciclo de Vida e Ambientes

Os **ambientes** de **teste**, **homologação** e **produção** são ambientes utilizados no **processo de implementação de modelos de Machine Learning** para **gerenciar o ciclo de vida** de um modelo. O ambiente de **teste** é onde são realizados os **testes iniciais**, em um ambiente semelhante ao de produção, para **identificar problemas iniciais**. O ambiente de **homologação** é onde são realizados **testes mais amplos**, **utilizando dados reais** e, em alguns casos, **clientes podem validar o modelo**. Já o ambiente de **produção** é onde o **modelo é liberado para utilização**, utilizando dados reais e em várias situações.

### Automatização

A **automatização** é a utilização de **tecnologias e ferramentas para automatizar processos e tarefas** que antes eram realizados manualmente. Pode ser aplicada em diversas áreas, como desenvolvimento de software, infraestrutura, operações, marketing, finanças, entre outras. Tem como objetivo **aumentar a eficiência e a produtividade, reduzir erros e custos**, além de **liberar os profissionais para se concentrarem em tarefas mais estratégicas e de maior valor agregado**. A automatização pode ser **realizada** por meio de **scripts**, ferramentas de integração contínua e entrega contínua **(CI/CD)**, **robôs**, **inteligência artificial**, entre **outras tecnologias**.

#### Testes automatizados

Testes automatizados são **testes de software** que são **executados automaticamente por meio de ferramentas e scripts**, **sem** a necessidade de **intervenção humana**. Esses testes são utilizados para **garantir** que o **software** está **funcionando corretamente** e que as **alterações** realizadas no código **não causaram efeitos colaterais indesejados**.

Os testes automatizados podem ser realizados em diferentes níveis, como **testes unitários**, **testes de integração**, **testes de aceitação**, entre outros. Eles **podem** ser **executados** em **diferentes momentos** do ciclo de vida do software, como **durante o desenvolviment**o, **antes do lançamento** ou **após a implantação**.

Entre as **vantagens** dos testes automatizados, estão a **redução de erros**, a **melhoria da qualidade do software**, a **documentação dos cenários esperados** e dos **tratamentos em caso de erro**, a **economia** de **tempo** e **recursos**, entre outras.

##### Testes em scripts de treinamento

Testes em scripts de treinamento são **testes automatizados** que **verificam** a **corretude** e a **consistência** do **código relacionado ao treinamento de modelos de machine learning**. Esses testes são projetados para **testar partes específicas do código do modelo** e ajudam a **garantir** que o **código esteja implementado corretamente** e que os **resultados produzidos** pelo modelo sejam **precisos** e **confiáveis**.

Os testes em scripts de treinamento podem ser **usados** para **validar** as **saídas** do modelo em **diferentes cenários** e **permitem** ter **confiança na qualidade do código** e nos **resultados produzidos**. Eles são uma parte importante do processo de desenvolvimento de modelos de machine learning e ajudam a **garantir** que o **modelo esteja funcionando corretamente** antes de ser implantado em produção.

O **pytest** é uma ferramenta muito útil para **escrever e executar testes em Python**. Ele facilita a automação de testes e a organização de casos de teste. A seguir serão apresentados alguns **passos básicos** para usar o **pytest** e **testar scripts de treinamento**.

1) Se ainda não tem o pytest instalado, pode instalá-lo usando o pip: ```pip install pytest``` 
2) Crie um arquivo chamado ```test_treinamento.py``` dentro do diretório de testes. Neste arquivo, você escreverá os testes para o seu script de treinamento.
3) No terminal, navegue até o diretório raiz do seu projeto e execute o comando: ```pytest```
4) O pytest irá procurar por arquivos que começam com ```test_``` ou terminam com ```_test.py``` e executará os testes contidos neles. Se tudo estiver configurado corretamente, você deverá ver a saída dos testes no console.

**Dicas adicionais:**

1) Use ```assert``` para verificar se o resultado retornado pela função de treinamento é o que você espera.
2) Você pode escrever vários testes diferentes para diferentes cenários e casos de borda.
3) Considere usar dados de teste reais ou gerados aleatoriamente para testar diferentes situações.

## UNIDADE 04