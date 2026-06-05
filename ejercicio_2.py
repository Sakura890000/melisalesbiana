"""
a=int(input("ingrese el valor de a"))
b=int(input("ingrese el valor de b"))

#ax+b=0
if a==0:
    print("no se puede resolver")
else:    
    x= -b/a
    print ("el resultado es ", x)   
"""
"""
a=int(input("ingrese el valor de a "))
b=int(input("ingrese el valor de b "))
c=int(input("ingrese el valor de c "))

#b^2-4ac

discriminante = (b*b)-(4*a*c)
if discriminante>0:
    print("la ecuacion tiene dos soluciones reales")
elif discriminante<0:
    print("la ecuacion tiene una solucion real")
elif discriminante==0:
    print("la ecuacion tienes dos soluciones complejas")        

raiz= discriminante**1/2

x1=(-b+raiz)/2

print("x1 es ", x1)

x2=(-b-raiz)/2

print("x2 es ", x2)
"""
#-----------------------------------------------------------------
"""
x=int(input("ingrese x-> "))
w=int(input("ingrese w-> "))
z=(3*x / (2*w))-((8*(x**2)-w)/3)
"""
#------------------------------------------------------------------

x=int(input("ingrese x-> "))
k=int(input("ingrese k-> "))
w=int(input("ingrese w-> "))
y=(2*(x**2))*((1/(k-(x/(2-w))))-((9-x)/(3*w)))

 