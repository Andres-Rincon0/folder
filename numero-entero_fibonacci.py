#RETO 1
def fibonacci(n):
    if n <= 0:
        return "El numero debe ser mayor a cero."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a , b = 0 , 1
        for _  in range (2, n):
            a , b = b, a + b
            return b 
    n = int(input('ingrese un numero entero para encontrar su numero fibonacci'))
    resultado = fibonacci(n)
    print(f"el numero de fibonacci en la posicion {n} es: {resultado}") 