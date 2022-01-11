print("2.feladat")

while True:

    valtozo = input("Melyik nap van?(Nagykezdő, ékezetek) :")

    try:
        if valtozo == "Hétfő":
            print("1. nap, hétköznap")
            break
        if valtozo == "Kedd":
            print("2. nap, hétköznap")
            break
        if valtozo == "Szerda":
            print("3. nap, hétköznap")
            break
        if valtozo == "Csütörtök":
            print("4. nap, hétköznap")
            break
        if valtozo == "Péntek":
            print("5. nap, hétköznap")
            break
        if valtozo == "Szombat":
            print("6. nap, hétvége")
            break
        if valtozo == "Vasárnap":
            print("7. nap, hétvége")
            break
        else:
            print("Szarul írtad! Írjad újra!")
    
    
    
    except Exception:
        print("error")