"""
#un for que imprima los numeros del 1 al 10
for i in range(1,11):
    print (i)
"""
"""
#un while que imprima los numeros del 1 al 10
n=1
while n<=10:
    print(n)
    n +=1
"""    
"""
#imprimir los numeros del 10 al 1
for i in range(10, 0,-1):
    print(i)
"""
"""
#mostrar los numeros pares del 1 al 20
for i in range (0,21,2):
    print(i)
"""
"""
#mostrar los numeros impares del 1 al 20
for i in range (1,20,2):
    print(i)
"""
"""
#calcular la suma de los numeros del 1 al 10
cont=0
for i in range (1,10):
    cont+=i
    print (i, ", ",cont)
"""
"""
#pedir un numero y mostrar la tabla de multiplicar
num= int(input("ingrese el numero->"))
cont=0
for i in range(1,10):
    cont+=num
    print(num, "*", i,"=", cont)
"""
"""
#mostrar los multiplos de un num del 1 al 30
num= int(input("ingrese el numero->"))
cont=0
for i in range (1,31):
    if i%num==0:
        cont+=1
print ("tu numero tiene ", cont ," multiplos del 1 al 30")
"""
"""
#florecitas
n=1
flor=[1,1,0,0,1]
for i in range (len(flor)):
    #verificar izquierda
    if i == 0:
        izquierda=0
    else:
        izquierda= flor[i-1]

    #verificar derecha
    if i==len(flor)-1:
        derecha=0
    else:
        derecha=flor[i+1]    

    #si estan vacias las posiciones
    if flor[i]==0 and derecha==0 and izquierda==0:
        n-=1    

if n<=0:
    print("true")
else:
    print("false")
"""
"""
#juego
jugador_1=[5,10,3,2]
jugador_2=[6,5,7,3]
suma_1=0
suma_2=0

for i in range (len(jugador_1)):
    puntos=jugador_1[i]
    if (i>0 and jugador_1[i-1]==10) or (i>1 and jugador_1[i-2]==10):
        puntos*=2
    suma_1+=puntos

for i in range (len(jugador_2)):
    puntos_2=jugador_2[i]
    if (i>0 and jugador_2[i-1]==10) or (i>1 and jugador_2[i-2]==10):
        puntos*=2
    suma_2+=puntos_2

print("suma jugador 1->", suma_1)
print("suma jugador 2->", suma_2)
if suma_1>suma_2:
    print("jugador 1 gana")
elif suma_2>suma_1:
    print("jugador 2 gana")
"""
"""
#pergaminos
pergaminos=[4,4,2,3,3,5,5,8,9,9,9]
cont=0
for i in range(len(pergaminos)-1):
    if  pergaminos[i+1]==pergaminos[i]:
        cont+=1


print(cont)
"""
"""
#promedio
num=[1,2,3,4,5,6]
n=len(num)
suma=0
promedio=0
for i in range(len(num)):
    suma+=num[i]

promedio= suma/n
print(promedio)
"""

lista=[1,0,0,0,1,0,0]
n=2

for i in range(len(lista)):
    if (lista[i]==0) and (lista[i-1]==0) and (lista[i+1]==0):
        n-=1
if n<=0:
    print("verdadero")
else:
    print("falso")
"""
jugador_1=[2,3,10,5,6]
jugador_2=[3,10,5,1,3]
suma_1=0
suma_2=0
for i in range (len(jugador_1)):
    if jugador_1[i-1]==10 or jugador_1[i-2]==10:
        multiplicacion = jugador_1[i]*2
        suma_1+=multiplicacion
    else:
        suma_1+=jugador_1[i]        
for i in range (len(jugador_2)):
    if jugador_2[i-1]==10 or jugador_2[i-2]==10:
        multiplicacion = jugador_2[i]*2
        suma_2+=multiplicacion
    else:
        suma_2+=jugador_2[i]   

if suma_1>suma_2:
    print("jugador 1")
elif suma_2>suma_1:
    print("jugador 2")      
"""
"""
#contraseña
contraseña=input("ingrese la contraseña-> ")
contraseña_2=input("vuelva a dijitar la contraseña-> ")
if contraseña==contraseña_2:
    print("contraseña correcta")
else:
    print("contraseña incorrecta") 
"""
"""
n=5
temp=[1,2,3,4,6]
suma=0
for i in range (len(temp)):
    suma+=temp[i]

promedio=suma/n
print(promedio)
for i in range(len(temp)):
    if temp[i] >=promedio:
        print("este dato es mayor a promedio: ",temp[i])
        """
"""
#palindormo
pala=input("ingrese la palabra-> ")
invertida=pala[::-1]
if pala==invertida:
    print("es un palindromo")
else:
    print("no es un palindromo")
"""
"""
#forma 1
lista=[]
matriz=[]
num=int(input("ingrese la cantidad-> "))
for i in range (1):
    for j in range(num):
        lista.append("*")
        matriz.append(lista [:])
        print(matriz)
        """
"""
#forma 2
num=int(input("ingrese la cantidad-> "))
matriz=[]
for i in range (1,num+1):
    lista=[]
    for j in range(i):
        lista.append("*")
    matriz.append(lista)
        #print(matriz)
for lista in matriz:

    print(lista)
"""
"""
hora=int(input("ingrese la hora sin minutos-> "))
min=int(input("ingrese los minutos-> "))
horario=input("ingrese si es am o pm")
if horario=="pm":
    resth=hora+12
    print("la hora en horario militar es: ", resth+ min)
else:
    print("la hora en horario militar es: ", hora+ min)


num=int(input("ingrese la cantidad-> "))
triangulo=[]
for i in range (num):
    lista=[]
    for j in range (num):
"""
"""
#matriz 3*3
matriz=[]
num=1
for i in range(3):
    fila=[]
    for j in range(3):
        fila.append(num)
        num+=1
    matriz.append(fila)
print(matriz)
"""
"""
matriz=[]
cant=int(input("ingrese el largo de la matriz-> "))
for i in range(cant):
    num=int(input("ingrese un numero-> "))
    matriz.append(num)
#suma=0  

#for i in range(len(matriz)):
 #   suma+=matriz[i]
#print(suma)    
mayor=0
for i in range(len(matriz)):
    if matriz[i]>mayor:
        mayor=matriz[i]


print("el mayor es ", mayor)

"""
