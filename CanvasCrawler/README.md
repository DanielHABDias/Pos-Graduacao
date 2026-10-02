# CanvasCrawler

> Este projeto faz parte do repositório de estudos `Pos-Graduacao`. Execute os comandos a partir desta pasta para que o `.env`, o ambiente virtual e o acervo local permaneçam isolados da documentação versionada.

Coletor API-first para organizar localmente o material didático dos cursos da PUC Minas hospedados no Canvas LMS.

O projeto acessará o Canvas com as credenciais do próprio aluno, identificará os cursos e seus módulos, baixará o conteúdo permitido e montará um acervo de estudo autocontido. Cada pasta de curso deverá poder ser movida posteriormente para o repositório `Pos-Graduacao` sem depender do código do crawler e sem perder imagens, documentos, HTMLs, transcrições ou informações de origem.

> Status: crawler documental funcional. É possível coletar uma disciplina ou todas as disciplinas
> de uma formação escolhida, incluindo páginas, HTML, documentos, imagens e mídias acessíveis.

## Objetivos

O CanvasCrawler será responsável por:

- autenticar na API do Canvas da PUC Minas;
- listar os cursos em que o usuário está matriculado;
- reproduzir localmente a ordem de cursos, módulos e itens;
- preservar o HTML original das páginas para permitir reprocessamento futuro;
- gerar uma versão Markdown legível de cada página;
- baixar PDFs, planilhas, apresentações, imagens e outros anexos permitidos;
- localizar mídias incorporadas nas páginas;
- baixar vídeos quando o Canvas ou o provedor permitir;
- produzir transcrições pesquisáveis, preferencialmente com timestamps;
- atribuir nomes claros e estáveis aos arquivos;
- corrigir os links do Markdown para que apontem para os arquivos locais;
- manter um manifesto de sincronização para evitar downloads duplicados;
- oferecer, em uma operação separada, a conclusão manual de itens elegíveis;
- ignorar provas, questionários e atividades avaliativas.

O objetivo final não é manter uma cópia visual do site. É produzir uma base documental organizada para leitura, pesquisa, resumo e estudo assistido por IA.

## Limites do projeto

O crawler não deverá:

- responder, iniciar, enviar ou concluir provas e atividades;
- tentar descobrir respostas de questionários;
- enviar arquivos ou alterar conteúdo dos cursos;
- contornar DRM, paywall, bloqueios de sessão ou permissões do provedor;
- coletar cursos ou materiais aos quais o usuário não tenha acesso normal;
- publicar tokens, cookies ou dados pessoais;
- marcar provas, atividades ou itens sem a opção manual de conclusão;
- usar automação de navegador como estratégia principal.

Playwright ou outro navegador automatizado somente deverá ser considerado para um caso isolado que não possua API, e apenas depois de documentada a limitação. A implementação principal será baseada na API REST oficial do Canvas.

## Fonte de dados

- Canvas da PUC Minas: <https://pucminas.instructure.com/>
- Base da API: `https://pucminas.instructure.com/api/v1`
- Cursos do usuário: `GET /api/v1/courses`

O endpoint completo de cursos que estava anotado no arquivo inicial será montado pelo cliente HTTP, com paginação e parâmetros próprios. Isso evita manter URLs extensas duplicadas no código.

## Estrutura do repositório

A estrutura atual separa configuração, acesso ao Canvas, modelos de domínio e interface de
linha de comando. Novos módulos serão adicionados somente quando as respectivas funções forem
implementadas:

```text
CanvasCrawler/
├── README.md
├── .env
├── .env.example
├── formations.toml
├── pyproject.toml
├── canvas.sh
├── canvas_crawler/
│   ├── __init__.py
│   ├── __main__.py
│   ├── catalog.py
│   ├── cli.py
│   ├── config.py
│   ├── completion.py
│   ├── crawler.py
│   ├── exceptions.py
│   ├── media.py
│   ├── storage.py
│   ├── transcription.py
│   ├── canvas/
│   │   ├── __init__.py
│   │   └── client.py
│   └── models/
│       ├── __init__.py
│       ├── course.py
│       ├── content.py
│       ├── module.py
│       └── program.py
├── tests/
│   ├── test_catalog.py
│   ├── test_client.py
│   ├── test_config.py
│   ├── test_completion.py
│   ├── test_crawler.py
│   └── test_media.py
└── acervo/                       # criada automaticamente pelo crawler
```

