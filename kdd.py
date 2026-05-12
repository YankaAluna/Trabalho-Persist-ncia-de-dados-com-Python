import time

# Função Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Função Selection Sort
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

# Leitura do arquivo txt e separação em palavras
texto = list()
with open("glossario.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        palavras = linha.split()
        for palavra in palavras:
            texto.append(palavra)

# Comparação de métodos de ordenação
# Bubble Sort
inicio = time.time()
resultado_bubble = bubble_sort(texto.copy())
fim = time.time()
print("Bubble Sort:", resultado_bubble[:20])
print("Tempo Bubble Sort:", fim - inicio, "segundos\n")

# Selection Sort
inicio = time.time()
resultado_selection = selection_sort(texto.copy())
fim = time.time()
print("Selection Sort:", resultado_selection[:20])
print("Tempo Selection Sort:", fim - inicio, "segundos\n")

# Sort nativo do Python
inicio = time.time()
resultado_sort = sorted(texto.copy())
fim = time.time()
print("Sort nativo:", resultado_sort[:20])
print("Tempo Sort nativo:", fim - inicio, "segundos\n")

# Após escolher o melhor método, salvar em novo arquivo
with open("glossario.txt", "w", encoding="utf-8") as saida:
    for palavra in resultado_sort:  
        saida.write(palavra + "\n")

