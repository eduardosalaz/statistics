# creo que este no funciona tampoco
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.api import SimpleExpSmoothing

data = [25, 31, 26, 29, 29, 31, 31, 33, 35, 35, 37, 41, 69, 75, 80, 80, 82, 83, 88, 90, 102, 104, 109, 113, 114, 132,
        173, 182, 186, 197, 201, 212, 231, 258, 265, 283, 302, 320, 342, 350, 370, 387, 411, 427, 437, 467, 477, 501,
        521, 534, 548, 561, 572, 591, 613, 627, 639, 681, 724, 742, 795, 808, 843, 865, 898, 952, 1002, 1039, 1090,
        1112, 1147, 1190, 1221, 1267, 1316, 1363, 1406, 1479, 1572, 1653, 1747, 1877, 1980, 2083, 2173, 2274, 2369,
        2473, 2590, 2686, 2767, 2857, 2932, 3014, 3148, 3234, 3315, 3377, 3440, 3537, 3625, 3696, 3780]
index = pd.date_range(start='04/11/2020', end='07/22/2020')
data_guadalupe = pd.Series(data, index)
ax = data_guadalupe.plot()
ax.set_xlabel('Fecha')
ax.set_ylabel('Casos en Guadalupe')
print('Figura 1: Casos Acumulados en el municipio de Guadalupe')
fit1 = SimpleExpSmoothing(data_guadalupe).fit(smoothing_level=0.2, optimized=False)
fcast1 = fit1.forecast(7).rename(r'$\alpha=0.2$')
fit2 = SimpleExpSmoothing(data_guadalupe).fit(smoothing_level=0.4, optimized=False)
fcast2 = fit1.forecast(7).rename(r'$\alpha=0.4$')
fit3 = SimpleExpSmoothing(data_guadalupe).fit(smoothing_level=0.6, optimized=False)
fcast3 = fit1.forecast(7).rename(r'$\alpha=0.6$')
fit4 = SimpleExpSmoothing(data_guadalupe).fit(smoothing_level=0.8, optimized=False)
fcast4 = fit1.forecast(7).rename(r'$\alpha=0.8$')

ax = data_guadalupe.plot(marker='o', color='black', figsize=(12, 8))
fcast1.plot(marker='o', ax=ax, color='blue', legend=True)
fit1.fittedvalues.plot(marker='o', ax=ax, color='blue')
fcast2.plot(marker='o', ax=ax, color='red', legend=True)
fit2.fittedvalues.plot(marker='o', ax=ax, color='red')
fcast3.plot(marker='o', ax=ax, color='green', legend=True)
fit3.fittedvalues.plot(marker='o', ax=ax, color='green')
fcast4.plot(marker='o', ax=ax, color='yellow', legend=True)
fit4.fittedvalues.plot(marker='o', ax=ax, color='yellow')

print(fit1.forecast(7))
print(fit2.forecast(7))
print(fit3.forecast(7))
print(fit4.forecast(7))
plt.show()
