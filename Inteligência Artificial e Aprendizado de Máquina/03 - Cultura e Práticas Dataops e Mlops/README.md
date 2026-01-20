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