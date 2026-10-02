# 05 - UNIDADE 4 - APLICAÇÕES COM REDES NEURAIS CONVOLUCIONAIS

[← Voltar à disciplina](../README.md)

## Resumo da unidade

A unidade usa transferência de aprendizado, ajuste fino e detectores de objetos. Detecção acrescenta localização à classificação e exige anotações consistentes.

### Exemplo

Comece congelando a rede pré-treinada e treinando a nova cabeça. Depois descongele poucas camadas com taxa menor e compare em validação.

## Conteúdo da unidade

- [Unidade 4 - Orientações de Estudo](paginas/01%20-%20Unidade%204%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md) — Muitas aplicações podem ser desenvolvidas utilizando as redes neurais para problemas de visão computacional. A classificação de imagens é uma das principais aplicações que será abordada nesta unidade. Ademais, aplicações de grande relevância para a área de visão computacional é a detecção de objetos em imagens. As redes neurais tornaram viáveis estas e outras aplicações, no entanto, muitos detalhes devem ser…
- [Unidade 4 - 1. Introdução a Transfer Learning](paginas/02%20-%20Unidade%204%20-%201.%20Introdu%C3%A7%C3%A3o%20a%20Transfer%20Learning.md)
- [Unidade 4 - 2. Redes pré-treinadas para extração de features de imagens](paginas/03%20-%20Unidade%204%20-%202.%20Redes%20pr%C3%A9-treinadas%20para%20extra%C3%A7%C3%A3o%20de%20features%20de%20imagens.md)
- [Unidade 4 - 3. Prática - Treinando um modelo a partir de uma rede pré-treinada e Fine-tuning](paginas/04%20-%20Unidade%204%20-%203.%20Pr%C3%A1tica%20-%20Treinando%20um%20modelo%20a%20partir%20de%20uma%20rede%20pr%C3%A9-treinada%20e%20Fine-tuning.md)
- [Unidade 4 - 4. Introdução a Detecção de Objetos](paginas/05%20-%20Unidade%204%20-%204.%20Introdu%C3%A7%C3%A3o%20a%20Detec%C3%A7%C3%A3o%20de%20Objetos.md)
- [Unidade 4 - 5. Anotação de Imagens](paginas/06%20-%20Unidade%204%20-%205.%20Anota%C3%A7%C3%A3o%20de%20Imagens.md)
- [Unidade 4 - 6. Métodos de Detecção de Objetos (R-CNNs, SSD e YOLO)](paginas/07%20-%20Unidade%204%20-%206.%20M%C3%A9todos%20de%20Detec%C3%A7%C3%A3o%20de%20Objetos%20%28R-CNNs%2C%20SSD%20e%20YOLO%29.md)
- [Unidade 4 - 7. Enunciado do Projeto - Detecção de Objetos](paginas/09%20-%20Unidade%204%20-%207.%20Enunciado%20do%20Projeto%20-%20Detec%C3%A7%C3%A3o%20de%20Objetos.md)
- [Unidade 4 - 8. Preparando o dataset](paginas/10%20-%20Unidade%204%20-%208.%20Preparando%20o%20dataset.md)
- [Unidade 4 - 9. Preparando o ambiente com Darknet](paginas/11%20-%20Unidade%204%20-%209.%20Preparando%20o%20ambiente%20com%20Darknet.md)
- [Unidade 4 - 10. Prática - (Detecção de Objetos) Criando o modelo](paginas/12%20-%20Unidade%204%20-%2010.%20Pr%C3%A1tica%20-%20%28Detec%C3%A7%C3%A3o%20de%20Objetos%29%20Criando%20o%20modelo.md)
- [Unidade 4 - 11. Prática - (Detecção de Objetos) Realizando inferência](paginas/13%20-%20Unidade%204%20-%2011.%20Pr%C3%A1tica%20-%20%28Detec%C3%A7%C3%A3o%20de%20Objetos%29%20Realizando%20infer%C3%AAncia.md)
- [Unidade 4 - 12. Considerações Finais](paginas/14%20-%20Unidade%204%20-%2012.%20Considera%C3%A7%C3%B5es%20Finais.md)
- [Unidade 4 - Material Complementar](paginas/15%20-%20Unidade%204%20-%20Material%20Complementar.md) — unidade04\ keras\ pre\ trained\ convnet.ipynb unidade04\ split\ train\ and\ test\ dataset\ yolov4.ipynb unidade04\ YOLOv4\ Training\ Tutorial\ Custom.ipynb Unidade 4 - yolov4-dataset\ car\ chair\ book.zip Projeto Final - CNN para Detecção de Objetos - Virtual

## Materiais

### PDFs (1)

- [4_01_Object Detection.pdf](documentos/4_01_Object%20Detection.pdf) (41 páginas)

