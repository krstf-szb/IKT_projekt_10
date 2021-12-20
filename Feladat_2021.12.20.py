import random


print('Feladat 1')

x = input('Jó napja van?(Igen/Nem): ')

if(x=='Igen'):
    print('Az fasza!')
elif(x=='igen'):
    print('Az fasza!')


elif(x=='Nem'):
    print('Az má nem fasza!')
elif(x=='nem'):
    print('Az má nem fasza!')


else:
    print('Sajnos nem értem a válaszod!')



print('Feladat 2')

x = int(input('Addjon meg egy számot: '))
if(x%2):
    print('A szám páratlan')
elif(x!=0):
    print('A szám páros')
else:
    print('A szám 0')



print('Feladat 3')

x = random.randint(1,6)

y = int(input('Adjon meg egy számot!: '))

if(x>y):
    print('A számod kissebb mint amire a gép gondolt.')
elif(x<y):
    print('A számod nagyobb mint amire a gép gondolt.')
else:
    print('A számod egyenlő a számmal amire a gép gondolt.')