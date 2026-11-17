import numpy as np

demanda = np.array([100, 150, 90, 160)]

demanda_aumentada = demanda * 1.10

print("Demanda original:", demanda)
print("Nova demanda:", demanda_aumentada)
print("Demanda média:", np.mean(demanda))