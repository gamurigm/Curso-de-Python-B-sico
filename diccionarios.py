def run():
    mi_dic = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3
    }

    print(mi_dic['llave1'])
    print(mi_dic['llave2'])
    print(mi_dic['llave3'])

    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 21047125,
        'Colombia': 50372424
    }

    # for pais in poblacion_paises.keys():
    #     print(pais)

    # for pais in poblacion_paises.values():
    #     print(pais)

    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene: ' + str(poblacion) + ' habitantes' ) 


if __name__ == "__main__":
    run()