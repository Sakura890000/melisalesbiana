##CAlculadora de Esteban Martinez
#2659626-3743
def sumar (a,b):
    return a+b

def restar(a,b):
    return(a-b)

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b
    
def cal():
    print("seleccione que tipo de operacion quiere")
    print("1. sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4. dividir")
    
    op = int(input("opcion: "))
    a = float(input("ingrese el primer termino: "))
    b = float(input("ingrese el segundo termino: "))
    if op ==1:
        print(sumar(a,b))
    elif op == 2:
        print(restar(a,b))
    elif op == 3:
        print(multiplicar(a, b))
    elif op ==4:
        print(dividir(a,b))
    else:
        print("No definido")
#calculadora de Esteban Martinez      
        
###entry point

if __name__ == "__main__":
    
    print("bienvenido a la calculadora")

    while (True):
        cal()
        x = input("si quiere salir, pulse x:")
        if x == 'x':
            break
