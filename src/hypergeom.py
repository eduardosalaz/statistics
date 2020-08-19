from scipy.stats import hypergeom
import matplotlib.pyplot as plt
import numpy as np

[N, k, n] = [10, 2, 3]
rv = hypergeom(N, k, n)
x = np.arange(0, k + 1)
fusibles = rv.pmf(x)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, fusibles, 'bo')
ax.vlines(x, 0, fusibles, lw=2)
ax.set_xlabel('# Fusibles defectuosos')
ax.set_ylabel('# Probabilidad')
plt.show()
