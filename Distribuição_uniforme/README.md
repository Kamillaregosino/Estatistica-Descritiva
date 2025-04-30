# Exemplo de uso da Distribuição Uniforme

Existe um sistema de agendamento, e os horários disponíveis são entre 14h e 16h. O cenário é simular a distribuição de chegada dos usuários, supondo que cada horaário nesse intervalo tem a mesma chance de ser escolhido. 

## O que usar?

- Importar uniform de scipy.stats
- Criar 1000 pontos igualmente espaçados entre 14 e 16
- Calcular a pdf(função densidade de probabilidade): uniform.pdf(x, loc=a, scale=b-a), loc=a -> define o início, scale=b-a -> define a largura do intervalo, nesse caso vai ser 2, e o x -> retorna o valor da densidade para cada ponto em x.