##Crea una función que reciba una lista de números.
##La función debe recorrer la lista con un for.
##Si encuentra un número mayor a 50, debe detenerse con break.
##Al final, devuelve cuántos elementos revisó usando len.

'''
def numeros(lista):
    contador = 0
    for i in (lista):
        if i > 50:
            break
        contador += 1
    return (contador)

if __name__ == "__main__":
    
    edades = [18, 22, 24, 28, 30, 38, 39, 39, 50, 55, 60]
    personas = numeros(edades)
    print (personas)

'''
#CORTE


##version que muestra que numero hizo detener el bucle

'''
def numeros(lista):
    contador = 0
    ruptura = None
    for i in (lista):
        if i > 50:
            ruptura = i
            break 
        contador += 1
    return contador, ruptura

if __name__ == "__main__":
    
    edades = [18, 22, 24, 28, 30, 38, 39, 39, 50, 55, 60]
    personas, stop = numeros(edades)
    print ("hay:", personas, "personas y la de edad:", stop, "detuvo el bucle")
'''

#CORTE

# - Reciba como argumento una matriz (lista de listas) y un límite.
# - Recorra la matriz usando dos bucles for anidados.
# - Cuente cuántos números se revisaron antes de encontrar el primer número mayor al límite.
# - Si encuentra un número mayor al límite, se detiene con break y devuelve:
# - El contador de elementos revisados.
# - El número que detuvo el bucle.
# - La posición (fila y columna) donde estaba ese número.
# - Si no encuentra ninguno mayor al límite, devuelve (contador, None, None).

'''
def buscar_mayor(matriz, limite):
    contador = 0
    mayor = None
    posicion = None
    for fila in range(len(matriz)):
        for col in range(len(matriz[fila])):
            contador += 1
            if matriz[fila][col] > limite:
               mayor = matriz [fila][col]
               posicion = (fila, col)
               break
        if mayor is not None:
            break
        
    return contador, mayor, posicion

if __name__ == "__main__":
    datos = [[10, 20, 30], [40, 50, 55], [60, 70, 80]]
    
elementos, ruptura, lugar = buscar_mayor(datos, 50)
print ("se revisaron", elementos, "elementos")
print ("se rompio el bucle con el numero:", ruptura)
print ("la ruptura estaba en la posicion:", lugar)
resultado = buscar_mayor(datos, 50)
print (resultado)
'''    
        
##CORTE

# Reciba una lista de números y un límite.
# Recorra la lista con un for.
# Use break si eneuentra un número mayor al límite.
# Devuelva cuántos números menores o iguales al límite se revisaron.
'''
def lista_n(lista, limite):
    contador = 0
    for i in lista:
        if i <= limite:
           contador += 1
        else: 
            break
    return contador

if __name__ == "__main__":
    numeros = [10, 20, 30, 55, 60]
    
revision = lista_n(numeros, 50)
print("se revisaron", revision, " elementos menores o iguales al limite")
'''       
        

#CORTE

# Crea una función llamada suma_matriz que:
# Reciba una matriz (lista de listas).
# Use bucles anidados for para recorrer todos los elementos.
# Devuelva la suma total de los números.

'''
def suma_matriz (matriz):
    suma = 0
    for i in matriz:
        for j in i:
            suma += j
    return suma

if __name__ == "__main__":
    matriz = [[1, 2], [3, 4]]
sumatoria = suma_matriz(matriz)
print(sumatoria)
'''      

#CORTE

# Crea una función llamada primer_par que:
# Reciba una lista de números.
# Use un bucle for para recorrerlos.
# Devuelva el primer número par que encuentre.
# Si no hay pares, devuelve None.
    
'''    
def primer_par(lista):
    n = 0
    for i in lista:
        if i % 2 == 0:
            n = i
            break
        if i % 2 != 0:
            n = None
        
    return n

if __name__ == "__main__":
    numeros = [1, 3, 5, 9]
par = primer_par(numeros)
print (par)
'''

#CORTE


# Crea una función llamada primer_par_matriz que:
# Reciba una matriz (lista de listas).
# Use bucles anidados para recorrer todos los elementos.
# Devuelva el primer número par que encuentre.
# Si no hay pares, devuelve None.

'''
def primer_par_matriz(matriz):
    n = None
    for i in matriz:
        for j in i:
            if j % 2 == 0:
                n = j
                break
    return n

if __name__ == "__main__":
    matriz = [[3, 7], [9, 11], [13, 11], [9, 11]]
    
par = primer_par_matriz(matriz)
print (par)
'''

