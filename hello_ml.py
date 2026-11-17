import numpy as np

x = np.array([1.0, 2.0, 3.0, 4.0])
w = 2.0
b = 1.0

y = w * x + b
print("Entradas:", x)
print("Previsoes (y = w*x + b):", y)
print("Versao do NumPy:", np.__version__)
