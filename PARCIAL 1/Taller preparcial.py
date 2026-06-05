#Diseñe un algoritmo que lea un número entero e indique si es positivo, negativo o cero.
#Justifique por qué el orden de las condiciones es suficiente.
"""
numero = int(input("ingrese un numero: "))

if numero > 0 :
    print ("el numero es positivo")
elif numero == 0 :
    print ("el numero es cero")
else: print ("el numero es negativo")
"""



#Diseñe un algoritmo que lea la edad de una persona e indique si es menor de edad, mayor
#de edad o adulto mayor. Defina claramente el rango de cada categoría.
"""
edad = int(input("digite su edad: "))

if edad < 18 : 
    print ("es menor de edad")
elif edad >= 18 and edad < 50 :
    print ("es un adulto")
elif edad >= 50 :
    print ("es un adulto mayor")

"""
#Lea tres números enteros e imprima el mayor de ellos. No use funciones predefinidas.


"""
n1 = int(input("digite un numero: "))
n2 = int(input("digite otro numero: "))
n3 = int(input("digite otro numero: "))

mayor = n1

if n2 > mayor :
    mayor = n2
if n3 > mayor :
    mayor =n3
    
print ("el numero mayor es", mayor)

"""

# Lea tres números enteros e indique si pueden representar los lados de un triángulo. Recuerde justificar la condición usada.
"""
l1 = int(input("ingrese una medida para el triangulo: "))
l2 = int(input("ingrese una segunda medida para el triangulo: "))
l3 = int(input("ingrese una tercera medida para el triangulo: "))

if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2 :
    print ("se forma el triangulo.")
else : print ("no se forma el triangulo")
"""

#Una tienda aplica la siguiente política:
#Si la compra es mayor o igual a 200.000, descuento del 15 %.
#Si la compra es mayor o igual a 100.000 y menor que 200.000, descuento del 8 %.
#En otro caso, no hay descuento.
#Diseñe un algoritmo que lea el valor de compra e imprima el valor a pagar.

"""
valor = int(input("ingrese el valor de compra: "))

if valor >= 200000 :
    valor = valor - valor *0.15
elif valor > 100000 :
    valor = valor - valor * 0.08
    
print("el valor final es: ", valor)
"""

#Diseñe un algoritmo que lea un número entero n y calcule la suma de los primeros n números naturales.\
  
  
"""  
n = int(input('ingrese un numero natural: '))

suma = 0
for i in range(1, n + 1) :
        suma = suma + i
print (suma)
"""

#Diseñe un algoritmo que lea un número entero n y determine cuántos divisores positivos tiene.

"""
n = int(input("ingrese un numero entero: "))


contador = 0
for i in range(1, n + 1) :
    if n % i == 0 :
        contador = contador + 1
    
    
print (contador)
"""

#Diseñe un algoritmo que determine si un número entero positivo es primo
"""
n = int(input("ingrese un numero entero: "))

contador = 0
for i in range(1, n + 1) :
    if n % i ==0 :
        contador = contador + 1

if contador == 2 :
    print ("el numero es primo")
else :
    print ("el numero no es primo")
"""

#Diseñe un algoritmo que lea un número entero positivo n y genere la secuencia: 1, 1, 2, 3, 5, 8, . . . hasta completar n términos.
"""

n = int(input("ingrese un numero: "))


primero = 1
segundo = 1

for i in range(n) :
    print (primero)
    suma = primero + segundo
    primero = segundo
    segundo = suma
    
"""
n = 5
while n <25 :
    print (n)
    n=n+5
