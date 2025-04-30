import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

# Parâmetros: intervalo de 14 a 16 (2 horas)
a = 14  
b = 16  

# Criar valores de tempo (em horas)
x = np.linspace(a, b, 1000)
pdf = uniform.pdf(x, loc=a, scale=b-a)

# Gráfico
plt.figure(figsize=(8, 4))
plt.plot(x, pdf, label='Distribuição Uniforme', color='blue')
plt.fill_between(x, pdf, alpha=0.3)
plt.title('Distribuição Uniforme - Horários de Agendamento')
plt.xlabel('Horário (h)')
plt.ylabel('Probabilidade')
plt.grid(True)
plt.legend()
plt.show()
