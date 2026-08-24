# 05 - Preparação e Integração de Dados

## SUMÁRIO

- [UNIDADE 01](#unidade-01)
    - [TEMAS ABORDADOS](#temas-abordados)
    - [Dados, informação, conhecimento e inteligência](#dados-informação-conhecimento-e-inteligência)
    - [Business Intelligence - BI](#business-intelligence---bi)
    - [Self Service BI - SSBI](#self-service-bi---ssbi)
    - [Governança de dados](#governança-de-dados---gd)
    - [Implementação](#implementação)
        - [Requisitos e realidade](#requisitos-e-realidade)
        - [Arquitetura](#arquitetura)
- [UNIDADE 02](#unidade-02)
    - [TEMAS ABORDADOS](#temas-abordados-1)
    - [Implementação do sistema - ETL](#implementação-do-sistema---etl)
        - [Extract](#e---extract)
        - [Transform](#t---transform)
        - [Load](#l---load)
        - [Ferramentas ETL](#ferramentas-etl)
    - [Estruturas de dados](#estruturas-de-dados)
- [UNIDADE 03](#unidade-03)
    - [TEMAS ABORDADOS](#temas-abordados-2)
    - [Projeto ETL com múltiplas fontes](#projeto-etl-com-múltiplas-fontes)
- [UNIDADE 04](#unidade-04)
    - [TEMAS ABORDADOS](#temas-abordados-3)
    - [Estudo de caso: vendas por região](#estudo-de-caso-vendas-por-região)
    - [Testes e operação](#testes-e-operação)

## UNIDADE 01

### TEMAS ABORDADOS

- Dados, Informação e Inteligência
- Business Intelligence
- Self Service BI (SSBI)
- Governança de dados
- Identificação de requisitos
- Definição da arquitetura do processo de coleta de dados.

### DADOS, INFORMAÇÃO, CONHECIMENTO E INTELIGÊNCIA

- Os *dados* são registros brutos, ainda sem contexto ou análise.
    - Ex: 500 mil. 500 mil o que?
- A *informação* surge quando os dados são organizados e recebem contexto.
    - Ex: Esse mês Minas Gerais faturou 500 mil reais.
- O *conhecimento* é o entendimento de padrões e relações a partir das informações.
    - Ex: Padrão da empresa é ganhar em média 1 milhão por mês.
- A *inteligência* é a capacidade de usar o conhecimento para tomar decisões e se adaptar a novas situações.
    - Ex: Já queimamos uma vez a mão com fogo, então nunca mais iremos tocar no fogo.

Esse fluxo mostra por que a preparação é importante: um dado isolado não ajuda muito. Quando ele é padronizado, relacionado a outros dados e analisado, pode apoiar uma decisão de negócio.

![fluxo do dado até o conhecimento](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/05%20-%20Preparação%20e%20Integração%20de%20Dados/images/fluxoDadoAteConhecimento.png)

![fluxo do dado até a informação](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/05%20-%20Preparação%20e%20Integração%20de%20Dados/images/fluxoDadoAteInformacao.png)

### BUSINESS INTELLIGENCE - BI

- *Business Intelligence (BI)* reúne processos, ferramentas e práticas para transformar dados em informações úteis para a tomada de decisão.

Um ambiente de BI normalmente recebe dados de sistemas operacionais, arquivos e fontes externas. Depois da preparação, esses dados podem ser apresentados em relatórios, indicadores e painéis. O BI não substitui a decisão humana: ele oferece uma visão mais confiável para que a decisão seja tomada.

> Os dados são coletados (extraídos), transformados e carregados em estruturas informacionais, oferecendo assim, desempenho e facilidade ao manipular os dados.

### SELF SERVICE BI - SSBI

- O *Self-Service BI* permite que profissionais de negócio consultem dados e criem relatórios com mais autonomia, contando com o suporte e as regras definidas pela TI.

Essa autonomia reduz a dependência de solicitações simples ao time técnico. Porém, ela precisa de limites: as fontes devem ser confiáveis, os indicadores devem ter definições conhecidas e o acesso deve respeitar as permissões de cada usuário. Sem esses cuidados, duas pessoas podem criar relatórios diferentes para responder à mesma pergunta.

> Antigamente um profissional específico tinha que gerar os blocos de análise, e hoje em dia o usuário final consegue acessar os dados e gerar relatórios muito mais facilmente. 

### GOVERNANÇA DE DADOS - G.D.

- *Governança de dados* é o conjunto de regras, papéis e processos usados para garantir que os dados sejam confiáveis, seguros, acessíveis e usados de forma adequada.

Na prática, a governança responde a perguntas como: quem é responsável por este dado? De onde ele veio? Quem pode acessá-lo? Como sua qualidade será verificada? Ela não é apenas uma tarefa técnica; envolve as áreas de negócio, TI e os responsáveis pelos dados.

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

O catálogo e a linhagem são especialmente importantes. O catálogo descreve os dados disponíveis, enquanto a linhagem mostra sua origem e as transformações pelas quais passaram. Assim, fica mais fácil investigar erros e confiar nos resultados.

### IMPLEMENTAÇÃO

*Ciclo* de Vida de *ETL*, segundo *Kimball*:

![The planning and design thread](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/05%20-%20Preparação%20e%20Integração%20de%20Dados/images/planningAndDesignThread.png)

#### REQUISITOS E REALIDADE

- **Requisitos do negócio:**
    - Envolvem entrevistas e reuniões.
    - Ocorre a identificação das fontes de dados.
    - Acontecem descobertas significativas que afetarão as necessidades do negócio.

- **Perfil de dados:**
    - Uma análise sistemática da qualidade dos dados nas fontes determina o esforço de construção de um produto.
    - Uma fonte de dados muito limpa exige o mínimo de intervenção humana antes de carregar no seu destino.

- **Segurança dos dados:**
    - Deve-se ter acesso a leitura as fontes de origem.
    - A gestão de segurança final deverá ser tratada na governança de dados da empresa, envolvendo profissionais de T.I.

Antes de construir o processo, é importante registrar o objetivo, as fontes, a frequência da carga, o responsável e o resultado esperado. Esse pequeno levantamento evita criar um pipeline tecnicamente correto, mas que não responde à necessidade do negócio.

#### ARQUITETURA

A escolha da arquitetura é uma decisão fundamental.

- PASSOS:
    - Definição/compra de uma ferramenta.
    - Definição do local (path) onde estão os dados.
    - Dependência de tarefas vertical X horizontal.
    - Agendamento (Scheduler) das tarefas.
    - Tratamento de exceções.
    - Recuperação e reinício.
    - Segurança do ambiente (rotinas de backup).

Uma arquitetura simples pode começar com uma fonte, uma área de preparação e um destino para análise. Conforme o volume e a quantidade de fontes aumentam, podem ser adicionados agendamento, monitoramento, armazenamento intermediário e ferramentas de controle de qualidade.

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

*ETL* significa **Extract, Transform, Load**: extrair, transformar e carregar. É um fluxo que leva dados de uma ou mais fontes até um local preparado para consulta e análise.

O processo pode ser representado assim:

```text
Fontes de dados -> Extração -> Transformação -> Validação -> Carga -> Relatórios
```

Exemplo de ETL: Projeto de Web Scrapping que coleta os dados, normaliza e salva no banco.

#### E - EXTRACT

- A primeira parte do processo ETL é coletar os dados das fontes de origem.
- Na maioria dos projetos existem fontes heterogêneas de dados.
- Fontes comuns são bancos de dados, arquivos CSV, planilhas, páginas web, APIs, XML e JSON.

Na extração, procure preservar os dados originais e registrar quando a coleta aconteceu. Manter uma cópia bruta ajuda a refazer o processo caso uma transformação tenha sido aplicada de maneira incorreta.

> Uma vez que seu sistema ETL é iniciado logo se percebe a necessidade de integração de fontes diferentes é um grande desafio.

#### T - Transform

[Fluxo do ETL](//Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/05%20-%20Preparação%20e%20Integração%20de%20Dados/images/fluxoETL.png)

- **Definindo dados com qualidade:**
    - Correto.
    - Sem ambiguidade.
    - Consistente.
    - Completo.
- **Analisando dados com anomalias:**
    - São dados que não se encaixam no contexto do restante dos dados armazenados.
    - Podem causar retrabalho, exigindo a correção e a execução novamente do processo ETL.
    - Existem técnicas de detecção para verificar esses dados com anomalias. Olham o histórico e fazem análises com amostras.

A transformação consiste em aplicar regras sobre os dados extraídos. Alguns exemplos são:

- Padronizar datas, textos, moedas e unidades de medida;
- Corrigir ou sinalizar valores ausentes e inválidos;
- Remover duplicidades;
- Relacionar tabelas por uma chave comum;
- Criar colunas calculadas e indicadores.

Essas regras devem ser baseadas nos requisitos do negócio e documentadas. Uma transformação não deve alterar o significado do dado apenas para facilitar a análise.

#### L - Load

Carga é o envio dos dados transformados para o destino, como um Data Warehouse, banco de dados ou repositório de uma ferramenta de BI. Antes de concluir, é importante verificar se a quantidade e os valores carregados estão de acordo com o esperado.

**Carga incremental x carga completa:** na carga incremental, somente os registros novos ou alterados são enviados. Na carga completa, todo o conjunto é carregado novamente. A incremental costuma ser mais rápida, mas exige uma forma confiável de identificar alterações, como uma data de atualização ou um identificador de mudança.

- **Batch:** processa dados em lotes, em horários definidos. É comum em arquivos e bancos relacionais, mas pode ter maior latência.
- **Near real-time:** processa pequenas alterações com pouco atraso. Soluções como CDC (*Change Data Capture*) identificam mudanças na fonte.
- **Real-time:** processa os dados quase no momento em que são gerados. Tem baixa latência, mas exige uma arquitetura mais preparada para esse fluxo.

Visão Data Warehouse:

> Fase de ETL desde a extração do dado até sua carga em um modelo dimensional consome, pelo menos, 70% do tempo, esforço e despesa da maioria dos projetos de Data Warehouse. (Kimball)

- Um Data Warehouse é um repositório que integra dados de fontes operacionais, organiza esses dados para análise e apoia consultas, relatórios e decisões de negócio.

Visão Self Service BI - SSBI:

- Os dados podem ser armazenados nos repositórios internos das ferramentas SSBI, que costumam oferecer compressão e índices otimizados para consultas.

![Visões ETL](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/05%20-%20Preparação%20e%20Integração%20de%20Dados/images/visoesETL.png)

#### Ferramentas ETL

- Power BI (Microsoft)
- Tableau
- Qlik
- ThoughtSpot

### ESTRUTURAS DE DADOS

- **Estruturados:** seguem um esquema definido de linhas e colunas, como uma tabela de banco relacional.
- **Semiestruturados:** possuem alguma organização, mas permitem variação de campos, como XML e JSON.
- **Não estruturados:** não seguem um formato tabular fixo, como textos, vídeos, imagens e áudios.

Um mesmo projeto pode combinar os três tipos. Por exemplo, uma empresa pode juntar vendas estruturadas, dados de uma API em JSON e comentários escritos pelos clientes.

![Diferença entre estruturas de dados](/Inteligência%20Artificial%20e%20Aprendizado%20de%20Máquina/05%20-%20Preparação%20e%20Integração%20de%20Dados/images/diffEstruturasDados.png)

## UNIDADE 03

### TEMAS ABORDADOS

- Projeto ETL com carga acessando Múltiplas fontes de dados
    - Entendimento do cenário
    - Criação do conceito único de cliente
    - Criação do conceito único de pedidos
    - Agendamento de carga – Usando Gateway
    - Publicação do dados

> Obs: Módulo foi totalmente prático, sobre criação de um projeto ETL com power BI.

### PROJETO ETL COM MÚLTIPLAS FONTES

O objetivo do projeto é combinar fontes diferentes em uma visão única. Para isso, é necessário definir uma chave ou regra que identifique o mesmo cliente e o mesmo pedido em todas as fontes.

Um fluxo possível é:

1. Entender o cenário e o resultado esperado;
2. Mapear as fontes e seus campos;
3. Padronizar nomes, tipos e valores;
4. Criar o conceito único de cliente e de pedido;
5. Validar os totais antes e depois da transformação;
6. Agendar e publicar a carga no Power BI.

O conceito único evita que o mesmo cliente seja contado duas vezes por possuir nomes ou cadastros diferentes nas fontes.

## UNIDADE 04

### TEMAS ABORDADOS

- Estudo de Caso: Carga Vendas por Região ( projeto baseado em uma realidade)
    - Projeto ETL com carga acessando Múltiplas fontes de dados
        - Entendimento do cenário
        - Criação do conceito único de cliente
        - Criação do conceito único de pedidos
        - Criando gráfico Tableau Desktop
- Implementação: Projetos ETL
    - Testes e Operação

> Obs: Módulo foi totalmente prático, sobre criação de um projeto ETL com Tableau. Dando Overview nas ferramentas do Tableau (Como Tableau Prep.).

### ESTUDO DE CASO: VENDAS POR REGIÃO

Neste estudo de caso, as fontes de vendas são integradas para responder perguntas como: qual região vende mais? Quais clientes e pedidos pertencem a cada região? O trabalho envolve entender o cenário, criar os conceitos únicos de cliente e pedido e construir um gráfico no Tableau Desktop.

O Tableau Prep pode ser usado para visualizar as etapas de preparação, combinar fontes, corrigir campos e enviar o resultado ao ambiente de análise. O gráfico deve apresentar uma comparação clara, com título, unidade de medida e filtros coerentes com a pergunta.

### IMPLEMENTAÇÃO
#### TESTES E OPERAÇÃO

Antes de publicar o processo, é necessário verificar se ele produz dados corretos e se pode ser executado de forma repetível.

**Passos principais:**

- Executar testes unitários nas transformações;
- Conferir totais, quantidades de registros e valores importantes;
- Criar um ambiente de produção estável com apoio da equipe de TI;
- Programar os agendamentos das cargas incrementais;
- Monitorar o ambiente por um período determinado;
- Documentar os procedimentos de recuperação de falhas.

Os testes unitários verificam pequenas partes do processo, como uma regra de conversão ou uma função de limpeza. Já os testes de integração verificam se as fontes, transformações e destino funcionam juntos. Os dois tipos ajudam a encontrar problemas antes que eles cheguem aos relatórios.

- Para fazer a migração/publicação para a produção tão simples quanto possível, crie documentos de apoio à produção. Nem sempre quem criou o processo será responsável por sua manutenção. Alguns documentos importantes são:
    - Relatório final com todos os artefatos produzidos durante o desenvolvimento;
    - Documento com os detalhes dos agendamentos das cargas;
    - Dicionário com os campos, regras e responsáveis;
    - Procedimento para identificar e corrigir uma falha.

O monitoramento deve observar pelo menos o horário da última execução, o tempo de processamento, a quantidade de registros e as falhas ocorridas. Uma carga pode terminar sem erro técnico e ainda assim entregar dados incompletos; por isso, também são necessárias verificações de qualidade.

- A missão da equipe de ETL, no nível mais alto, é construir os bastidores de uma solução de analytics:
    - Fornecer dados de forma mais eficaz para o negócio.
    - Agregar valor dos dados nos passos de limpeza e transformação.
    - Proteger e documentar o fluxo dos dados.

- Para que a missão ocorra, são necessárias 4 fases:
    1. *Extração* de dados das fontes originais.
    2. Garantir a qualidade e *limpeza* de dados.
    3. *Transformar* os dados para atender aos requisitos de negócio, mantendo coerência com as fontes originais.
    4. *Carregar* os dados no repositório da ferramenta, proporcionando consultas, relatórios e painéis.

- Responsabilidades da equipe de ETL:
    - Definir escopo do processo ETL.
    - Analisar performance do sistema de origem.
    - Definir uma estratégia de qualidade dos dados.
    - Documentar as regras de negócio.
    - Desenvolver os códigos físicos dos processos de carga.
    - Criar e executar testes de carga.
    - Acompanhar processos quando migrados para produção.
    - Realizar manutenção dos processos de carga.