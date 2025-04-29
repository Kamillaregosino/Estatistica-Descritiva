# Exemplo de uso da Distribuição Normal

## Problema

Uma fábrica produz lâmpadas com vida útil média de 1000 horas e desvio padraão de 50 horas. Suponha que a vida útil siga uma distribuição normal. Aqui será interessante usar essa distribuição, pois é um fenômeno natural com variação.

## Responder as perguntas

- Qual a probabilidade de uma lâmpada durar menos de 940 horas?

- Qual a proporção de lâmpadas que durarão entre 950 e 1050 horas?

- Quantas lâmpadas, em um lote de 10.000, você espera que durem mais que 1100 horas?

## O que usar para resolver o problema

- Biblioteca scipy.stats do Python

- usar função de distribuição acumulada da biblioteca (cdf)

## Respondendo as perguntas

**Durar menor de 940 horas**: P(x <= 940) : .cdf(940, media, desvio)

**Durar entre 950 e 1050**: P(950 <= X <= 1050) : .cdf(1050, media, desvio) - .cdf(950, media, desvio)

**Em um lote de 10.000, quantas duram mais de 1100 horas?**: 1 - P( x <= 1100) : 1 - cdf(1100, media, desvio), depois multiplica por 10.000