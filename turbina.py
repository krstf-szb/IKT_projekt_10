turbina_szamlalo = 1
minden_turbina = 25
turbina_teljesitmeny = 2000
full_teljesitmeny = 0

while turbina_szamlalo <= minden_turbina:
    if turbina_szamlalo <= 10:
        full_teljesitmeny += turbina_teljesitmeny
        print(f'A(z) {turbina_szamlalo}. számú szélturbina teljes fordulaton működik, 2000MWh-t termelve.')

    elif turbina_szamlalo <= 20:
        full_teljesitmeny += turbina_teljesitmeny/2
        print(f'A(z) {turbina_szamlalo}. számú szélturbina fél fordulaton működik, 1000MWh-t termelve.')

    else:
        print(f'A(z) {turbina_szamlalo}. számú szélturbina nem működik, 0MWh-t termel.')
    
    turbina_szamlalo += 1

print(f'Az össz termelés: {full_teljesitmeny}MWh.')
    