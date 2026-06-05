agenda={}

agenda["123"]="sergio"
agenda["456"]="juan jose"
agenda["789"]="maikol"

agenda["123"]={"nombre":"sergio", "equipo":"Barca"}
agenda["456"]={"nombre":"juan jose","equipo":"Alianza petrolera"}
agenda["789"]={"nombre":"maikol","equipo":"Liverpool"}
agenda["666"]={"nombre":"mateo","equipo":"america de cali"}

"""
for clave.valor in agenda.items():
    print(clave,valor)
"""
def agregar_persona():
    nombre=input("Ingrese el nombre: ")
    equipo=input("Ingrese el equipo: ")
    telefono=int(input("ingrese el telefono: "))

    #agrgar un nuevo elemento en el diccionario
    agenda[telefono]={"Nombre":nombre,"Equipo":equipo}

def eliminar_persona():
    try:
        telefono=input("ingrese el numero de la persona que desea eliminar: ")
        agenda.pop(telefono)
    except:
        print("el codigo no existe")

if __name__=="__main__":
    opcion=""
    while opcion!="salir":
        print("Bienvenido a la agenda")
        print("1-Agregar un contacto")
        print("2-Ver la agenda")
        print("3-eliminar persona")
        print("salir")

        opcion=input("Seleccione la opcion: ")

        if opcion=="1":
            agregar_persona()
        elif opcion=="2":
            for clave,valor in agenda.items():
                print(clave,valor)
        elif opcion=="3":
            eliminar_persona()


