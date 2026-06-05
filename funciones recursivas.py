def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
#enesimo numero de fibonacci
def fibonacci(n):
    if n == 9:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
#funcion recursiva para sumar los digitos de un numero
def sumar_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumar_digitos(n // 10)

print(sumar_digitos(4351))
