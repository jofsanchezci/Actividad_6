#Punto 2
import pandas as pd
import matplotlib.pyplot as plt
from statistics import median
from statistics import mean
from statistics import mode
from statistics import quantiles
df = pd.read_excel('datos_C.xlsx',sheet_name='Hoja1')
datos=list(df['id'])

def contar(n, vec):
  '''Para esta funcion n es el numero a contar y vec es la lista donde contar '''
  count=0
  for i in vec:
    if i==n:
      count+=1
  return count

azul=contar('Azul', datos)
negro=contar('Negro',datos)
amarillo=contar('Amarillo', datos)
rojo=contar('Rojo',datos)
verde=contar('Verde',datos)
blanco=contar('Blanco',datos)
morado=contar('Morado',datos)
rosado=contar('Rosado',datos)
lista_colores=[azul,negro,amarillo,rojo,verde,blanco,morado,rosado]

#Frecuencia relativa
fr_a=azul/sum(lista_colores)
fr_n=negro/sum(lista_colores)
fr_am=amarillo/sum(lista_colores)
fr_r=rojo/sum(lista_colores)
fr_v=verde/sum(lista_colores)
fr_b=blanco/sum(lista_colores)
fr_m=morado/sum(lista_colores)
fr_ro=rosado/sum(lista_colores)


F=[lista_colores[0]]
acum=F[0]
for i in range(1,len(lista_colores)):
  acum+=lista_colores[i]
  F.append(acum)
#print(F)
print('El promedio de la lista es: ',mean(lista_colores))
print(lista_colores)
#Grafica
plt.boxplot(lista_colores,vert=False,patch_artist=True);
plt.title("Diagrama de Caja")
plt.show()









