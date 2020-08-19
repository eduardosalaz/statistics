import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.regressionplots import influence_plot

# importante el ultimo import
# leer dataset
df = pd.read_csv('../csv/longley.csv', index_col=0)
# print(df.head())
# aplicar api de statsmodels
est = smf.ols(formula='Employed ~ GNP', data=df).fit()
print(est.summary())
# analisis de minimos cuadrados ordinarios
# separar ejes
y = df.Employed
x = df.GNP
x = sm.add_constant(x)
# agregamos constante para usarlo como un valor multiplicativo, el predict ocupa para
# saber cuantas veces se va a recalcular
# regresion
x_1 = pd.DataFrame({'GNP': np.linspace(x.GNP.min(), x.GNP.max(), 100)})
# para agarrar intervalos ocupas la constante en el dataframe original
x_1 = sm.add_constant(x_1)
# crear un df con los datos de GNP para poder usarlos
# print(x_1)
y_pron = est.predict(x_1)
plt.scatter(x.GNP, y, alpha=0.3)  # alpha es la separacion entre los puntos
plt.ylim(30, 100)  # acotar la grafica
plt.xlabel('PIB')
plt.ylabel('Tasas de Empleo')
plt.title('Ajuste de Regresion')
plt.plot(x_1.GNP, y_pron, 'r', alpha=0.9)
plt.savefig('../out/lineal_simple_gdp.png')
plt.show()
inf = influence_plot(est)
inf.savefig('../out/influencia.png')
inf.show()

# estadistica descriptiva
# apalancamiento y residuales, grafico de influencia, tamaño de los circulos