`CanvasClient` concentra autenticação, tratamento de erros e paginação. `Settings` valida o
ambiente sem expor o token, e `CourseCatalog` aplica as regras de `formations.toml`. Essa divisão
evita duplicar regras HTTP nas próximas funcionalidades sem introduzir camadas sem função real.

### Formação, disciplina, módulo e item

O Canvas chama cada disciplina individual de `course`, mas neste projeto usamos uma linguagem
mais próxima da organização acadêmica:

```text
Formação (ADS ou IA)
└── Disciplina (um course da API do Canvas)
    └── Módulo
        └── Item (página, arquivo, link, atividade etc.)
```

A API não informa a formação real do aluno em disciplinas compartilhadas. Por isso
`formations.toml` associa as disciplinas às duas formações conhecidas. Novas formações podem ser
adicionadas nesse arquivo sem mudar o código. Cursos globais ou não reconhecidos ficam fora do
menu principal até receberem uma regra explícita. Regras por ID de conta têm prioridade sobre
regras amplas de período, o que permite acrescentar futuramente outra graduação sem misturá-la
com ADS.

## Estrutura do acervo

O formato precisa conciliar dois objetivos:

1. preservar a estrutura original do Canvas por curso e por módulo;
2. permitir mover a pasta de um curso diretamente para `Pos-Graduacao`.

Estrutura proposta:

```text
acervo/
└── Nome da Formação/
    └── Nome da Disciplina/
        ├── README.md
        ├── .canvas/
        │   └── manifest.json
        ├── 01 - Nome do Módulo/
        │   ├── README.md
        │   ├── paginas/
        │   │   ├── 01 - Introducao.md
        │   │   └── 02 - Conceitos fundamentais.md
        │   ├── html/
        │   │   ├── 01 - Introducao.html
        │   │   └── 02 - Conceitos fundamentais.html
        │   ├── documentos/
        │   │   ├── Unidade_01_Introducao.pdf
        │   │   └── Base_Vendas.xlsx
        │   ├── images/
        │   │   ├── Arquitetura_Data_Warehouse.png
        │   │   └── Fluxo_Processamento_Dados.png
        │   └── transcricoes/
        │       ├── Apresentacao da disciplina.md
        │       └── Apresentacao da disciplina.json
        └── 02 - Outro Módulo/
            └── ...
```

### Pasta do curso

A pasta do curso é a unidade portátil. Ela deve conter tudo que for necessário para abrir os documentos e navegar pelos links localmente. Depois da revisão, ela poderá ser movida integralmente para dentro da formação correspondente no projeto `Pos-Graduacao`.

O `README.md` do curso será inicialmente um índice gerado a partir do Canvas. Depois poderá ser ampliado com resumos, explicações e material de estudo, seguindo o padrão já usado no outro repositório.

### Pasta do módulo

Cada módulo manterá sua posição original. A numeração no início do nome evita que a ordem das aulas dependa da ordenação alfabética.

O `README.md` do módulo funcionará como sumário dos itens coletados, indicando:

- título e tipo do item;
- link para a versão Markdown;
- anexos associados;
- transcrição de vídeo, quando existir;
- URL original no Canvas;
- data da coleta;
- avisos sobre conteúdo indisponível.

### HTML e Markdown

Para cada página do Canvas serão preservadas duas representações:

- `html/`: conteúdo original retornado pela API, útil para auditoria e reprocessamento;
- `paginas/`: conteúdo convertido para Markdown e pronto para estudo.

O Markdown deverá usar caminhos relativos. Assim, mover a pasta inteira do curso não quebrará imagens nem documentos.

### Documentos

Arquivos como PDF, DOCX, PPTX, XLSX, CSV e notebooks serão preservados em seu formato original. O crawler não deverá alterar o conteúdo desses arquivos.

Se um mesmo arquivo aparecer em mais de uma página do módulo, o manifesto deverá impedir downloads duplicados. As páginas poderão apontar para uma única cópia local.

### Imagens e nomes semânticos

As imagens ficarão em `images/`, como no projeto `Pos-Graduacao`, mas o nome será normalizado para ser legível e estável.

Ordem de preferência para determinar o nome:

1. nome original significativo do arquivo;
2. texto alternativo (`alt`) da imagem;
3. legenda ou título próximo no HTML;
4. título da página mais uma sequência;
5. ID do arquivo no Canvas como último recurso.

