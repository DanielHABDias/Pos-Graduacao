# 06 - UNIDADE 4 - DATAOPS E MLOPS NA PRÁTICA - PARTE II

[← Voltar à disciplina](../README.md)

## Resumo da unidade

A unidade empacota e expõe modelos com Docker e APIs, depois mede o comportamento sob carga. Implantar inclui definir contrato de entrada, tratamento de erro e observabilidade.

### Exemplo

Uma API de previsão deve validar tipos e limites, devolver erro compreensível para entradas inválidas e registrar latência sem armazenar dados sensíveis.

## Conteúdo da unidade

- [Unidade 4 - Orientações de Estudo](paginas/01%20-%20Unidade%204%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md) — Bem-vindo a segunda parte prática da disciplina, onde mergulharemos ainda mais fundo nas estratégias e ferramentas essenciais para garantir o sucesso na implantação e operação de modelos de Machine Learning em ambientes reais. No nosso trajeto, exploraremos uma série de tópicos cruciais que permitem a entrega confiável e eficiente de modelos, desde sua criação até sua manutenção contínua. Uma das pedras angulares…
- [Unidade 4 - 1. Deploy de modelos - Docker](paginas/02%20-%20Unidade%204%20-%201.%20Deploy%20de%20modelos%20-%20Docker.md) — Containers são unidades isoladas de software que empacotam todas as dependências e bibliotecas necessárias para executar um aplicativo. Eles fornecem uma maneira consistente e portátil de implantar aplicativos em diferentes ambientes. Os containers permitem isolamento de aplicativos, portabilidade, eficiência de recursos, escalabilidade e facilidade de implantação.
- [Unidade 4 - 2. Deploy de modelos - APIs](paginas/03%20-%20Unidade%204%20-%202.%20Deploy%20de%20modelos%20-%20APIs.md) — Uma API ( Application Programming Interface ) é um conjunto de regras e protocolos que define como diferentes softwares podem interagir entre si. Ela fornece uma interface padronizada para acessar recursos e funcionalidades de um software, permitindo que outros aplicativos possam se integrar e interagir com ele de forma programática. As APIs são amplamente utilizadas na indústria de software para permitir a…
- [Unidade 4 - 3. Teste de carga](paginas/04%20-%20Unidade%204%20-%203.%20Teste%20de%20carga.md) — Os testes de carga (ou load tests , em inglês) em modelos de ML referem-se à avaliação do desempenho e capacidade de um modelo em lidar com grandes volumes de dados ou requisições simultâneas. Em vez de avaliar a precisão ou acurácia do modelo, os testes de carga visam entender como o modelo se comporta sob carga intensa. Aqui estão alguns aspectos importantes sobre testes de carga em modelos de machine learning :
- [Unidade 4 - 4. Introdução às práticas da unidade](paginas/05%20-%20Unidade%204%20-%204.%20Introdu%C3%A7%C3%A3o%20%C3%A0s%20pr%C3%A1ticas%20da%20unidade.md) — Nesta seção você será convidado a fazer uma sequência de atividades práticas para aprofundar nos conhecimentos da disciplina. As práticas estão relacionadas aos conceitos de deploy de modelos e criação de APIs com FastAPI.
- [Unidade 4 - 4.1. Prática - Criação de uma API](paginas/06%20-%20Unidade%204%20-%204.1.%20Pr%C3%A1tica%20-%20Cria%C3%A7%C3%A3o%20de%20uma%20API.md) — Nesta prática será apresentada uma forma de criar uma API com FastAPI. Assista a seguir o vídeo explicando como criar a aplicação:
- [Unidade 4 - 4.2. Prática - Customização da API](paginas/07%20-%20Unidade%204%20-%204.2.%20Pr%C3%A1tica%20-%20Customiza%C3%A7%C3%A3o%20da%20API.md) — Nesta prática será apresentado como customizar a API anterior. Assista a seguir o vídeo explicando como customizar a aplicação:
- [Unidade 4 - 4.3. Prática - Criação da API do modelo](paginas/08%20-%20Unidade%204%20-%204.3.%20Pr%C3%A1tica%20-%20Cria%C3%A7%C3%A3o%20da%20API%20do%20modelo.md) — Nesta prática será apresentada uma forma de criar uma API com FastAPI para o modelo. Assista a seguir o vídeo explicando como criar a aplicação:
- [Unidade 4 - 4.4. Prática - Uso do Docker](paginas/09%20-%20Unidade%204%20-%204.4.%20Pr%C3%A1tica%20-%20Uso%20do%20Docker.md) — Nesta prática será apresentado o Docker e como executá-lo localmente. Assista a seguir o vídeo sobre o uso do Docker:
- [Unidade 4 - 4.5. Prática - Deploy do Modelo - Parte 1](paginas/10%20-%20Unidade%204%20-%204.5.%20Pr%C3%A1tica%20-%20Deploy%20do%20Modelo%20-%20Parte%201.md) — Nesta prática será apresentada a primeira parte do deploy do nosso modelo treinado no Azure:
- [Unidade 4 - 4.6. Prática - Deploy do Modelo - Parte 2](paginas/11%20-%20Unidade%204%20-%204.6.%20Pr%C3%A1tica%20-%20Deploy%20do%20Modelo%20-%20Parte%202.md) — Nesta prática será apresentada a segunda parte do deploy do nosso modelo treinado no Azure:
- [Unidade 4 - 4.7. Prática - Teste de Carga](paginas/12%20-%20Unidade%204%20-%204.7.%20Pr%C3%A1tica%20-%20Teste%20de%20Carga.md) — Nesta prática será apresentada uma forma de realiar um teste de carga por meio do framework Locust:
- [Unidade 4 - 4.8. Prática - DataOps](paginas/13%20-%20Unidade%204%20-%204.8.%20Pr%C3%A1tica%20-%20DataOps.md) — Nesta prática será apresentada uma forma de trabalhar com uma operacionalização de dados por meio do framework evidently. Serão aplicados testes estatísticos para validar a existência ou não de diferença significativa dos dados utilizados para treinar o modelo. Use o arquivo datops\ datadrift.ipynb
- [Unidade 4 - 4.9. Prática - AutoML](paginas/14%20-%20Unidade%204%20-%204.9.%20Pr%C3%A1tica%20-%20AutoML.md) — Nesta prática será apresentada uma forma de usar o AutoML com AutoKeras para buscar uma melhor arquitetura para nosso modelo. Utilize o arquivo AutoML\ com\ AutoKeras.ipynb:
- [Unidade 4 - Material Complementar](paginas/15%20-%20Unidade%204%20-%20Material%20Complementar.md) — Em um mundo cada vez mais orientado pela eficiência e escalabilidade, a combinação de containers Docker e a agilidade proporcionada pelo FastAPI representa um marco significativo para o desenvolvimento e implantação de aplicações. Os containers oferecem um ambiente encapsulado e portátil, permitindo que as aplicações sejam executadas consistentemente em diferentes ambientes. Isso proporciona uma flexibilidade…
- [Unidade 4 - Desafio e Resolução](paginas/20%20-%20Unidade%204%20-%20Desafio%20e%20Resolu%C3%A7%C3%A3o.md) — Crie um teste de elasticidade de exemplo para uma aplicação que posteriormente se tornaria uma API para predição. Um teste de elasticidade no contexto do Locust envolve simular um aumento ou diminuição dinâmica da carga para avaliar como o sistema responde a mudanças na demanda. Para isso, você pode usar estratégias de escalabilidade automática ou ajustar manualmente o número de usuários virtuais durante a execução…

