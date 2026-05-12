import random

def selectionSort(array):
    # Percorre todos os elementos do array
    for i in range(len(array)):
        # Encontra o menor elemento no array não ordenado
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        # Troca o elemento encontrado com o primeiro elemento do array não ordenado
        array[i], array[min_idx] = array[min_idx], array[i]

# Criando um array de 15 números inteiros aleatórios
array_numeros = [random.randint(1, 100) for _ in range(15)]
print("Array original:", array_numeros)

# Aplicando Selection Sort
selectionSort(array_numeros)
print("Array ordenado (crescente):", array_numeros)
# Para ordenar em ordem decrescente, basta inverter a comparação
def selectionSortDescending(array): 
    for i in range(len(array)): 
        max_idx = i 
        for j in range(i + 1, len(array)): 
            if array[j] > array[max_idx]: 
                max_idx = j 
        array[i], array[max_idx] = array[max_idx], array[i] 
        