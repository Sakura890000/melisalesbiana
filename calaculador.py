
def suma(cant):
    lista=[]
    for i in range(cant):
        num=int(input("ingrese un numero"))
        lista.append(num)
    resultado=0
    for i in range(len(lista)):
        resultado+=lista[i]
    return (resultado)

def resta(cant):
    lista=[]
    for i in range(cant):
        num=int(input("ingrese un numero"))
        lista.append(num)
    resultado=lista[0]
    for i in range(1,len(lista)):
        resultado-=lista[i]
    return resultado
def multiplicacion(cant):
    lista=[]
    for i in range(cant):
        num=int(input("ingrese un numero"))
        lista.append(num)
    resultado=1
    for i in range(len(lista)):
        resultado*=lista[i]
    return (resultado)
def division(cant):
    lista=[]
    for i in range(cant):
        num=int(input("ingrese un numero"))
        lista.append(num)
    resultado=lista[0]
    for i in range(1,len(lista)):
        resultado/=lista[i]
    return (resultado)

opcion=""
while opcion!="salir":
    print("elige que operacion hacer")
    print("1-suma")    
    print("2-resta")    
    print("3-multiplicacion")    
    print("4-division")
    print("5-salir")   
    oper=int(input("digita el numero de la operacion-> "))
    if oper==1:
        cant=int(input("ingrese cuantos numeros quiere sumar"))
        print(suma(cant))
    elif oper==2:
        cant=int(input("ingrese cuantos numeros quiere restar"))
        print(resta(cant))
    elif oper==3:
        cant=int(input("ingrese cuantos numeros quiere multiplicar"))
        print(multiplicacion(cant))
    elif oper==4:
        cant=int(input("ingrese cuantos numeros quiere dividir"))
        print(division(cant)) 
    elif oper==5:
        break   
    else:
        print("no sea pendejo vaya duerma")
