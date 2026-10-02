# 03 - UNIDADE 2 - INTRODUÇÃO AOS SISTEMAS DE RECOMENDAÇÃO E ABORDAGEM BASEADA EM CONTEÚDO

[← Voltar à disciplina](../README.md)

## Resumo da unidade

A unidade apresenta recomendação baseada em conteúdo e similaridade. Itens e perfis precisam compartilhar uma representação, e a avaliação deve evitar usar interações futuras no treino.

### Exemplo

Um perfil pode ser a média ponderada dos vetores dos filmes curtidos. O sistema recomenda itens próximos que o usuário ainda não consumiu.

## Fórmulas essenciais

### Similaridade do cosseno

$$
\cos(\mathbf{i},\mathbf{u})=\frac{\mathbf{i}\cdot\mathbf{u}}{\lVert\mathbf{i}\rVert\lVert\mathbf{u}\rVert}
$$

Compara o vetor de um item com o perfil do usuário.


## Conteúdo da unidade

- [Unidade 2 - Orientações de Estudo](paginas/01%20-%20Unidade%202%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md) — INTRODUÇÃO AOS SISTEMAS DE RECOMENDAÇÃO E ABORDAGEM BASEADA EM CONTEÚDO Olá! Seja bem-vindo e bem-vinda à segunda etapa de estudos da nossa disciplina. Na Unidade 2: Introdução aos Sistemas de Recomendação e Abordagem Baseada em Conteúdo , serão apresentados os fundamentos teóricos e as aplicações práticas dos sistemas que personalizam a experiência do usuário. Em um cenário de abundância de dados, entender como…
- [Unidade 2 - 1. Fundamentos de Sistemas de Recomendação: Conceitos e Abordagens](paginas/02%20-%20Unidade%202%20-%201.%20Fundamentos%20de%20Sistemas%20de%20Recomenda%C3%A7%C3%A3o_%20Conceitos%20e%20Abordagens.md) — Nesta aula, vamos abordar os seguintes tópicos: - Introdução aos sistemas de recomendação; - Técnicas de recomendação pelo nível de personalização; - Abordagens de sistemas de recomendação; - Recomendação não personalizada. - Identificar o conceito de sistemas de recomendação; - Reconhecer as diferenças entre recomendações não personalizadas e recomendações personalizadas; - Compreender os requisitos fundamentais e…
- [Unidade 2 - 2. Técnicas de Recuperação de Informação e Similaridade](paginas/03%20-%20Unidade%202%20-%202.%20T%C3%A9cnicas%20de%20Recupera%C3%A7%C3%A3o%20de%20Informa%C3%A7%C3%A3o%20e%20Similaridade.md) — Nesta aula, vamos abordar os seguintes tópicos: - Recuperação de informação; - Modelo vetorial e cálculo de similaridade. - Compreender os conceitos fundamentais de Recuperação de Informação (RI); - Compreender os métodos de cálculo de similaridade, com foco na Similaridade de Cosseno; - Reconhecer a aplicação prática do modelo vetorial, distinguindo os desafios de implementação técnica entre a teoria e o…
- [Unidade 2 - 3. Abordagem Baseada em Conteúdo: Representação de Itens e Perfil do Usuário](paginas/04%20-%20Unidade%202%20-%203.%20Abordagem%20Baseada%20em%20Conte%C3%BAdo_%20Representa%C3%A7%C3%A3o%20de%20Itens%20e%20Perfil%20do%20Usu%C3%A1rio.md) — Nesta aula, vamos abordar os seguintes tópicos: - Recomendação baseada em conteúdo; - Recomendação baseada em conteúdo personalizada e perfil do usuário. - Compreender a lógica da filtragem baseada em conteúdo; - Identificar métodos de representação de itens, reconhecendo a importância do uso de metadados, tags e descritores textuais; - Compreender o processo de construção do perfil do usuário; - Diferenciar…
- [Unidade 2 - Material Complementar](paginas/05%20-%20Unidade%202%20-%20Material%20Complementar.md) — Técnicas de recomendação pelo nível de personalização.pptx Recomendação não personalizada - Prática.pptx Prática U2-T1-V4.2-Recomendação não personalizada.ipynb Modelo vetorial e similaridade - Prática.pptx Prática U2-T2-V2.2-Modelo vetorial e similaridade.ipynb Recomendação baseada em conteúdo - Prática.pptx Prática U2-T3-V1.2-Recomendação baseada em conteúdo.ipynb

