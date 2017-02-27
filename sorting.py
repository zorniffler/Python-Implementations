import random
import matplotlib.pyplot as plt
import numpy as np
from time import time




# Funciones a testear.

def Burbuja(a,n):
    for i in range(1,n):
        for j in range(0,n-i):
            if(a[j] > a[j+1]):
                k = a[j+1]
                a[j+1] = a[j]
                a[j] = k;

def Insercion(a,n):
    for i in range(1,n):
        v=a[i]
        j=i-1
        while j >= 0 and a[j] > v:
            a[j+1] = a[j]
            j=j-1
        a[j+1]=v

def Seleccion(a,n):
    for i in range(0,n-1):
        min=i
        for j in range(i+1,n):
            if a[min] > a[j]:
                min=j
        aux=a[min]
        a[min]=a[i]
        a[i]=aux


##################################################################

            # PRUEBAS DE ALGORITMOS CON ARRAYS DIRECTOS
##################################################################

timesBD = []
timesID = []
timesSD = []

def GraficasD():
    
    timesBD = BurbujaD()
    timesID = InsercionD()
    timesSD = SeleccionD()
    
    plt.plot(timesBD,'b--',label="Burbuja Directo")
    plt.plot(timesID,'y--',label="Inserción Directo")
    plt.plot(timesSD,'g--',label="Selección Directo")
    
    plt.title("Gráfica Pruebas Directo")
    plt.legend(loc="upper left")
    plt.show()
   
###############################################################################
                    # AJUSTES A FUNCIÓN
###############################################################################    
    
def AjusteBurbujaD():
    
    x = []
    y_ajuste = []
    y = BurbujaD()
    
    for i in range(100,2001,100):
        x.append(i)
    
    p = np.poly1d(np.polyfit(x,y,2))

    for j in range(0,len(x)):   
        #y_ajuste.append((p[0]*x[j]**2)+p[1]*x[j]+p[2])
        y_ajuste.append(p(x[j]))
        
    #p_datos = plt.plot(x,y, 'b.')
        
    plt.plot(x,y_ajuste,'r--',label="Ajuste a Ecuación Cuadratica")
    plt.plot(x,y,'b--',label="Datos experimentales")
    plt.legend(loc="upper left")
    plt.show()


def AjusteInsercionD():
    x = []
    y_ajuste = []
    y = InsercionD()
    
    for i in range(100,2001,100):
        x.append(i)
    
    p = np.poly1d(np.polyfit(x,y,2))

    for j in range(0,len(x)):   
        #y_ajuste.append((p[0]*x[j]**2)+p[1]*x[j]+p[2])
        y_ajuste.append(p(x[j]))
        
    #p_datos = plt.plot(x,y, 'b.')
        
    plt.plot(x,y_ajuste,'r--',label="Ajuste a Ecuación Cuadratica")
    plt.plot(x,y,'b--',label="Datos experimentales")
    plt.legend(loc="upper left")
    plt.show()


def AjusteSeleccionD():
    x = []
    y_ajuste = []
    y = SeleccionD()
    
    for i in range(100,2001,100):
        x.append(i)
    
    p = np.poly1d(np.polyfit(x,y,2))

    for j in range(0,len(x)):   
        #y_ajuste.append((p[0]*x[j]**2)+p[1]*x[j]+p[2])
        y_ajuste.append(p(x[j]))
        
    #p_datos = plt.plot(x,y, 'b.')
        
    plt.plot(x,y_ajuste,'r--',label="Ajuste a Ecuación Cuadratica")
    plt.plot(x,y,'b--',label="Datos experimentales")
    plt.legend(loc="upper left")
    plt.show()



def VisualizarTablasD():

    j = 0
    timesBD = BurbujaD()
    timesID = InsercionD()
    timesSD = SeleccionD()
    
    print("TABLA ALGORITMOS CON ARRAYS DIRECTOS")
    print('{:^20}{:^20}{:^20}{:^20}'.format('Tamaño','Tiempo Burbuja','Tiempo Insercion','Tiempo Selección'))
    for a in range(100,2001,100):
        print('{:^20}{:^20}{:^20}{:^20}'.format(a,timesBD[j],timesID[j],timesSD[j]))
        j = j+1
        
      


def BurbujaD():

    # Variables previas.
    times = []
    list1 = []
    n = 100
    
    # Pruebas con array directo.
    while len(times) != 20:
        for i in range(0,n):   
            list1.append(i)
        t = time()
        Burbuja(list1,len(list1))
        t = time()-t
        times.append(t)
        n = n+100
        list1 = []
    return times[:]
    
   
    
def InsercionD():

    # Variables previas.
    times = []
    list1 = []
    n = 100

    # Pruebas con array directo.
    while len(times) != 20:
        for i in range(0,n):   
            list1.append(i)
        t = time()
        Insercion(list1,len(list1))
        t = time()-t
        times.append(t)
        n = n+100
        list1 = []
    return times[:]



