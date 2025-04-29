from scipy.stats import norm


mu = 1000
sigma = 50

# Probabilidade de durar menos de 940 horas
p1 = norm.cdf(940, mu, sigma)

# Proporção entre 950 e 1050 horas
p2 = norm.cdf(1050, mu, sigma) - norm.cdf(950, mu, sigma)

# Quantas duram mais de 1100 horas em 10.000 lâmpadas?
p3 = 1 - norm.cdf(1100, mu, sigma)
qtd = int(p3 * 10000)

print(f"Prob. de durar < 940h: {p1:.2%}")
print(f"Prob. de durar entre 950h e 1050h: {p2:.2%}")
print(f"Número esperado de lâmpadas com > 1100h: {qtd}")
