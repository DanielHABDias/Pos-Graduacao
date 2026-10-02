# Unidade 3 - 4. Testes Automatizados

- Origem: [Canvas](https://pucminas.instructure.com/courses/230797/pages/unidade-3-4-testes-automatizados)

![](../images/banner-pos-2023.jpg)

---

#### **Automatização**

A automatização é a utilização de tecnologias e ferramentas para automatizar processos e tarefas que antes eram realizados manualmente. Pode ser aplicada em diversas áreas, como desenvolvimento de software, infraestrutura, operações, marketing, finanças, entre outras. Tem como objetivo aumentar a eficiência e a produtividade, reduzir erros e custos, além de liberar os profissionais para se concentrarem em tarefas mais estratégicas e de maior valor agregado. A automatização pode ser realizada por meio de scripts, ferramentas de integração contínua e entrega contínua (CI/CD), robôs, inteligência artificial, entre outras tecnologias.

Assista o vídeo a seguir abordando testes:

#### **Testes automatizados**

Testes automatizados são testes de software que são executados automaticamente por meio de ferramentas e scripts, sem a necessidade de intervenção humana. Esses testes são utilizados para garantir que o software está funcionando corretamente e que as alterações realizadas no código não causaram efeitos colaterais indesejados.

Os testes automatizados podem ser realizados em diferentes níveis, como testes unitários, testes de integração, testes de aceitação, entre outros. Eles podem ser executados em diferentes momentos do ciclo de vida do software, como durante o desenvolvimento, antes do lançamento ou após a implantação.

Entre as vantagens dos testes automatizados, estão a redução de erros, a melhoria da qualidade do software, a documentação dos cenários esperados e dos tratamentos em caso de erro, a economia de tempo e recursos, entre outras.

**Testes em scripts de treinamento**

Testes em scripts de treinamento são testes automatizados que verificam a corretude e a consistência do código relacionado ao treinamento de modelos de *machine learning*. Esses testes são projetados para testar partes específicas do código do modelo e ajudam a garantir que o código esteja implementado corretamente e que os resultados produzidos pelo modelo sejam precisos e confiáveis.

Os testes em scripts de treinamento podem ser usados para validar as saídas do modelo em diferentes cenários e permitem ter confiança na qualidade do código e nos resultados produzidos. Eles são uma parte importante do processo de desenvolvimento de modelos de *machine learning* e ajudam a garantir que o modelo esteja funcionando corretamente antes de ser implantado em produção.

O `pytest` é uma ferramenta muito útil para escrever e executar testes em Python. Ele facilita a automação de testes e a organização de casos de teste. A seguir serão apresentados alguns passos básicos para usar o `pytest` e testar scripts de treinamento.

1. Se ainda não tem o pytest instalado, pode instalá-lo usando o pip: `pip install pytest`
2. Crie um arquivo chamado `test_treinamento.py` dentro do diretório de testes. Neste arquivo, você escreverá os testes para o seu script de treinamento.
3. No terminal, navegue até o diretório raiz do seu projeto e execute o comando: `pytest`
4. O pytest irá procurar por arquivos que começam com `test_` ou terminam com `_test.py` e executará os testes contidos neles. Se tudo estiver configurado corretamente, você deverá ver a saída dos testes no console.

Dicas adicionais:

- Use `assert` para verificar se o resultado retornado pela função de treinamento é o que você espera.
- Você pode escrever vários testes diferentes para diferentes cenários e casos de borda.
- Considere usar dados de teste reais ou gerados aleatoriamente para testar diferentes situações.
