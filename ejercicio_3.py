def calcular_nota(porcen_1,porcen_2,porcen_3):
    nombre=input("ingrese el nombre de la persona-> ")
    codigo=int(input("ingrese el codigo de la persona-> "))

    parcial_1=float(input("ingrese la nota del parcial 1-> "))
    parcial_2=float(input("ingrese la nota del parcial 2-> "))
    taller=float(input("ingrese la nota del taller-> "))

    nota_final =parcial_1*porcen_1+parcial_2*porcen_2+taller*porcen_3

    return nombre,codigo,nota_final ## tener en cuenta el orden


estudiantes = []
opcion = ""
while opcion !="salir":
    n,c,nf = calcular_nota(0.35,0.35,0.3)
    estudiante = [n,c,nf]
    estudiantes.append(estudiante[:]) # [:] crear una copia
    opcion = input("si desea salir digite salir-> ")


for e in estudiantes:
    print(e)#hace que se imprima abajo
