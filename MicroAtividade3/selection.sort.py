#--------------------------------------------------
# Nome do Programa: bubble.sort.py
# Descricao: Descrever a utilização do algoritmo de ordenação “Selection Sort” 
# Autor: Evando Chaves
# Data: Setembro 2024
#--------------------------------------------------

# Algoritmo Selection Sort
def selectionSort(array):
    # Laço for que percorre o array
    for i in range(len(array)):
        # Definindo o índice mínimo inicialmente como 'i'
        min_idx = i
        
        # Segundo laço for para comparar os elementos à frente de 'i'
        for j in range(i + 1, len(array)):
            # Se o valor de array[min_idx] for maior que array[j], atualize min_idx
            if array[min_idx] > array[j]:
                min_idx = j
        
        # Troca dos valores: array[i] e array[min_idx]
        array[i], array[min_idx] = array[min_idx], array[i]

# Criando um array de 15 números inteiros, sem ordenação
array_numeros = [29, 10, 14, 37, 13, 8, 22, 7, 45, 6, 20, 1, 39, 34, 30]

print("Array original:")
print(array_numeros)

# Aplicando o algoritmo de Selection Sort
selectionSort(array_numeros)

# Imprimindo o array ordenado
print("\nArray ordenado de forma crescente:")
print(array_numeros)