import os

# Descobre a pasta onde este script está salvo e cria o caminho absoluto para o texto
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(diretorio_atual, "loremipsum.txt")

try:
    arquivo = open(caminho_arquivo, "r", encoding="utf-8")

    # Lendo todo o conteúdo
    conteudo = arquivo.read()
    print("Conteúdo completo do arquivo:\n")
    print(conteudo)

    # Fechando o arquivo (boa prática)
    arquivo.close()

    # --- Lendo novamente para pegar partes específicas ---
    arquivo = open(caminho_arquivo, "r", encoding="utf-8")

    # Primeira linha
    primeira_linha = arquivo.readline()
    print("\nPrimeira linha do arquivo:")
    print(primeira_linha)

    # Voltando ao início do arquivo para pegar os 3 primeiros caracteres
    arquivo.seek(0)
    tres_caracteres = arquivo.read(3)
    print("\nPrimeiros 3 caracteres do arquivo:")
    print(tres_caracteres)

    arquivo.close()

    print("\nUsando 'with' para abrir o arquivo:")
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo_with = arquivo.read()
        print(conteudo_with)

except FileNotFoundError:
    print(f"Erro: O arquivo não foi encontrado no caminho:\n{caminho_arquivo}")
    print("Verifique se o arquivo 'loremipsum.txt' está salvo na mesma pasta ou se a extensão não está duplicada (.txt.txt).")
