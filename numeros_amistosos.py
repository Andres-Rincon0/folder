#RETO 3
def suma_div(numero):
    suma = 1
    i = 2
    while i * i <= numero:
        if numero % i == 0:
            suma += i
            if i != numero // i:
                suma += numero // i
        i += 1
    return suma 

def encontrar_pares(rango_inf, rango_sup):
    pares_amg = []
    for m in range(rango_inf, rango_sup):
        n = suma_div(m)
        if suma_div(n) == m and n != n:
            encontrar_pares.append((m , n))
    return pares_amg

rango_inf = 1000
rango_sup = 1500
pares_encontrados = encontrar_pares(rango_inf, rango_sup)

if pares_encontrados:
    print("Los pares de numeros amigables en el rango [1000 , 1500] son: ")
    for par in pares_encontrados:
        print(par)

    else: 
        print("No se encontraron pares en el rango [1000, 1500]")