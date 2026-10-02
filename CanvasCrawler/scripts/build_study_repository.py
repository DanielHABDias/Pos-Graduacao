"""Gera a camada navegável do repositório de estudos a partir do acervo do Canvas."""

from __future__ import annotations

import json
import re
import subprocess
from collections import Counter
from pathlib import Path
from urllib.parse import quote


# O script vive em Pos-Graduacao/CanvasCrawler/scripts e encontra o repositório
# sem depender do nome do usuário ou de um caminho absoluto.
ROOT = Path(__file__).resolve().parents[2]
FORMATION = ROOT / "Inteligência Artificial e Aprendizado de Máquina"


COURSES: dict[str, tuple[str, tuple[str, ...], tuple[tuple[str, str], ...]]] = {
    "01": ("Transformar dados em decisões por meio de BI, OLAP, análise descritiva, preditiva e prescritiva.", ("KPIs e suporte à decisão", "arquiteturas de BI e operações OLAP", "cultura data-driven", "data discovery e visualização"), (("Tableau", "https://help.tableau.com/current/pro/desktop/en-us/default.htm"),)),
    "02": ("Construir a base probabilística e inferencial necessária para analisar dados e avaliar evidências.", ("estatística descritiva", "probabilidade e distribuições", "estimação e intervalos de confiança", "testes de hipóteses"), (("NIST Engineering Statistics Handbook", "https://www.itl.nist.gov/div898/handbook/"),)),
    "03": ("Aplicar princípios de DevOps ao ciclo de vida de dados e modelos, com automação, rastreabilidade e operação confiável.", ("cultura DevOps", "DataOps e qualidade de pipelines", "MLOps, experimentos e registro de modelos", "containers, APIs, testes e CI/CD"), (("MLflow", "https://mlflow.org/docs/latest/"), ("Docker", "https://docs.docker.com/"))),
    "04": ("Usar Python e seu ecossistema científico para representar, transformar, analisar e visualizar dados.", ("fundamentos da linguagem", "NumPy e vetorização", "pandas e manipulação de dados", "visualização e notebooks reprodutíveis"), (("Python", "https://docs.python.org/3/"), ("NumPy", "https://numpy.org/doc/stable/"), ("pandas", "https://pandas.pydata.org/docs/"))),
    "05": ("Preparar dados confiáveis e integrados, da origem ao consumo analítico ou por modelos de machine learning.", ("qualidade, limpeza e transformação", "ETL e ELT", "integração de fontes e SQL", "governança, linhagem e orquestração"), (("Apache Airflow", "https://airflow.apache.org/docs/apache-airflow/stable/"), ("dbt", "https://docs.getdbt.com/docs/introduction"))),
    "06": ("Modelar relações, incertezas e resultados por meio de técnicas estatísticas interpretáveis e verificáveis.", ("correlação e regressão", "modelos lineares e generalizados", "diagnóstico e validação", "seleção de modelos e interpretação"), (("statsmodels", "https://www.statsmodels.org/stable/"),)),
    "07": ("Projetar e avaliar sistemas de aprendizado supervisionado e não supervisionado com rigor experimental.", ("pré-processamento e engenharia de atributos", "classificação e regressão", "agrupamento e redução de dimensionalidade", "métricas, validação e ajuste"), (("scikit-learn", "https://scikit-learn.org/stable/"),)),
    "08": ("Compreender redes neurais e treinar modelos profundos, conectando fundamentos matemáticos a aplicações.", ("perceptrons e retropropagação", "otimização e regularização", "arquiteturas profundas", "avaliação e generalização"), (("Deep Learning Book", "https://www.deeplearningbook.org/"),)),
    "09": ("Implementar redes neurais com frameworks modernos e organizar treinamento, avaliação e persistência de modelos.", ("tensores e diferenciação automática", "Keras e TensorFlow", "PyTorch", "pipelines de treinamento e deployment"), (("TensorFlow", "https://www.tensorflow.org/guide"), ("PyTorch", "https://pytorch.org/docs/stable/index.html"))),
    "10": ("Extrair informação de imagens com processamento digital e modelos de visão computacional clássicos e profundos.", ("representação e transformação de imagens", "filtros, bordas e segmentação", "extração de características", "CNNs, detecção e classificação"), (("OpenCV", "https://docs.opencv.org/4.x/"),)),
    "11": ("Representar, analisar e modelar linguagem humana, de técnicas linguísticas clássicas a modelos neurais.", ("normalização e análise linguística", "representações vetoriais", "classificação e extração de informação", "modelos de linguagem"), (("spaCy", "https://spacy.io/usage"), ("Hugging Face NLP Course", "https://huggingface.co/learn/nlp-course/"))),
    "12": ("Modelar sequências com redes recorrentes, mecanismos de atenção e Transformers.", ("RNN, LSTM e GRU", "encoder-decoder e atenção", "arquitetura Transformer", "treinamento e aplicações em sequências"), (("Attention Is All You Need", "https://arxiv.org/abs/1706.03762"),)),
    "13": ("Entender modelos generativos e criar novas amostras a partir da distribuição aprendida dos dados.", ("autoencoders e modelos latentes", "GANs", "modelos de difusão", "avaliação, riscos e aplicações"), (("Generative Adversarial Networks", "https://arxiv.org/abs/1406.2661"),)),
    "14": ("Formular decisões sequenciais e aprender políticas por interação com ambientes.", ("processos de decisão de Markov", "funções de valor e Bellman", "métodos Monte Carlo e diferença temporal", "Q-learning, políticas e deep RL"), (("Reinforcement Learning: An Introduction", "https://www.incompleteideas.net/book/the-book-2nd.html"), ("Gymnasium", "https://gymnasium.farama.org/"))),
    "15": ("Combinar compreensão de opinião em texto com técnicas de personalização e recomendação.", ("polaridade, emoções e aspectos", "representações e classificadores de sentimento", "recomendação baseada em conteúdo e filtragem colaborativa", "modelos híbridos, métricas e vieses"), (("TensorFlow Recommenders", "https://www.tensorflow.org/recommenders"),)),
    "16": ("Relacionar tecnologia, ética e sociedade para avaliar criticamente impactos humanos da inteligência artificial.", ("concepções contemporâneas de humanismo", "fundamentação ética", "responsabilidade e dignidade humana", "ética aplicada à ciência, aos dados e à IA"), (("Recomendação da UNESCO sobre Ética da IA", "https://www.unesco.org/en/legal-affairs/recommendation-ethics-artificial-intelligence"),)),
}


