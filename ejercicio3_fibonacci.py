#RETO 1
def fibonacci(m):
    if m <= 0:
        return "ingrese un numero mayor a cero"
    elif m == 1:
        return[0]
    elif m == 2: 
        return[0,1]
    else:
        fib_squence = [0,1]
        for _ in range(2 , m):
            next_num = fib_squence[-1] + fib_squence[-2]
            fib_squence.append(next_num)
        return fib_squence
    
m = int(input("Ingrese el numero de elementos de la secuencia de fibonacci que desea mostrar: "))
resultado = fibonacci(m)
print(f"Los pirmeros {m} numero de la secuencia de fibonacci son {resultado}")