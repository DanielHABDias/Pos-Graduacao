# 01 - Data Discovery e Analytics

## 📘 Sumário
- [01 - Data Discovery e Analytics](#01---data-discovery-e-analytics)
  - [📘 Sumário](#-sumário)
  - [UNIDADE 01](#unidade-01)
    - [Dados para Negócios](#dados-para-negócios)
    - [KPIs](#kpis)
      - [O que são KPIs?](#o-que-são-kpis)
      - [**KPI Finalidade:**](#kpi-finalidade)
      - [**KPI Benefícios: (Controle da Organização)**](#kpi-benefícios-controle-da-organização)
      - [**KPI Etapas:**](#kpi-etapas)
      - [**KPI Exemplos:**](#kpi-exemplos)
    - [Sistema de Suporte à Decisão (SSD)](#sistema-de-suporte-à-decisão-ssd)
      - [O que é SSD?](#o-que-é-ssd)
      - [Modelos de SSD](#modelos-de-ssd)
    - [OLAP (Online Analytical Processing)](#olap-online-analytical-processing)
      - [O que é OLAP?](#o-que-é-olap)
      - [Arquitetura de Business Intelligence (BI)](#arquitetura-de-business-intelligence-bi)
      - [OLAP Cubes](#olap-cubes)
      - [Arquitetura OLAP](#arquitetura-olap)
      - [Tipos de Operações OLAP](#tipos-de-operações-olap)
      - [Ciclo de Vida Projeto Dados](#ciclo-de-vida-projeto-dados)
      - [Passo a Passo de Criação de OLAP](#passo-a-passo-de-criação-de-olap)
      - [Resultado OLAP](#resultado-olap)
      - [Ferramentas OLAP](#ferramentas-olap)
    - [🧭 Conclusão da Unidade 1](#-conclusão-da-unidade-1)
  - [UNIDADE 02](#unidade-02)
    - [Data-Driven](#data-driven)
      - [O que é Data-Driven](#o-que-é-data-driven)
      - [Características de uma empresa Data Driven](#características-de-uma-empresa-data-driven)
      - [Benefícios de ser Data-Driven:](#benefícios-de-ser-data-driven)
      - [Exemplo de Sucesso do WalMart](#exemplo-de-sucesso-do-walmart)
      - [O que não é Data-Driven](#o-que-não-é-data-driven)
      - [Como criar essa cultura?](#como-criar-essa-cultura)
      - [Diferenças entre empresas Data-Driven e Não Data-Driven](#diferenças-entre-empresas-data-driven-e-não-data-driven)
      - [Etapas Data-Driven](#etapas-data-driven)
    - [Data Discovery](#data-discovery)
      - [O que é Data Discovery?](#o-que-é-data-discovery)
      - [Etapas de Data Discovery](#etapas-de-data-discovery)
      - [Análise Descritiva e Diagnóstica](#análise-descritiva-e-diagnóstica)
      - [Análise Preditiva](#análise-preditiva)
      - [Análise Prescritiva](#análise-prescritiva)
      - [Tradicional BI x Data Discovery](#tradicional-bi-x-data-discovery)
        - [Fluxo do BI Tradicional:](#fluxo-do-bi-tradicional)
        - [Fluxo do Self-Service (Data Discovery):](#fluxo-do-self-service-data-discovery)
      - [O que é Self Service Analytics?](#o-que-é-self-service-analytics)
    - [Análise Descritiva](#análise-descritiva)
      - [O que é Análise Descritiva?](#o-que-é-análise-descritiva)
      - [Objetivo da Análise Descritiva](#objetivo-da-análise-descritiva)
      - [Características da Adequação dos Dados para Análise](#características-da-adequação-dos-dados-para-análise)
      - [Vantagens e Desvantagens](#vantagens-e-desvantagens)
      - [Variáveis](#variáveis)
      - [Taxonomia das Variáveis](#taxonomia-das-variáveis)
        - [Variáveis Qualitativas (Categóricas)](#variáveis-qualitativas-categóricas)
        - [Variáveis Quantitativas (Numéricas)](#variáveis-quantitativas-numéricas)
      - [Distribuição de Frequência](#distribuição-de-frequência)
        - [Por que usar?](#por-que-usar)
        - [Distribuição de Frequência para Variáveis Qualitativas](#distribuição-de-frequência-para-variáveis-qualitativas)
        - [Distribuição de Frequência para Quantitativas Discretas](#distribuição-de-frequência-para-quantitativas-discretas)
        - [Distribuição de Frequência para Quantitativas Contínuas](#distribuição-de-frequência-para-quantitativas-contínuas)
      - [Séries Temporarais](#séries-temporarais)
      - [Etapas da Análise Descritiva](#etapas-da-análise-descritiva)
    - [Análise Preditiva](#análise-preditiva-1)
      - [O que é Análise Preditiva?](#o-que-é-análise-preditiva)
      - [Objetivo da Análise Preditiva](#objetivo-da-análise-preditiva)
      - [Cuidados com a Análise Preditiva](#cuidados-com-a-análise-preditiva)
      - [Onde se aplica?](#onde-se-aplica)
      - [Os 3 V's da Análise Preditiva](#os-3-vs-da-análise-preditiva)
        - [Variedade](#variedade)
        - [Veracidade](#veracidade)
        - [Velocidade](#velocidade)
      - [Etapas da Análise Preditiva](#etapas-da-análise-preditiva)
        - [Como estruturar?](#como-estruturar)
      - [Técnicas de Regressão](#técnicas-de-regressão)
        - [O que é Regressão?](#o-que-é-regressão)
        - [Objetivos da Regressão](#objetivos-da-regressão)
        - [Regressão Linear Simples](#regressão-linear-simples)
        - [Regressão Linear Múltipla](#regressão-linear-múltipla)
        - [Regressão Polinomial](#regressão-polinomial)
        - [Regressão Logística (Classificação)](#regressão-logística-classificação)
        - [Regressão Ridge](#regressão-ridge)
        - [Regressão Lasso](#regressão-lasso)
        - [Elastic Net](#elastic-net)
        - [Regressão por Árvore de Decisão](#regressão-por-árvore-de-decisão)
        - [Regressão com Redes Neurais](#regressão-com-redes-neurais)
        - [Etapas de Construção de um Modelo de Regressão](#etapas-de-construção-de-um-modelo-de-regressão)
        - [Pressupostos da Regressão Linear](#pressupostos-da-regressão-linear)
        - [Aplicações Típicas](#aplicações-típicas)
        - [Quando Usar Cada Tipo de Regressão](#quando-usar-cada-tipo-de-regressão)
        - [Vantagens](#vantagens)
        - [Desvantagens](#desvantagens)
    - [Análise Prescritiva](#análise-prescritiva-1)
      - [O que é Análise Prescritiva?](#o-que-é-análise-prescritiva)
    - [Aprendizado de Máquina](#aprendizado-de-máquina)
      - [O que é Aprendizado de Máquina?](#o-que-é-aprendizado-de-máquina)
      - [Como os sistemas aprendem](#como-os-sistemas-aprendem)
      - [Relação com outras áreas](#relação-com-outras-áreas)
      - [Principais métodos](#principais-métodos)
    - [Cenarização](#cenarização)
    - [🧭 Conclusão da Unidade 2](#-conclusão-da-unidade-2)
  - [UNIDADE 03](#unidade-03)
    - [Tableau](#tableau)
      - [Utilização do Tableau](#utilização-do-tableau)
      - [Exemplo do Tableau](#exemplo-do-tableau)
      - [Utilização do Tableau](#utilização-do-tableau-1)
        - [Fazendo Joins (União, Interceção e etc)](#fazendo-joins-união-interceção-e-etc)
        - [Nomeclatura das Colunas](#nomeclatura-das-colunas)
        - [Abas do Tableau](#abas-do-tableau)

## UNIDADE 01
### Dados para Negócios

- **Por que utilizar dados que são gerados nas organizações para direcionar os negócios?**
  - Para o auxilio na tomada de decisões estratégicas.
  - Nenhum dado é bom ser descartado, pois no futuro pode ser útil no futuro, pois podem se relacionar com muitas áreas e situações.

### KPIs
#### O que são KPIs?
  - **KPI ou Indicador-Chave de Desempenho**, é uma **métrica** usada para medir o progresso de uma **empresa** ou **projeto** em relação às suas **metas estratégicas**.

  - **Segundo Ferreira, Cassiolato e Gonzales (2009)**, por exemplo:
    > *O indicador é uma medida, de ordem quantitativa ou qualitativa, dotada de significado particular e utilizada para organizar e captar as informações relevantes dos elementos que compõem o objeto da observação. É um recurso metodológico que informa empiricamente sobre a evolução do aspecto observado.* 

  - **Indicadores servem para:**
    - Mensurar os resultados e gerir o desempenho.
    - Embasar a análise crítica dos resultados obtidos e do processo de tomada de decição.
    - Contribuir para a melhora continua dos processos organizacionais.
    - Facilitar o planejamento e o controle do desempenho.
    - Viabilizar a análise comparativa do desempenho da organização e do desempenho de diversas organizações atuantes em áreas ou ambientes semelhantes.

#### **KPI Finalidade:**
  - Indicadores permitem o conhecimento sobre a situação que se deseja modificar,
    estabelecer as prioridades, escolher os beneficiados, identificar os objetivos e traduzi-los em metas e, assim, acompanhar com mais efetividade o andamento dos trabalhos, avaliar os processos, adotar os redirecionamentos necessários e verificar os resultados e os impactos obtidos. Dessa forma, aumentam as chances de serem tomadas decisões corretas e de se potencializar o uso dos recursos.

  - **IMPORTANTE:** 
    - *indicadores apontam mas não resolvem problemas!*
    - *Não é bom começar com muitos indicadores, os melhores indicadores são montados com o tempo*
    - *O escopo devem começar pequeno e depois ir crescendo*

#### **KPI Benefícios: (Controle da Organização)**
  - Coletar dados de uma variável previamente escolhida por meio de sensores posicionados adequadamente;
  - Analisar os dados e detectar desvios em relação a um valor ideal ou planejado;
  - Colocar uma ação corretiva que diminua o gap ou desvio em relação ao valor ideal.
    > Medir é o primeiro passo que leva ao controle e eventualmente à melhoria.
    Se você não a entende, não a controla. Se não a controla, não pode melhorá-la.


#### **KPI Etapas:**
![KPI Etapas](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/KPI_Etapas.png)

#### **KPI Exemplos:**
![KPI Exemplos](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/KPI_Exemplos.png)

  - **NPS significado:** Net Promoter Score, uma métrica que mede a lealdade e a satisfação do cliente com base na probabilidade de recomendarem a empresa a um amigo.

### Sistema de Suporte à Decisão (SSD)
#### O que é SSD?
  - Um **sistema** que proporciona aos seus usuários, não só um **acesso rápido à "sua" informação**, mas também capacidade de realizar a sua **análise e formatação à medida das suas necessidades**.
  -  Um **interativo**, **flexível** e **adaptável** **sistema de informação**, especialmente desenvolvido para **apoiar a solução de um problema gerencial não estruturado para aperfeiçoar a tomada de decisão**. Utiliza dados, provê uma interface amigável e permite ao tomador de decisão ter sua própria percepção.

#### Modelos de SSD
![SSD Modelos](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/SSD_Modelos.png)

### OLAP (Online Analytical Processing)
#### O que é OLAP?
  - O conceito de **O**nline **A**nalytical **P**rocessing ou simplismente **OLAP**, refere-se a um **conjunto de ferramentos** voltadas para acesso e **análise ad hoc de dados**(Usuário constroi relatório), com o **objetivo final de transformar dados** em informações capazes de dar **suporte às decisões gerenciais** de forma **amigável** e **flexível** ao usuário e em **tempo hábil**.
  - Antes tinha de abrir chamados e esperar, hoje em dia é possivel criar gráficos de forma simples e impressionante, mesmo sendo um usuário mais leigo de tecnologia.

#### Arquitetura de Business Intelligence (BI)
![OLAP Arquitetura](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/BI_Arquitetura.png)

  1. **Fontes de Informação (Information Sources – Tier 0)**
  - **Operational Databases**
    - Bases de dados transacionais (OLTP).
    - Usadas no dia a dia da empresa (ERP, CRM, sistemas de vendas).
  - **External Sources**
    - Dados vindos de arquivos, APIs, planilhas e fontes externas à organização. 
  1. **Servidor de Data Warehouse (Tier 1)**
  - **Data Warehouse**
    - Repositório central de dados integrados de várias fontes.
    - Estruturado para análise e tomada de decisão, não para operações transacionais.
  - **Processos ETL (Extract, Transform, Load)**
    - Extract: extração dos dados de múltiplas fontes.
    - Transform: limpeza, padronização, agregação e modelagem dos dados.
    - Load: carregamento dos dados no data warehouse.
  - **Metadata Repository**
    - Repositório com informações sobre os dados (tabelas, tipos, origem, regras de transformação).
    - Garante governança e entendimento dos dados.
  - **Data Marts**
    - Subconjuntos do Data Warehouse focados em áreas específicas (ex.: vendas, finanças, logística).
    - Podem ser dependentes (a partir do Data Warehouse) ou independentes. 
  1. **Servidores OLAP (Tier 2)**
  - **Cubos OLAP**
    - Estruturas multidimensionais que permitem analisar dados em diferentes perspectivas (tempo, região, produto).
    - Suportam operações como drill-down, roll-up, slice e dice.
  - **Processamento Analítico**
    - Computação prévia de agregações para consultas mais rápidas.
    - Pode ser:
      - **MOLAP** (Multidimensional OLAP)
      - **ROLAP** (Relational OLAP)
      - **HOLAP** (Hybrid OLAP)
  1. **Clientes (Tier 3) – Ferramentas de BI**
  - **Data Analysis**
    - Ferramentas de visualização e dashboards (ex.: Power BI, Tableau).
    - Usuários podem explorar os cubos OLAP.
  - **Key Performance Indicators (KPIs)**
    - Indicadores estratégicos extraídos dos dados.
    - Auxiliam na avaliação de desempenho da organização.
  - **Data Mining**
    - Técnicas avançadas para descobrir padrões e predições.
    - Usa algoritmos de inteligência artificial e estatística.
  
  1. **Fluxo Geral do Processo**
    1. Dados são coletados das fontes operacionais e externas.
    2. São processados via ETL e armazenados no Data Warehouse.
    3. São organizados em Data Marts e cubos OLAP para consultas rápidas.
    4. Usuários finais acessam os dados por meio de ferramentas analíticas e de mineração.
   
  2. **Objetivo Final**
    **Transformar dados brutos em informações estratégicas** que possibilitam:
    - Melhor **tomada de decisão**;
    - Maior **eficiência** operacional;
    - **Antecipação** de tendências e oportunidades.

#### OLAP Cubes
![OLAP Cubes](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/OLAP_Cubes.png)

> "Parece uma planilha para acesso rápido do usuário"

**Exemplo:**
![OLAP Exemplo 1](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/OLAP_Exemplos_1.png)
![OLAP Exemplo 2](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/OLAP_Exemplos_2.png)
![OLAP Exemplo 3](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/OLAP_Exemplos_3.png)

#### Arquitetura OLAP
![OLAP Arquitetura](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/OLAP_Arquitetura.png)

#### Tipos de Operações OLAP
![OLAP Operações](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/OLAP_Operacoes.png)

**Pivot** é trocar o que é linha para coluna e vice-versa:
![OLAP Pivot](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/OLAP_Pivot.png)

Exemplo de **ROLL-UP** e **DRILL-DOWN**:
![Exemplo Roll-UP e Drill-Down](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/OLAP_ExemplosOperacoes_1.png)

Exemplo de **DICE** e **SLICE**:
![Exemplo de Dice e Slice](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/OLAP_ExemplosOperacoes_2.png)

#### Ciclo de Vida Projeto Dados
![Ciclo de Vida de Projeto de Dados](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/ProjetoDados_CicloVida.png)

#### Passo a Passo de Criação de OLAP
![Passo a Passo de Criação de OLAP](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/OLAP_PassoAPasso.png)

Sobre a **Entrevista** com o Usuário Chave:
![Entrevista para OLAP Usuario Chave](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/OLAP_EntrevistaUsuario.png)

**Dicas:**
  - Criar Atas de reunião para registrar tudo e não ter futuros conflitos com o cliente.
  - Criar interfaces com as cores bem definidas para ajudar na visualização(priorize cores da marca da empresa).
  - Levantar requisitos corretamente e planejar a interface de forma visual.

#### Resultado OLAP
![Resultado OLAP](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/OLAP_Resultado.png)

#### Ferramentas OLAP

> Utilizadas para criação de interfaces para análise de dados.

- **COGNOS**
- **SAP**
- **ORACLE**
- **PENTHO**
- **MicroStrategy**
- **ThoughtSpot**
- **QLIK**
- **TABLEAU**
- **POWER BI**

### 🧭 Conclusão da Unidade 1

A **Unidade 1 – Dados para Negócios e Suporte à Decisão** apresentou os **fundamentos essenciais da análise de dados corporativos**, abordando desde a **importância dos dados** até o uso de **ferramentas analíticas** para apoiar decisões estratégicas.

📊 **Primeiramente**, foi destacado o papel dos **dados** como ativos valiosos para as organizações modernas. A coleta, organização e análise eficiente dessas informações permite compreender o desempenho empresarial e antecipar oportunidades e riscos.

🎯 **Em seguida**, exploramos o conceito de **KPIs (Key Performance Indicators)** — indicadores que traduzem os objetivos estratégicos em métricas mensuráveis. Aprendemos que os KPIs não apenas monitoram resultados, mas também **orientam ações corretivas e melhorias contínuas**, sendo a base de qualquer processo de **gestão orientada a dados**.

🧩 **Avançando**, estudamos os **Sistemas de Suporte à Decisão (SSD)**, que integram dados, modelos e interfaces amigáveis para **auxiliar gestores em decisões complexas e não estruturadas**. Eles representam o elo entre os dados operacionais e a inteligência empresarial.

📈 Por fim, aprofundamos o **conceito de OLAP (Online Analytical Processing)** e sua **arquitetura dentro do Business Intelligence (BI)**.  
O OLAP permite **analisar grandes volumes de dados de forma multidimensional e interativa**, utilizando operações como *drill-down*, *roll-up*, *slice*, *dice* e *pivot*.  
Essas operações tornam a exploração dos dados rápida e intuitiva, permitindo que os usuários **gerem relatórios e insights sem depender de TI**.

💡 **Em resumo**, a Unidade 1 demonstra que:
- A **tomada de decisão moderna** depende fortemente de **dados estruturados e bem analisados**;
- **Indicadores (KPIs)** e **sistemas OLAP/BI** são os pilares do **suporte analítico** às estratégias empresariais;
- E que o **profissional de dados** deve compreender não apenas as ferramentas, mas também o **contexto de negócio** e as **necessidades dos usuários-chave**.

> **Conclusão final:**  
> A transformação de dados em conhecimento é o verdadeiro diferencial competitivo nas organizações do século XXI.  
> Quem domina os dados, domina as decisões.

## UNIDADE 02
  - A chave está na cultura de dados, não apenas em ferramentas ou bancos.
  - Pessoas e processos são mais importantes do que a tecnologia em si.
  - O cientista de dados é uma combinação moderna de estatístico, programador e comunicador, capaz de transformar dados em histórias que geram ação.
  - Mais do que dominar técnicas, ele precisa fazer as perguntas certas, unindo conhecimento técnico e visão de negócio.

### Data-Driven
#### O que é Data-Driven

**Data Driven** significa **“orientado por dados”** — é uma abordagem em que as **decisões, estratégias e ações** de uma organização são **baseadas** em **análises e evidências obtidas a partir de dados**, e não apenas em intuição, opinião ou experiência pessoal.

**Em outras palavras:**
> Ser **Data Driven** é usar **dados** como **guia** para **entender** o **presente**, **prever** o **futuro** e **decidir** com mais **precisão**.

#### Características de uma empresa Data Driven
  - Coleta e organiza dados continuamente de várias fontes (internas e externas).
  - Baseia decisões estratégicas em métricas e indicadores (KPIs).
  - Utiliza ferramentas de Business Intelligence (BI) e análise de dados.
  - Estimula uma cultura de dados, onde todos os níveis da empresa valorizam informações concretas.
  - Monitora resultados e ajusta ações com base em análises e evidências.

#### Benefícios de ser Data-Driven:
  - Decisões mais **assertivas** e **rápidas**;
  - **Redução de erros e custos**;
  - **Maior competitividade** e inovação;
  - **Melhoria contínua** com base em resultados reais.
  
#### Exemplo de Sucesso do WalMart

![Exemplo de sucesso do WalMart](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/DataDriven_Exemplo.png)

> Eles **analisaram** utilizando os **dados do DW** (Data Warehouse enorme deles), que após um caso de furacão o maior número de vendas **não foram de itens óbvios** (Lanterna e etc), mas sim de torta de morango para comemorar. Então realizaram um **grande movimento logístico** para os futuros  furacões e **ganharam muito dinheiro**.

#### O que não é Data-Driven

Muitas **empresas morrem**, por conta de passarem pelos seguintes estados:
![Erro Corporativo](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/DataDriven_ErroCorporativo.png)

> A **falta** de **planejamento**, **trabalho em equipe** e muitos outros fatores podem **levar uma empresa a falência**.

Uma empresa que acerta:
![Acerto Corporativo](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/DataDriven_AcertoCorporativo.png)

#### Como criar essa cultura?
  - As **melhore organizações** orientadas a dados se **concentram incansavelmente em manter seus 
    dados limpos.** 
  - Os dados devem ser:
    - **organizados**
    - **bem documentados**
    - **livres de erros**
  - A **limpeza dos dado**s costuma ser a parte mais **desgastante**. Organizações bem-sucedidas 
    investem pesadamente em ferramentas, processos e auditorias regulares. 
  - Em resumo... **Investir pesado na Qualidade de Dados**
  - Uma das **distinções** mais importantes **entre organizações** que são orientadas por 
    dados e aquelas que não são é **como elas abordam a formulação de hipóteses e a 
    resolução de problemas**. 
  - Todas as organizações orientadas por dados seguem alguma variante do método 
    científico, que chamamos de método científico de dados: 
    - **Comece com dados.** 
    - **Desenvolva intuições sobre os dados** e as **perguntas** que eles podem responder.
    - **Aproveite seus dados atuais** para entender melhor se é a pergunta certa a ser 
      feita. **Se não, itere até que você tenha uma hipótese testável.**

#### Diferenças entre empresas Data-Driven e Não Data-Driven
  - Empresas Data-Driven fazem **perguntas** sobre o **futuro**: "Quanto **vamos** vender no Natal?"
  - Empresas Não Data-Driven fazem **perguntas** somente sobre o **presente** e o **passado**: "Quanto **vendemos** no Natal passado?"

#### Etapas Data-Driven

Empresas Data-Driven segue as seguintes etapas:
![Etapas Data-Driven 1](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/DataDriven_Etapas_1.png)

![Etapas Data-Driven 2](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/DataDriven_Etapas_2.png)

> **"Ser Data-Drive não é ignorar seus instintos."**

### Data Discovery

#### O que é Data Discovery?
- Permite que os usuários desenvolvam e refinem visualizações e análises de dados
  estruturados e não estruturados usando termos de pesquisa.
- Possibilita que as áreas de negócio utilizem dados relevantes em modo “self-service”e
  em todo lugar – a ferramenta fornece ao usuário flexibilidade na composição e
  utilização das informações, acessados de tablets e smartphones, sem a necessidade de
  relatórios pré-definidos e estáticos, que normalmente demoram muito tempo para
  serem desenvolvidos e que criam uma alta dependência do setor de TI.
- Sem a necessidade de criar relatórios pré-definidos, como anteriormente, é possível
  levar a análise de informações para todos os setores e camadas das empresas.

#### Etapas de Data Discovery

- Visualização de dados
- Descoberta destas informações
- Influência nos negócios (momento em que a análise reflete em ações)
- Análise preditiva
  
![Data Discovery Etapas](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/DataDiscovery_Etapas.png)

#### Análise Descritiva e Diagnóstica

- Monitorar e Interpretar KPIs através de dados históricos
- Normalmente a pergunta é O que?
  - Ajudar entender o porque estamos neste ponto
- Permite investigar os dados para detectar a causa raiz do problema.
- Normalmente a pergunta é Por quê?

#### Análise Preditiva

- Utilização de dados históricos para prever eventos futuros.
- Normalmente a pergunta é O que vai acontecer?

> Avaliar de forma preditiva significa tomar como referência dados do passado e do presente para, a 
  partir deles, formular prognósticos.
  Esse tipo de análise serve para trazer respostas tanto para questões já conhecidas quanto para 
  aquelas que você nem desconfiava que existiam.
  Isso porque, ao avaliar o negócio de maneira preditiva, a empresa se habilita a ver ainda mais longe, 
  se valendo de recursos e técnicas especiais.

#### Análise Prescritiva

- Recomendações de ações a serem tomadas
- Normalmente a pergunta é O que devo fazer?

#### Tradicional BI x Data Discovery

![Comparação Tradicional BI x Data Discovery](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/DataDiscovery_Comparacao.png)

> **Recomendação da Gartner:**
  “Usar Business Intelligence e Data Discovery ao mesmo tempo é o ideal.”

| Aspecto | **BI Tradicional (Business Intelligence)** | **Data Discovery (Descoberta de Dados)** |
|----------|--------------------------------------------|-------------------------------------------|
| **Objetivo** | Monitorar e reportar **indicadores e métricas já definidas** | Explorar dados para **descobrir padrões, insights e relações** inesperadas |
| **Abordagem** | **Descritiva** – mostra *o que aconteceu* | **Exploratória e Diagnóstica** – busca entender *por que aconteceu* e *o que pode acontecer* |
| **Modelo de uso** | Estruturado, com **relatórios fixos e dashboards padronizados** | **Interativo e dinâmico**, o usuário faz perguntas e visualiza respostas em tempo real |
| **Usuário principal** | **Profissionais de TI e analistas** especializados que constroem relatórios para gestores | **Usuários de negócio** (ex: marketing, finanças) com autonomia para explorar os dados |
| **Fonte de dados** | Dados já tratados e consolidados em **Data Warehouse** | Pode combinar **múltiplas fontes** (DW, planilhas, APIs, etc.) em tempo real |
| **Tempo de resposta** | **Lento** — depende da TI para mudanças em relatórios (pode levar 2 a 4 meses uma solicitação de informação nova) | **Rápido** — o usuário faz autoanálise (*self-service BI*) |
| **Ferramentas típicas** | Cognos, Business Objects, Oracle BI, SSRS | Power BI, Tableau, Qlik Sense, Looker |
| **Governança** | **Alta** — controle rígido sobre dados e acesso | **Mais flexível** — permite experimentação e análises ad hoc |
| **Tratamento de dados** | **Muito forte** — dados passam por ETL (Extração, Transformação e Carga) antes de chegar aos relatórios. São **limpos, padronizados e confiáveis**. | **Mais flexível**, mas nem sempre tão limpo — pode trabalhar com dados crus ou **semi-tratados,** permitindo análise imediata, mas com risco de inconsistências. |
| **Velocidade de análise** | **Mais lento** — porque depende da equipe de TI e de pipelines formais. | **Mais rápido** — o próprio usuário de negócio explora e filtra os dados em tempo real. |

- **BI Tradicional** → Foco em **relatórios consolidados**, úteis para **acompanhamento estratégico** e **indicadores fixos**.  
- **Data Discovery** → Foco em **exploração livre e visual dos dados**, permitindo **insights rápidos e dinâmicos** sem depender da TI.

##### Fluxo do BI Tradicional:
![Fluxo do BI Tradicional](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/DataDiscovery_FluxoBI.png)

##### Fluxo do Self-Service (Data Discovery):
![Fluxo do Self-Service](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/DataDiscovery_FluxoSelfService.png)

#### O que é Self Service Analytics?

Permitir que as **análises de indicadores e manipulação de informações não fique restrita a um pequeno grupo de especialistas.** Ao contrário, o que se deseja é que todos sejam capazes de contribuir como “Analistas de Dados”. Para isso, deve-se criar **interfaces amigáveis** e de **fácil usabilidade** para os **relatórios de acompanhamento** por Analytics.

> É uma forma de **análise** na qual profissionais são incentivados a realizar consultas e gerar **insights** por **conta própria**, com **pouco ou nenhum suporte de TI**.

Para criar um com sucesso:
  - Preparar os Dados
  - Criação de Dashboards
  - Possibilitar Interação Visual
  - Treinar os usuários para análisarem por conta própria montando analises

### Análise Descritiva

#### O que é Análise Descritiva?

Descreve o momento atual, faz um **diagnóstico geral** encima da **base**, **descrevendo** o que **já aconteceu** e o que **está acontecendo**.

> Muito ligada ao BI Tradicional

Por meio da utilização de um Data Warehouse podem desenvolver relatórios, consultas, alertas e tendências usando ferramentas e técnicas de extração de relatótios.

Muito importante e fundamental a área de visualização para realização da análise.

#### Objetivo da Análise Descritiva

- Apresentar o que está acontecendo na organização e entender tendências e causas subjacentes de tais ocorrências.
- Envolve consolidação de fontes de dados e a disponibilização de todos os dados julgados.

#### Características da Adequação dos Dados para Análise

- Confiabilidade 
- Precisão e consistência
- Acessibilidade 
- Segurança e privacidade
- Riqueza de dados 
- Valor corrente/atualidade dos dados
- Granularidade
- Validade
- Relevância

#### Vantagens e Desvantagens 
- **Vantagem** principal é ser um instrumento que confere **imparcialidade** a um estudo, evitando que se formem juízos de valor.
  - Também é o método mais indicado quando se deseja ter uma visão abrangente de um fenômeno e para coletar dados sobre comportamentos.
- **Desvantagem** é se a **amostra utilizada que, se mal selecionada, pode levar a respostas confusas** ou mesmo **não verdadeiras**, o que pode levar a tomadas de **decisões incorretas.**

#### Variáveis 

- Variáveis representam características observadas em um estudo ou conjunto de dados. 
- Podem ser usadas para descrever, comparar e analisar fenômenos.
- Dividem-se em Qualitativas e Quantitativas.
  
#### Taxonomia das Variáveis

![Taxonomia dos Dados](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/AnaliseDescritiva_Taxonomia.png)

##### Variáveis Qualitativas (Categóricas)

- Não possuem valor numérico significativo.
- Representam categorias ou classificações.
- Tipos:
  - Nominais: sem ordem natural.
  Ex.: sexo, cor dos olhos, fumante/não fumante.
  - Ordinais: possuem ordem entre as categorias.
  Ex.: nível de crédito (baixo/médio/alto), escolaridade.

> Observação importante: números usados apenas como códigos (ex.: 1 = masculino, 2 = feminino) não tornam a variável quantitativa. 

##### Variáveis Quantitativas (Numéricas) 

- Representam valores numéricos que fazem sentido matemático.
- Tipos:
  - Discretas: assumem valores inteiros, geralmente contagens.
  Ex.: número de filhos, número de cigarros por dia.
  - Contínuas: assumem infinitos valores dentro de intervalos (podem ter decimais).
  Ex.: peso, altura, idade, tempo, pressão arterial.

> Observação: uma variável pode mudar de tipo conforme o modo de coleta (ex.: idade em anos completos → quantitativa; idade por faixas → qualitativa ordinal).

#### Distribuição de Frequência

Distribuição de frequência é uma forma de organizar dados mostrando quantas vezes cada valor/categoria aparece.

##### Por que usar?
- Facilita análise, interpretação e identificação de padrões.
- Permite visualizar frequências absolutas, relativas (%) e acumuladas.

##### Distribuição de Frequência para Variáveis Qualitativas
- Usada para nominais e ordinais.
- Tabela inclui:
  - Frequência absoluta (contagem)
  - Frequência relativa (percentual)
- Para variáveis ordinais, as categorias devem seguir a ordem natural.
Ex.: meses do ano, níveis de escolaridade.

![Tabela de Variáveis Qualitativas](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/AnaliseDescritiva_VariaveisQualitativas.png)

##### Distribuição de Frequência para Quantitativas Discretas
- Caso assumam poucos valores distintos, tratam-se como classes ordenadas.
Ex.: número de filhos por família.
- Podem incluir:
  - Frequência absoluta
  - Frequência relativa
  - Frequência acumulada

![Tabela de Variáveis Discretas](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/AnaliseDescritiva_VariaveisQuantitativasDiscreta.png)

##### Distribuição de Frequência para Quantitativas Contínuas
- Exige agrupamento em classes.
- Classes seguem o padrão:
  - Ex.: 25 |- 50 (inclui 25.0 até 49.9; 50 entra na classe seguinte).
- Frequentemente representada por histogramas.

![Tabela de Variáveis Discretas](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/AnaliseDescritiva_VariaveisQuantitativasContinua.png)

#### Séries Temporarais

- **Série Temporal** é um **conjunto de observações sobre uma variável, ordenado no tempo**: diariamente (preço de ações, relatórios meteorológicos), mensalmente (taxa de desemprego, IPC), trimestralmente
(PIB).
- **Um dos objetivos do estudo de séries temporais é conhecer o comportamento da série ao longo do tempo** (aumento, estabilidade ou declínio dos valores). Em alguns estudos, esse conhecimento pode ser usado para se fazer previsões de valores futuros com base no comportamento dos valores passados

![Gráfico com Exemplo de Série Temporal](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/AnaliseDescritiva_SeriesTemporais.png)

#### Etapas da Análise Descritiva

![Etapas para Análise Descritiva](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/AnaliseDescritiva_Etapas_1.png)

![Etapas para Análise Descritiva Continuação](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/AnaliseDescritiva_Etapas_2.png)

### Análise Preditiva

#### O que é Análise Preditiva?

**Prever o futuro** sempre foi um grande desejo da humanidade. A análise de dados preditiva significa tomar como **referência dados do passado** e do **presente** para, a partir deles, **formular prognósticos**. Esse tipo de análise **serve para trazer respostas tanto para questões já conhecidas quanto para aquelas que possam vir a acontecer.**

> Este tipo de Análise se alinha mais com **Data Driven**

![Comparação Análise Preditiva](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/AnalisePreditiva_Comparacao.png)

> Segundo o Gartner, a análise preditiva é uma forma de **análise avançada** que **verifica dados** ou conteúdos para responder à pergunta: **o que é provável que aconteça no futuro?**

#### Objetivo da Análise Preditiva
- Por conhecer os dados do passado é **possível prever o comportamento futuro.**
- Em um mercado cada vez mais competitivo a empresa que aplica a **análise preditiva (data-driven)** costuma estar **um passo a frente da concorrência.**
- Utiliza o **máximo dos dados para realizar cáculos para criação de análises** para **prever os futuros comportamentos** e assim realizar **tomadas de decisões estratégicas.**

#### Cuidados com a Análise Preditiva 
- A validação dos modelos preditivos são um tópico à parte, porém, em simples termos, é **necessário** que o modelo preditivo seja **capaz de acertar pelo menos de 70% a 90% em das tentativas.** 
- **Caso ele acerte menos de 50%**, seria o mesmo que competir com a predição de **cara ou coroa**. Já se ele **conseguir atingir 100% ou acima de 95%**, pode ser que exista 
alguma **variável no modelo comprometida.**
- Algumas limitações típicas de modelos preditivos são a **dificuldade de fazer predições sobre categorias múltiplas ou invés de prever se o cliente vai pagar não.** Digamos que os clientes podem: “Pagar à vista”, “Pagar a prazo”, “Pagar por cartão”, “Pagar por boleto”, “Não vai pagar”.
- **As taxas de assertividade por categoria podem ser muito discrepantes.** **Para superar essa limitação** é preciso construir **algoritmos específicos** para o problema além de **efetuar transformações na fase de preparação de dados.**
#### Onde se aplica?

![Onde se aplica 1](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/AnalisePreditiva_OndeAplica_1.png)
![Onde se aplica 2](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/AnalisePreditiva_OndeAplica_2.png)

#### Os 3 V's da Análise Preditiva

![Os 3 V's da Análise Preditiva](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/AnalisePreditiva_3Vs.png)

##### Variedade
- É importante ter uma **boa diversidade de fontes e formatos de dados**, que permitirão uma **análise mais profunda**.
- Apostar em variedade também ajuda a ter **resultados menos “viciados”**, que podem ser causados por uma base de dados única.

##### Veracidade
- De nada adianta ter em mãos um volume enorme de dados se as informações que eles trazem não são **confiáveis.**

##### Velocidade
- Tão importante quanto ter dados confiáveis e diversificados é ter **agilidade para processá-los**, já que **muitos insights podem não ser mais úteis se o timing relevante já tiver passado.**

#### Etapas da Análise Preditiva
##### Como estruturar?

![Etapa para estruturar Análise Predititva](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/AnalisePreditiva_Etapas.png)

1) Definir Objetivo
  - Antes de tudo, é preciso definir: qual é a finalidade da iniciativa? A utilização de um modelo deve ter objetivos claros e alinhados com a estratégia da empresa.
  - O passo seguinte é buscar o benefício esperado com  a  análise  preditiva, seja ele a compreensão do consumidor, seja observar tendências e oportunidades.
  - Existem incontáveis aplicações da tecnologia nos negócios de uma empresa, por isso é importante determinar a abordagem antes de qualquer coisa.

1) Criar um Modelo
  - Definido o objetivo, é  importante criar o  modelo preditivo  que  será utilizado para alcançá-lo.
  - O modelo define o modo como os dados selecionados  para o projeto serão trabalhados, então ele é crucial para o sucesso.
  - Esse passo envolve preparar os dados para que eles possam ser analisados de forma  apropriada, realizar a amostragem experimental e testar qual formato de análise apresenta os melhores resultados.

2) Coletar Dados
  - Tão fundamentais quanto o modelo são os dados com os quais ele será alimentado. 
  
3) Estruturar Dados
  - Uma vez que as fontes foram definidas e os dados  coletados, o passo seguinte envolve a estruturação.  Ela ajudará a organizar as informações para viabilizar análises mais eficientes.
  - Esse processo inclui realizar a limpeza dos dados e também organizá-los em conjuntos que facilitem o processo.

4) Analisar Dados
  - Após os dados estarem prontos, resta realizar a análise propriamente dita, o que deve ser feito com cuidado para alcançar os melhores desfechos.
  - É nesta fase que são produzidos os insights. Para isso, é necessário ter noções estatísticas a fim de avaliar e interpretar gráficos e as tendências que eles apontam.
  - Existem três tipos de análise. A primeira é a univariada, em que cada variável é analisada isoladamente antes do cruzamento; outra é a bivariada, que estabelece relações entre duas variáveis, e a última é a multivariada, que estabelece relações entre mais variáveis.
  
5) Fazer Modelagem
  - Após a condução da análise, é hora de criar o modelo preditivo utilizado para interpretar as informações.
  - Aqui, utilizando técnicas estatísticas, é possível visualizar as relações estabelecidas entre as informações extraídas do banco de dados.
  - Isso é feito por meio de técnicas estatísticas e matemáticas, que podem retornar os insights desejados.

6) Monitorar Dados
  - Nem sempre o modelo utilizado é eterno. É importante acompanhar os resultados que ele produz para fazer os ajustes necessários com o tempo para garantir a qualidade da análise.

> **CUIDADO!!!**
>  - O mercado já comprovou a utilização de técnicas avançadas de análise, como as de machine learning, como ferramentas poderosas para apoiar as organizações nos desafios de retenção de clientes. 
> - Mas estes não devem, no entanto, ser considerados como a solução para este problema. Apesar dos modelos preditivos fornecerem informações valiosas para direcionar as ações de retenção, a fidelidade dos clientes será realmente mantida por boas experiências e uma real vantagem competitiva enxergada sobre os demais concorrentes.

#### Técnicas de Regressão

A regressão é uma técnica estatística usada para **modelar relações
entre variáveis**, permitindo **explicar fenômenos**, **medir impactos**
e **prever valores futuros**. É uma das bases da **Análise Preditiva**.

##### O que é Regressão?

-   Método que estuda a relação entre uma **variável dependente (Y)** e
    uma ou mais **variáveis independentes (X)**.
-   Permite:
    -   Entender como mudanças em X afetam Y.
    -   Prever o comportamento futuro de Y.
    -   Identificar padrões e tendências ocultas nos dados.
-   É fundamental em áreas como negócios, economia, finanças, saúde,
    engenharia e ciência de dados.

##### Objetivos da Regressão

-   **Explicação:** determinar quais variáveis influenciam Y e em que
    intensidade.
-   **Predição:** estimar valores futuros com base em dados históricos.
-   **Diagnóstico:** identificar variáveis mais relevantes, ruídos e
    padrões.
-   **Tomada de decisão:** suportar decisões com base em modelos
    estatísticos.

##### Regressão Linear Simples

Modelo para **uma variável independente**.

**Equação:**

    Y = a + bX

-   Relação linear entre X e Y.
-   Fácil interpretação.
-   Usada em fenômenos com comportamento de tendência simples.

![Regressão Linear](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/AnalisePreditiva_RegressaoLinear.png)

##### Regressão Linear Múltipla

Extensão para **múltiplos preditores (X1, X2, ..., Xn)**.

**Equação:**

    Y = a + b1X1 + b2X2 + ... + bnXn

-   Considera vários fatores simultâneos.
-   Muito utilizada em modelos de negócios.

##### Regressão Polinomial

Captura **relações curvilíneas** entre X e Y.

**Exemplo (2º grau):**

    Y = a + bX + cX²

-   Resolve limitações da regressão linear simples quando o padrão dos
    dados não é linear.
-   Deve ser usada com cautela para evitar overfitting.

##### Regressão Logística (Classificação)

Usada quando Y é **categórica** (ex.: 0/1, sim/não, aprovado/reprovado).

-   Modela **probabilidades** (0 a 1).
-   Baseada na função sigmoide.

![Regressão Logística](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/AnalisePreditiva_RegressaoLogistica.png)

##### Regressão Ridge

-   Técnica **regularizada** para evitar overfitting.
-   Penaliza coeficientes grandes.

##### Regressão Lasso

-   Técnica regularizada com capacidade de **zerar coeficientes**,
    realizando seleção automática de variáveis.

##### Elastic Net

-   Combinação de Ridge + Lasso.
-   Balanceia estabilização e seleção de variáveis.

##### Regressão por Árvore de Decisão

-   Modelo não linear.
-   Interpretação fácil.
-   Capta interações e não exige normalidade.

##### Regressão com Redes Neurais

-   Captura padrões complexos e não lineares.
-   Usada em grandes volumes de dados.

##### Etapas de Construção de um Modelo de Regressão

1.  Definição da variável dependente (Y).
2.  Seleção das variáveis independentes (X).
3.  Coleta e limpeza dos dados.
4.  Análise exploratória (EDA).
5.  Divisão treino/teste.
6.  Treinamento do modelo.
7.  Avaliação (R², RMSE, MAE, AUC etc.).
8.  Interpretação dos coeficientes.
9.  Validação (cross-validation).
10. Implantação e monitoramento.

##### Pressupostos da Regressão Linear

-   Linearidade.
-   Resíduos com média zero.
-   Homocedasticidade.
-   Ausência de multicolinearidade severa.
-   Independência dos erros.
-   Normalidade dos resíduos.

##### Aplicações Típicas

-   Previsão de vendas e demanda.
-   Estimativas financeiras.
-   Modelos de risco.
-   Previsão de churn.
-   Análise de impacto de variáveis.

##### Quando Usar Cada Tipo de Regressão

  |Tipo             | Quando Usar                             |
  |-----------------|-----------------------------------------|
  |Linear Simples   | Relação direta e única entre X → Y      |
  |Linear Múltipla  | Vários fatores influenciam o resultado  |
  |Polinomial       | Relação curva ou não linear             |
  |Logística        | Resultados binários (0/1)               |
  |Ridge            | Multicolinearidade forte                |
  |Lasso            | Muitas variáveis, seleção automática    |
  |Elastic Net      | Multicolinearidade + seleção            |
  |Árvores          | Relações não lineares                   |
  |Redes Neurais    | Alta complexidade e muitos dados        |

##### Vantagens
-   Interpretação simples.
-   Base estatística sólida.
-   Versátil e amplamente aplicável.

##### Desvantagens
-   Sensível a outliers.
-   Depende de pressupostos.
-   Pode sofrer com multicolinearidade.

### Análise Prescritiva
#### O que é Análise Prescritiva?

- Fornecer **recomendações inteligentes para ajudar a alterar o futuro.** Enquanto as **análises preditivas preveem futuros possíveis**, as **análises prescritivas criam suas recomendações** específicas para lidar com esse futuro.

- As **análises prescritivas** na maioria das vezes **dependem de um esforço em equipe** para funcionarem. É preciso criar **recomendações alinhadas com o contexto da empresa** e com as condições de cada equipe que irá realizar essas ações.

![Comparação Análise Prescritiva](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/AnalisePrescritiva_Comparacao.png)

> Aqui vale um parênteses sobre a diferença entre predição (prescritiva) e previsão (preditiva). Entenda a previsão como um subconjunto da predição. Enquanto a predição trata de dizer, de forma genérica, como um fato seria antes de sua ocorrência, a previsão parte do mesmo princípio, mas apenas aplica-se a fatos que estão vinculados ao tempo.

Enquanto a **análise preditiva** se limita a dizer **como provavelmente será o futuro**, a **análise prescritiva** fornece subsídios para **tomar decisões que irão alterar o futuro**. Em outras palavras, **o que deve ser feito para que o futuro desejado se realize.**

### Aprendizado de Máquina
#### O que é Aprendizado de Máquina?

**Aprendizado de máquina (AM) é um ramo da inteligência artificial** que permite que c**omputadores aprendam padrões a partir de dados** e **tomem decisões** com **mínima intervenção humana**. Seu **objetivo central** é fazer com que **sistemas melhorem automaticamente** seu desempenho à medida que **acumulam experiência.**

> Em seu livro pioneiro, T. Mitchell define aprendizagem de máquina (AM) como a área de pesquisa que visa desenvolver programas computacionais capazes de automaticamente melhorar seu desempenho por meio da experiência. A área de AM está baseada em conceitos e resultados de muitas outras áreas, como estatística, inteligência artificial, filosofia, teoria da informação, biologia, ciências cognitivas, complexidade computacional e teoria de controle.

> Seguindo uma linha similar, Alpaydin define a aprendizagem de máquina como a programação de computadores para otimizar um critério de desempenho usando experiências passadas, chamadas de exemplos ou simplesmente dados de entrada. A ideia é que as técnicas envolvidas na AM sejam capazes, de alguma forma, de aprender a resolver os problemas.

#### Como os sistemas aprendem

Sistemas que aprendem são capazes de **adaptar seu comportamento com base em exemplos**. A **aprendizagem** geralmente ocorre de **forma gradual**, por meio de **processos iterativos de ajuste e interação com o ambiente**. Diferentes de **simples memorização**, esses sistemas **modificam características internas para melhorar seu desempenho.**

É importante notar que aprendizagem não exige consciência ou inteligência: animais, insetos e outros seres vivos aprendem estratégias para sobrevivência, indicando que aprender é essencialmente adaptar-se.

#### Relação com outras áreas
A aprendizagem de máquina está profundamente relacionada a:
- **Mineração de dados**, por também extrair conhecimento de grandes bases;
- **Estatística**, pela modelagem de incertezas e padrões;
- **Inteligência artificial**, por compor métodos de tomada de decisão;
- **Teoria da computação**, que fundamenta a complexidade e limites dos algoritmos;
- **Áreas como computação natural, sistemas adaptativos e computação flexível.**

#### Principais métodos
Entre os **métodos** mais estudados em AM, destacam-se técnicas que operam com **dados nominais**, como:

- **Árvores de decisão**
- **Regras de associação e classificação**
- **Tabelas de decisão**
- **Outros algoritmos simbólicos e estruturados**

Esses métodos ajudam a **modelar dados** de forma **interpretável e eficiente**, permitindo que o **sistema aprenda a partir de exemplos** para **realizar previsões, classificações ou diagnósticos.**

### Cenarização

A **cenarização** é uma técnica de **análise multivariada** usada para **identificar combinações de variáveis** que, **quando atuam juntas**, **levam a um determinado resultado ou comportamento de negócio.** Em vez de observar cada variável isoladamente, a cenarização busca **compreender** como **diferentes fatores interagem de maneira sistêmica para gerar cenários específicos.**

Essa abordagem é especialmente útil para:

- **Explorar padrões complexos em dados;**
- **Entender caminhos alternativos que levam ao mesmo desfecho;**
- **Auxiliar na tomada de decisão baseada em múltiplas condições simultâneas;**
- **Antecipar cenários favoráveis ou críticos em ambientes de incerteza.**

Ela permite **visualizar não apenas o que está acontecendo,** mas **por que está acontecendo**, **revelando combinações de variáveis** que seriam **difíceis de detectar por métodos tradicionais.**

![Exemplo de Cenarização](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/Cenarizacao_Exemplo.png)

### 🧭 Conclusão da Unidade 2

A Unidade 2 mostra como **transformar dados em vantagem competitiva**: **não basta armazenar dados**, é preciso **cultura**, **métodos** e **execução** para **extrair valor**. **Tecnologia é ferramenta**; a diferença vem de processos, pessoas e governança.

🔹 Cultura Data-Driven

- **Decidir com evidências**, não intuição.
- Requisitos: **dados confiáveis**, **governança**, **acesso democratizado** e **maturidade analítica**.
- Resultado: **decisões mais rápidas**, menos vieses e **melhor antecipação de problemas**.

🔹 Data Discovery

- **Democratiza a exploração de dados** com **interfaces visuais e self-service.**
- Empodera áreas de negócio, **reduz gargalos de TI** e **acelera insights** acionáveis.

🔹 Análise Descritiva

- Responde **“o que aconteceu”**.
- Ferramentas: **distribuição de frequência, séries temporais, taxonomia de variáveis (nominais, ordinais, discretas, contínuas).**
- Objetivo: **organizar**, **detectar anomalias** e **preparar base** para **análises avançadas**.

🔹 Análise Preditiva

- Responde **“o que provavelmente vai acontecer”.**
- Baseada em **modelos estatísticos** e de **machine learning (regressões, árvores, ensembles, redes neurais).**
- Requisitos: **features bem construídas**, **validação robusta** e **monitoramento** (drift).

🔹 Aprendizado de Máquina (Machine Learning)

- Conjunto de técnicas que permite aos **sistemas aprender padrões** a **partir de dados e generalizar para novos casos.**
- Exemplos: **classificação** (churn, fraude), **regressão** (previsão de demanda), **clustering** (segmentação).

Importante: selecionar algoritmo adequado, evitar overfitting, validar com cross-validation e cuidar de vieses nos dados.

🔹 Cenarização

- Técnica para **identificar combinações de variáveis** que geram **cenários específicos**.
- Útil para **explorar caminhos múltiplos** que levam ao mesmo desfecho (ex.: causas de churn).
- **Complementa predição** ao mostrar contextos e condições — **essencial para planejar intervenções direcionadas.**

🔹 Análise Prescritiva

- Responde **“o que fazer” com base nas previsões.**
- **Traduz modelos e cenários em recomendações operacionais e estratégicas.**
- Exige **integração** entre **análise**, **negócio** e **execução**.

> Para **extrair valor real** dos dados é preciso cultura **Data-Driven + Data Discovery + Análise Descritiva (base) + Análise Preditiva e Machine Learning (prever) + Cenarização (entender contextos) + Análise Prescritiva (agir)**. Só quando esses elementos trabalham juntos os dados passam a guiar **decisões eficazes e gerar vantagem competitiva.**

## UNIDADE 03

Essa **unidade é prática**, onde **analisaremos bases de dados** usando **Power BI** e o **Tableau**.

### Tableau
#### Utilização do Tableau
Tableau Public: https://www.tableau.com/pt-br/products/public/download
  - É grátis de utilizar e pode ser executado online também.
Tableau Acadêmico: https://www.tableau.com/pt-br/academic/students
  - Utilizar de preferência email da instituição matriculada.
Tableau Online: https://online.tableau.com/

#### Exemplo do Tableau
![Tableau do Tableau](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/Tableau_Exemplo.png)

#### Utilização do Tableau
##### Fazendo Joins (União, Interceção e etc)
![Joins entre tabelas](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/Tableau_Joins.png)

##### Nomeclatura das Colunas
O **nome das colunas é muito importante**, pois a **ferramente** já consegue **inferir um tipo** dependendo do nome, exemplo:
**Nome da Coluna é "Cidade" o tipo é "cidade".**

##### Abas do Tableau 
![Abas do Tableau](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/01%20-%20Data%20Discovery%20e%20Analytics/images/Tableau_Abas.png)

1) Fonte de Dados: Aba principal onde carregamos conexões e fontes de dados.
2) Primeiro Icone: Criar novas análises de dados com gráficos
3) Segundo Icone: Criar dashboards (paineis)
4) Terceiro Icone: Criar histórias (slides)