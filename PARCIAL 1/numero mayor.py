      
#Hacer un programa que: pida 5 números al usuario - los guarde en una lista - muestre el número mayor

""""

lista = []

for i in range(5):
    numero = int(input("Ingrese un número: "))
    lista.append(numero)

print("la lista es: ", lista)

mayor = 0

for i in range(len(lista)) :
    if lista[i] > mayor :
        mayor = lista[i]
print (mayor)

"""

# pida 5 números
# guarde en lista
# muestre solo los que son mayores a 10

"""
lista = []

for i in range(5):
    numero = int(input("Ingrese un número: "))
    lista.append(numero)

lista2 = []

for i in range(len(lista)) :
    if lista[i] > 10 :
       lista2.append(lista[i])

print (lista2)

"""        
# pida 5 números
# los guarde en una lista
# muestre el menor
# y cuente cuántos son mayores a 10
   
lista = []

for i in range(5):
    numero = int(input("ingrese un numero: ")) 
    lista.append(numero)
    
menor = lista[0]

for i in range(len(lista)) :
    if lista[i] < menor :
        menor = lista[i]
        
lista2 = []
        
for i in range(len(lista)) :
    if lista[i] > 10 :
        lista2.append(lista[i])
          
print ("el numero menor es: ", menor, ", y hay ", len(lista2), " numeros mayores a 10" )        