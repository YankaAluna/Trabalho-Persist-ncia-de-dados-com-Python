import random

# Método Bubble Sort
def bubbleSort(array):
    # Primeiro laço for
    for i in range(len(array)):
        # Segundo laço for (comparando de dois em dois)
        for j in range(0, len(array) - i - 1):
            # Se o elemento atual for maior que o próximo
            if array[j] > array[j + 1]:
                # Troca os valores
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


array_numeros = [random.randint(1, 100) for _ in range(15)]
print("Array original:", array_numeros)


bubbleSort(array_numeros)
print("Array ordenado (crescente):", array_numeros)
