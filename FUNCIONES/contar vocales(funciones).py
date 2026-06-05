"""

                                 ##contar vocales
def contar_vocales(cadena):   #SE DECLARO
    contador = 0
    for letra in cadena:
        if letra in "aeiou": ##
            contador += 1
                    
    return contador

                          #entry point

if __name__ =="__main__":
    
    palabra = input("ingrese la palabra")
    cantidad = contar_vocales(palabra)
    print("la palabra tiene ", cantidad, "vocales")
    
""" 

#corte

"""

                              ###invertir lista
def invertir_lista(lista):
    lista[::-1]
if __name__ =="__main__":
    lista = [1, 2, 3, 4, 5, 6,7 ,8 ,9]
    print (lista [2:5])

"""
    
#CORTE

"""

                             ##suma elementos de una matriz
def sumar_elementos(matriz):
    suma =0
    for fila in matriz:
        for elemento in fila: 
            suma += elemento 
    return suma

m = [[1, 4, 5, 7], [6, 8, 9, 3], [1, 0, 4, 8]]
print(sumar_elementos(m))

"""

#CORTE

"""

                            ##funcion que retoren el mayor, menor y el promedio de una lista
def encontrar_mayor(A):
    mayor = A[0]
    for n in A:
        if n > mayor:
            mayor = n
            
    return mayor
def encontrar_menor(A):
    menor = A[0]
    for n in A:
        if n < menor:
            menor = n
    return menor

def encontrar_prom(A):
    resultado = 0
    for i in A:
        resultado += i
    return resultado/len(A)

def menor_mayor_prom(A):
    menor = encontrar_menor(A)
    mayor = encontrar_mayor(A)
    prom = encontrar_prom(A)
    
    return menor, mayor, prom

if __name__ =="__main__":
    m = [1, 4, 5, 7, 6, 8, 9, 3, 10, 4, 8]
    menor, mayor, prom = menor_mayor_prom(m)
    print("el menor es: ", menor)
    print("el mayor es: ", mayor)
    print("el promedio es: ", prom)
    
"""
    
    
