import random

bekert_szamok=[]

for i in range(5):
    bekert_szamok.append(int(input(f'Add meg a(z) {i+1}. számot: ')))

huzas=0
while True:
    sorsolt_szamok = [random.randint(1,90) for _ in range(5)]

    szamlalo=0
    for data in bekert_szamok:
        if data in sorsolt_szamok:
            szamlalo+=1
            huzas+=1
    
    if szamlalo==4:
        print(f'Húzások: {huzas}')
        print(f'A sorsolt számok: {sorsolt_szamok}')
        print(f'A Te számaid: {bekert_szamok}')
        break