import turtle

def mover_ficha(f,pasos):
    if f% 2==1: 
        ### borrar ficha
        t.pencolor("white")        # Color del trazo
        t.fillcolor("white")     # Color de relleno
        t.begin_fill()
        t.penup()
        t.goto(f1["x"],f1["y"])
        t.pendown()
        t.circle(10)
        t.end_fill()
        f1["y1"]+=pasos
        if f1["y1"]>10:
            f1["x1"]+=f1["y1"]//10
            f1["y1"]=f1["y1"]%10
        f1["x"]=(tamano*5+13)-(f1["x1"]-1)*50
        if f1["x1"]% 2==1:
            f1["y"]=((-tamano*4)+8)+((f1["y1"]-1)*50)
        else:
            f1["y"]=((tamano*5)+8)-((f1["y1"]-1)*50)
        
        t.pencolor("black")        # Color del trazo
        t.fillcolor(f1["color"])     # Color de relleno
        t.begin_fill()
        t.penup()
        t.goto(f1["x"],f1["y"])
        t.pendown()
        t.circle(10)
        t.end_fill()
    if f% 2==0:
        ### borrar ficha
        t.pencolor("white")        # Color del trazo
        t.fillcolor("white")     # Color de relleno
        t.begin_fill()
        t.penup()
        t.goto(f2["x"],f2["y"])
        t.pendown()
        t.circle(10)
        t.end_fill()
        f2["y1"]+=pasos
        if f2["y1"]>10:
            f2["x1"]+=f2["y1"]//10
            f2["y1"]=f2["y1"]%10
        f2["x"]=(tamano*5+35)-(f2["x1"]-1)*50
        if f2["x1"]% 2==1:
            f2["y"]=((-tamano*4)+8)+((f2["y1"]-1)*50)
        else:
            f2["y"]=((tamano*5)+8)-((f2["y1"]-1)*50)  

        t.pencolor("black")        # Color del trazo
        t.fillcolor(f2["color"])     # Color de relleno
        t.begin_fill()
        t.penup()
        t.goto(f2["x"],f2["y"])
        t.pendown()
        t.circle(10)
        t.end_fill()




tamano=50
f1={
    "color":"#ff1744",
    "x":tamano*5+13,
    "y":(-tamano*4)+8,
    "x1":1,
    "y1":1
}
f2={
    "color":"#00e5ff",
    "x":tamano*5+35,
    "y":(-tamano*4)+8,
    "x1":1,
    "y1":1
}
t = turtle.Turtle()
turtle.tracer(0)
t.speed(0)
t.penup()
t.goto(-(tamano*5),-(tamano*5))
t.pendown()

for i in range(1,11):
    t.penup()
    t.goto(-(tamano*5),-(tamano*(5-i)))
    t.pendown()
    for _ in range(10):
        t.penup()
        t.forward(50)
        t.pendown()
        for _ in range(4):
            t.forward(50)
            t.left(90)

turtle.update()


t.pencolor("black")        # Color del trazo
t.fillcolor(f1["color"])     # Color de relleno
t.begin_fill()
t.penup()
t.goto(f1["x"],f1["y"])
t.pendown()
t.circle(10)
t.end_fill()

t.pencolor("black")        # Color del trazo
t.fillcolor(f2["color"])     # Color de relleno
t.begin_fill()
t.penup()
t.goto(f2["x"],f2["y"])
t.pendown()
t.circle(10)
t.end_fill()             # Dibuja un círculo
turno=1
while f1["x1"]+f1["y1"]<100:

    x=int(input("ingrese los pasos"))
    mover_ficha(turno,x)
    turno+=1

turtle.done()