### Notebooks (5)

- [unidade04_export_datasets_fiftyone.ipynb](documentos/unidade04_export_datasets_fiftyone.ipynb)
- [unidade04_keras_extract_features.ipynb](documentos/unidade04_keras_extract_features.ipynb)
- [unidade04_keras_pre_trained_convnet.ipynb](documentos/unidade04_keras_pre_trained_convnet.ipynb)
- [unidade04_split_train_and_test_dataset_yolov4.ipynb](documentos/unidade04_split_train_and_test_dataset_yolov4.ipynb)
- [unidade04_YOLOv4_Training_Tutorial_Custom.ipynb](documentos/unidade04_YOLOv4_Training_Tutorial_Custom.ipynb)

### Dados e artefatos (3)

- [obj.data](documentos/obj.data)
- [obj.names](documentos/obj.names)
- [yolov4-dataset_car_chair_book.zip](documentos/yolov4-dataset_car_chair_book.zip)

### Páginas e textos (14)

- [01 - Unidade 4 - Orientações de Estudo.md](paginas/01%20-%20Unidade%204%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.md)
- [02 - Unidade 4 - 1. Introdução a Transfer Learning.md](paginas/02%20-%20Unidade%204%20-%201.%20Introdu%C3%A7%C3%A3o%20a%20Transfer%20Learning.md)
- [03 - Unidade 4 - 2. Redes pré-treinadas para extração de features de imagens.md](paginas/03%20-%20Unidade%204%20-%202.%20Redes%20pr%C3%A9-treinadas%20para%20extra%C3%A7%C3%A3o%20de%20features%20de%20imagens.md)
- [04 - Unidade 4 - 3. Prática - Treinando um modelo a partir de uma rede pré-treinada e Fine-tuning.md](paginas/04%20-%20Unidade%204%20-%203.%20Pr%C3%A1tica%20-%20Treinando%20um%20modelo%20a%20partir%20de%20uma%20rede%20pr%C3%A9-treinada%20e%20Fine-tuning.md)
- [05 - Unidade 4 - 4. Introdução a Detecção de Objetos.md](paginas/05%20-%20Unidade%204%20-%204.%20Introdu%C3%A7%C3%A3o%20a%20Detec%C3%A7%C3%A3o%20de%20Objetos.md)
- [06 - Unidade 4 - 5. Anotação de Imagens.md](paginas/06%20-%20Unidade%204%20-%205.%20Anota%C3%A7%C3%A3o%20de%20Imagens.md)
- [07 - Unidade 4 - 6. Métodos de Detecção de Objetos (R-CNNs, SSD e YOLO).md](paginas/07%20-%20Unidade%204%20-%206.%20M%C3%A9todos%20de%20Detec%C3%A7%C3%A3o%20de%20Objetos%20%28R-CNNs%2C%20SSD%20e%20YOLO%29.md)
- [09 - Unidade 4 - 7. Enunciado do Projeto - Detecção de Objetos.md](paginas/09%20-%20Unidade%204%20-%207.%20Enunciado%20do%20Projeto%20-%20Detec%C3%A7%C3%A3o%20de%20Objetos.md)
- [10 - Unidade 4 - 8. Preparando o dataset.md](paginas/10%20-%20Unidade%204%20-%208.%20Preparando%20o%20dataset.md)
- [11 - Unidade 4 - 9. Preparando o ambiente com Darknet.md](paginas/11%20-%20Unidade%204%20-%209.%20Preparando%20o%20ambiente%20com%20Darknet.md)
- [12 - Unidade 4 - 10. Prática - (Detecção de Objetos) Criando o modelo.md](paginas/12%20-%20Unidade%204%20-%2010.%20Pr%C3%A1tica%20-%20%28Detec%C3%A7%C3%A3o%20de%20Objetos%29%20Criando%20o%20modelo.md)
- [13 - Unidade 4 - 11. Prática - (Detecção de Objetos) Realizando inferência.md](paginas/13%20-%20Unidade%204%20-%2011.%20Pr%C3%A1tica%20-%20%28Detec%C3%A7%C3%A3o%20de%20Objetos%29%20Realizando%20infer%C3%AAncia.md)
- [14 - Unidade 4 - 12. Considerações Finais.md](paginas/14%20-%20Unidade%204%20-%2012.%20Considera%C3%A7%C3%B5es%20Finais.md)
- [15 - Unidade 4 - Material Complementar.md](paginas/15%20-%20Unidade%204%20-%20Material%20Complementar.md)

### Imagens (5)

- [banner-pos-2022.jpg](images/banner-pos-2022.jpg)
- [icone-bussola.png](images/icone-bussola.png)
- [icone-coruja.png](images/icone-coruja.png)
- [Leitura.png](images/Leitura.png)
- [material-b.png](images/material-b.png)