# Sínteses curtas baseadas no programa efetivamente encontrado em cada unidade.
# A chave usa (número da disciplina, número do módulo no Canvas).
UNIT_GUIDES: dict[tuple[str, str], tuple[str, str]] = {
    ("01", "02"): ("A unidade apresenta indicadores de desempenho, sistemas de apoio à decisão e análise multidimensional. O objetivo é ligar uma pergunta de negócio às métricas e dimensões que permitem investigá-la.", "Uma rede varejista pode analisar vendas por tempo, loja e produto. O OLAP permite começar pelo total anual e detalhar até uma loja e um mês específicos."),
    ("01", "03"): ("A unidade diferencia organizações orientadas por dados de organizações que apenas acumulam dados. Também relaciona análise descritiva, preditiva e prescritiva ao processo de descoberta e decisão.", "Uma queda nas vendas pode ser descrita por região, explicada por mudanças no mix de produtos, projetada para o próximo trimestre e tratada com uma política de preços."),
    ("01", "04"): ("A unidade transforma conceitos analíticos em visualizações no Tableau. A ênfase está na preparação da base, escolha do gráfico, cálculos de tabela e construção de dashboards coerentes.", "Um painel de vendas pode combinar receita mensal, margem por categoria e um filtro regional. Cada gráfico deve responder a uma pergunta específica."),
    ("01", "05"): ("A prática aplica exploração e visualização a dados públicos da Prefeitura de Belo Horizonte. O foco está em entender as colunas antes de calcular indicadores e comunicar padrões.", "Antes de comparar bairros, verifique período, unidade de medida, valores ausentes e possíveis duplicidades. Só então agregue e visualize."),
    ("02", "02"): ("A unidade resume dados com tabelas, gráficos e medidas numéricas. Média, mediana e dispersão devem ser interpretadas em conjunto, porque uma medida isolada pode esconder assimetria ou valores extremos.", "Nos salários 2, 2, 3, 3 e 20 mil, a média é 6 mil e a mediana é 3 mil. A diferença revela a influência do valor extremo."),
    ("02", "03"): ("A unidade formaliza incerteza com regras de probabilidade, variáveis aleatórias e distribuições. Bayes atualiza uma crença inicial depois de observar uma evidência.", "Um teste médico positivo não implica doença com 100% de certeza. O resultado depende da sensibilidade, da especificidade e da prevalência na população."),
    ("02", "04"): ("A unidade usa amostras para estimar parâmetros populacionais. Intervalos de confiança expressam uma faixa compatível com os dados e o método, enquanto o tamanho amostral controla a precisão esperada.", "Uma pesquisa pode estimar a proporção de clientes satisfeitos e informar a margem de erro, em vez de apresentar apenas um percentual pontual."),
    ("02", "05"): ("A unidade organiza testes de hipóteses em quatro decisões: formular hipóteses, escolher a estatística, calcular a evidência e interpretar o resultado no contexto. O valor-p não mede a probabilidade de a hipótese nula ser verdadeira.", "Ao comparar duas versões de uma página, um resultado estatisticamente significativo ainda precisa ter efeito grande o bastante para justificar a mudança."),
    ("03", "02"): ("Este módulo reúne scripts, notebooks e arquivos usados nas práticas. Consulte-o junto das unidades conceituais e execute os exemplos em ambiente isolado.", "Crie um ambiente virtual, fixe versões das dependências e registre o comando necessário para reproduzir cada execução."),
    ("03", "03"): ("A unidade apresenta cultura DevOps como colaboração apoiada por automação, versionamento e feedback rápido. O foco não está em uma ferramenta específica, mas em reduzir trabalho manual e tornar mudanças verificáveis.", "Uma alteração passa por revisão, testes automáticos e implantação controlada. Se um teste falhar, o pipeline interrompe a entrega antes de afetar usuários."),
    ("03", "04"): ("DataOps aplica qualidade e automação ao fluxo de dados. MLOps amplia essa disciplina para experimentos, modelos, implantação e monitoramento, incluindo dados e métricas além do código.", "Dois modelos só podem ser comparados com segurança quando dados, parâmetros, ambiente e métrica ficam registrados junto do resultado."),
    ("03", "05"): ("A unidade implementa versionamento, ambientes reproduzíveis, testes e pipelines. O registro de modelos conecta uma execução experimental ao artefato que poderá ser promovido.", "Um teste pode verificar se o pré-processamento mantém as colunas esperadas e rejeita categorias inválidas antes do treinamento."),
    ("03", "06"): ("A unidade empacota e expõe modelos com Docker e APIs, depois mede o comportamento sob carga. Implantar inclui definir contrato de entrada, tratamento de erro e observabilidade.", "Uma API de previsão deve validar tipos e limites, devolver erro compreensível para entradas inválidas e registrar latência sem armazenar dados sensíveis."),
    ("04", "02"): ("A unidade cobre os elementos básicos de Python: valores, coleções, decisões, repetições e funções. A escolha da estrutura de dados afeta clareza e custo das operações.", "Use uma lista para uma sequência ordenada, um conjunto para testar pertencimento sem duplicidade e um dicionário para associar chaves a valores."),
    ("04", "03"): ("A unidade introduz arrays NumPy e vetorização. Operações sobre arrays evitam laços explícitos, deixam a intenção matemática mais clara e aproveitam implementações otimizadas.", "Para normalizar uma coluna, subtraia a média do array inteiro e divida pelo desvio padrão, em vez de atualizar elemento por elemento."),
    ("04", "04"): ("A unidade usa pandas para selecionar, transformar, agrupar e combinar dados tabulares. Índices, tipos e valores ausentes precisam ser verificados antes da análise.", "Para calcular receita por categoria, valide quantidade e preço, crie a coluna de receita e só então use `groupby` para agregar."),
    ("04", "05"): ("A unidade trata visualização como parte da análise. O gráfico deve corresponder ao tipo de variável e à comparação desejada, com escalas e rótulos que não distorçam a leitura.", "Use barras para comparar categorias, linhas para evolução temporal e dispersão para investigar relação entre duas variáveis quantitativas."),
    ("05", "02"): ("A unidade conecta dado, informação, conhecimento, BI e governança. Governança define responsabilidades, significado, qualidade, segurança e uso permitido dos dados.", "Um campo chamado `cliente_ativo` precisa de definição, responsável, regra de atualização e tratamento conhecido para valores ausentes."),
    ("05", "03"): ("A unidade detalha ETL: extrair sem perder a origem, transformar com regras verificáveis e carregar no destino com controle de falhas. As práticas usam arquivos, SQL Server e Power BI.", "Uma carga incremental deve identificar registros novos ou alterados e ser idempotente, para que uma repetição não duplique dados."),
    ("05", "04"): ("A unidade constrói um fluxo no Power BI para padronizar clientes e pedidos de várias regiões. União e relacionamento exigem chaves compatíveis e controle de duplicidade.", "Antes de unir clientes pessoa física e jurídica, crie um identificador consistente e preserve o tipo original para auditoria."),
    ("05", "05"): ("A unidade reproduz a integração no Tableau Prep. O resultado deve ser equivalente independentemente da ferramenta: mesmas regras, mesmas contagens e mesmas exceções documentadas.", "Compare quantidade de linhas, chaves únicas e totais antes e depois de cada etapa. Uma junção que aumenta linhas pode indicar relação muitos-para-muitos."),
    ("06", "02"): ("A unidade modela uma variável quantitativa com regressão linear simples e múltipla. A interpretação depende dos coeficientes e da análise dos resíduos, não apenas do valor de R².", "Em um modelo de preço por área e idade, o coeficiente da área representa a variação média esperada no preço ao aumentar uma unidade de área, mantendo a idade constante."),
    ("06", "03"): ("Modelos lineares generalizados ligam uma distribuição da família exponencial a um preditor linear. Isso permite tratar respostas binárias, contagens e outros dados que não seguem uma normal.", "A regressão logística estima a probabilidade de inadimplência, enquanto uma regressão de Poisson pode modelar a quantidade de chamados por dia."),
    ("06", "04"): ("A unidade analisa observações ordenadas no tempo. Tendência, sazonalidade, autocorrelação e estacionariedade orientam transformação, diferenciação e escolha do modelo.", "Vendas mensais podem crescer ao longo do tempo e subir todo dezembro. A decomposição separa tendência e sazonalidade antes de analisar o restante."),
    ("07", "02"): ("A unidade apresenta o ciclo de machine learning, da definição do problema à preparação dos dados. O viés indutivo representa as suposições que permitem ao algoritmo generalizar além dos exemplos observados.", "Antes de prever cancelamento, defina quando a previsão será feita. Dados registrados depois desse momento causam vazamento e produzem uma avaliação irreal."),
    ("07", "03"): ("A unidade cobre classificação e regressão supervisionadas, separação de dados, seleção de atributos, árvores e avaliação. A métrica deve refletir o custo de falso positivo e falso negativo.", "Em detecção de fraude, acurácia pode ser alta mesmo se o modelo ignorar todas as fraudes. Precisão, revocação e matriz de confusão mostram o comportamento real."),
    ("07", "04"): ("A unidade estuda regras de associação, agrupamento, medidas de distância e detecção de observações atípicas. Como não existe rótulo de resposta, a validação combina métricas internas e utilidade no domínio.", "Em uma cesta de compras, suporte mede frequência conjunta. Confiança mede com que frequência B aparece quando A aparece. Lift compara essa relação com o acaso."),
    ("08", "02"): ("A unidade introduz predição, funções de perda, Softmax e regularização. Treinar significa ajustar parâmetros para reduzir uma medida de erro em dados de treino sem perder capacidade de generalização.", "Em classificação de imagens, Softmax transforma escores em probabilidades que somam 1. A entropia cruzada penaliza baixa probabilidade atribuída à classe correta."),
    ("08", "03"): ("A unidade explica camadas, ativações, descida do gradiente e retropropagação. A regra da cadeia transporta o efeito do erro da saída até cada peso da rede.", "Se a taxa de aprendizado for alta, a otimização pode oscilar. Se for muito baixa, o treinamento avança devagar ou fica preso em uma região ruim."),
    ("08", "04"): ("A unidade trata redes profundas, otimizadores, normalização em lote e dropout. Essas técnicas melhoram estabilidade ou generalização, mas não substituem dados adequados e validação correta.", "Dropout desativa unidades aleatoriamente durante o treino e reduz dependências frágeis. Na inferência, a rede usa todas as unidades com a escala apropriada."),
    ("08", "05"): ("A unidade compara convoluções para padrões espaciais e recorrência para sequências. CNNs compartilham filtros entre posições, enquanto LSTMs controlam o fluxo de memória ao longo do tempo.", "Um filtro pode aprender bordas em camadas iniciais e partes de objetos em camadas posteriores. Uma LSTM pode manter informação relevante de palavras anteriores."),
    ("09", "02"): ("A unidade apresenta frameworks de deep learning e usa orientação a objetos para organizar dados, modelos e treinamento. Separar responsabilidades facilita teste e troca de componentes.", "Uma classe de modelo define a arquitetura. O laço de treinamento recebe lotes, calcula perda, propaga gradientes e atualiza parâmetros."),
    ("09", "03"): ("A unidade usa Keras como API de alto nível para definir, compilar, treinar e avaliar redes. O histórico de treino deve ser comparado com validação para detectar sobreajuste.", "Se a perda de treino cai enquanto a de validação sobe, aumente regularização, reveja a complexidade ou obtenha dados mais representativos."),
    ("09", "04"): ("A unidade trabalha com tensores, operações, diferenciação automática e módulos no PyTorch. Gradientes acumulam por padrão, por isso o laço deve zerá-los antes de uma nova atualização.", "O ciclo básico é `zero_grad`, cálculo da saída, cálculo da perda, `backward` e `step`. O modo de avaliação desativa comportamentos específicos de treino."),
    ("10", "02"): ("A unidade diferencia processamento de imagens de visão computacional e apresenta aplicações. Imagens são matrizes de intensidades, mas o significado depende de aquisição, escala, cor e contexto.", "Converter uma imagem para tons de cinza pode reduzir custo, mas remove informação cromática que pode ser essencial para a tarefa."),
    ("10", "03"): ("A unidade constrói busca visual por conteúdo. Descritores transformam imagens ou quadros em vetores, e uma medida de distância permite recuperar itens semelhantes.", "Em busca de cenas, extraia descritores de cada quadro, crie um vocabulário visual e compare a consulta com o índice em vez de percorrer vídeos brutos."),
    ("10", "04"): ("A unidade aplica CNNs à classificação, incluindo aumento de dados e avaliação. Aumentação deve simular variações plausíveis sem alterar a classe.", "Espelhar uma foto de um animal costuma preservar a classe. Espelhar um texto ou um exame com lateralidade pode criar um exemplo incorreto."),
    ("10", "05"): ("A unidade usa transferência de aprendizado, ajuste fino e detectores de objetos. Detecção acrescenta localização à classificação e exige anotações consistentes.", "Comece congelando a rede pré-treinada e treinando a nova cabeça. Depois descongele poucas camadas com taxa menor e compare em validação."),
    ("11", "02"): ("A unidade organiza aquisição de texto por bases públicas, raspagem e enriquecimento. A coleta deve respeitar licença, privacidade, codificação e estrutura da fonte.", "Ao coletar notícias, preserve URL, data e fonte. Esses campos permitem rastrear duplicatas e mudanças de distribuição."),
    ("11", "03"): ("A unidade limpa e normaliza texto com expressões regulares e técnicas linguísticas. Cada transformação pode remover sinal útil, por isso precisa ser justificada pela tarefa.", "Remover pontuação pode ajudar uma contagem simples, mas prejudicar análise de emoção em que exclamações carregam informação."),
    ("11", "04"): ("A unidade compara one-hot, bag of words, TF-IDF e embeddings. Representações esparsas preservam contagens explícitas, enquanto embeddings aproximam relações semânticas em vetores densos.", "TF-IDF reduz o peso de palavras frequentes em muitos documentos e destaca termos mais específicos de cada texto."),
    ("11", "05"): ("A unidade aplica similaridade, classificação e análise de sentimentos, chegando a aplicações com modelos GPT. Avaliação deve incluir exemplos de erro, não apenas uma média global.", "Compare textos com similaridade do cosseno e inspecione falsos positivos. Duas frases podem compartilhar vocabulário e ainda expressar sentidos opostos."),
    ("12", "02"): ("A unidade modela sequências com RNNs, LSTMs e GRUs. Portas controlam que informação entra, permanece ou sai do estado, reduzindo o problema de dependências longas.", "Em previsão de texto, o estado resume o contexto anterior. Sequências muito longas ainda podem exigir atenção ou Transformers."),
    ("12", "03"): ("A unidade apresenta atenção e a arquitetura Transformer. Cada token combina informação dos demais tokens em paralelo, com codificação de posição para representar ordem.", "Na frase “o banco aprovou o crédito”, a atenção pode relacionar “banco” a “crédito” e distinguir o sentido financeiro de outros usos."),
    ("12", "04"): ("A unidade explica pré-treinamento, ajuste e avaliação de modelos de linguagem. Perplexidade mede previsão de tokens, mas não cobre factualidade, segurança ou utilidade.", "Um modelo pode escrever com fluência e ainda inventar uma fonte. Avalie a tarefa com critérios objetivos e revisão humana dos erros."),
    ("13", "02"): ("A unidade usa autoencoders para comprimir e reconstruir dados. VAEs aprendem uma distribuição latente regularizada, o que permite amostrar novas representações.", "Um denoising autoencoder recebe uma imagem corrompida e aprende a reconstruir a versão limpa, evitando apenas copiar a entrada."),
    ("13", "03"): ("A unidade compara GANs e modelos de difusão. GANs treinam gerador e discriminador em competição. Difusão aprende a reverter um processo gradual de adição de ruído.", "Mode collapse ocorre quando uma GAN gera pouca variedade. Inspecione diversidade e cobertura dos modos além da qualidade visual."),
    ("13", "04"): ("A unidade detalha atenção causal, múltiplas cabeças, posição e treinamento de GPT. A máscara causal impede que o modelo consulte tokens futuros durante a previsão.", "Ao prever a próxima palavra, o token na posição t pode usar apenas as posições anteriores e a própria posição, nunca o restante da resposta."),
    ("14", "02"): ("A unidade formaliza agente, ambiente, estado, ação, recompensa e processo de decisão de Markov. A recompensa acumulada representa consequências imediatas e futuras.", "Em controle de estoque, o estado inclui nível atual e demanda observada. A ação decide reposição e a recompensa combina venda, falta e custo de armazenagem."),
    ("14", "03"): ("A unidade compara Monte Carlo, diferença temporal, aproximação de funções e cenários multiagente. TD atualiza estimativas antes do episódio terminar usando outra estimativa como alvo.", "Q-learning aprende o valor de cada ação e pode agir com exploração epsilon-greedy para não repetir apenas a escolha conhecida."),
    ("14", "04"): ("A unidade combina redes profundas com reforço e apresenta métodos baseados em política. Segurança exige limitar ações, avaliar cenários raros e evitar que uma recompensa mal definida gere atalhos indesejados.", "Um agente pode maximizar pontos explorando uma falha do simulador. Testes devem verificar o comportamento, não apenas a recompensa total."),
    ("15", "02"): ("A unidade modela polaridade, subjetividade e emoções. Métricas por classe são essenciais quando opiniões negativas ou categorias emocionais aparecem com frequências diferentes.", "Uma frase como “o atendimento foi ótimo, mas o produto quebrou” exige análise por aspecto para não reduzir avaliações distintas a um único rótulo."),
    ("15", "03"): ("A unidade apresenta recomendação baseada em conteúdo e similaridade. Itens e perfis precisam compartilhar uma representação, e a avaliação deve evitar usar interações futuras no treino.", "Um perfil pode ser a média ponderada dos vetores dos filmes curtidos. O sistema recomenda itens próximos que o usuário ainda não consumiu."),
    ("15", "04"): ("A unidade cobre filtragem colaborativa e modelos híbridos. A colaboração encontra padrões entre usuários e itens, mas sofre com usuários novos, itens novos e interações esparsas.", "Um híbrido pode combinar similaridade de conteúdo com fatoração de matriz e usar popularidade controlada quando ainda não há histórico suficiente."),
    ("16", "02"): ("A unidade discute alteridade, liberdade, justiça, afetividade e cultura da paz. A alteridade exige reconhecer o outro como sujeito, não apenas como objeto de uma decisão.", "Ao projetar um sistema público, consulte os grupos afetados e crie meios de contestação. Eficiência não compensa exclusão ou tratamento indigno."),
    ("16", "03"): ("A unidade relaciona ética, ecologia, economia e equidade. Decisões técnicas distribuem benefícios, custos e riscos entre pessoas e gerações.", "Um modelo eficiente que consome muita energia ou prejudica grupos vulneráveis precisa ser avaliado pelo impacto completo, não só pela acurácia."),
    ("16", "04"): ("A unidade conecta democracia, diálogo, ciência e responsabilidade. Conhecimento técnico amplia poder de ação e, por isso, aumenta a obrigação de explicar escolhas e responder por consequências.", "Uma decisão automatizada de alto impacto deve permitir auditoria, supervisão humana e recurso por parte da pessoa afetada."),
}


