import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

# setear tamaño de figura y dimensiones
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
# estilo de ploteado
df = pd.read_csv('articulos_ml.csv')
# observar dimensiones y registros de los datos
print(df.iloc[:, 2:])  # imprime todas las filas y las columnas despues de la priemra
print(df.shape)
print(df.head())
# visualizar estadisticas de los datos
print(df.describe())
# visualizar caracteristicas de los datos de entrada
df.drop(['Title', 'url', 'Elapsed days'], 1).hist()  # ignora las columnas incluidas en el drop
# y plotealas en el histograma las demás
plt.savefig("../out/histograma_lineal.png")
plt.show()

# filtrar datos
df_filtrado = df[(df['Word count'] <= 3500) & (df['# Shares'] <= 80000)]
# print(df_filtrado)

colores = ['orange', 'blue']
tamanos = [30, 60]
f1 = df_filtrado['Word count'].values
f2 = df_filtrado['# Shares'].values
# asignar colores debajo o arriba de un criterio
asignar = []
for index, row in df_filtrado.iterrows():
    if (row['Word count'] > 1808):  # valor arriba del 50% percentil para asginar colores
        asignar.append(colores[0])
    else:
        asignar.append(colores[1])
# 1era grafica 
plt.scatter(f1, f2, c=asignar, s=tamanos[0])
# asignar datos de X para entrenamiento de Y
dataX = df_filtrado[['Word count']]
x_train = np.array(dataX)
y_train = df_filtrado['# Shares'].values
# instancia de regresion lineal
regL = linear_model.LinearRegression()

# entrenar el modelo
regL.fit(x_train, y_train)
# forecast
y_pron = regL.predict(x_train)  # no hay subset de prueba, se usara el de entrenamiento
# visualizar coeficiente de correlación
print("Coeficiente R: \n", regL.coef_)
# Y intersect
print("Termino independiente: \n", regL.intercept_)
# MSE
print("Error cuadrado medio: %.2f" % mean_squared_error(y_train, y_pron))
# Score de varianza 0<score<1
print("Score de Varianza: %.2f" % r2_score(y_train, y_pron))

plt.plot(x_train, y_pron, color='r')
plt.savefig("../out/regresion_lineal_simple.png")
plt.show()
# seria mejor un holt winters
print(int(regL.predict([[2000]])))

# REGRESION MULTIPLE LINEAL
# clasica = calcular pendiente y agregar n variables independientes y 1 variable dependiente
# resumida = agarrar la variable independiente que tenga mejor correlacion
# y agregar otra independiente que sea el recalculo de todos los demas factores
suma = (df_filtrado["# of Links"] + df_filtrado["# of comments"].fillna(0) + df_filtrado["# Images video"])
dataX2 = pd.DataFrame()
dataX2["Word count"] = df_filtrado["Word count"]
dataX2["suma"] = suma
# x y y seran variables independientes, Z la dependiente
# x numero de shares Y la suma de lso demas
XY_train = np.array(dataX2)
z_train = df_filtrado['# Shares'].values
# crear nuevo modelo de regresion lineal
regL2 = linear_model.LinearRegression()
# entrenar el nuevo modelo
regL2.fit(XY_train, z_train)
# No tenemos subdataset de pruebas entonces hacemos la prediccion para el set de entrenamiento para recalcular
z_pron = regL2.predict(XY_train)
# visualizar coeficiente de correlación
print("Coeficiente R: \n",
      regL2.coef_)  # inversamente proporcional ,POR ESO ES NEGATIVO, NO ES FIABLE EL RESULTADO DE LOS COMBINADOS
# no hay Y intersect
# MSE
print("Error cuadrado medio: %.2f" % mean_squared_error(z_train, z_pron))
# Score de varianza 0<score<1 que tan bueno es el pronostico
print("Score de Varianza: %.2f" % r2_score(z_train, z_pron))
fig = plt.figure()
ax = Axes3D(fig)
# crear malla donde se graficara
xx, yy = np.meshgrid(np.linspace(0, 3500, num=10), np.linspace(0, 60, num=10))
# calcular losd valores del plano para los puntos X y Y
nuevoX = (regL2.coef_[0] * xx)
nuevoY = (regL2.coef_[1] * yy)
# calcular valores para z y sumar el punto de intercepcion
z = (nuevoX + nuevoY + regL2.intercept_)
# graficar el plano
ax.plot_surface(xx, yy, z, alpha=0.2, cmap='hot')
# graficar los puntos en 3D
ax.scatter(XY_train[:, 0], XY_train[:, 1], z_train, c='blue',
           s=30)  # primero la word count, luego la suma luego los valores de entrenamiento
ax.scatter(XY_train[:, 0], XY_train[:, 1], z_pron, c='red', s=40)  # valores de pronostico
# situar camara
ax.view_init(elev=30, azim=65)  # elevacion y azimutal(angulo)
ax.set_xlabel('Cantidad de Palabras')
ax.set_ylabel('Cantidad de enlaces, comentarios e imagenes')
ax.set_zlabel('numero de compartidos')
ax.set_title('Regresion Lineal multiple')
plt.savefig("../out/regresion_lineal_multiple.png")
plt.show()
# ejemplo de como usar regresion multiple para pronosticar
print("Pronosticos")
print(int(regL2.predict([[2000, 10 + 4 + 6]])))
# predice la cantidad de shares con 2000 comentarios, 10 links, 4 comentarios y 6 imagenes
