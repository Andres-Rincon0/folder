def votos():
    cantidad_universidades = int(input("ingrese la cantidad de universidades que participan en el processo: "))

    votos_universidad = {"aceptar": 0, "rechazar":0, "nulo": 0, "blanco": 0}

    unis_aceptan = 0
    unis_rechazan = 0 
    unis_empate = 0  

    for i in range(cantidad_universidades):
        nombre_uni = input(f"ingrese el nombre de la universidad{i+1}: ")
        print(f"Ingrese los votos para la universidad {nombre_uni}:")
        while True: 
            voto = input("voto (A para aceptar, R para Rechazar, N para nulo, B para blanco, X para terminar").upper()
            if voto == 'X':
                break
            elif voto in ('A' , 'R', 'N', 'B'): 
                votos_universidad[voto.lower()] += 1

    print(f"\nTotal de votos para la universidad {nombre_uni}:")
    for voto, total in votos_universidad.items():
        print(f"Votos {voto}: {total}")

    if votos_universidad["aceptar"] > votos_universidad["rechazar"]:
        unis_aceptan += 1
    elif votos_universidad["rechazar"] > votos_universidad["aceptar"]:
        unis_rechazan += 1
    else:
        unis_empate += 1
    
    votos_universidad = {"aceptar": 0, "rechazar":0, "nulo": 0, "blanco": 0}

    print("\nResultado de la votacion: ")
    print(f"universidades que aceptan : {unis_aceptan}")
    print(f"universidades que rechazan {unis_rechazan}")
    print(f"Universidades con empate: {unis_empate}")

    votos()