#Punto 1
from statistics import median
from statistics import mean
from statistics import mode
from statistics import quantiles
datos=[8, 8, 13, 15, 16, 16, 16, 16, 24, 29, 30, 30, 49, 55, 55, 60]
print('La media de los datos es: ',mean(datos))
print('La mediana de los datos es: ',median(datos))
print('La moda de los datos es: ',mode(datos))
percentil=quantiles(datos, n=100)
print("El Percentil de los datos es:",percentil)


