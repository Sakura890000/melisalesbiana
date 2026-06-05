"""def contar_vocales(cadena):
    cont=0
    for i in cadena:
        if i in "aeiou":
            cont+=1
    return cont
if __name__=="__main__":
    palabra=input("ingrese la palabra-> ")
    cantidad = contar_vocales(palabra)
    print("la palabra tiene ", cantidad, " vocales")

def invertir_lista(lista):
    lista[::-1]
"""
"""
def sumar_elementos(matriz):
    suma=0
    for fila in matriz:
        for elemento in matriz:
            suma+=elemento
    return suma
"""
"""
matriz=[[1,2,3],
        [4,5,6],
        [7,8,9]]

#funcion que retorne el mayor, el menor y el promedio
def encontrar_mayor(A):
    mayor=A[0]
    for i in A:
        if i>mayor:
            mayor=i
    return mayor

def encontrar_menor(A):
    menor=A[0]
    for i in A:
        if i<menor:
            menor=i
    return menor

def prom(A):
    suma=0
    for i in A:
        suma+=i

    return suma/len(A)

def menor_mayor_prom(A):
    mayor=encontrar_mayor(A)
    menor=encontrar_menor(A)
    promedio=prom(A)

    return mayor,menor,promedio


if __name__=="__main__":
    A=[1,2,3,4,5,6,7,8,9]
    m, me, pro=menor_mayor_prom(A)
    print("el mayor es: ",m," el menor es: ",me," el promedio es: ", pro)

"""
    ###listas por comprension
numeros=[1,2,3,4,5,6,7,8,9]
pares=[n for n in numeros if n%2 ==0 ]
print(pares)