### HTML original (14)

- [01 - Unidade 4 - Orientações de Estudo.html](html/01%20-%20Unidade%204%20-%20Orienta%C3%A7%C3%B5es%20de%20Estudo.html)
- [02 - Unidade 4 - 1. Introdução a Transfer Learning.html](html/02%20-%20Unidade%204%20-%201.%20Introdu%C3%A7%C3%A3o%20a%20Transfer%20Learning.html)
- [03 - Unidade 4 - 2. Redes pré-treinadas para extração de features de imagens.html](html/03%20-%20Unidade%204%20-%202.%20Redes%20pr%C3%A9-treinadas%20para%20extra%C3%A7%C3%A3o%20de%20features%20de%20imagens.html)
- [04 - Unidade 4 - 3. Prática - Treinando um modelo a partir de uma rede pré-treinada e Fine-tuning.html](html/04%20-%20Unidade%204%20-%203.%20Pr%C3%A1tica%20-%20Treinando%20um%20modelo%20a%20partir%20de%20uma%20rede%20pr%C3%A9-treinada%20e%20Fine-tuning.html)
- [05 - Unidade 4 - 4. Introdução a Detecção de Objetos.html](html/05%20-%20Unidade%204%20-%204.%20Introdu%C3%A7%C3%A3o%20a%20Detec%C3%A7%C3%A3o%20de%20Objetos.html)
- [06 - Unidade 4 - 5. Anotação de Imagens.html](html/06%20-%20Unidade%204%20-%205.%20Anota%C3%A7%C3%A3o%20de%20Imagens.html)
- [07 - Unidade 4 - 6. Métodos de Detecção de Objetos (R-CNNs, SSD e YOLO).html](html/07%20-%20Unidade%204%20-%206.%20M%C3%A9todos%20de%20Detec%C3%A7%C3%A3o%20de%20Objetos%20%28R-CNNs%2C%20SSD%20e%20YOLO%29.html)
- [09 - Unidade 4 - 7. Enunciado do Projeto - Detecção de Objetos.html](html/09%20-%20Unidade%204%20-%207.%20Enunciado%20do%20Projeto%20-%20Detec%C3%A7%C3%A3o%20de%20Objetos.html)
- [10 - Unidade 4 - 8. Preparando o dataset.html](html/10%20-%20Unidade%204%20-%208.%20Preparando%20o%20dataset.html)
- [11 - Unidade 4 - 9. Preparando o ambiente com Darknet.html](html/11%20-%20Unidade%204%20-%209.%20Preparando%20o%20ambiente%20com%20Darknet.html)
- [12 - Unidade 4 - 10. Prática - (Detecção de Objetos) Criando o modelo.html](html/12%20-%20Unidade%204%20-%2010.%20Pr%C3%A1tica%20-%20%28Detec%C3%A7%C3%A3o%20de%20Objetos%29%20Criando%20o%20modelo.html)
- [13 - Unidade 4 - 11. Prática - (Detecção de Objetos) Realizando inferência.html](html/13%20-%20Unidade%204%20-%2011.%20Pr%C3%A1tica%20-%20%28Detec%C3%A7%C3%A3o%20de%20Objetos%29%20Realizando%20infer%C3%AAncia.html)
- [14 - Unidade 4 - 12. Considerações Finais.html](html/14%20-%20Unidade%204%20-%2012.%20Considera%C3%A7%C3%B5es%20Finais.html)
- [15 - Unidade 4 - Material Complementar.html](html/15%20-%20Unidade%204%20-%20Material%20Complementar.html)

### Outros materiais (1)

- [Projeto Final - CNN para Detecção de Objetos - Virtual.txt](documentos/Projeto%20Final%20-%20CNN%20para%20Detec%C3%A7%C3%A3o%20de%20Objetos%20-%20Virtual.txt)

## Roteiro de estudo

1. Leia as páginas na ordem apresentada pelo módulo.
2. Consulte os PDFs e apresentações enquanto registra definições, hipóteses e exemplos.
3. Execute notebooks e códigos, verificando entradas, saídas e limitações.
4. Ao final, responda:

   - Como você explicaria **Unidade 4 - Orientações de Estudo** sem consultar o material?
   - Como você explicaria **Unidade 4 - 1. Introdução a Transfer Learning** sem consultar o material?
   - Como você explicaria **Unidade 4 - 2. Redes pré-treinadas para extração de features de imagens** sem consultar o material?
   - Como você explicaria **Unidade 4 - 3. Prática - Treinando um modelo a partir de uma rede pré-treinada e Fine-tuning** sem consultar o material?
   - Como você explicaria **Unidade 4 - 4. Introdução a Detecção de Objetos** sem consultar o material?