Exemplos:

```text
BI_Arquitetura.png
Data_Discovery_Fluxo_Self_Service.png
Regressao_Linear_Formula_01.png
Introducao_Imagem_03_canvas_918273.png
```

O nome exibido ao usuário pode preservar acentos, mas o componente de armazenamento deverá remover caracteres inválidos, impedir colisões e limitar o tamanho do caminho. O ID do Canvas será acrescentado somente quando necessário para diferenciar arquivos.

### Vídeos e transcrições

Quando o download for permitido, o vídeo será gravado somente em `acervo/.tmp/`, transcrito e
apagado em um bloco `finally`, inclusive quando houver falha durante o processamento. O acervo
preservará apenas `transcricao.md` e `transcricao.json`; arquivos de vídeo nunca farão parte da
estrutura portátil.

Embeds do Canvas Studio são abertos por uma URL LTI temporária gerada oficialmente pelo Canvas;
o bearer token do Canvas não é enviado ao domínio do Studio. O crawler usa uma legenda quando o
proprietário permite seu download ou baixa temporariamente a mídia quando o download está
habilitado. Respostas `403`, mídias protegidas e provedores externos sem API autorizada ficam no
manifesto como `media-pending`, em vez de serem contornados.

Uma nova execução é incremental: documentos e imagens existentes não ganham uma segunda cópia,
páginas idênticas não são regravadas e transcrições que já possuam os arquivos Markdown e JSON
são puladas. Embeds pendentes são tentados novamente, permitindo preencher o que faltar quando a
permissão ou o provedor mudar.

A transcrição terá:

- um arquivo `transcricao.md` legível;
- um arquivo `transcricao.json` com segmentos e timestamps;
- identificação do idioma e do modelo utilizado;
- título do item de origem;
- probabilidade do idioma detectado no arquivo JSON.

Formato esperado:

```markdown
# Apresentação da disciplina

- Curso: Nome do curso
- Módulo: Apresentação
- Origem: Canvas
- Duração: 00:18:42

## Transcrição

**[00:00:00] Professor:** Bem-vindos à disciplina...

**[00:00:17] Professor:** Nesta primeira unidade...
```

Vídeos hospedados em ferramentas externas podem exigir uma integração específica. O crawler deverá registrar claramente os casos não suportados, sem tentar contornar as regras do provedor.

## Tipos de item do Canvas

Tratamento inicial planejado:

| Tipo | Comportamento |
| --- | --- |
| `Page` | Salvar HTML, converter para Markdown e baixar recursos incorporados |
| `File` | Baixar o arquivo original |
| `ExternalUrl` | Registrar URL e coletar somente quando houver permissão e suporte explícito |
| `ExternalTool` | Identificar o provedor; coletar somente por API ou download autorizado |
| `SubHeader` | Preservar como seção no sumário |
| `Assignment` | Ignorar |
| `Quiz` | Ignorar |
| `Discussion` | Ignorar por padrão |

Mesmo quando uma atividade contiver um arquivo, ela continuará excluída até existir uma regra explícita e segura que diferencie material de apoio de conteúdo avaliativo.

## Manifestação e sincronização incremental

Cada curso possuirá `.canvas/manifest.json`. Esse arquivo deverá guardar, por item:

- ID do curso;
- ID e posição do módulo;
- ID, posição e tipo do item;
- título original;
- URL original;
- data de criação e atualização informada pelo Canvas;
- caminho local de cada artefato;
- tamanho e hash SHA-256 dos arquivos;
- status da coleta e da transcrição;
- requisito de conclusão do item;
- mensagens de erro da última tentativa.

Com isso, as sincronizações seguintes poderão:

- pular arquivos inalterados;
- baixar novamente arquivos modificados;
- detectar mudanças de nome ou posição;
- retomar downloads incompletos;
- refazer somente transcrições ausentes;
- apresentar um relatório antes de qualquer alteração de progresso no Canvas.

Arquivos locais editados pelo estudante não deverão ser sobrescritos silenciosamente. Quando houver conflito, a nova versão deverá ser salva separadamente ou o item deverá ser sinalizado para revisão.

## Baixar uma disciplina ou uma formação

O comando `./canvas.sh baixar` abre um submenu persistente. Nele é possível escolher uma única
disciplina, escolher uma formação e baixar todas as disciplinas dela, ou voltar ao menu principal.

