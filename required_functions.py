from big_o import big_o
from big_o import complexities as cls
from random import shuffle
import matplotlib.pyplot as plt

def generar_aleatorio(n):
    A = list(range(0, n))
    shuffle(A)
    return A

def generear_ordenado_asc(n):
    A = list(range(0, n))
    return A

def generar_ordenado_des(n):
    A = list(range(0, n))
    A.reverse()
    return A

def aprox_asintotica(datos):
    ys = datos['times']
    for k, v in datos.items():
        if isinstance(k, cls.ComplexityClass):
            residual = v
            r2 = 1 - residual / (ys.size * ys.var())
            print(k, f' (r={residual}, r^2={r2})')

def graficar_comportamiento(xs, ys, aprox):
    plt.plot(xs, ys)
    plt.plot(xs, aprox, label = 'Aproximación estimada')
    plt.plot(xs, ys, label = 'Resultados reales')
    plt.ylabel('Tiempo (s)')
    plt.xlabel('n (tamaño del arreglo)')
    plt.legend(loc = 2)
    plt.show()

def comparar_comportamiento(xs, ys, xs1,ys1, aprox1, aprox2, label1, label2):
    plt.plot(xs,ys, label = "Resultados Reales" + label1)    #Se dibujan resultados Obtenidos de Experimentos del algoritmo ys
    plt.plot(xs,ys_2,label = "Resultados Reales" + label2)   #Se dibujan resultados Obtenidos de Experimentos del algoritmo ys1
    plt.plot(xs, aprox1, label = label1)                     #Se dibuja Aproximación temporal del algoritmo ys
    plt.plot(xs1,aprox2, label = label2)		     #Se dibuja Aproximación temporal del algoritmo ys1
    ##pls.plot(xs, ys, label = D
    plt.ylabel('Tiempo (s)')
    plt.xlabel('n (tamaño del arreglo)')
    plt.legend(loc = 2)
    plt.show()
    
def graficar_comparacion(x1, y1, aprox1, x2, y2, aprox2, x3, y3, aprox3, x4, y4, aprox4):
    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.plot(x3, y3)
    plt.plot(x4, y4)
    plt.plot(x1, aprox1, label = 'Selection Sort')
    plt.plot(x2, aprox2, label = 'Insertion Sort')
    plt.plot(x3, aprox3, label = 'Bubble Sort')
    plt.plot(x4, aprox4, label = 'Optimized Bubble Sort')
    plt.plot(x1, y1, label = 'Resultados reales Selection Sort')
    plt.plot(x2, y2, label = 'Resultados reales Insetion Sort')
    plt.plot(x3, y3, label = 'Resultados reales Bubble Sort')
    plt.plot(x4, y4, label = 'Resultados reales Optimized Bubble Sort')
    plt.ylabel('Tiempo (s)')
    plt.xlabel('n (tamaño del arreglo)')
    plt.legend(loc = 2)
    plt.show()

def comparacion(x1, y1, aprox1, x2, y2, aprox2):
    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.plot(x1, aprox1, label = 'Merge Sort')
    plt.plot(x2, aprox2, label = 'QuickSort')
    plt.plot(x1, y1, label = 'Resultados reales Merge Sort')
    plt.plot(x2, y2, label = 'Resultados reales QuickSort')
    plt.ylabel('Tiempo (s)')
    plt.xlabel('n (tamaño del arreglo)')
    plt.legend(loc = 2)
    plt.show()




