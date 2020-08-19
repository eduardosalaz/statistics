from scipy import stats
import numpy as np
from prob140 import Table
from prob140 import Plot

# distribucion binomial ploteada

n = 4
p = 3 / 4
k = np.arange(n + 1)
binom_4_dist = stats.binom.pmf(k, n, p)
binom_4_dist_graph = Table().values(k).probabilities(binom_4_dist)
Plot(binom_4_dist_graph)
