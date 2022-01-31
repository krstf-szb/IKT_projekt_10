busz_szamlalo = 1

while busz_szamlalo <= 10:
    if busz_szamlalo <=7:
        print(f'A(z) {busz_szamlalo}. busz üzemképes, sofőrre vár.')
    else:
        print(f'A {busz_szamlalo}. busz nem üzemképes, szervizre vár.')
    busz_szamlalo += 1