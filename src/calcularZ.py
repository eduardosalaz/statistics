from scipy import stats


def calcZ(x, miu, sigma):
    z = (x - miu) / sigma
    return z


x = 75
miu = 90
sigma = 22
valZ = calcZ(x, miu, sigma)
print(stats.norm.sf(abs(valZ)))