#CORTAR

# Crea una función llamada contar_mayores_matriz que:
# Reciba una matriz y un límite.
# Recorra todos los elementos con bucles anidados.
# Devuelva cuántos números son mayores al límite.

'''
def contar_mayores_matriz(matriz, limite):
    mayor = 0
    for i in matriz:
        for j in i:
            if j > limite:
                mayor += 1
    return mayor

if __name__ == "__main__":
    matriz = [[1, 5], [10, 15], [20, 25]]
    
numeros = contar_mayores_matriz(matriz, 10)

print (numeros)
'''

#CORTE

# Crea una función llamada sumas_pares_impares que:
# Reciba una matriz.
# Recorra todos los elementos.
# Devuelva dos resultados: la suma de los pares y la suma de los impares.

'''
def sumas_pares_impares (matriz):
    par = 0
    impar = 0
    for i in matriz:
        for j in i:
            if j % 2 ==0:
                par += j
            else:
                impar += j
                
    return par, impar

if __name__ == "__main__":
    matriz = [[2, 3], [4, 5]]
    
pares, impares = sumas_pares_impares(matriz)

print("pares: ", pares)
print("impares: ", impares)
'''

#CORTE
   
# Inicializamos una variable maximo con un valor muy pequeño (por ejemplo, None o el primer elemento de la matriz).
# Guardamos también la posición (fila, columna) del número más grande.
# Recorremos la matriz con bucles anidados.
# Si encontramos un número mayor al actual maximo, lo actualizamos junto con su posición.
# Al final devolvemos el número y su posición.

'''
def maximo_matriz(matriz):
    maximo = matriz[0][0]          # empezamos con el primer elemento
    posicion = (0, 0)              # posición inicial
    
    for i in range(len(matriz)):          # recorre filas
        for j in range(len(matriz[i])):   # recorre columnas
            if matriz[i][j] > maximo:
                maximo = matriz[i][j]
                posicion = (i, j)
    
    return maximo, posicion

if __name__ == "__main__":
    matriz = [[3, 8, 2], [4, 15, 6], [7, 1, 9]]
    numero, pos = maximo_matriz(matriz)
    print("Número más grande:", numero)
    print("Posición (fila, columna):", pos)
'''

#CORTE

# Tienes una lista que representa un jardín, donde:
# 0 significa espacio vacío.
# 1 significa que ya hay una flor.
# La regla es que no puedes poner flores en espacios que estén justo al lado de otra flor.
# Crea una función llamada puede_plantar que:
# Reciba la lista del jardín y un número n (cantidad de flores que quieres plantar).
# Devuelva True si es posible plantar esas flores sin romper la regla, o False si no se puede.

'''
def puede_plantar(jardin, flores):
    contador = 0
    valor = False
    for i in range(1, len(jardin)-1):
        if jardin[i] == 0 and jardin[i-1] == 0 and jardin[i+1] == 0:
            jardin[i] = 1
            contador += 1
        if contador >= flores:
            valor =  True


    return valor

if __name__ == "__main__":
    lista = [1,0,0,0,1]


planta = puede_plantar(lista, 1)
print (planta)
planta = puede_plantar(lista, 2)
print (planta)
'''

#CORTE

# Imagina que tienes una matriz con temperaturas registradas 
# en diferentes días y horas.
# Crea una función llamada temperatura_maxima que:
# Reciba la matriz.
# Devuelva la temperatura más alta y su posición (día, hora).

'''
def temperatura_maxima (matriz):
    maximo = matriz[0][0]
    posicion = (0, 0)
    for dia in range(len(matriz)):
        for hora in range(len(matriz[dia])):
            if matriz[dia][hora] > maximo:
                maximo = matriz[dia][hora]
                posicion = (dia, hora)
                
                
    return maximo, posicion

if __name__ == "__main__":
    matriz = [[22, 25, 19], [30, 28, 27], [26, 29, 31]]

temperatura, fecha = temperatura_maxima(matriz)
 
print (temperatura, fecha)
'''

#CORTE
            
# Tienes una lista con las puntuaciones de un juego.
# Crea una función llamada ganador que:
# Reciba la lista de puntuaciones.
# Devuelva el valor más alto y cuántas veces aparece.           

