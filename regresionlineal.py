tablax=[5,15,20,25]
tablay=[375,487,450,500]
producto=[]
cuadrados=[]
index=0
index2=0
print '| x  |  y  |'
print '| 5  | 375 |'
print '| 15 | 487 |'
print '| 20 | 450 |'
print '| 25 | 500 |'

for a in tablax:
    #print tablax[index]*tablay[index]
    producto.append(tablax[index] * tablay[index])
    index=index+1

        #print (tablax[a])*(tablay[a])
for b in tablax:
    #print tablax[index2]**2
    cuadrados.append(tablax[index2]**2)
    index2=index2+1

sumx= sum(tablax)
sumy= sum(tablay)
sump= sum(producto)
sumc= sum(cuadrados)

despejem1=(sump-((sumx*sumy)/len(tablax)))
despejem2=sumc-((sumx)**2/len(tablax))

pendiente= despejem1/despejem2
print '___________'
print ''
print 'Pendiente: ',pendiente

despejeb=sumy/len(tablax)-(pendiente)*sumx/len(tablax)
print 'Interseccion:',despejeb

pronostico=despejeb+(pendiente*35)
print 'Pronosticco para una casa de 35 metros: ',pronostico