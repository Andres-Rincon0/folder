#RETO 1
import math

def es_numero_fibonacci(n):
    return (es_cuadrado_perfecto (5 * n * n + 4 ) or es_cuadrado_perfecto(5 * n * n - 4))

def es_cuadrado_perfecto(x):
    raiz = int(math.sqrt(x))
    return raiz * raiz == x

numero = int(input("ingrese el numero el numero entero para verificar si es un numero fibonacci: "))
if es_numero_fibonacci(numero):
    print(f"{numero} es un numero de la secuencia de fibonacci")
else:
    print(f"{numero} no es un numero de la secuencia de fibonacci") 