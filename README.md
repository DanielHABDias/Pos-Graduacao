# Pós-Graduação

Repositório pessoal de estudos de Daniel Henrique Alves Bicalho Dias, desenvolvedor de sistemas, criado para aprofundamento em Dados e Inteligência Artificial.

## Cursos

- [Inteligência Artificial e Aprendizado de Máquina](Intelig%C3%AAncia%20Artificial%20e%20Aprendizado%20de%20M%C3%A1quina/README.md)

## Ferramenta de coleta

O [CanvasCrawler](CanvasCrawler/README.md) faz parte deste mesmo repositório. Ele usa a API do Canvas da PUC Minas para listar formações e disciplinas, organizar materiais e, quando permitido pelo provedor, produzir transcrições de vídeos sem manter os arquivos de mídia.

Para abrir o menu:

```bash
cd CanvasCrawler
./canvas.sh
```

O token permanece apenas no arquivo local `CanvasCrawler/.env`, que não é versionado.

## Arquivos grandes

Alguns conjuntos de dados e notebooks ultrapassam o limite de 100 MB por arquivo comum do GitHub. O conteúdo completo está compactado ou dividido em [`arquivos-grandes/`](arquivos-grandes/README.md). Depois de clonar o repositório, execute `python3 scripts/restaurar_arquivos_grandes.py` para reconstruir e validar os cinco arquivos nos caminhos originais.

## Organização

O conteúdo está estruturado por disciplina e unidade. Cada nível possui um índice em Markdown, com acesso às páginas das aulas, documentos, apresentações, notebooks, códigos, bases de dados e imagens. Anotações pessoais anteriores foram preservadas e aparecem separadas dos materiais importados do ambiente acadêmico.

## Objetivo

Concentrar materiais e resumos em uma base pesquisável, versionável e adequada para revisão, experimentação prática e estudo assistido por IA.