def SeleccionD():

    # Variables previas.
    times = []
    list1 = []
    n = 100

    # Pruebas con array directo.
    while len(times) != 20:
        for i in range(0,n):   
            list1.append(i)
        t = time()
        Seleccion(list1,len(list1))
        t = time()-t
        times.append(t)
        n = n+100
        list1 = []
    return times[:]



##################################################################

            # PRUEBAS DE ALGORITMOS CON ARRAYS INVERSOS
##################################################################


timesBI = []
timesII = []
timesSI = []

def GraficasI():
    
    timesBI = BurbujaI()
    timesII = InsercionI()
    timesSI = SeleccionI()
    
    plt.plot(timesBI,'b--',label="Burbuja Inverso")
    plt.plot(timesII,'y--',label="Inversión Inverso")
    plt.plot(timesSI,'g--',label="Selección Inverso")
    
    plt.title("Gráfica Pruebas Array inverso")
    plt.legend(loc="upper left")
    plt.show()
    
###############################################################################
                    # AJUSTES A FUNCIÓN
###############################################################################    
    
    
def AjusteBurbujaI():
    
    x = []
    y_ajuste = []
    y = BurbujaI()
    
    for i in range(100,2001,100):
        x.append(i)
    
    p = np.poly1d(np.polyfit(x,y,2))

    for j in range(0,len(x)):   
        #y_ajuste.append((p[0]*x[j]**2)+p[1]*x[j]+p[2])
        y_ajuste.append(p(x[j]))
        
    #p_datos = plt.plot(x,y, 'b.')
        
    plt.plot(x,y_ajuste,'r--',label="Ajuste a Ecuación Cuadratica")
    plt.plot(x,y,'b--',label="Datos experimentales")
    plt.legend(loc="upper left")
    plt.show()
 
def AjusteInsercionI():
    
    x = []
    y_ajuste = []
    y = InsercionI()
    
    for i in range(100,2001,100):
        x.append(i)
    
    p = np.poly1d(np.polyfit(x,y,2))

    for j in range(0,len(x)):   
        #y_ajuste.append((p[0]*x[j]**2)+p[1]*x[j]+p[2])
        y_ajuste.append(p(x[j]))
        
    #p_datos = plt.plot(x,y, 'b.')
        
    plt.plot(x,y_ajuste,'r--',label="Ajuste a Ecuación Cuadratica")
    plt.plot(x,y,'b--',label="Datos experimentales")
    plt.legend(loc="upper left")
    plt.show()
    
    
    
def AjusteSeleccionI():
    
    x = []
    y_ajuste = []
    y = SeleccionI()
    
    for i in range(100,2001,100):
        x.append(i)
    
    p = np.poly1d(np.polyfit(x,y,2))

    for j in range(0,len(x)):   
        #y_ajuste.append((p[0]*x[j]**2)+p[1]*x[j]+p[2])
        y_ajuste.append(p(x[j]))
       
        
    #p_datos = plt.plot(x,y, 'b.')
        
    plt.plot(x,y_ajuste,'r--',label="Ajuste a Ecuación Cuadratica")
    plt.plot(x,y,'b--',label="Datos experimentales")
    plt.legend(loc="upper left")
    plt.show()
    
    

def VisualizarTablasI():
    j = 0
  
    timesBI = BurbujaI()
    timesII = InsercionI()
    timesSI = SeleccionI()
    
    #Ampliar bastante la ventana de salida.
    print("TABLA ALGORITMOS CON ARRAYS INVERSOS")
    print('{:^30}{:^30}{:^30}{:^30}'.format('Tamaño','Tiempo Burbuja','Tiempo Inserción','Tiempo Seleccion'))
    for a in range(100,2001,100):
        print('{:^30}{:^30}{:^30}{:^30}'.format(a,timesBI[j],timesII[j],timesSI[j]))
        j = j+1
        

def BurbujaI():
    # Variable previas.
    times = []
    list1 = []
    n = 100

    # Pruebas con array inverso.
    while len(times) != 20:
        for i in range(0,n):   
            list1.append(i)
        list1.reverse()
        t = time()
        Burbuja(list1,len(list1))
        t = time()-t
        times.append(t)
        n = n+100
        list1 = []
    return times[:]

def InsercionI():
    # Variable previas.
    times = []
    list1 = []
    n = 100
    
    # Pruebas con array inverso.
    while len(times) != 20:
        for i in range(0,n):   
            list1.append(i)
        list1.reverse()
        t = time()
        Insercion(list1,len(list1))
        t = time()-t
        times.append(t)
        n = n+100
        list1 = []
    return times[:]
   
        
def SeleccionI():
    # Variable previas.
    times = []
    list1 = []
    n = 100

    # Pruebas con array inverso.
    while len(times) != 20:
        for i in range(0,n):   
            list1.append(i)
        list1.reverse()
        t = time()
        Seleccion(list1,len(list1))
        t = time()-t
        times.append(t)
        n = n+100
        list1 = []
    return times[:]    
    


