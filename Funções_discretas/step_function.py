import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
    return np.where(x >= 0, 1, 0)

x = np.linspace(-5, 5, 100)
y = step_function(x)

plt.plot(x, y)
plt.title("Função Degrau")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()
