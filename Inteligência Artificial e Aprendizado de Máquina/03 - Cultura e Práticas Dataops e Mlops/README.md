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

## Papel do Engenheiro de Aprendizado de Máquina

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

## UNIDADE 04