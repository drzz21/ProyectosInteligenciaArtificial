datosa=(0,0,1,1)
datosb=(0,1,0,1)
pesos = (-10, 20, 20)

print('g({} + ({} * x1) + ({} * x2)'.format(pesos[0], pesos[1], pesos[2]))
print('')

for a in datosa:
    for b in datosb:
        res = pesos[0] + (20 * a + (20 * b))
        print('g(-10+20*['+str(a)+']+20*['+str(b)+']) = '+str(res))
        
        if res<0:
            print('por lo tanto es 0')
            print('')
        else:
            print('por lo tanto es 1')
            print('')
