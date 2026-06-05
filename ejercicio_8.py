
"""
def lista():
    lista1=[]
    cant=int(input("Cuantos numeros desea ingresar: "))
    for i in range(cant):
        num=int(input("Ingrese un numero: "))
        lista1.append(num)
    return lista1  


def inversa():
    L=lista()
    lista2=[]
    for i in range(len(L)-1,-1,-1):
        lista2.append(L[i])

    return lista2
print(inversa())
"""
"""
def matriz1():
    matriz=[]
    fila=int(input("Cuantos filas desea ingresar: "))
    columna=int(input("Cuantas columnas desea ingresar: "))
    for i in range(fila):
        l=[]
        for j in range(columna):
            num=int(input("Ingrese un numero: "))
            l.append(num)
        matriz.append(l)
    return matriz

m = matriz1()

def suma_filas(m):
    lista_suma=[]
    for i in range(len(m)):
        sum=0
        matriz2=m[i]
        for j in range(len(matriz2)):
            sum+=matriz2[j]
        lista_suma.append(sum)
    return lista_suma


print(suma_filas(m))

def suma_columnas(m):
    lista2_suma=[]
    for i in range(len(m[0])):
        sum=0
        for j in range(len(m)):
            sum+=m[j][i]
        lista2_suma.append(sum)
    return lista2_suma


print(suma_columnas(m))
"""