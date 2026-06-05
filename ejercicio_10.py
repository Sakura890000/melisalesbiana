#inventario de una tienda


def menu():
    
    print("Que quieres hacer: ")
    print("1-Agregar un producto")
    print("2-Modificar un producto")
    print("3-Ver productos")
    print("4-Salir")
    opc=int(input("Ingresa el numero de la opcion: "))
    return opc


def agregar_productos(tienda):
    
    codigo=int(input("Ingresa el codigo del producto: "))
    nombre=(input("Ingresa el nombre: "))
    cant=int(input("Ingresa la cantidad que hay: "))
    precio=int(input("Ingresa  el precio que tiene: "))

    tienda[codigo]={"nombre":nombre,"cant":cant,"precio":precio}
    return tienda

def modificar_productos(tienda):
    print("1-Nombre")
    print("2-Cantidad")
    print("3-Precio")
    opc=int(input("Digita el numero de lo que desees modificar: "))
    codigo=int(input("Ingresa el codigo del producto"))

    
    if opc==1:
        modi=input("Ingresa el nuevo nombre: ")
        tienda[codigo]["nombre"]=modi
    elif opc==2:
        modi=int(input("Ingresa la nueva cant: "))
        tienda[codigo]["cant"]=modi
    elif opc==3:
        modi=int(input("Ingresa el nuevo precio: "))
        tienda[codigo]["precio"]=modi
    else:
        print("incorrecto vuelva a intentar")

def ver_productos(tienda):
    tienda=agregar_productos
    print(tienda)

if __name__=="__main__":
    tienda={}
    x = menu()
    while x!=4:
        
        if x==1:
            tienda=agregar_productos(tienda)
        elif x==2:
            modificar_productos(tienda)
        elif x==3:
            ver_productos(tienda)
        x=menu()