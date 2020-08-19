from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# densidad probabilidad
media = 90
desviacion = 22.0
x_1 = np.linspace(stats.norm(media, desviacion).ppf(0.01), stats.norm(media, desviacion).ppf(0.99), 100)
FDP_normal = stats.norm(media, desviacion).pdf(x_1)  # fdp en ingles
plt.plot(x_1, FDP_normal, label='FDP normal')
plt.title('Funcion de densidad de probabilidad')
plt.ylabel('Probabilidad')
plt.xlabel('Valores')
plt.show()
plt.savefig('../out/normal.png')
