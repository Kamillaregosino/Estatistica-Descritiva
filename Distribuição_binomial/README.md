# Exemplo de uso da Distribuição Binomial

Uma empresa envia uma campanha de e-mail marketing para 1000 clientes. Com base em campanhas anteriores, sabe-se que a taxa média de clique é de 20%. Qual é a probabilidade exata de exatamente 210 pessoas clicarem no e-mail?

## Aplicando A distribuição Binomial

- Número de ensaios(n): 1000;
- Probabilidade de sucesso(p): 0.20;
- Número de sucessos(k): 210

## O que usar?

- Importar ``binom`` da biblioteca scipy.stats
- Definir o n, p e k
- Usar o parâmetro .pmf de binom para calcular a probabilidade exata. O ``pmf`` significa: função de massa de probabilidade, por isso usa-se binom.pmf(k, n, p).

# Como escolher intervalos de valores para k

- Média: n x p;
- Desvio Padrão: raíz quadrada de (n x p x (1 - p));
- Aproximações: média - 2 x desvio, média + 2 x desvio;
- O resultado oferece as probabilidades relevantes que estarão concentradas. É importante para visualizar bem a região útil da distribuição (onde a probabilidade não é quase zero).
