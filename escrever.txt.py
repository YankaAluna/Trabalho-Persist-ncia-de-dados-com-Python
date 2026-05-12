# Abrir (ou criar) o arquivo texto.txt em modo de escrita
arquivo = open("texto.txt", "w")

# Criar uma lista
texto = list()

# Adicionar frases à lista usando append
texto.append("Primeira frase adicionada à lista.")
texto.append("Segunda frase adicionada à lista.")
texto.append("Terceira frase adicionada à lista.")

# Escrever o conteúdo da lista no arquivo
for linha in texto:
    arquivo.write(linha + "\n")

# Fechar o arquivo
arquivo.close()