FORMULAS: dict[tuple[str, str], tuple[tuple[str, str, str], ...]] = {
    ("02", "02"): (("Média amostral", r"\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i", "Soma os valores e divide pelo número de observações."), ("Desvio padrão amostral", r"s=\sqrt{\frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}}", "Mede a dispersão em torno da média.")),
    ("02", "03"): (("Teorema de Bayes", r"P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}", "Atualiza a probabilidade de A depois de observar B."),),
    ("02", "04"): (("Intervalo para uma média", r"\bar{x}\pm z_{\alpha/2}\frac{\sigma}{\sqrt{n}}", "Mostra o efeito do tamanho da amostra sobre a margem de erro, quando as condições do método são atendidas."),),
    ("06", "02"): (("Regressão linear múltipla", r"Y_i=\beta_0+\beta_1X_{i1}+\cdots+\beta_pX_{ip}+\varepsilon_i", "Relaciona a resposta a vários preditores."), ("Coeficiente de determinação", r"R^2=1-\frac{\sum_i(y_i-\hat{y}_i)^2}{\sum_i(y_i-\bar{y})^2}", "Compara o erro do modelo com a variação total da resposta.")),
    ("06", "03"): (("Estrutura de um GLM", r"g(\mu_i)=\eta_i=\mathbf{x}_i^\top\boldsymbol{\beta}", "A função de ligação conecta a média da resposta ao preditor linear."),),
    ("07", "03"): (("Precisão", r"\mathrm{Precisão}=\frac{VP}{VP+FP}", "Entre os casos previstos como positivos, mede quantos estavam corretos."), ("Revocação", r"\mathrm{Revocação}=\frac{VP}{VP+FN}", "Entre os positivos reais, mede quantos foram encontrados."), ("F1", r"F_1=2\frac{\mathrm{Precisão}\cdot\mathrm{Revocação}}{\mathrm{Precisão}+\mathrm{Revocação}}", "Resume precisão e revocação pela média harmônica.")),
    ("07", "04"): (("Lift de uma regra", r"\mathrm{lift}(A\to B)=\frac{P(A\cap B)}{P(A)P(B)}", "Valores acima de 1 indicam ocorrência conjunta maior que a esperada sob independência."), ("Distância euclidiana", r"d(\mathbf{x},\mathbf{y})=\sqrt{\sum_{j=1}^{p}(x_j-y_j)^2}", "Compara vetores numéricos na mesma escala.")),
    ("08", "02"): (("Entropia cruzada", r"L=-\sum_{k=1}^{K}y_k\log(\hat{p}_k)", "Penaliza probabilidade baixa atribuída à classe correta."),),
    ("08", "03"): (("Atualização por gradiente", r"\theta_{t+1}=\theta_t-\eta\nabla_{\theta}L(\theta_t)", "Move os parâmetros na direção que reduz a perda localmente."),),
    ("11", "04"): (("TF-IDF", r"\mathrm{tfidf}(t,d)=\mathrm{tf}(t,d)\log\left(\frac{N}{\mathrm{df}(t)}\right)", "Combina frequência no documento com raridade no conjunto."),),
    ("11", "05"): (("Similaridade do cosseno", r"\cos(\mathbf{a},\mathbf{b})=\frac{\mathbf{a}\cdot\mathbf{b}}{\lVert\mathbf{a}\rVert\lVert\mathbf{b}\rVert}", "Compara a direção de dois vetores, reduzindo o efeito da magnitude."),),
    ("12", "03"): (("Atenção escalada", r"\mathrm{Attention}(Q,K,V)=\mathrm{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V", "Calcula quanto cada consulta deve combinar os valores associados às chaves."),),
    ("13", "02"): (("Objetivo de um VAE", r"\mathcal{L}=\mathbb{E}_{q(z\mid x)}[\log p(x\mid z)]-D_{KL}(q(z\mid x)\Vert p(z))", "Equilibra reconstrução e organização do espaço latente."),),
    ("14", "02"): (("Retorno descontado", r"G_t=\sum_{k=0}^{\infty}\gamma^kR_{t+k+1}", "Combina recompensas futuras e reduz o peso das mais distantes."), ("Equação de Bellman", r"V^{\pi}(s)=\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)[r+\gamma V^{\pi}(s')]", "Decompõe o valor entre recompensa imediata e valor futuro.")),
    ("14", "03"): (("Atualização Q-learning", r"Q(s,a)\leftarrow Q(s,a)+\alpha[r+\gamma\max_{a'}Q(s',a')-Q(s,a)]", "Atualiza o valor da ação usando o melhor valor estimado do próximo estado."),),
    ("15", "03"): (("Similaridade do cosseno", r"\cos(\mathbf{i},\mathbf{u})=\frac{\mathbf{i}\cdot\mathbf{u}}{\lVert\mathbf{i}\rVert\lVert\mathbf{u}\rVert}", "Compara o vetor de um item com o perfil do usuário."),),
    ("15", "04"): (("Erro quadrático médio", r"\mathrm{RMSE}=\sqrt{\frac{1}{n}\sum_{i=1}^{n}(r_i-\hat{r}_i)^2}", "Mede erro de previsão de notas na mesma unidade da avaliação."),),
}


