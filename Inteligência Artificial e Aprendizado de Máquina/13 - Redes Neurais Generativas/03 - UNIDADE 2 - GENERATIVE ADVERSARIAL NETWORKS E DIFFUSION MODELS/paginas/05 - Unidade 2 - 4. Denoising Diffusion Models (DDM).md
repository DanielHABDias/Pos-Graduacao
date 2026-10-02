# Unidade 2 - 4. Denoising Diffusion Models (DDM)

- Origem: [Canvas](https://pucminas.instructure.com/courses/230806/pages/unidade-2-4-denoising-diffusion-models-ddm)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar o seguinte tópico:**

- Arquitetura e Funcionamento dos DDMs.

**Ao final, você será capaz de:**

- Reconhecer o processo de difusão direta e reversa e entender como os modelos de denoising aprendem a reconstruir dados a partir de ruído progressivo.

---

#### **Denoising Diffusion Models (DDM)**

Em nossa próxima videoaula, você irá compreender como funcionam os Denoising Diffusion Models (DDMs), uma das arquiteturas mais avançadas e estáveis para geração de imagens. Você verá que esses modelos se baseiam em um processo simples, porém extremamente poderoso: começar com uma imagem totalmente preenchida por ruído aleatório e, passo a passo, removê-lo até que surja uma imagem plausível e visualmente coerente com o conjunto de treinamento. Antes disso, o modelo aprende o processo inverso: como corromper gradualmente uma imagem real com pequenas quantidades de ruído gaussiano ao longo de centenas ou milhares de etapas. Esse ciclo direto é fundamental para que o modelo aprenda o caminho reverso — denoising — que, aplicado sobre ruído puro, permite gerar imagens inéditas e realistas.

Além disso, você irá explorar estratégias de difusão amplamente utilizadas, como o linear schedule e o cosine schedule, entendendo como diferentes ritmos de adição de ruído preservam ou aceleram a degradação da imagem durante o processo direto. Você também verá por que o treinamento do modelo é estruturado para prever o ruído adicionado em cada etapa, em vez de tentar reconstruir diretamente a imagem limpa. A videoaula ainda destaca a relação conceitual entre diffusion models e autoencoders variacionais, mostrando como ambos usam ruído e representações intermediárias, mas diferem na forma como o ruído é controlado e aprendido. Preparado(a) para entender o mecanismo por trás dos modelos que revolucionaram a geração de imagens? Então, assista à videoaula a seguir!
