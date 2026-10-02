# Unidade 3 - Desafio e Resolução

- Origem: [Canvas](https://pucminas.instructure.com/courses/230797/pages/unidade-3-desafio-e-resolucao)

![](../images/banner-pos-2023.jpg)

---

#### **Desafio 3 - Uso do MLflow com DagsHub**

**Enunciado**

Como podemos utilizar o pacote do MLflow em conjunto com DagsHub para monitorar o treino de um modelo de *Machine Learning*  

**Resolução**

Para integrar um treinamento de um modelo usando MLflow com a plataforma Dagshub, é importante primeiro garantir que o pacote Dagshub esteja devidamente instalado. Isso pode ser feito através do comando `pip install dagshub`.

Com o ambiente devidamente configurado para trabalhar com MLflow, inicie o processo de vinculação ao Dagshub. No script de treinamento onde o MLflow é utilizado, comece por inicializar um experimento no Dagshub utilizando o método `dagshub.init()`. Isso estabelece a conexão entre o ambiente de treinamento e a plataforma do Dagshub.

Em seguida, proceda com o treinamento do modelo, registrando parâmetros e métricas como de costume com o MLflow. O MLflow é uma ferramenta essencial para o rastreamento de experimentos, e sua integração com o Dagshub facilita a organização e visualização dos resultados.

Ao finalizar o experimento, certifique-se de encerrar tanto a execução no MLflow quanto no Dagshub. Utilize `mlflow.end_run()` para encerrar o experimento no MLflow e `dagshub.end()` para finalizar a execução no Dagshub.

Garanta que suas credenciais do Dagshub estejam devidamente configuradas através das variáveis de ambiente `DAGSHUB_USERNAME` e `DAGSHUB_API_KEY*`. Para obter as credenciais, crie uma conta no [DagsHub](https://dagshub.com).

Por fim, execute o script de treinamento normalmente. O Dagshub irá capturar e registrar os experimentos do MLflow na plataforma, proporcionando uma visão organizada e acessível dos resultados.

Ao seguir esses passos, você conseguirá vincular com facilidade o treinamento do seu modelo de Machine Learning com Scikit-learn e MLflow à plataforma Dagshub, permitindo um registro organizado e visualização dos experimentos na plataforma. Essa integração é valiosa para o gerenciamento eficiente de experimentos e resultados em projetos de machine learning.

**\*Resolução Adicional**

Para obter a sua `DAGSHUB_API_KEY`, siga os passos abaixo:

1. Acesse novamente o site do [Dagshub.](https://dagshub.com/ "Link")
2. Faça login na sua conta Dagshub ou crie uma nova conta se ainda não tiver uma.
3. Após fazer login, clique no seu avatar no canto superior direito da página e selecione "Settings" no menu suspenso.
4. Na página de configurações, vá para a seção "API & Keys".
5. Você encontrará a sua `DAGSHUB_API_KEY` listada lá. Clique no ícone de olho para revelá-la. Lembre-se de mantê-la em local seguro, pois é uma chave confidencial.
