numeros = [64, 34, 25, 12, 22, 11, 90, 1, 0, 95, 5, 100, 50, 75, 80,];

print(numeros);

print("\n" + "-"*50 + "\n")

n = len(numeros);

for i in range(n):

    swapped = False;

    for j in range(0, n-i-1):

        if numeros[j] > numeros[j+1]:

            numeros[j], numeros[j+1] = numeros[j+1], numeros[j];

            swapped = True;

    if not swapped:

        break;

print("Array ordenado é:");

for i in range(n):

    print("%d" % numeros[i], end=" ");

numeros.sort(key=None, reverse=True) 

print("\n" + "-"*50 + "\n")

print("Array ordenado de forma decrescente usando sort() é:")
for i in range(n):
    print("%d" % numeros[i], end=" ")

print("\n" + "-"*50 + "\n")

array_strings = ["nome", "dataNascimento", "cpf", "rg"]
print("Array original (strings):", array_strings)

# Ordenação crescente (alfabética)
array_strings.sort()
print("Array ordenado crescente:", array_strings)

# Ordenação decrescente (alfabética inversa)
array_strings.sort(key=None, reverse=True)
print("Array ordenado decrescente:", array_strings)

