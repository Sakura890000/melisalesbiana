#notas
calificacion={}

def menu():
    print("Elige una opcion ")
    print("1-Agregar una nota")
    print("2-Mostrar todas las notas")
    print("3-Calcular el promedio")
    print("4-Mostrar la nota más alta y la más baja")
    print("5-Salir")
    opcion=int(input("Ingrese el numero de la opcion-> "))
    return opcion

def agregar_notas():
    num=int(input("Ingrese el numero de la nota: "))
    nota=float(input("Ingresa el valor de la nota: "))

    calificacion[num]={"nota":nota}
    return(calificacion)
     
def mostrar_notas():
    for clave,valor in calificacion.items( ):
        print(clave,valor)

def calcular_promedio():
    promedio=0
    num=0
    for clave,valor in calificacion.items():
        promedio+=valor["nota"]
        num+=1
    prom=promedio/num
    
    print("El promedio es: ", prom  )

def num_mayor():
    mayor=0
    for clave,valor in calificacion.items():
        if valor["nota"]>mayor:
            mayor=valor["nota"]
    print("El numero mayor es: ",mayor)

def num_menor():
    menor=0
    for clave,valor in calificacion.items():
        if valor["nota"]<menor:
            menor=valor["nota"]
    print("El numero menor es: ",menor)


if __name__=="__main__":
    opc=""
    while opc!=5:
        opc=menu()
        if opc==1:
            agregar_notas()
        elif opc==2:
            mostrar_notas()
        elif opc==3:
            calcular_promedio()
        elif opc==4:
            num_mayor()
            num_menor()

