from math import sqrt,fsum

archivo = open("hola.txt", "r")
data = archivo.read()
archivo.close()

datab=data.split(",")
datac=[]

listaparamedia=[1525, 257, 378, 9543, 7854, 152]

#media
print 'Media de 1525, 257, 378, 9543, 7854, 152'
print 'Media:', sum(listaparamedia)/len(listaparamedia)
print ''

for i in datab:
    datac.append(int(i))

ordenado=sorted(datac)

longitud=len(ordenado)
middle=longitud/2


#mediana
print 'Mediana de',data
if longitud%2==0:
    mediana=(ordenado[middle-1] + ordenado[middle]) / 2
else:
    mediana = ordenado[middle + 1]


print 'Mediana: ', mediana
print ''


#moda
repetir = 0
for i in datac:
    aparece = datac.count(i)
    if aparece > repetir:
        repetir = aparece

moda = []
for i in datac:
    aparece = datac.count(i)
    if aparece == repetir and i not in moda:
        moda.append(i)

print 'Moda de ',data
print "Moda:", moda
print ''

#varianza
listaparavarianza=[13, 14, 15, 15, 15, 16, 17, 18, 20]
print 'Varianza de 13, 14, 15, 15, 15, 16, 17, 18, 20'
mv1=fsum(listaparavarianza)
mv2=len(listaparavarianza)
medvar=mv1/mv2

lista2=[]

for m in listaparavarianza:
    lista2.append((m-medvar)**2)


div= (len(lista2)-1)**-1
varianzaa=fsum(lista2)*div
print varianzaa

print 'Desviacion estandar de 13, 14, 15, 15, 15, 16, 17, 18, 20'
desv=sqrt(varianzaa)
print desv

