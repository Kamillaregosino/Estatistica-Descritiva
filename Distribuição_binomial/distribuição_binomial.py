import matplotlib.pyplot as plt
from scipy.stats import binom
import numpy as np

# Parâmetros da distribuição
n = 1000
p = 0.20
k = 210

# Intervalo de valores para k
x = np.arange(180, 241)  
y = binom.pmf(x, n, p)   

# Gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'bo-', label='Distribuição Binomial')
plt.axvline(k, color='red', linestyle='--', label=f'k = {k}')
plt.title('Distribuição Binomial - Cliques em E-mails')
plt.xlabel('Número de cliques')
plt.ylabel('Probabilidade')
plt.legend()
plt.grid(True)
plt.show()
