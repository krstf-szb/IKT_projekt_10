#format string használata:
import random


var=input('Add meg a neved: ')
print(f'Szia {var}')


#for ciklus
for _ in range(100):
    #Számol 0->99
    #Valamit meg kell csinálni 100x
	print('Peti')

#for ciklus
for x in range(100):
	print(f'{x}. sor')

for x in range(10,21):
	print(f'{x}. sor')


#lista
db=3
nevek = ['']*db

for i in range(db):
    nevek[i]=input('név: ')

print(nevek)

#lista2
szinek=['piros','kék','cigány']
print(szinek[random.randint(0,3)])
print(random.choice(szinek))


#while
szamlal=1

while szamlal<100:
    szamlal+=1
    print(szamlal)