##################################################################

            # PRUEBAS DE ALGORITMOS CON ARRAYS ALEATORIOS
##################################################################




def RandomExperiment():

    # Variables previas.
    list1 = []
    n = 100
    

    # Semilla fija para generación similar.
    random.seed(1)
    timeBR = []
    timeIR = []
    timeSR = []
    times = []
    for n in range(100,2001,100): # Rango de tamaños.
        for k in range(0,10):   # Número de repeticiones de elemento.
            acumBR = 0
            acumIR = 0
            acumSR = 0
            for j in range(0,n):  #Generación de elementos de 0 a tamaño.
                list1.append(random.randrange(0,n))
            t = time()
            Burbuja(list1[:], n) # Aplicación de Burbuja.
            t = time() - t
            acumBR += t        
            t = time()
            Insercion(list1[:], n) # Aplicación de Insercion.
            t = time() - t
            acumIR += t        
            t = time()
            Seleccion(list1[:], n) # Aplicación de Seleccion.
            t = time() - t
            acumSR += t        
            list1 = []
        timeBR.append(acumBR/10)
        timeIR.append(acumIR/10)
        timeSR.append(acumSR/10)
    
    times.append(timeBR)
    times.append(timeIR)
    times.append(timeSR)
    return times[:]              
            
        
##################################################################

            # PRUEBAS DE ALGORITMOS CON ARRAYS INVERSOS
##################################################################


timesBR = []
timesIR = []
timesSR = []

def GraficasR():
    
    
    times = RandomExperiment()
    timesBR = times[0] 
    timesIR = times[1]
    timesSR = times[2]
    
    plt.plot(timesBR,'b--',label="Burbuja Aleatorio")
    plt.plot(timesIR,'y--',label="Inversión Aleatorio")
    plt.plot(timesSR,'g--',label="Selección Aleatorio")
    
    plt.title("Gráfica Pruebas Array Aleatorio")
    plt.legend(loc="upper left")
    plt.show()

def VisualizarTablasR():

    j = 0
  
    times = RandomExperiment()
    timesBR = times[0] 
    timesIR = times[1]
    timesSR = times[2]
    
    #Ampliar bastante la ventana de salida.
    print("TABLA ALGORITMOS CON ARRAYS ALEATORIOS")
    print('{:^30}{:^30}{:^30}{:^30}'.format('Tamaño','Tiempo Burbuja','Tiempo Inserción','Tiempo Seleccion'))
    for a in range(100,2001,100):
        print('{:^30}{:^30}{:^30}{:^30}'.format(a,timesBR[j],timesIR[j],timesSR[j]))
        j = j+1


    
###############################################################################
                    # AJUSTES A FUNCIÓN
###############################################################################    
    
def AjusteBurbujaR():
    
    times = RandomExperiment()
    y = times[0] 
    
    x = []
    y_ajuste = []
    
    for i in range(100,2001,100):
        x.append(i)
    
    p = np.poly1d(np.polyfit(x,y,2))

    for j in range(0,len(x)):   
        #y_ajuste.append((p[0]*x[j]**2)+p[1]*x[j]+p[2])
        y_ajuste.append(p(x[j]))
        
    #p_datos = plt.plot(x,y, 'b.')
        
    plt.plot(x,y_ajuste,'r--',label="Ajuste a Ecuación Cuadratica")
    plt.plot(x,y,'b--',label="Datos experimentales")
    plt.legend(loc="upper left")
    plt.show()
    
    
def AjusteInsercionR():
    times = RandomExperiment()
    y = times[1] 
    
    x = []
    y_ajuste = []
    
    for i in range(100,2001,100):
        x.append(i)
    
    p = np.poly1d(np.polyfit(x,y,2))

    for j in range(0,len(x)):   
        #y_ajuste.append((p[0]*x[j]**2)+p[1]*x[j]+p[2])
        y_ajuste.append(p(x[j]))
        
    #p_datos = plt.plot(x,y, 'b.')
        
    plt.plot(x,y_ajuste,'r--',label="Ajuste a Ecuación Cuadratica")
    plt.plot(x,y,'b--',label="Datos experimentales")
    plt.legend(loc="upper left")
    plt.show()
    
def AjusteSeleccionR():
    times = RandomExperiment()
    y = times[2] 
    
    x = []
    y_ajuste = []
    
    for i in range(100,2001,100):
        x.append(i)
    
    p = np.poly1d(np.polyfit(x,y,2))

    for j in range(0,len(x)):   
        #y_ajuste.append((p[0]*x[j]**2)+p[1]*x[j]+p[2])
        y_ajuste.append(p(x[j]))
        
    #p_datos = plt.plot(x,y, 'b.')
        
    plt.plot(x,y_ajuste,'r--',label="Ajuste a Ecuación Cuadratica")
    plt.plot(x,y,'b--',label="Datos experimentales")
    plt.legend(loc="upper left")
    plt.show()
    
















