import matplotlib.pyplot as plt
import random

vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range (10):
    numero_aleatório = random.randint(0, 5)
    vetor.append(numero_aleatório)

plt.boxplot(vetor)
plt.title("Boxplot")
plt.show()