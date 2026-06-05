'''
agenda = {} 

# agenda["123"] = "Sergio"
# agenda["456"] = "Juan Jose"
# agenda["789"] = "Maikol"

# print (agenda)

# agenda["123"] = {"Nombre": "Sergio", "Equipo": "Barca"}
# agenda["456"] = {"Nombre": "Juan Jose", "Equipo": "Alianza petrolera"}
# agenda["789"] = {"Nombre": "Maikol", "Equipo": "Liverpool"}
# agenda["666"] = {"Nombre": "Mateo", "Equipo": "America"}

# print (agenda["456"]["Equipo"])

# print(agenda.items())

# for k, v in agenda.items():
#     print(k, "->", v)
    
def agregar_persona():
    nombre = input("ingrese el nombre: ")
    equipo = input("ingrese el equipo: ")
    telefono = int(input("ingrese el numero de telefono: "))
    
    agenda[telefono] = {"nombre": nombre, "equipo": equipo}
    
    
def eliminar_personas():
    try:
         telefono = int(input("ingrese el numero de la persona a eliminiar: "))
    
         agenda.pop(telefono)
    except: 
        print("ese numero no existe en la agenda")

def modificar_valores():
     telefono = 1
    
    
        
        
if __name__ == "__main__":
    
    opcion = ""
    while opcion != "salir":
         print ("Bienvenido a la agenda")
         print ("1. (agergar un contacto)")
         print ("2. (eliminar un contacto)")
         print ("3. (modificar un contacto (nombre y equipo))")
         print ("4. (modificar contacto(solo el numero))")
         print ("ver. (ver la agenda)")
         print ("salir. (salir)")
         
         opcion = input("seleccione la opcion: ")
         
         if opcion == "1":
             agregar_persona()
         elif opcion == "2":
             eliminar_personas()
         elif opcion == "ver":
            for k, v in agenda.items():
                print (k, "->", v)

'''

#####CORTE

# Crea una función que reciba una lista de productos vendidos
# en el día y devuelva un diccionario con la cantidad de cada producto.
# Ejemplo: ["pan","pan","leche","huevos","pan"] → {"pan":3,"leche":1,"huevos":1}.

ventas = {}

def cargar_ventas():
    """Lee las ventas desde el archivo y reconstruye el diccionario"""
    ventas = {}
    try:
        with open("ventas.txt", "r") as f:
            for linea in f:
                fecha, producto, cantidad = linea.strip().split(",")
                ventas[int(fecha)] = {"producto": producto, "cantidad": int(cantidad)}
    except FileNotFoundError:
        ventas = {}  # si no existe el archivo, empieza vacío
    return ventas


def guardar_ventas():
    """Guarda todas las ventas en el archivo"""
    with open("ventas.txt", "w") as f:
        for fecha, datos in ventas.items():
            f.write(f"{fecha},{datos['producto']},{datos['cantidad']}\n")
            
            
def agregar_venta ():
    producto = input("escriba el nombre del producto: ")
    cantidad = int(input("escriba la cantidad de producto vendido: "))
    fecha = int(input("introduce el dia de la venta (1 - 31): "))
    
    ventas[fecha] = {"producto": producto, "cantidad": cantidad}
    guardar_ventas()
    
if __name__ == "__main__":
    ventas = cargar_ventas()
    
    opcion = ""
    while opcion != "3":
        print ("")
        print ("bienvenido al programa de ventas")
        print ("para agregar una venta escriba 1")
        print ("para ver las ventas pulse 2")
        print ("para salir pulse 3")
        
        opcion = input ()
        if opcion == "1":
            agregar_venta()
        elif opcion == "2":
            for k, v in ventas.items():
                print (k, "--", v)

                
                
            
        
    
    

