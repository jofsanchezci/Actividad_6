#Punto 2
import pandas as pd
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


d_c={'Azul':[azul,fr_a,F[0]],'Negro':[negro,fr_n,F[1]],
	'Amarrillo':[amarillo,fr_am,F[2]],
	'Rojo':[rojo,fr_r,F[3]],'Verde':[verde,fr_v,F[4]],
	'Blanco':[blanco,fr_b,F[5]],'Morado':[morado,fr_m,F[6]],
	'Rosado':[rosado,fr_ro,F[7]]}

#print(d_c)
print('--------------------------')
print('Tabla de Frecuencias')
for i in d_c.values():
	print(i)
print('--------------------------')




