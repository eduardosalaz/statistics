from numpy import genfromtxt
import pandas as pd

muestra = genfromtxt('valores.csv', delimiter=',')
# muestra = [1, 2, 3, 7, 9]
ventana_size = 3

serie = pd.Series(muestra)
ventanas = serie.rolling(ventana_size)
medias_moviles = ventanas.mean()

lista_medias_moviles = medias_moviles.tolist()

print(lista_medias_moviles)
