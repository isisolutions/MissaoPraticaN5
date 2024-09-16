#--------------------------------------------------
# Nome do Programa: bubble.sort.py
# Descricao:  Descrever a leitura de dados a partir de um arquivo externo 
# Autor: Evando Chaves
# Data: Setembro 2024
#--------------------------------------------------

# Abrindo o arquivo com o método open e lendo o conteúdo
arquivo = open('loremipsum.txt', 'r')

# Imprimindo todo o conteúdo do arquivo
print("Conteúdo completo do arquivo:\n")
conteudo = arquivo.read()
print(conteudo)

# Fechando o arquivo após a leitura
arquivo.close()

# Abrindo novamente para ler a primeira linha
arquivo = open('loremipsum.txt', 'r')

# Imprimindo apenas a primeira linha
print("\nPrimeira linha do arquivo:\n")
primeira_linha = arquivo.readline()
print(primeira_linha)

# Fechando o arquivo
arquivo.close()

# Abrindo para ler os 3 primeiros caracteres
arquivo = open('loremipsum.txt', 'r')

# Lendo e imprimindo apenas os 3 primeiros caracteres
print("\nTrês primeiros caracteres do arquivo:\n")
primeiros_caracteres = arquivo.read(3)
print(primeiros_caracteres)

# Fechando o arquivo
arquivo.close()

# Utilizando a instrução "with" para abrir e ler o arquivo
print("\nUsando 'with' para abrir e ler o arquivo:\n")
with open('loremipsum.txt', 'r') as arquivo:
    conteudo_with = arquivo.read()
    print(conteudo_with)