Não existe operação para baixar todas as formações juntas. O modo em lote exige selecionar a
formação e digitar `BAIXAR FORMAÇÃO`. Suas disciplinas são processadas uma por vez. Uma falha
total ou parcial é mostrada no relatório e não impede a próxima disciplina. Executar novamente
reaproveita os caminhos e arquivos já presentes no acervo.

## Marcar itens como concluídos

Essa função é separada do crawler e sempre exige confirmação no menu. Ela usa somente o endpoint
`PUT /courses/:course_id/modules/:module_id/items/:id/done`, destinado aos itens cujo requisito é
`must_mark_done` — isto é, aqueles que mostram ao aluno a opção manual de conclusão.

O serviço:

- nunca conclui `Quiz`, `Assignment` ou `Discussion`;
- não envia outra requisição para itens que já estejam concluídos;
- ignora itens sem requisito ou com requisitos como `must_view`, `must_submit` e `min_score`;
- ignora e informa itens bloqueados, não publicados ou recusados pelo Canvas;
- permite escolher uma disciplina ou todas as disciplinas de uma formação escolhida;
- permanece no submenu até a opção de voltar ser escolhida.

A operação em lote nunca atravessa formações: ela exige escolher uma formação e digitar
`CONCLUIR FORMAÇÃO`, evitando uma alteração ampla por engano.

## Configuração

O projeto usa variáveis de ambiente. O arquivo `.env.example` documenta os valores esperados, enquanto `.env` contém a configuração local e não deve ser versionado.

Principais variáveis:

| Variável | Finalidade | Padrão inicial |
| --- | --- | --- |
| `CANVAS_BASE_URL` | Endereço da instalação do Canvas | `https://pucminas.instructure.com` |
| `CANVAS_ACCESS_TOKEN` | Token pessoal usado na API | vazio |
| `CANVAS_OUTPUT_DIR` | Pasta do acervo portátil | `./acervo` |
| `CANVAS_PER_PAGE` | Quantidade solicitada por página da API | `100` |
| `CANVAS_REQUEST_TIMEOUT_SECONDS` | Timeout de requisição/download | `60` |
| `CANVAS_DOWNLOAD_CONCURRENCY` | Downloads simultâneos | `4` |
| `CANVAS_INCLUDE_CONCLUDED_COURSES` | Incluir cursos encerrados | `false` |
| `CANVAS_KEEP_SOURCE_HTML` | Preservar HTML original | `true` |
| `TRANSCRIPTION_ENABLED` | Ativar transcrição | `true` |
| `TRANSCRIPTION_PROVIDER` | Implementação de transcrição | `faster-whisper` |
| `WHISPER_MODEL` | Modelo local do Whisper | `medium` |
| `WHISPER_LANGUAGE` | Idioma principal das aulas | `pt` |

### Token de acesso

Se a instituição permitir tokens pessoais, o token deverá ser criado nas configurações do perfil do Canvas e inserido somente no `.env` local:

```dotenv
CANVAS_ACCESS_TOKEN=cole_o_token_aqui
```

O token equivale a uma senha. Ele não deve ser colocado no README, em commits, screenshots, logs, argumentos de linha de comando ou mensagens de chat.

Se a PUC Minas tiver desabilitado tokens pessoais, será necessário avaliar OAuth2 com uma Developer Key aprovada pela instituição.

## Execução simples

A maneira recomendada de usar o projeto é pelo launcher em português. Não é necessário ativar
a `.venv` nem digitar comandos Python:

```bash
./canvas.sh
```

O menu apresentado permite:

1. verificar a conexão com o Canvas;
2. visualizar as formações configuradas;
3. escolher uma formação e listar suas disciplinas;
4. navegar por formação, disciplina e módulo até seus itens;
5. baixar uma disciplina ou todas as disciplinas de uma formação;
6. marcar itens manuais como concluídos;
7. consultar os comandos rápidos.

Também é possível executar uma opção diretamente:

```bash
./canvas.sh verificar
./canvas.sh formacoes
./canvas.sh disciplinas
./canvas.sh explorar
./canvas.sh baixar
./canvas.sh concluir
./canvas.sh ajuda
```

O script localiza a pasta do projeto automaticamente e executa o Python existente em `.venv`
sem ativá-la no terminal. Em uma instalação nova, ele tenta criar o ambiente e instalar as
dependências antes de abrir o menu.

