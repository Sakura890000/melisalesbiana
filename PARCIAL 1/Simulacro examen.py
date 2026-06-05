#Se pide un algoritmo que dada la hora ingresada como una cadena de la siguiente manera 2:03PM la transforme
#a formato 24 Horas asi 14:03
"""
hora = int(input("ingrese la hora: "))
minutos = int(input("ingrese los minutos: "))
dia = input("ingrese AM o PM: ")

for i in range(1, 12):
    if hora == i :
        if dia == "PM" :
            hora = hora + 12
    
print (hora,":",minutos)
"""
#Se pide un algoritmo que dada la hora ingresada como una cadena de la siguiente manera 2:03PM la transforme
#a formato 24 Horas asi 14:03
"""
hora = int(input("ingrese la hora: "))
minutos = int(input("ingrese los minutos: "))
dia = input("ingrese AM o PM: ")

if dia == "PM" and hora != 12:
    hora = hora + 12
elif dia == "AM" and hora == 12:
    hora = 0

print(hora, ":", minutos)
"""

#Escribe un programa que dada una secuencia de N enteros y un entero k, 
#reimprima la secuencia dada reemplazando los enteros que no son m´ultiplos de k por una X mayuscula.

"""
lista = []
n = int(input("ingrese la cantidad de numeros que quieres en tu lista: "))
for i in range(n) :
    numero = int(input("ingrese un numero de su lista: "))
    lista.append (numero)
    
k = int(input("de un valor para dividirlo con su lista: "))
for i in range(len(lista)) :
    if lista[i] % k != 0 :
        lista[i]= "X"
for i in lista:
    print(i, end=" ")   
"""
#Escribir un programa que pida al usuario un n´umero entero y muestre por pantalla un tri´angulo
#rect´angulo como el siguiente.
#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1


n = int(input("Ingrese un número: "))

for i in range(1, n + 1):
    
    inicio = 2 * i - 1
    
    for j in range(inicio, 0, -2):
        print(j, end=" ")
    
    print()        