def link(path: Path, base: Path) -> str:
    # Parênteses precisam ser codificados para não encerrarem o destino Markdown antes da hora.
    return quote(path.relative_to(base).as_posix(), safe="/#")


def clean_text(value: str) -> str:
    value = re.sub(r"!\[[^]]*]\([^)]*\)", "", value)
    value = re.sub(r"\[([^]]+)]\([^)]*\)", r"\1", value)
    value = re.sub(r"[`*_>#|]", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def page_summary(path: Path) -> tuple[str, str]:
    title = path.stem
    paragraphs: list[str] = []
    for block in re.split(r"\n\s*\n", path.read_text(encoding="utf-8", errors="ignore")):
        text = clean_text(block)
        if not text:
            continue
        if block.lstrip().startswith("#") and title == path.stem:
            title = clean_text(block.lstrip("# ")) or title
            continue
        if len(text) >= 45 and not text.lower().startswith(("origem:", "tipo:")):
            paragraphs.append(text)
        if sum(map(len, paragraphs)) >= 360:
            break
    summary = " ".join(paragraphs)[:420].rstrip()
    if len(summary) == 420:
        summary = summary.rsplit(" ", 1)[0] + "…"
    return title, summary


def pdf_pages(path: Path) -> int | None:
    try:
        output = subprocess.run(
            ["pdfinfo", str(path)], check=True, capture_output=True, text=True, timeout=20
        ).stdout
        match = re.search(r"^Pages:\s+(\d+)", output, re.MULTILINE)
        return int(match.group(1)) if match else None
    except (OSError, subprocess.SubprocessError, ValueError):
        return -1


def canvas_placeholder(path: Path) -> bool:
    """Identifica respostas JSON que o Canvas salvou com a extensão do anexo."""
    try:
        if path.stat().st_size > 4096:
            return False
        payload = json.loads(path.read_text(encoding="utf-8"))
        return isinstance(payload, dict) and isinstance(payload.get("attachment"), dict)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return False


def category(path: Path) -> str:
    suffix = path.suffix.casefold()
    if suffix == ".pdf": return "PDFs"
    if suffix in {".ppt", ".pptx"}: return "Apresentações"
    if suffix == ".ipynb": return "Notebooks"
    if suffix in {".py", ".r", ".rmd", ".sql", ".yml", ".yaml", ""}: return "Código e configuração"
    if suffix in {".csv", ".xls", ".xlsx", ".json", ".xml", ".data", ".names", ".twb", ".twbx", ".pbix", ".zip"}: return "Dados e artefatos"
    if suffix in {".png", ".jpg", ".jpeg", ".gif", ".svg"}: return "Imagens"
    if suffix == ".html": return "HTML original"
    if suffix == ".md": return "Páginas e textos"
    return "Outros materiais"


def module_readme(module: Path, course_number: str) -> None:
    files = sorted(
        (path for path in module.rglob("*") if path.is_file() and path.name != "README.md"),
        key=lambda path: path.as_posix().casefold(),
    )
    pages = sorted((module / "paginas").glob("*.md")) if (module / "paginas").exists() else []
    module_number = module.name[:2]
    guide = UNIT_GUIDES.get((course_number, module_number))
    lines = [f"# {module.name}", "", "[← Voltar à disciplina](../README.md)", "", "## Resumo da unidade", ""]
    if guide:
        lines.append(guide[0])
        lines.extend(["", "### Exemplo", "", guide[1]])
    elif "APRESENTA" in module.name.upper():
        lines.append("Este módulo reúne a apresentação, o plano de ensino e as referências da disciplina. Use-o para conferir objetivos, sequência das unidades e bibliografia indicada pelo professor.")
    elif "PESQUISA" in module.name.upper():
        lines.append("Espaço reservado no Canvas para pesquisa ou avaliação. O crawler não executa atividades e, por isso, apenas preserva a posição deste módulo na estrutura da disciplina.")
    elif "PROVA" in module.name.upper():
        lines.append("Módulo avaliativo preservado apenas como referência estrutural. Nenhuma prova foi aberta, respondida ou copiada pelo crawler.")
    elif pages:
        topics = [page_summary(path)[0] for path in pages[:8]]
        lines.append("Esta unidade reúne conteúdos sobre " + ", ".join(topics) + ". Consulte as páginas e os materiais na ordem indicada.")
    else:
        lines.append("Módulo de apoio mantido conforme a estrutura original do Canvas. Não há páginas textuais coletadas nesta seção.")
    formulas = FORMULAS.get((course_number, module_number), ())
    if formulas:
        lines.extend(["", "## Fórmulas essenciais", ""])
        for name, expression, explanation in formulas:
            lines.extend([f"### {name}", "", "$$", expression, "$$", "", explanation, ""])
    lines.extend(["", "## Conteúdo da unidade", ""])
    if pages:
        for path in pages:
            title, summary = page_summary(path)
            lines.append(f"- [{title}]({link(path, module)})" + (f" — {summary}" if summary else ""))
    else:
        lines.append("- Nenhuma página textual disponível.")

    grouped: dict[str, list[Path]] = {}
    for path in files:
        grouped.setdefault(category(path), []).append(path)
    lines.extend(["", "## Materiais", ""])
    order = ("PDFs", "Apresentações", "Notebooks", "Código e configuração", "Dados e artefatos", "Páginas e textos", "Imagens", "HTML original", "Outros materiais")
    for name in order:
        values = grouped.get(name, [])
        if not values:
            continue
        lines.extend([f"### {name} ({len(values)})", ""])
        visible = values if name not in {"Imagens", "HTML original"} else values[:20]
        for path in visible:
            detail = ""
            if canvas_placeholder(path):
                detail = " (arquivo indisponível ou ainda em processamento no Canvas)"
            elif path.suffix.casefold() == ".pdf":
                count = pdf_pages(path)
                if count == -1:
                    detail = " (arquivo indisponível ou ainda em processamento no Canvas)"
                elif count:
                    detail = f" ({count} páginas)"
            lines.append(f"- [{path.name}]({link(path, module)}){detail}")
        if len(visible) < len(values):
            directory = values[0].parent
            lines.append(f"- … e mais {len(values) - len(visible)} arquivos em [{directory.name}/]({link(directory, module)}/)")
        lines.append("")

    focus = [page_summary(path)[0] for path in pages[:5]]
    if focus:
        lines.extend(["## Roteiro de estudo", "", "1. Leia as páginas na ordem apresentada pelo módulo.", "2. Consulte os PDFs e apresentações enquanto registra definições, hipóteses e exemplos.", "3. Execute notebooks e códigos, verificando entradas, saídas e limitações.", "4. Ao final, responda:", ""])
        lines.extend(f"   - Como você explicaria **{topic}** sem consultar o material?" for topic in focus)
        lines.append("")
    module.joinpath("README.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def course_readme(course: Path) -> None:
    number = course.name[:2]
    description, concepts, references = COURSES[number]
    modules = sorted(path for path in course.iterdir() if path.is_dir() and not path.name.startswith((".", "images")))
    for module in modules:
        module_readme(module, number)
    lines = [f"# {course.name}", "", "## Resumo da disciplina", "", description, "", "A disciplina avança pelos seguintes eixos: " + ", ".join(concepts) + ".", "", "## Objetivos de aprendizagem", ""]
    lines.extend(f"- Compreender e aplicar {concept}." for concept in concepts)
    lines.extend(["", "## Sumário", ""])
    for module in modules:
        counts = Counter(category(path) for path in module.rglob("*") if path.is_file() and path.name != "README.md")
        detail = ", ".join(f"{value} {name.lower()}" for name, value in counts.most_common(3))
        lines.append(f"- [{module.name}]({link(module / 'README.md', course)})" + (f" — {detail}" if detail else ""))
    if (course / "ANOTACOES.md").exists():
        lines.extend(["", "## Anotações autorais", "", "- [Resumo e anotações anteriores](ANOTACOES.md), preservados integralmente."])
    root_materials = sorted(path for path in course.iterdir() if path.is_file() and path.name not in {"README.md", "ANOTACOES.md"})
    if root_materials:
        lines.extend(["", "## Materiais complementares já organizados", ""])
        lines.extend(f"- [{path.name}]({link(path, course)})" for path in root_materials)
    lines.extend(["", "## Referências externas para aprofundamento", ""])
    lines.extend(f"- [{label}]({url})" for label, url in references)
    lines.extend(["", "## Como estudar esta disciplina", "", "1. Comece pelas páginas de cada unidade para formar o mapa conceitual.", "2. Use os PDFs como fonte principal e as apresentações como revisão visual.", "3. Reproduza notebooks, scripts e exercícios com um ambiente isolado.", "4. Registre dúvidas e conecte os conceitos às disciplinas anteriores.", "5. Termine cada unidade produzindo uma explicação própria e um exemplo prático.", ""])
    course.joinpath("README.md").write_text("\n".join(lines), encoding="utf-8")


def build() -> None:
    courses = sorted(path for path in FORMATION.iterdir() if path.is_dir() and path.name[:2] in COURSES)
    for course in courses:
        course_readme(course)
    lines = ["# Inteligência Artificial e Aprendizado de Máquina", "", "Acervo de estudo da pós-graduação, organizado a partir das anotações pessoais e dos materiais acadêmicos coletados no Canvas da PUC Minas.", "", "- [Guia integrado de estudos](GUIA-DE-ESTUDOS.md)", "- [Materiais indisponíveis no Canvas](MATERIAIS-INDISPONIVEIS.md)", "", "## Trilha do curso", "", "| # | Disciplina | Foco principal |", "|---:|---|---|"]
    for course in courses:
        description = COURSES[course.name[:2]][0]
        lines.append(f"| {course.name[:2]} | [{course.name[5:]}]({link(course / 'README.md', FORMATION)}) | {description} |")
    lines.extend(["", "## Percurso sugerido", "", "1. **Fundamentos de dados e estatística (01–06):** entender o ciclo dos dados, programação e modelagem estatística.", "2. **Machine learning e deep learning (07–10):** construir, avaliar e operacionalizar modelos para dados estruturados e imagens.", "3. **Linguagem e modelos avançados (11–15):** estudar NLP, Transformers, geração, reforço, sentimentos e recomendação.", "4. **Formação humana (16):** analisar impactos éticos e sociais da tecnologia.", "", "## Convenções do acervo", "", "- Cada disciplina possui um README com objetivos, módulos, materiais e referências.", "- Cada módulo possui um índice próprio para páginas, PDFs, apresentações, notebooks, códigos, dados e imagens.", "- `ANOTACOES.md` preserva os resumos pessoais que já existiam.", "- `html/` mantém a versão original recebida do Canvas; `paginas/` contém a versão Markdown para leitura.", "- `.canvas/manifest.json` registra a proveniência técnica dos arquivos coletados.", "- Provas e atividades não foram executadas nem respondidas pelo crawler.", "- Vídeos bloqueados pelo proprietário não fazem parte deste acervo; os demais materiais foram mantidos para compensar essa lacuna.", ""])
    FORMATION.joinpath("README.md").write_text("\n".join(lines), encoding="utf-8")
    unavailable_paths: set[Path] = set()
    for path in FORMATION.rglob("*"):
        if path.is_file() and canvas_placeholder(path):
            unavailable_paths.add(path)
    for pdf in sorted(FORMATION.rglob("*.pdf")):
        if pdf_pages(pdf) == -1:
            unavailable_paths.add(pdf)
    unavailable = ["# Materiais indisponíveis", "", "Estes arquivos foram entregues pelo Canvas como respostas de processamento ou conteúdos inválidos, embora mantenham a extensão original do anexo. Eles foram preservados para rastreabilidade e devem ser coletados novamente quando o Canvas disponibilizar o conteúdo real.", "", f"Total: **{len(unavailable_paths)} arquivos**.", ""]
    unavailable.extend(
        f"- [{path.name}]({link(path, FORMATION)})" for path in sorted(unavailable_paths)
    )
    FORMATION.joinpath("MATERIAIS-INDISPONIVEIS.md").write_text("\n".join(unavailable) + "\n", encoding="utf-8")
    ROOT.joinpath("README.md").write_text("""# Pós-Graduação

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
""", encoding="utf-8")


if __name__ == "__main__":
    build()
