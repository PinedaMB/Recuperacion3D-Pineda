"""
Intersection example
Brayan Pineda Méndez - 18390039
Examen de recuperación 3D - Enero 03, 2021
"""
"""
Para usar la libreria Keyboard se tiene que instalar mediante cmd o consola de comando
usando el comando: pip install keyboard
una vez listo se permitirá usar el programa sin ningún problema

Importar también desde math sqrt que es raiz cuadrada

Nota!!!!! El programa funcina correctamente, pero la variable "flag" 
que marca si está dentro o fuera no se reinicia, pienso que es error de mi computadora, 
pero si sale del programa (ESC) y lo veulve a ejecutar 
cambia el mensaje y lo muestra correctamente !!!!!
"""

#Se importan las librerías
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
import keyboard as keyboard

#------------ Arreglo inicial
xg = []
yg = []
zg = []

xc = 80
yc = 40
zc = 40

#----------- Plotear el sistema
def plotPlaneLine(xg, yg, zg, A, A1, A2, flag):
    plt.title('Examen recuperación 3D - Pineda')
    plt.axis([0, 200, 100, -50]) #----Tamaño del grid
    plt.axis('on')
    plt.grid(True)

    #----- Formar el triángulo Base
    plt.plot([xg[0], xg[1]], [yg[0], yg[1]], color='k')
    plt.plot([xg[0], xg[2]], [yg[0], yg[2]], color='k')
    plt.plot([xg[1], xg[2]], [yg[1], yg[2]], color='k')

    #----- Triangulo Hit point
    plt.plot([xg[0], xg[3]], [yg[0], yg[3]], linestyle=':', color='r')
    plt.plot([xg[1], xg[3]], [yg[1], yg[3]], linestyle=':', color='r')
    plt.plot([xg[2], xg[3]], [yg[2], yg[3]], linestyle=':', color='r')

    plt.text(100, 0, flag)
    plt.text(100, 15, A)
    plt.text(100, 30, A1)
    plt.text(100, 45, A2)

    plt.show()

def calcularAreas(xg, yg, zg):
    #-----------------------------------------
    a=xg[1]-xg[0]
    b=yg[1]-yg[0]#-----Distancia de 0 a 1
    c=zg[1]-zg[0]
    D01=sqrt(a*a+b*b+c*c) 
    a=xg[2]-xg[1]
    b=yg[2]-yg[1]#-----Distancia de 1 a 2
    c=zg[2]-zg[1]
    D12=sqrt(a*a+b*b+c*c) 
    a=xg[2]-xg[0]
    b=yg[2]-yg[0]#-----Distancia de 0 a 2
    c=zg[2]-zg[0]
    D02=sqrt(a*a+b*b+c*c)

    #Cálculo de area con formula de Heron
    s=(D01+D12+D02)/2
    A=sqrt(s*(s-D01)*(s-D12)*(s-D02))
        
    #-----------------------------------------
    a=xg[1]-xg[0]
    b=yg[1]-yg[0]#----Distancia de 0 a 1
    c=zg[1]-zg[0]
    D01=sqrt(a*a+b*b+c*c) 
    a=xg[3]-xg[1]
    b=yg[3]-yg[1]#----Distancia de 1 a 3
    c=zg[3]-zg[1]
    D13=sqrt(a*a+b*b+c*c) 
    a=xg[3]-xg[0]
    b=yg[3]-yg[0]#----Distancia de 0 a 3
    c=zg[3]-zg[0]
    D03=sqrt(a*a+b*b+c*c)

    #cálculo de area con formula
    s=(D01+D13+D03)/2
    A1=sqrt(s*(s-D01)*(s-D13)*(s-D03))

    #-----------------------------------------
    a=xg[2]-xg[0]
    b=yg[2]-yg[0]#-----Distancia de o a 2
    c=zg[2]-zg[0]
    D02=sqrt(a*a+b*b+c*c) 
    a=xg[3]-xg[2]
    b=yg[3]-yg[2]#-----Distancia de 2 a 3
    c=zg[3]-zg[2]
    D23=sqrt(a*a+b*b+c*c) 
    a=xg[3]-xg[0]
    b=yg[3]-yg[0]#-----Distancia de 0 a 3
    c=zg[3]-zg[0]
    D03=sqrt(a*a+b*b+c*c)

    #Cálculo de area con formula
    s=(D02+D23+D03)/2
    A2=sqrt(s*(s-D02)*(s-D23)*(s-D03))

    #Verificacion del hitpoint
    flag = ""
    if((A1 + A2) < A):
        flag = "Dentro del Área"
    else:
        flag = "Fuera del Área"
    
    #-----Se manda a plotear el programa principal
    plotPlaneLine(x, y, z, A, A1, A2, flag)


#Pedir los datos del hitpoint
print('Presiona ENTER para ingresar los datos.')
print('Presiona ESC para salir del programa.')
while True:
    if keyboard.is_pressed('ENTER'): #Se requiere instalar Keyboard 
        input()
        axis = int(input('Valor del hitpoint 1: '))
        x = [40, 30, 80, axis]
        axis = int(input('Valor del hitpoint 2: '))
        y = [60, 10, 60, axis]
        z = [-10, 10, 10, -10]

        for i in range(len(x)):
            xg.append(x[i]+xc)
            yg.append(y[i]+yc)
            zg.append(z[i]+zc)

        calcularAreas(xg, yg, zg)#Se llama al programa para calcular areas

    elif keyboard.is_pressed('ESC'): #Se valdia si se ha presionado Esc
        break