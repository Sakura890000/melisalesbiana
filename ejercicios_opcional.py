"""
dias=5
est=3
lista=[]
asistencia=[[1,1,0,1,1,]
            [1,0,0,1,0,]
            [1,1,1,1,1]]

asis_mayor=0
asis_completa=0
dia_mayor=0


for i in range(len(dias)):
    asis=0
    for j in range(len(est)):
        if asistencia[i][j]==1:
            asis+=1
            if asis==5:
                asis_completa+=1

            lista.append(asis[:])
            if asis>asis_mayor:
                asis_mayor=asis
                dia_mayor=i
            

print("Asistencias por estudiante: ",lista)
print("Estudiantes con asistencia completa: ",asis_completa)
print("Dia con mayor asistencia: ",dia_mayor)
"""
matriz=[[30,40,50],
        [28,50,33],
        [27,29,31]]

zona_cal=0
pos=[]
fila=3
columna=3

for i in range(fila):
    for j in range(columna):
        if (matriz[i][j]>matriz[i+1][j+1]) and (matriz[i][j]>matriz[i-1][j-1]):
            zona_cal+=1
            pos.append([i,j][:])


print("Zonas caliente: ",zona_cal)
print("posicion: ",pos)
