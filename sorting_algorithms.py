import big_o
from random import shuffle

def selectionSort(arreglo):
  n = len(arreglo)
  for i in range(n):
    minimo = i

    for j in range(i+1, n):
      if (arreglo[j] < arreglo[minimo]):
        minimo = j

    temp = arreglo[i]
    arreglo[i] = arreglo[minimo]
    arreglo[minimo] = temp
    
  return arreglo

def insertionSort(arreglo): 

    for i in range(len(arreglo)): 
        j = i 
        while j > 0 and arreglo[j] < arreglo[j - 1]:
                temp = arreglo[j]
                arreglo[j] = arreglo[j - 1]
                arreglo[j-1] = temp
                j -= 1

    return arreglo

def bubbleSort(arreglo):
    n = len(arreglo)
    i = n-1
    while  i > 0:
        for j in range(0, i):
            if arreglo[j] > arreglo[j+1] :
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
        i -= 1
    return arreglo


def quicksort(n):

    size = len(n)
    menores = []
    mayores = []

    if size == 1 or size == 0:
        return n

    else:
        pivote = n[(size - 1) // 2]

        for j in range(size):
            if n[j] < pivote:
                menores.append(n[j])
            elif n[j] > pivote:
                mayores.append(n[j])
        
        menores = quicksort(menores)
        mayores = quicksort(mayores)
        menores.append(pivote)

        return menores + mayores

def quicksort_wc(n):

    size = len(n)
    menores = []
    mayores = []

    if size == 1 or size == 0:
        return n

    else:
        pivote = n[size -1]

        for j in range(size):
            if n[j] < pivote:
                menores.append(n[j])
            elif n[j] > pivote:
                mayores.append(n[j])
        
        menores = quicksort_wc(menores)
        mayores = quicksort_wc(mayores)
        menores.append(pivote)

        return menores + mayores
    
    
def mergeSort(arreglo):
	if len(arreglo) <= 1:
		return arreglo
	else:
		mitad = int(len(arreglo)//2)

		izquierda = mergeSort(arreglo[:mitad])
		derecha = mergeSort(arreglo[mitad:])

		return merge(izquierda,derecha)

def merge(izquierda,derecha):
	i,j = 0,0
	result = []

	while i<len(izquierda) and j<len(derecha):

		if izquierda[i] <= derecha[j]:
			result.append(izquierda[i])
			i += 1
		else:

			result.append(derecha[j])
			j += 1

	result += izquierda[i:]
	result += derecha[j:]
	return result
		
def optimizedBubbleSort(arreglo):
    update=True
    n=len(arreglo)
    while(update==True and n>1):
        update = False
        for i in range(len(arreglo)-1):
            if arreglo[i]>arreglo[i+1]:
                arreglo[i],arreglo[i+1]=arreglo[i+1],arreglo[i]
                update = True
        n-=1
    return arreglo

	

