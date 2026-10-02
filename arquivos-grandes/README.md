# Arquivos acadêmicos grandes

Esta pasta preserva, em formato compactado ou dividido, materiais que ultrapassam o limite de 100 MB por arquivo comum do GitHub.

Para reconstruir os cinco arquivos nos caminhos originais, execute na raiz do repositório:

```bash
python3 scripts/restaurar_arquivos_grandes.py
```

O processo é incremental: arquivos já íntegros são ignorados. Cada resultado é validado por SHA-256 antes de ser aceito. As duas cópias do CSV e as duas cópias do notebook têm conteúdo idêntico, por isso apenas um exemplar compactado de cada conteúdo é versionado.

## Conteúdo armazenado

- `modelos-estatisticos/covid_doencas_preexistentes.csv.gz`: base de doenças preexistentes usada em Modelos Estatísticos;
- `modelos-estatisticos/regressao-binaria-python.ipynb.gz`: notebook de regressão binária;
- `visao-computacional/yolov4-dataset_car_chair_book.zip.part-*`: três partes ordenadas do conjunto de dados YOLOv4.

Os arquivos reconstruídos são ignorados pelo Git para evitar que uma execução do restaurador volte a ultrapassar o limite do GitHub.
