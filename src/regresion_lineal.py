import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Cargar el dataframe

df = pd.read_csv('../csv/Salary_Data.csv')
x = df.iloc[:, :-1].values  # todas las filas, todas las columans hasta la penultima
y = df.iloc[:, 1].values  # todas las filas y la segunda columna

# print(df)

print(x)
print(y)

# dividr los datos en un subdataset de entrenamiento y otro de pruebas
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1 / 3, random_state=0)
# el subset de prueba será 1/3 del original
# random_state=0 para agarrar los valores continuos en la sucesión que vienen
# cargar el modelo de regresion lineal
regressor = LinearRegression()
# entrenar el modelo de regresion lineal en base a nuestros subsets
regressor.fit(x_train, y_train)

# probar con los subset de pruebas
y_pred = regressor.predict(x_test)

# comparar visualmente los resultados con una grafica de puntos de dispersion
plt.scatter(x_test, y_test, color='red')
plt.plot(x_test, y_pred, color='blue')
# una linea que une a todos los puntos
plt.title('Salario vs Experiencia (conjunto de prueba)')
plt.xlabel('Años de experiencia')
plt.ylabel('Salario')
# plt.show()
print(regressor.predict([[12]]))

nuevos_datos = [[12], [13], [14], [15], [16], [17], [18]]
nuevo_pronostico = regressor.predict(nuevos_datos)
plt.plot(nuevos_datos, nuevo_pronostico, color='m')
plt.savefig('../out/lineal_simple_salario.png')
plt.show()

errores = abs(y_test - y_pred)
maep = (errores.sum() / y_test.sum()) * 100
print(maep)