## Instalação manual

O projeto requer Python 3.12 ou superior. O ambiente virtual local já está ignorado pelo Git.

```bash
# Criar o ambiente em uma instalação nova
python3 -m venv .venv

# Ativar e instalar o pacote em modo editável
source .venv/bin/activate
python -m pip install -e .

# Executar os testes
python -m unittest discover -s tests -v
```

Em Debian ou Ubuntu, a criação de um ambiente novo pode exigir o pacote do sistema
`python3-venv`. O ambiente `.venv` desta cópia do projeto já foi criado e está funcional.

## Interface Python avançada

Comandos já implementados:

```bash
# Confere a configuração e autentica sem modificar o Canvas
canvas-crawler doctor

# Lista os cursos ativos visíveis para o usuário
canvas-crawler courses

# Mostra as formações e suas chaves sem abrir o menu
canvas-crawler programs

# Seleciona diretamente uma formação, útil para scripts
canvas-crawler courses --program ia-pos

# Navega por formação, disciplina e módulo e lista os itens
canvas-crawler inspect

# Ignora o menu e lista todas as disciplinas das formações configuradas
canvas-crawler courses --all

# Inclui também cursos associados a matrículas concluídas
canvas-crawler courses --include-concluded

# Abre o submenu para baixar uma disciplina ou uma formação
canvas-crawler crawl

# Abre o submenu de conclusão manual
canvas-crawler complete
```

Também é possível executar sem ativar o ambiente:

```bash
./.venv/bin/canvas-crawler doctor
./.venv/bin/canvas-crawler courses
```

Comandos planejados para as próximas fases:

```bash
# Verifica hashes e links relativos de uma pasta já coletada
canvas-crawler verify "./acervo/01 - Nome do Curso"
```

Os comandos de consulta fazem somente requisições `GET`. O comando `crawl` também baixa os
materiais para o disco local, mas não altera conteúdo, atividades ou progresso no Canvas.

### Como o comando `canvas-crawler` funciona

O bloco `[project.scripts]` do `pyproject.toml` registra o nome `canvas-crawler` como ponto de
entrada para a função `canvas_crawler.cli:main`. Durante `pip install -e .`, o Python cria um
pequeno executável dentro de `.venv/bin/`. Quando o ambiente virtual está ativo, essa pasta fica
no início da variável `PATH`; por isso o terminal encontra `canvas-crawler` sem ser necessário
digitar `python -m canvas_crawler`.

A instalação é *editável*: o executável aponta para esta pasta do projeto. Alterações no código
passam a valer sem reinstalar o pacote, exceto quando mudamos metadados do `pyproject.toml` ou a
localização do pacote.

## Fluxo de coleta

Uma sincronização completa deverá seguir estas etapas:

1. carregar e validar a configuração;
2. autenticar o usuário;
3. listar cursos ativos e aplicar os filtros solicitados;
4. listar os módulos na ordem apresentada pelo Canvas;
5. listar os itens e classificar tipos permitidos e excluídos;
6. criar os nomes e caminhos locais de forma determinística;
7. coletar páginas, arquivos e recursos incorporados;
8. reescrever links internos para caminhos relativos;
9. processar vídeos e gerar transcrições;
10. gerar os READMEs de índice;
11. calcular hashes e atualizar o manifesto;
12. verificar a integridade do curso;
13. emitir um relatório final com sucessos, exclusões e falhas.

## Estratégia de implementação

### Fase 1 — acesso e diagnóstico

- estrutura do pacote Python;
- leitura segura do `.env`;
- cliente HTTP com Bearer token;
- paginação baseada no cabeçalho `Link`;
- retries com backoff para limites e falhas transitórias;
- comandos `doctor`, `courses` e `inspect`;
- testes com respostas simuladas.

### Fase 2 — acervo documental

- criação determinística de cursos e módulos;
- download de arquivos;
- coleta de páginas;
- preservação do HTML;
- conversão para Markdown;
- download e nomenclatura de imagens;
- reescrita de links;
- geração do manifesto e dos READMEs.

### Fase 3 — mídia e transcrição

- identificação de vídeos nativos;
- inventário das ferramentas externas usadas pela PUC;
- download autorizado por provedor;
- extração de áudio com FFmpeg;
- transcrição local com `faster-whisper`;
- timestamps e metadados;
- retomada de processamento interrompido.

### Fase 4 — progresso e robustez

