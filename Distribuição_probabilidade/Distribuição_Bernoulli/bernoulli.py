import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

# Função para simular a distribuição de Bernoulli
def simular_bernoulli(p, n):
    """
    Simula a distribuição de Bernoulli com probabilidade p e n experimentos.
    
    Parâmetros:
    - p: Probabilidade de sucesso (0 ≤ p ≤ 1)
    - n: Número de experimentos
    
    Retorna:
    - Um gráfico mostrando a distribuição de 0s e 1s.
    """
    # Gerando amostras
    samples = bernoulli.rvs(p, size=n)

    # Contagem de sucessos e fracassos
    unique, counts = np.unique(samples, return_counts=True)

    plt.bar(unique, counts, tick_label=["Fracasso (0)", "Sucesso (1)"])
    plt.title(f"Distribuição de Bernoulli (p={p}, n={n})")
    plt.ylabel("Frequência")
    plt.show()

# Simulando com p=0.7 e n=10000
simular_bernoulli(0.7, 10000)
