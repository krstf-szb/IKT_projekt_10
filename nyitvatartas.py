time = int(input('Hány óra van most?: '))

if (time >= 8 and time <= 16):
    print('A bolt nyitva van.')
    print('Ennyi idő van még zárásig:' , (16 - time))

else: 
    print('A bolt zárva van.')
    if time > 16 :
        print('Ennyi idő mulva nyit:' , (32 - time))
    else:
        print('Ennyi óra mulva lesz nyitva', (8 - time))