## Materiais

### Apresentações (12)

- [Abordagens sistemas de recomendação.pptx](documentos/Abordagens%20sistemas%20de%20recomenda%C3%A7%C3%A3o.pptx)
- [Introdução aos sistemas de recomendação.pptx](documentos/Introdu%C3%A7%C3%A3o%20aos%20sistemas%20de%20recomenda%C3%A7%C3%A3o.pptx)
- [Modelo vetorial e similaridade - Prática.pptx](documentos/Modelo%20vetorial%20e%20similaridade%20-%20Pr%C3%A1tica.pptx)
- [Modelo vetorial e similaridade.pptx](documentos/Modelo%20vetorial%20e%20similaridade.pptx)
- [Recomendação baseada em conteúdo - Prática.pptx](documentos/Recomenda%C3%A7%C3%A3o%20baseada%20em%20conte%C3%BAdo%20-%20Pr%C3%A1tica.pptx)
- [Recomendação baseada em conteúdo personalizada - Prática.pptx](documentos/Recomenda%C3%A7%C3%A3o%20baseada%20em%20conte%C3%BAdo%20personalizada%20-%20Pr%C3%A1tica.pptx)
- [Recomendação baseada em conteúdo personalizada.pptx](documentos/Recomenda%C3%A7%C3%A3o%20baseada%20em%20conte%C3%BAdo%20personalizada.pptx)
- [Recomendação baseada em conteúdo.pptx](documentos/Recomenda%C3%A7%C3%A3o%20baseada%20em%20conte%C3%BAdo.pptx)
- [Recomendação não personalizada - Prática.pptx](documentos/Recomenda%C3%A7%C3%A3o%20n%C3%A3o%20personalizada%20-%20Pr%C3%A1tica.pptx)
- [Recomendação não personalizada.pptx](documentos/Recomenda%C3%A7%C3%A3o%20n%C3%A3o%20personalizada.pptx)
- [Recuperação de informação.pptx](documentos/Recupera%C3%A7%C3%A3o%20de%20informa%C3%A7%C3%A3o.pptx)
- [Técnicas de recomendação pelo nível de personalização.pptx](documentos/T%C3%A9cnicas%20de%20recomenda%C3%A7%C3%A3o%20pelo%20n%C3%ADvel%20de%20personaliza%C3%A7%C3%A3o.pptx)

### Notebooks (4)

- [Prática U2-T1-V4.2-Recomendação não personalizada.ipynb](documentos/Pr%C3%A1tica%20U2-T1-V4.2-Recomenda%C3%A7%C3%A3o%20n%C3%A3o%20personalizada.ipynb)
- [Prática U2-T2-V2.2-Modelo vetorial e similaridade.ipynb](documentos/Pr%C3%A1tica%20U2-T2-V2.2-Modelo%20vetorial%20e%20similaridade.ipynb)
- [Prática U2-T3-V1.2-Recomendação baseada em conteúdo.ipynb](documentos/Pr%C3%A1tica%20U2-T3-V1.2-Recomenda%C3%A7%C3%A3o%20baseada%20em%20conte%C3%BAdo.ipynb)
- [Prática U2-T3-V2.2-Recomendação baseada em conteúdo personalizada.ipynb](documentos/Pr%C3%A1tica%20U2-T3-V2.2-Recomenda%C3%A7%C3%A3o%20baseada%20em%20conte%C3%BAdo%20personalizada.ipynb)

### Páginas e textos (5)

