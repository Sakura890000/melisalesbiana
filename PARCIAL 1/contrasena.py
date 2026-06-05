contrasena = input("cree su nueva constrasena: ")
entrada = ""
intentos = 0

while entrada != contrasena and intentos < 3:
    entrada = input("Ingrese la contraseña: ")
    
    if entrada != contrasena:
        intentos = intentos + 1
        
    if intentos == 1:
            print("le quedan dos intentos")
            
    elif intentos == 2 :
            print("le queda un intento")
        
        

if entrada == contrasena:
    print("Acceso permitido")
else:
    print("Se quedó sin intentos")