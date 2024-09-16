#--------------------------------------------------
# Nome do Programa: bubble.sort.py
# Descricao: Descrever a utilização do algoritmo de ordenação “Buble Sort”
# Autor: Evando Chaves
# Data: Setembro 2024
#--------------------------------------------------

def bubbleSort(array):
    # Primeiro laço for que percorre o array
    for i in range(len(array)):
        # Segundo laço for que compara os elementos adjacentes
        for j in range(0, len(array) - i - 1):
            # Comparação dos elementos adjacentes
            if array[j] > array[j + 1]:
                # Se o elemento à esquerda for maior, troca os elementos
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

# Declarando o array de números com 15 posições
array_numeros = [64, 34, 25, 12, 22, 11, 90, 45, 77, 56, 3, 8, 89, 2, 67]

print("Array original:")
print(array_numeros)

# Aplicando o método bubbleSort no array
bubbleSort(array_numeros)

# Imprimindo o array ordenado
print("Array ordenado de forma crescente:")
print(array_numeros)