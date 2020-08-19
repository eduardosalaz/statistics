from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

media = 90
desviacion = 22

x_1 = np.linspace(stats.norm(media, desviacion).ppf(0.01), stats.norm(media, desviacion).ppf(0.99), 100)
FDP_normal = stats.norm(media, desviacion).pdf(x_1)
plt.plot(x_1, FDP_normal, label='FDP nromal')
plt.ylabel('prob')
plt.xlabel('valores')
px = np.arange(75, 90, 0.01)
plt.fill_between(px, stats.norm(media, desviacion).pdf(px), color='r')
plt.savefig('norm.png')
plt.show()