- verificação integral do acervo;
- modo `--dry-run` detalhado;
- conclusão manual em operação independente, com confirmação e filtros de segurança;
- logs sem credenciais ou URLs assinadas;
- relatórios de sincronização;
- tratamento de conflitos com edições locais.

## Tecnologias utilizadas

- Python 3.12 ou superior;
- `httpx` para API e downloads;
- `python-dotenv` para configuração local;
- `beautifulsoup4` para analisar HTML;
- `markdownify` para conversão inicial em Markdown;
- `faster-whisper` e PyAV para transcrição local de áudio e vídeo;
- `unittest` da biblioteca padrão para testes automatizados.

## Segurança e privacidade

- `.env` está ignorado pelo Git;
- o token será enviado no cabeçalho `Authorization`, nunca na query string;
- cabeçalhos de autenticação e URLs temporárias serão removidos dos logs;
- os arquivos serão gravados inicialmente com extensão temporária e renomeados após validação;
- caminhos recebidos da API serão sanitizados contra traversal;
- redirects de download deverão ser validados;
- a concorrência será limitada para respeitar a plataforma;
- respostas `429` e cabeçalhos de rate limit serão tratados;
- o acervo coletado deverá permanecer privado e ser usado respeitando os direitos dos autores e as regras da instituição.

## Critérios para mover um curso

Uma pasta estará pronta para ser movida ao projeto `Pos-Graduacao` quando:

- todos os itens suportados tiverem status final no manifesto;
- nenhum download estiver incompleto;
- os hashes dos arquivos forem válidos;
- os links relativos do Markdown funcionarem;
- as imagens tiverem nomes compreensíveis;
- os vídeos acessíveis tiverem transcrição;
- itens ignorados estiverem registrados;
- o README do curso fornecer um índice completo;
- o relatório de verificação não apontar erros bloqueantes.

Depois disso, a operação de transferência será simplesmente mover a pasta do curso. O crawler não deverá mover ou apagar automaticamente o material sem uma ordem explícita.

## Documentação oficial relevante

- [Canvas LMS REST API](https://developerdocs.instructure.com/services/canvas)
- [Cursos](https://developerdocs.instructure.com/services/canvas/resources/courses)
- [Módulos e progresso](https://developerdocs.instructure.com/services/canvas/resources/modules)
- [Páginas](https://developerdocs.instructure.com/services/canvas/resources/pages)
- [Arquivos](https://developerdocs.instructure.com/services/canvas/resources/files)
- [Objetos de mídia](https://developerdocs.instructure.com/services/canvas/resources/media_objects)
- [OAuth2](https://developerdocs.instructure.com/services/canvas/oauth2)

## Próximo passo

Executar novamente a coleta da formação desejada. A coleta agora é incremental: documentos,
imagens e transcrições que já existirem são preservados, enquanto somente artefatos ausentes são
baixados ou produzidos. Atividades e provas continuam excluídas do acervo.

## Estado validado

Em 2 de outubro de 2026, a versão atual foi validada diretamente contra a conta configurada:

- `GET /api/v1/users/self/profile` autenticou corretamente;
- `GET /api/v1/courses` retornou 62 cursos;
- o catálogo organizou 41 disciplinas em ADS e 17 em IA;
- quatro cursos globais ou fora do escopo ficaram sem classificação e não aparecem no menu;
- o comando `inspect` navegou até um módulo real e listou somente os metadados de seus itens;
- nenhuma operação de escrita foi executada;
- o crawler foi validado com uma árvore simulada contendo HTML, Markdown, imagem, PDF e vídeo temporário;
- embeds do Canvas Studio são resolvidos pelo lançamento LTI autorizado, sem compartilhar o token
  pessoal do Canvas com o provedor;
- legendas autorizadas são convertidas em Markdown e JSON; quando apenas o vídeo é baixável, ele é
  transcrito e apagado imediatamente após o processamento;
- mídias com download e transcrição desabilitados pelo proprietário são registradas no manifesto
  como bloqueadas, separadas de falhas técnicas e provedores ainda não suportados, sem contornar a
  permissão;
- os 21 testes automatizados passaram.

O modelo do Whisper é carregado somente quando a primeira mídia é encontrada. Na primeira
transcrição, o `faster-whisper` poderá baixar o modelo configurado em `WHISPER_MODEL`; nas
execuções seguintes ele reutiliza o cache local.
