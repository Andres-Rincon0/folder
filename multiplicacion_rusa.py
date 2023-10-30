#RETO 2
def mult_rusa(multiplicador, multiplicando):
    resultado = 0
    while multiplicador > 0:
        if multiplicador % 2 != 0:
            resultado += multiplicando
        multiplicador //= 2
        multiplicando *= 2
    return resultado

multiplicador = int(input("ingrese el multiplicador: "))
multiplicando = int(input("ingrese el multiplicando: "))

resultado = mult_rusa(multiplicador, multiplicando)
print(f"el producto de {multiplicador} y {multiplicando} es: {resultado}")