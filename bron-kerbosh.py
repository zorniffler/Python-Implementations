import re

# Abre archivo en modo lectura
archivo = open('MANN_a9.clq.txt','r')  

# Extraemos el tamaño del grafo del fichero.
while True:
    linea = archivo.readline()
    # Filtrado de lineas que comienzan por 'c'
    if linea[0] == 'c':
        # Localizamos la linea que contiene el tamaño del grafo
        if re.search('Graph Size:',linea):
            linea = linea.split(',') # Partimos la linea
            size = int(re.sub("\D","",linea[0])) # Filtramos enteros
            break
archivo.close()


# Inicializacion del grafo
graph= [[]]
graph = [[0 for j in range(size)] for i in range(size)]


archivo = open('MANN_a9.clq.txt','r')

# Obtencion del grafo para la estructura de datos DIMACS obtenida del fichero.
# Inicia bucle infinito para leer línea a línea
while True: 
    linea = archivo.readline().rstrip('\n')  # lectura de línea eliminando el salto
    #Coger el primer caracter de la linea y comprobar si pertenece al grafo.
    if not linea : 
       break  # Si no hay más se rompe bucle
	   
    if linea[0] == 'e':
        linea = linea.split(' ') # Partimos la linea
        graph[int(linea[1]) - 1][int(linea[2]) - 1] = 1
        graph[int(linea[2]) - 1][int(linea[1]) - 1] = 1            
archivo.close  # Cierra archivo

# Representación del grafo como una lista de listas
#graph = [[0,1,0,0,1,0],[1,0,1,0,1,0],[0,1,0,1,0,0],[0,0,1,0,1,1],[1,1,0,1,0,0],[0,0,0,1,0,0]]

# Función que determina la obtención de los vecinos de un vertice.
def Neighbours(vertex):
    c = 0
    l = []
    for i in graph[vertex - 1]:
        if i == 1 :
         l.append(c + 1)
        c+=1   
    return set(l) 

# Definicion recursiva del algoritmo de Bron-Kerbosch
def bronk(r,p,x):
    if len(p) == 0 and len(x) == 0:
        #print (r)
        sol = [r]
        return sol
    sol = []
    for v in p:
        r_new = set(r) | {v}
        n = Neighbours(v)
        p_new = p & n # p intersects Neighbours(vertex)
        x_new = x & n # x intersects Neighbours(vertex)
        sol = sol + bronk(r_new,p_new,x_new)
        p = p - {v}
        x = x | {v}
    return sol

def getBClique(cliques):
    return sorted(cliques, key=lambda clique: -len(clique))[0]