## Materiais

### PDFs (2)

- [Introdução ao Docker.pdf](documentos/Introdu%C3%A7%C3%A3o%20ao%20Docker.pdf) (20 páginas)
- [Testes e APIs.pdf](documentos/Testes%20e%20APIs.pdf) (22 páginas)

### Notebooks (2)

- [AutoML_com_AutoKeras.ipynb](documentos/AutoML_com_AutoKeras.ipynb)
- [dataops_datadrift.ipynb](documentos/dataops_datadrift.ipynb)

### Páginas e textos (16)

- [01 - Unidade 4 - Orientações de Estudo.md](paginas/01%20-%20Unidade%204%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md)
- [02 - Unidade 4 - 1. Deploy de modelos - Docker.md](paginas/02%20-%20Unidade%204%20-%201.%20Deploy%20de%20modelos%20-%20Docker.md)
- [03 - Unidade 4 - 2. Deploy de modelos - APIs.md](paginas/03%20-%20Unidade%204%20-%202.%20Deploy%20de%20modelos%20-%20APIs.md)
- [04 - Unidade 4 - 3. Teste de carga.md](paginas/04%20-%20Unidade%204%20-%203.%20Teste%20de%20carga.md)
- [05 - Unidade 4 - 4. Introdução às práticas da unidade.md](paginas/05%20-%20Unidade%204%20-%204.%20Introdu%C3%A7%C3%A3o%20%C3%A0s%20pr%C3%A1ticas%20da%20unidade.md)
- [06 - Unidade 4 - 4.1. Prática - Criação de uma API.md](paginas/06%20-%20Unidade%204%20-%204.1.%20Pr%C3%A1tica%20-%20Cria%C3%A7%C3%A3o%20de%20uma%20API.md)
- [07 - Unidade 4 - 4.2. Prática - Customização da API.md](paginas/07%20-%20Unidade%204%20-%204.2.%20Pr%C3%A1tica%20-%20Customiza%C3%A7%C3%A3o%20da%20API.md)
- [08 - Unidade 4 - 4.3. Prática - Criação da API do modelo.md](paginas/08%20-%20Unidade%204%20-%204.3.%20Pr%C3%A1tica%20-%20Cria%C3%A7%C3%A3o%20da%20API%20do%20modelo.md)
- [09 - Unidade 4 - 4.4. Prática - Uso do Docker.md](paginas/09%20-%20Unidade%204%20-%204.4.%20Pr%C3%A1tica%20-%20Uso%20do%20Docker.md)
- [10 - Unidade 4 - 4.5. Prática - Deploy do Modelo - Parte 1.md](paginas/10%20-%20Unidade%204%20-%204.5.%20Pr%C3%A1tica%20-%20Deploy%20do%20Modelo%20-%20Parte%201.md)
- [11 - Unidade 4 - 4.6. Prática - Deploy do Modelo - Parte 2.md](paginas/11%20-%20Unidade%204%20-%204.6.%20Pr%C3%A1tica%20-%20Deploy%20do%20Modelo%20-%20Parte%202.md)
- [12 - Unidade 4 - 4.7. Prática - Teste de Carga.md](paginas/12%20-%20Unidade%204%20-%204.7.%20Pr%C3%A1tica%20-%20Teste%20de%20Carga.md)
- [13 - Unidade 4 - 4.8. Prática - DataOps.md](paginas/13%20-%20Unidade%204%20-%204.8.%20Pr%C3%A1tica%20-%20DataOps.md)
- [14 - Unidade 4 - 4.9. Prática - AutoML.md](paginas/14%20-%20Unidade%204%20-%204.9.%20Pr%C3%A1tica%20-%20AutoML.md)
- [15 - Unidade 4 - Material Complementar.md](paginas/15%20-%20Unidade%204%20-%20Material%20Complementar.md)
- [20 - Unidade 4 - Desafio e Resolução.md](paginas/20%20-%20Unidade%204%20-%20Desafio%20e%20Resolu%C3%A7%C3%A3o.md)

