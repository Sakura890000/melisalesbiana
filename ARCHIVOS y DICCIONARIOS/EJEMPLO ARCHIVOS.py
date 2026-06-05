
archivo = open("ARCHIVOS.txt", 'r+')

# for linea in archivo:
#     print(linea)

lineas = archivo.readlines()

# print(lineas)

estudiantes = {}
for linea in lineas:
    aux = linea.split("-")
    print(aux)
    estudiantes[aux[0]] = {
        "nombre":aux[1],
        "nota1":aux[2],
        "nota2":aux[3],
        "nota3":aux[4]
    }

print(estudiantes)
    