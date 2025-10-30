# 01 - Data Discovery e Analytics

## Sumário
- ![Unidade 01](#unidade-01)
  - ![Dados para Negócios](#dados-para-negócios)
  - ![O que são KPIs?](#o-que-são-kpis)

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