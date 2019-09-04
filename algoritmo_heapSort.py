from random import shuffle
import random
import math
import timeit
import matplotlib.pyplot as plt


timeHeap = []
elementos = [100000, 200000, 300000, 400000, 500000, 1000000, 2000000]

def geraLista(tam):
    
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista

def heapify(arr, n, i): 
	largest = i  
	l = 2 * i + 1	 
	r = 2 * i + 2	 
  
	 
	if l < n and arr[i] < arr[l]: 
		largest = l 

	
	if r < n and arr[largest] < arr[r]: 
		largest = r 

	
	if largest != i: 
		arr[i],arr[largest] = arr[largest],arr[i] 

		 
		heapify(arr, n, largest) 


def heapSort(arr): 
	n = len(arr) 
 
	for i in range(n, -1, -1): 
		heapify(arr, n, i) 

	 
	for i in range(n-1, 0, -1): 
		heapify(arr, i, 0)  


def timePopulate():
	for numElementos in elementos:
		base = []
		base = geraLista(numElementos)

	
		_tmp = list(base)
		timeHeap.append(timeit.timeit("heapSort({})".format(_tmp), \
        setup="from __main__ import heapSort", \
        number=1))
		

def axis():
	timePopulate()

	
	plt.plot(elementos, timeHeap, label="heapSort")
  
def graphic():
	plt.legend(loc='upper center', shadow=True).get_frame().set_facecolor('0.90')
	plt.xlabel('Tamanho(int)')
	plt.ylabel('Tempo(s)')
	plt.show()

def main():
	axis()
	graphic()

if __name__ == "__main__":
	main()
