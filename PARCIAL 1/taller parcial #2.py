#Diseñe un algoritmo que lea una lista de n números enteros  
#e imprima cuántos son positivos, cuántos son negativos y cuántos son cero

"""
n = int(input("¿Cuántos números quiere ingresar?: ")) 

lista = []

for i in range(n):
    numero = int(input("Ingrese un número: "))
    lista.append(numero)

positivo = 0
negativo = 0
cero = 0

for i in lista :
    if i > 0 :
        positivo = positivo + 1
    elif i < 0 :
        negativo = negativo + 1
    else :
        cero = cero + 1

print ("hay ", positivo, "numeros positivos, ", negativo, "numeros negativos, ", cero, "numeros cero")
"""

#Diseñe un algoritmo que lea una lista de n números enteros y determine si la secuencia
#es no decreciente, es decir, si cada elemento es mayor o igual que el anterior.

"""
lista = []

n = int(input("cuantos numeros quiere que tenga la lista?: "))

for i in range(n) :
    numero = int(input("ingrese un numero para anadir a la lista: "))
    lista.append (numero)
    
contador = 0
for i in range(len(lista) -1 ) :
    if lista [i] > lista [i + 1] :
        contador = contador + 1
if contador == 0 :
    print ("la lista es no decreciente")
else :
    print ("la lista no es no decreciente")
"""


#Dada una lista de n enteros, cuente cuántos elementos son pares y mayores que 10.
"""   
lista = []
n = int(input("diga de que  tamano quiere que sea la lista: "))
for i in range(n) :
    numero = int(input("ingrese el numero que quiera agregar a la lista: "))
    lista.append (numero)


pares = 0
mayores = 0
for i in lista :
    if i % 2 == 0 and i > 10 :
        pares = pares + 1
  
print (pares)
"""

#Diseñe un algoritmo que reciba una lista de enteros e imprima el índice de la primera
#aparición del número mayor. Si el mayor aparece varias veces, se debe conservar el primer
#índice.

"""
lista = []
n= int(input("ingrese la cantidad de numeros que quiere que tenga su lista: "))
for i in range(n) :
    numero = int(input("ingrese un numero para su lista: "))
    lista.append (numero)
    
indice = 0
for i in range(len(lista) -1 ) :
    if lista[i] < lista[i+1] :
        indice = i+1

print (indice)

"""

#Diseñe un algoritmo que lea una lista y determine si existe al menos un par de elementos
#consecutivos iguales.

"""
lista = []
n = int(input("ingresse la cantidad de numeros que quiere que tenga su lista: "))

for i in range(n) :
    numero = int(input("ingrese un valor para su lista: "))
    lista.append (numero)
    
valor = 0
for i in range(len(lista) -1) :
    if lista[i] == lista[i+1] :
       valor = valor + 1
       
if valor == 0 :
    print ("no existe ninguna pareja de numeros conseccutiva.")
else :
    print ("existe al menos una pareja de numeros consecutiva.")
    
"""


