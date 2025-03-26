# Funções Discretas

Uma função discreta é uma função matemática cujo domínio (conjunto de entrada) e/ou imagem (conjunto de saída) é um conjunto discreto, ou seja, composto por valores isolados e contáveis, como números inteiros ou categorias.

## Usos em Machine Learning

- Classificação: a saída do modelo pertence a um conjunto finito de classes;
- Funções de ativação discretas: como a função ``step function`` usada em perceptrons;
- Distribuições discretas de probabilidade: como a distribuição de Bernoulli ou Poisson;
- Modelos baseados em contagens: como Naive Bayes e Decision Trees.

## Exemplos de funções

**Step Function**: Retorna apenas dois valores, dependendo da entrada x. f(x) = 1 se x >= 0, e f(x) = 0 se x < 0. Essa função é usada no Perceptron. É usado como uma função de ativação para tomar decisões binárias. A função tem suas limitações, ela não resolve problemas não lineares.

**Função Indicadora**: define se um elemento pertence a um subconjunto A: IA(x) = 1, se x pertence à A, e IA(x) = 0, se x não pertence à A. Usa-se essa ideia em ``Árvores de decisão e Regras de Classificação``.

## Aplicações em Machine Learning

- Classificação com variáveis discretas: Em problemas de classificação, a saída do modelo 'discreta. Um exemplo é um modelo que prevê a categoria de um cliente. Com isso, usa-se técnicas como Árvores de decição, Naive Bayes e Redes Neurais para lidar com variáveis discretas.

- Modelos probabilísticos discretos: Distribuição de Bernoulli (evento binário, 'comprou', 'não comprou'). Distribuição de Poisson (contagem de eventos, 'quantas compras um cliente faz por mês').

