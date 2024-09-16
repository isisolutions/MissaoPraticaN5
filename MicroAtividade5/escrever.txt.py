#--------------------------------------------------
# Nome do Programa: bubble.sort.py
# Descricao:  Descrever a escrita de dados em um arquivo externo em Python
# Autor: Evando Chaves
# Data: Setembro 2024
#--------------------------------------------------

# Abrindo (ou criando) o arquivo 'texto.txt' para escrita
with open('texto.txt', 'w') as arquivo:
    # Criando uma lista de frases
    texto = list()
    texto.append("Esta é a primeira frase.")
    texto.append("Aqui está a segunda frase.")
    texto.append("Finalmente, a terceira frase.")

    # Escrevendo cada frase no arquivo
    for frase in texto:
        arquivo.write(frase + '\n')

print("Arquivo 'texto.txt' criado e escrito com sucesso.")