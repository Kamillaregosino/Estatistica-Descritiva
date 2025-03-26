import numpy as np

dados = np.random.binomial(n=1, p=0.3, size=1000)

print(f"Frequência de 1's: {np.sum(dados)} / 1000")