'''
def ganador(lista):
    contador = 0
    alta = lista[0]
    for i in lista:
        if i > alta:
            alta = i
    for i in lista:
        if i == alta:
            contador += 1
            
    return alta, contador

if __name__ == "__main__":
    puntuacion = ([10, 20, 20, 15, 30, 30, 30])
    
maximo, veces =  ganador(puntuacion)

print (maximo, veces)
'''

#CORTE     

# Dada una lista de números, crea una función que devuelva cuántos son mayores a un límite.
'''
def numeros(lista, limite):
    contador = 0
    for i in lista:
        if i > limite:
            contador += 1
    return(contador)

if __name__ == "__main__":
    
    lista = [1, 7, 9 ,3 ,4, 2, 12, 91, 2, 92]
    
numeros = numeros(lista, 10)
print (numeros)
'''

#CORTE

# Dada una lista de palabras, devuelve la longitud de la palabra más larga.
'''
def palabras(palabra):
    larga = ""
    for i in palabra:
        
        if len(i) > len(larga):
            larga = i
    letras = len(larga)
    return letras

if __name__ == "__main__":
    lista = ["hola", "hijo", "cacorro", "mosasaurus", "electromecanografista", "velocirraptor", "uno", "willyrex"]
    
cantidad = palabras(lista)
print (cantidad)
'''

#CORTE

#Dada una lista de números, devuelve el primer número impar. Si no hay, devuelve None.

'''
def lista_numeros(numeros):
    num = None
    for i in numeros:
        if i % 2 != 0:
            num = i
            break
            
    return num

if __name__ == "__main__":
    numeros = [ 0, 2, 3, 4, 5, 6]
    
impar = lista_numeros(numeros)
print (impar)
'''

#CORTE MATRICES

# Encuentra el número más pequeño en una matriz y devuelve su posición (fila, columna).

'''
def numerosx(matriz):
    menor = matriz[0][0]
    posicion = (0, 0)
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] < menor:
                menor = matriz[fila][columna]
                posicion = (fila, columna)
                
    return posicion

if __name__ == "__main__":
    lista = [[1, 3, 5], 
             [2, 4, 9], 
             [0, 4, 1]]
    
menor = numerosx(lista)
print (menor)
'''

#CORTE

#Dada una matriz de enteros, devuelve la suma de cada fila en una lista.
'''
def matriz_enteros(matriz):
    sumas = []
    for fila in matriz:
        suma = 0
        for columna in fila:
            suma = columna + suma
        sumas.append(suma)
        
    return sumas
if __name__ == "__main__":
    numeros = [[1, 2], [3, 2], [4, 1], [5, 5]]
    
sumas = matriz_enteros(numeros)
print (sumas)
'''

#CORTE

#Verifica si alguna fila de la matriz está compuesta solo por números pares.

'''
def matriz_pares(matriz):

    for fila in matriz:
        pares = True
        for columna in fila:
            if columna % 2 != 0:
                pares = False
                break
        if pares:
            return True             
    return False

if __name__ == "__main__":
    matrizx = [
    #[2, 4, 6],      # ✅ todos pares
    [1, 3, 5],      # ❌ todos impares
    [8, 10, 12],    # ✅ todos pares
    [7, 2, 9]]      # ❌ mezcl]
     
valor = matriz_pares(matrizx)
print (valor)
'''
#CORTE


#Crea una función que reciba una lista de listas (matriz)
#y devuelva cuántos números son mayores que el promedio de toda la matriz.

'''
def n_mayores(matriz):
    numeros = 0
    suma = 0
    mayores = 0
    for fila in matriz:
        for columna in fila:
            numeros += 1
            suma += columna
    promedio = suma/ numeros
    for fila in matriz:
        for columna in fila:
            if columna > promedio:
                mayores += 1
                
    return mayores

if __name__ == "__main__":
    matrizz = [
    [2, 4, 6],      # ✅ todos pares
    [1, 3, 5],      # ❌ todos impares
    [8, 10, 12],    # ✅ todos pares
    [7, 2, 9]]      # ❌ mezcl]
            
mayor = n_mayores(matrizz)
print (mayor)
            
'''

#CORTE

#Crea una función que reciba una lista y devuelva 
#True si está ordenada de menor a mayor, False si no.

'''
def n_ordenados (lista):
    for i in range(1, len (lista)-1):
        if lista[i] >= lista[i -1] and lista[i] <= lista[i +1]:
            valor = True
        else:
            valor = False
            break
    return valor

if __name__ == "__main__":
    lista = [5, 2, 3, 4, 4, 6]
    
ordenados = n_ordenados(lista)
print (ordenados)
'''     