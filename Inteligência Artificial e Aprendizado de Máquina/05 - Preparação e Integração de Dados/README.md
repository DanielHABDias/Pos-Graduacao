# 05 - Preparação e Integração de Dados

## SUMÁRIO

## UNIDADE 01

### TEMAS ABORDADOS

- Dados, Informação e Inteligência
- Bussines Intelligence
- Self Service BI (SSBI)
- Governança de dados
- Identificação de requisitos
- Definição de Arquitetura processo de coleta de dados.

### DADOS, INFORMAÇÃO, CONHECIMENTO E INTELIGÊNCIA

- Os *Dados* são registros soltos sem nenhuma qualquer análise.
    - Ex: 500 mil. 500 mil o que?
- A *Informação* seria qualquer estruturação ou organização desses dados.
    - Ex: Esse mês Minas Gerais faturou 500 mil reais.
- O *Conhecimento* envolve o entendimento, por alguém, de um padrão a ser seguido baseado em informações.
    - Ex: Padrão da empresa é ganhar em média 1 milhão por mês.
- *Inteligência* é a capacidade de aprender com a experiência, resolver problemas e usar o conhecimento para se adaptar a novas situações.    
    - Ex: Já queimamos uma vez a mão com fogo, então nunca mais iremos tocar no fogo.

![fluxo do dado até o conhecimento](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/05%20-%20Preparação%20e%20Integração%20de%20Dados/images/fluxoDadoAteConhecimento.png)

![fluxo do dado até a informação](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/05%20-%20Preparação%20e%20Integração%20de%20Dados/images/fluxoDadoAteInformacao.png)

### BUSINESS INTELLIGENCE - BI

- *BI* é um termo abrangente que inclui apps, infraestruturas, ferramentas e práticas que permuitem: *o acesso e a análise das informações para melhorar e otimizar decisões e desempenho das CORPORAÇÕES*.

> Os dados são coletados (extraídos), transformados e carregados em estruturas informacionais, oferecendo assim, desempenho e facilidade ao manipular os dados.

### SELF SERVICE BI - SSBI

- O *Self-Service BI* é uma forma de "autoserviço" na qual os profissionais de negócios são habilitados e incentivados a realizar consultas, gerar relatórios por conta própria, com suporte da TI. Ele ajuda a criar Governança de Dados na cultura da empresa.

> Antigamente um profissional específico tinha que gerar os blocos de análise, e hoje em dia o usuário final consegue acessar os dados e gerar relatórios muito mais facilmente. 

### GOVERNANÇA DE DADOS - G.D.

- *Governaça de dados* é o exercícios de autoridade, controle, planejamento, monitoramento, disponibilidade, segurança e execução dos ativos de dados e seu respectivo consumo.

- PASSOS: 
    1. *Requisitos externos, Conformidade e Patrocínio.*
    2. *Objetivos e Resultados Chave.*
    3. *Escritório de Governança de Dados.*
    4. *Dados críticos de negócio.*
    5. *Catálogo/Linhagem de Dados.*
    6. *Normas, Padrões e Procedimentos.*
    7. *Camada acesso/compartilhamento de dados.*
    8. *Qualidade dos dados.*
    9. *Segurança dos dados.*

![Passos para Governança de Dados](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/05%20-%20Preparação%20e%20Integração%20de%20Dados/images/passosGovernancaDados.png)

### IMPLEMENTAÇÃO

*Ciclo* de Vida de *ETL*, segundo *Kimball*:

![The planning and design thread](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/05%20-%20Preparação%20e%20Integração%20de%20Dados/images/planningAndDesignThread.png)

#### REQUISITOS E REALIDADE

- Requisitos do neǵocio:
    - Envolvem entrevistas e reuniões.
    - Ocorre a identificação das fontes de dados.
    - Acontecem descobertas significativas que afetarão as necessidades do negócio.

- Perfil de Dados:
    - Uma análise sistemática da qualidade dos dados nas fontes determina o esforço de construção de um produto.
    - Uma fonte de dados muito limpa exige o mínimo de intervenção humana antes de carregar no seu destino.

- Segurança dos dados:
    - Deve-se ter acesso a leitura as fontes de origem.
    - A gestão de segurança final deverá ser tratada na governança de dados da empresa, envolvendo profissionais de T.I.

#### ARQUITETURA

A escolha da arquitetura é uma decisão fundamental.

- PASSOS:
    - Definição/compra de uma ferramenta.
    - Definição do local (path) onde estão os dados.
    - Dependência de tarefas vertical X horizontal.
    - Agendamento (Scheduler) das tarefas.
    - Tratamento de exceção.
    - Recuperação e reinicio.
    - Segurança do ambiente (rotinas de backup).

## UNIDADE 02

### TEMAS ABORDADOS

- Entendimento do processo ETL.
- Ferramentas de Self Service Business Intelligence (SSBI).
- Conceitos de estrutura dos dados – Fontes de dados:
    - Estruturado
    - Semi-estruturado
    - Não estruturado
    - Projeto ETL - Ferramenta Power BI

### IMPLEMENTAÇÃO DO SISTEMA - ETL

*ETL:* 
    - *E*xtract
    - *T*ransform
    - *L*oad

Exemplo de ETL: Projeto de Web Scrapping que coleta os dados, normaliza e salva no banco.

#### E - EXTRACT

- A primeira parte do processo ETL é coletar os dados das fontes de origem.
- Na grande maioria existem fontes heterogêneas de dados.
- Fonte comuns são bases de dados, flat-files, planilhas, páginas web, XML etc.

> Uma vez que seu sistema ETL é iniciado logo se percebe a necessidade de integração de fontes diferentes é um grande desafio.

#### T - Transform

[Flux do ETL](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/05%20-%20Preparação%20e%20Integração%20de%20Dados/images/fluxoETL.png)

- Definindo Dados com Qualidade:
    - Correto.
    - Sem ambiguidade.
    - Consistente.
    - Completo.
- Analisando Dados com Anomalias
    - São dados que não se encaixam no contexto do restante dos dados armazenados.
    - Tem por consequência o retrabalho, tendo que refazer o processo ETL.
    - Existem técnicas de detecção para verificar esses dados com anomalias. Olham o histórico e fazem análises com amostras.

- A fase de transformação consiste em aplicar uma série de regras ou funções sobre os dados extraídos.
- Essas regras são baseadas nos requisitos de negócios levantados.