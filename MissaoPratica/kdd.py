#--------------------------------------------------
# Nome do Programa: bubble.sort.py
# Descricao: Criar um glossário de palavras ordenadas
# Autor: Evando Chaves
# Data: Setembro 2024
#--------------------------------------------------
import time

# Função de Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Função de Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Função para medir o tempo de execução
def measure_time(sort_function, arr):
    start_time = time.time()
    sorted_arr = sort_function(arr)
    end_time = time.time()
    return sorted_arr, end_time - start_time

# Lendo o conteúdo do arquivo e separando palavras
def read_file_and_split_words(file_path):
    words = []
    with open(file_path, 'r') as file:
        for line in file:
            words.extend(line.split())
    return words

# Caminho do arquivo
file_path = 'texto.txt'  # Altere para o caminho do seu arquivo

# Lendo e separando palavras
words = read_file_and_split_words(file_path)

# Medindo o tempo e ordenando com Bubble Sort
print("Ordenando com Bubble Sort:")
words_copy = words[:]
sorted_words, bubble_time = measure_time(bubble_sort, words_copy)
print("Tempo de execução:", bubble_time)
print("Palavras ordenadas:", sorted_words)

# Medindo o tempo e ordenando com Selection Sort
print("\nOrdenando com Selection Sort:")
words_copy = words[:]
sorted_words, selection_time = measure_time(selection_sort, words_copy)
print("Tempo de execução:", selection_time)
print("Palavras ordenadas:", sorted_words)

# Medindo o tempo e ordenando com sort() do Python
print("\nOrdenando com sort() do Python:")
words_copy = words[:]
start_time = time.time()
words_copy.sort()
end_time = time.time()
python_sort_time = end_time - start_time
print("Tempo de execução:", python_sort_time)
print("Palavras ordenadas:", words_copy)

# Salvando as palavras ordenadas em um novo arquivo
output_file_path = 'palavras_ordenadas.txt'
with open(output_file_path, 'w') as file:
    for word in words_copy:
        file.write(word + '\n')

print(f"\nPalavras ordenadas salvas em '{output_file_path}'")
