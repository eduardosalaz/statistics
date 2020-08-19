import matplotlib.pyplot
import numpy as np
# creo que es tampoco sirve pero no me acuerdo porque
# definimos una time series
ts = [12, 8, 9, 15, 12, 10, 18, 6, 8, 12, 10, 16, 12, 13, 9]
# definimos alfa
alpha = 0.3
# el primer valor del pronostico no existe

f = [np.nan, ts[0]]
f2 = [np.nan, ts[0]]

for t in range(1, len(ts) - 1):
    f2.append(f[-1] + alpha * (ts[t] + f[-1]))
# segundo pronostico es el primer valor en la ts
f.append(ts[0])
# se agregan los calculos
# for t in range(1, len(ts)-1):
#	f.append((1-alpha)*f[-1]+alpha*ts[t])
# se pasa a dataframe
import pandas as pd

# dic = {"demanda":ts,"pronostico":f}
dic2 = {"demanda": ts, "pronostico": f2}
# print(dic)
print(dic2)
results2 = pd.DataFrame.from_dict(dic2).round(0)
# results = pd.DataFrame.from_dict(dic).round(0)
# results.index.name = 'Periodo'
# results["error"] = results["demanda"] - results["pronostico"]
results2.index.name = 'Periodo'
results2["error"] = results2["demanda"] - results2["pronostico"]

# imprimir el df
# print(results)
print(results2)
# plotear los resultados
# results[["demanda", "pronostico"]].plot(title="Suavizamiento exponencial")
results2[["demanda", "pronostico"]].plot(title="Suavizamiento exponencial")

# obtener el MAEP mean absolute error percentage
# maep = abs(results["error"]).sum()/(results["demanda"].sum())
maep = abs(results2["error"]).sum() / (results2["demanda"].sum())
print("Mae: ", int(maep * 100), "%")