### Imagens (16)

- [banner-pos-2023.jpg](images/banner-pos-2023.jpg)
- [icone-bussola-1.png](images/icone-bussola-1.png)
- [icone-coruja-1.png](images/icone-coruja-1.png)
- [icone-lampada-1.png](images/icone-lampada-1.png)
- [image-1409c751-3b01-4a31-8b4c-a964f29ec6b6.png](images/image-1409c751-3b01-4a31-8b4c-a964f29ec6b6.png)
- [image-20a71b19-3019-406d-908a-fa2a9ff44b5c.png](images/image-20a71b19-3019-406d-908a-fa2a9ff44b5c.png)
- [image-266157d9-6929-428d-9689-2c2338a031a7.png](images/image-266157d9-6929-428d-9689-2c2338a031a7.png)
- [image-3cdc58e2-a510-4c51-b2e4-d8bfa7b4cdab.png](images/image-3cdc58e2-a510-4c51-b2e4-d8bfa7b4cdab.png)
- [image-458c8a31-8c0d-41b0-93e1-3807c573636e.png](images/image-458c8a31-8c0d-41b0-93e1-3807c573636e.png)
- [image-99f72e56-069f-4629-baed-0b8442a54d72.png](images/image-99f72e56-069f-4629-baed-0b8442a54d72.png)
- [image-c21f6567-f741-4a24-b803-34788dbf3698.png](images/image-c21f6567-f741-4a24-b803-34788dbf3698.png)
- [image-dcc4ad38-6184-4204-b4ab-5ab35fe7c1d3.png](images/image-dcc4ad38-6184-4204-b4ab-5ab35fe7c1d3.png)
- [image-dea9f491-311a-4c09-b7c6-fbb1a46b18fb.png](images/image-dea9f491-311a-4c09-b7c6-fbb1a46b18fb.png)
- [image-eba5f97a-6d1e-49b8-aec6-8232dacf9560.png](images/image-eba5f97a-6d1e-49b8-aec6-8232dacf9560.png)
- [image-f8a4d9ad-89b3-4fce-b384-4c4adf95d287.png](images/image-f8a4d9ad-89b3-4fce-b384-4c4adf95d287.png)
- [material-b-1.png](images/material-b-1.png)