- [01 - Unidade 2 - Orientações de Estudo.md](paginas/01%20-%20Unidade%202%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md)
- [02 - Unidade 2 - 1. Fundamentos de Sistemas de Recomendação_ Conceitos e Abordagens.md](paginas/02%20-%20Unidade%202%20-%201.%20Fundamentos%20de%20Sistemas%20de%20Recomenda%C3%A7%C3%A3o_%20Conceitos%20e%20Abordagens.md)
- [03 - Unidade 2 - 2. Técnicas de Recuperação de Informação e Similaridade.md](paginas/03%20-%20Unidade%202%20-%202.%20T%C3%A9cnicas%20de%20Recupera%C3%A7%C3%A3o%20de%20Informa%C3%A7%C3%A3o%20e%20Similaridade.md)
- [04 - Unidade 2 - 3. Abordagem Baseada em Conteúdo_ Representação de Itens e Perfil do Usuário.md](paginas/04%20-%20Unidade%202%20-%203.%20Abordagem%20Baseada%20em%20Conte%C3%BAdo_%20Representa%C3%A7%C3%A3o%20de%20Itens%20e%20Perfil%20do%20Usu%C3%A1rio.md)
- [05 - Unidade 2 - Material Complementar.md](paginas/05%20-%20Unidade%202%20-%20Material%20Complementar.md)

### Imagens (6)

- [banner-pos-2022-1.jpg](images/banner-pos-2022-1.jpg)
- [banner-pos-2022.jpg](images/banner-pos-2022.jpg)
- [icone-bussola.png](images/icone-bussola.png)
- [Leitura (2).png](images/Leitura%20%282%29.png)
- [material-b.png](images/material-b.png)
- [Play (1).png](images/Play%20%281%29.png)

### HTML original (5)

- [01 - Unidade 2 - Orientações de Estudo.html](html/01%20-%20Unidade%202%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.html)
- [02 - Unidade 2 - 1. Fundamentos de Sistemas de Recomendação_ Conceitos e Abordagens.html](html/02%20-%20Unidade%202%20-%201.%20Fundamentos%20de%20Sistemas%20de%20Recomenda%C3%A7%C3%A3o_%20Conceitos%20e%20Abordagens.html)
- [03 - Unidade 2 - 2. Técnicas de Recuperação de Informação e Similaridade.html](html/03%20-%20Unidade%202%20-%202.%20T%C3%A9cnicas%20de%20Recupera%C3%A7%C3%A3o%20de%20Informa%C3%A7%C3%A3o%20e%20Similaridade.html)
- [04 - Unidade 2 - 3. Abordagem Baseada em Conteúdo_ Representação de Itens e Perfil do Usuário.html](html/04%20-%20Unidade%202%20-%203.%20Abordagem%20Baseada%20em%20Conte%C3%BAdo_%20Representa%C3%A7%C3%A3o%20de%20Itens%20e%20Perfil%20do%20Usu%C3%A1rio.html)
- [05 - Unidade 2 - Material Complementar.html](html/05%20-%20Unidade%202%20-%20Material%20Complementar.html)

## Roteiro de estudo

1. Leia as páginas na ordem apresentada pelo módulo.
2. Consulte os PDFs e apresentações enquanto registra definições, hipóteses e exemplos.
3. Execute notebooks e códigos, verificando entradas, saídas e limitações.
4. Ao final, responda:

   - Como você explicaria **Unidade 2 - Orientações de Estudo** sem consultar o material?
   - Como você explicaria **Unidade 2 - 1. Fundamentos de Sistemas de Recomendação: Conceitos e Abordagens** sem consultar o material?
   - Como você explicaria **Unidade 2 - 2. Técnicas de Recuperação de Informação e Similaridade** sem consultar o material?
   - Como você explicaria **Unidade 2 - 3. Abordagem Baseada em Conteúdo: Representação de Itens e Perfil do Usuário** sem consultar o material?
   - Como você explicaria **Unidade 2 - Material Complementar** sem consultar o material?
