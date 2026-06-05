import turtle as tr
import random as rm
ventana = tr.Screen()
ventana.bgcolor("#00bfff")
ventana.setup(600, 600)  #tamano de ventana
ventana.tracer(0)  #animaciones fluidas


lapiz = tr.Turtle()   #CREO EL LAPIz
lapiz.shape("turtle")  #CREO LA TORTUGA
lapiz.hideturtle()  #ocurlto la tortuga
lapiz.color("blue")
lapiz.speed(0)

circulos = []
def get_coords (x, y):
    print(x, y)
    
    
def guardar_circle(x, y):
        circulo = {
        'x' : x,
        'y' : y,
        'dx' : rm.randint (-10, 10),
        'dy' : rm.randint (-10, 10),
        'radio' : rm.randint (7, 12)
        }
    
        circulos.append(circulo)
    
    
def dibujar_circle(x, y, radio):

    lapiz.penup()
    lapiz.goto(x, y)
    lapiz.pendown()
    lapiz.fillcolor("red")  #COLOrear poligonos relleno
    lapiz.begin_fill()
    lapiz.circle(radio)
    lapiz.end_fill() #finaliza la accion de colorear
        
def mover_circulos():
    tr.clear()
    for circulo in circulos:
        
        circulo['x'] += circulo["dx"]
        circulo['y'] += circulo["dy"]
        
        #choque contra pared horizontal
        if circulo["x"] > 300 or circulo["x"] < -300:
            circulo["dx"] *= -1
        
        if circulo["y"] > 300 or circulo["y"] < -300:
            circulo["dy"] *= -1
        
        dibujar_circle(circulo['x'], circulo ['y'], circulo['radio'])
    ventana.update() ##para que se vean los circulos nuevos
    
    #moverlos cada 30 msec
    ventana.ontimer(mover_circulos, 30)
            
ventana.onscreenclick(guardar_circle)  ###EVEnto click en la pantalla
mover_circulos()




'''

##MANEJAR El turtle con las flechas
def arriba():
    lapiz.setheading(90)  #apunte hacia arriba
    lapiz.forward(10)
    
def abajo():
    lapiz.setheading(270)
    lapiz.forward(10)
    
def izquierda():
    lapiz.setheading(180)
    lapiz.forward(10)
    
def derecha():
    lapiz.setheading(0)
    lapiz.forward(10)
    
def borrador():
    col = lapiz.getturtle().color()
    
    if(col[1] == "Black"):
        lapiz.color("White")
    else:
        lapiz.color("Black")



ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(derecha, "Right")


'''


'''
##dibujar cuadrado
for i in range(4):
    lapiz.forward(50)
    lapiz.right(90)
    
lapiz.penup()
lapiz.goto(100, -100)  #mover el lapiz a otra coordenada
lapiz.pendown()

lapiz.right(70)
lapiz.forward(50)

lapiz.right(150)
lapiz.forward(50)
    
lapiz.right(140)
lapiz.forward(40)
    
lapiz.right(140)
lapiz.forward(50)

lapiz.right(150)
lapiz.forward(50)
'''



##SIN ESTO NO FUNCIONA
ventana.listen()
tr.done()


#O ventana.mainloop()