# Unidade 2 - 5. U-Net Denoising Model

- Origem: [Canvas](https://pucminas.instructure.com/courses/230806/pages/unidade-2-5-u-net-denoising-model)

![](../images/banner-pos-2022-1.jpg)

---

#### **OBJETIVOS DA AULA**

**Nesta aula, vamos abordar o seguinte tópico:**

- Estrutura do U-Net para Denoising.

**Ao final, você será capaz de:**

- Identificar os componentes principais da arquitetura U-Net e compreender seu papel na remoção de ruído durante o processo de difusão.

---

#### **U-Net Denoising Model**

Na videoaula a seguir, você irá compreender como a arquitetura U‑Net se tornou um dos componentes fundamentais dos modelos de difusão modernos, graças à sua capacidade de capturar detalhes finos e reconstruir imagens com alta fidelidade. Embora originalmente criada para tarefas de segmentação médica, a U‑Net provou ser extremamente eficaz em problemas de reconstrução, restauração e remoção de ruído. Você verá como sua estrutura simétrica, composta por um encoder que reduz a resolução enquanto extrai características profundas e um decoder que expande essa representação, permite que o modelo recupere informações visuais com precisão impressionante.

Além disso, a videoaula explora o papel crucial dos skip connections e dos blocos residuais, elementos que permitem que detalhes de baixo nível fluam das camadas iniciais para as finais sem serem perdidos no caminho. Esses atalhos fazem com que o modelo aprenda apenas o “resíduo” que falta entre a entrada e a saída esperada, o que torna o processo de denoising mais estável e eficiente. Ao acompanhar o funcionamento dos down blocks e up blocks, você entenderá como a U‑Net equilibra profundidade e resolução, aumentando o número de canais ao comprimir a imagem e reduzindo‑os ao reconstruí-la. Vamos aprender como essa arquitetura se tornou o coração dos modelos de difusão e por que ela é tão poderosa em tarefas de geração de imagens? Dê o play e assista à videoaula!