### HTML original (16)

- [01 - Unidade 4 - Orientações de Estudo.html](html/01%20-%20Unidade%204%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.html)
- [02 - Unidade 4 - 1. Deploy de modelos - Docker.html](html/02%20-%20Unidade%204%20-%201.%20Deploy%20de%20modelos%20-%20Docker.html)
- [03 - Unidade 4 - 2. Deploy de modelos - APIs.html](html/03%20-%20Unidade%204%20-%202.%20Deploy%20de%20modelos%20-%20APIs.html)
- [04 - Unidade 4 - 3. Teste de carga.html](html/04%20-%20Unidade%204%20-%203.%20Teste%20de%20carga.html)
- [05 - Unidade 4 - 4. Introdução às práticas da unidade.html](html/05%20-%20Unidade%204%20-%204.%20Introdu%C3%A7%C3%A3o%20%C3%A0s%20pr%C3%A1ticas%20da%20unidade.html)
- [06 - Unidade 4 - 4.1. Prática - Criação de uma API.html](html/06%20-%20Unidade%204%20-%204.1.%20Pr%C3%A1tica%20-%20Cria%C3%A7%C3%A3o%20de%20uma%20API.html)
- [07 - Unidade 4 - 4.2. Prática - Customização da API.html](html/07%20-%20Unidade%204%20-%204.2.%20Pr%C3%A1tica%20-%20Customiza%C3%A7%C3%A3o%20da%20API.html)
- [08 - Unidade 4 - 4.3. Prática - Criação da API do modelo.html](html/08%20-%20Unidade%204%20-%204.3.%20Pr%C3%A1tica%20-%20Cria%C3%A7%C3%A3o%20da%20API%20do%20modelo.html)
- [09 - Unidade 4 - 4.4. Prática - Uso do Docker.html](html/09%20-%20Unidade%204%20-%204.4.%20Pr%C3%A1tica%20-%20Uso%20do%20Docker.html)
- [10 - Unidade 4 - 4.5. Prática - Deploy do Modelo - Parte 1.html](html/10%20-%20Unidade%204%20-%204.5.%20Pr%C3%A1tica%20-%20Deploy%20do%20Modelo%20-%20Parte%201.html)
- [11 - Unidade 4 - 4.6. Prática - Deploy do Modelo - Parte 2.html](html/11%20-%20Unidade%204%20-%204.6.%20Pr%C3%A1tica%20-%20Deploy%20do%20Modelo%20-%20Parte%202.html)
- [12 - Unidade 4 - 4.7. Prática - Teste de Carga.html](html/12%20-%20Unidade%204%20-%204.7.%20Pr%C3%A1tica%20-%20Teste%20de%20Carga.html)
- [13 - Unidade 4 - 4.8. Prática - DataOps.html](html/13%20-%20Unidade%204%20-%204.8.%20Pr%C3%A1tica%20-%20DataOps.html)
- [14 - Unidade 4 - 4.9. Prática - AutoML.html](html/14%20-%20Unidade%204%20-%204.9.%20Pr%C3%A1tica%20-%20AutoML.html)
- [15 - Unidade 4 - Material Complementar.html](html/15%20-%20Unidade%204%20-%20Material%20Complementar.html)
- [20 - Unidade 4 - Desafio e Resolução.html](html/20%20-%20Unidade%204%20-%20Desafio%20e%20Resolu%C3%A7%C3%A3o.html)

## Roteiro de estudo

1. Leia as páginas na ordem apresentada pelo módulo.
2. Consulte os PDFs e apresentações enquanto registra definições, hipóteses e exemplos.
3. Execute notebooks e códigos, verificando entradas, saídas e limitações.
4. Ao final, responda:

   - Como você explicaria **Unidade 4 - Orientações de Estudo** sem consultar o material?
   - Como você explicaria **Unidade 4 - 1. Deploy de modelos - Docker** sem consultar o material?
   - Como você explicaria **Unidade 4 - 2. Deploy de modelos - APIs** sem consultar o material?
   - Como você explicaria **Unidade 4 - 3. Teste de carga** sem consultar o material?
   - Como você explicaria **Unidade 4 - 4. Introdução às práticas da unidade** sem consultar o material?
