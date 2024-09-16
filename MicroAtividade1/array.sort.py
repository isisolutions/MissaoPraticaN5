#--------------------------------------------------
# Nome do Programa: array.sort.py
# Descricao: Descrever a ordenacao de um array
# Autor: Evando Chaves
# Data: Setembro 2024
#--------------------------------------------------

import random

# Criacao de vetores com numeros inteiros e aleatorios
array_numeros = [random.randint(1, 100) for _ in range(15)]
    
print("Array nao ordenado: ")
print(array_numeros)

array_numeros.sort()
print("Ordenacao de forma crescente:")
print(array_numeros)

array_numeros.sort(key=None, reverse = True)
print("Ordenacao de forma decrescente:")
print(array_numeros)

#Nome
array_strings = ["Joao", "Maria", "Pedro", "Ana", "Carlos"]
print("Array nao ordenado NOME: ")
print(array_strings)

array_strings.sort()
print("Ordenacao de forma crescente - NOME:")
print(array_strings)

array_strings.sort(key=None, reverse = True)
print("Ordenacao de forma decrescente - NOME:")
print(array_strings)

#Data Nascimento
array_strings = ["1971/04/15", "2001/03/16", "2000/01/15", "1982/12/16", "1950/11/16"]
print("Array nao ordenado Data Nascimento: ")
print(array_strings)

array_strings.sort()
print("Ordenacao de forma crescente - Data Nascimento:")
print(array_strings)

array_strings.sort(key=None, reverse = True)
print("Ordenacao de forma decrescente - Data Nascimento:")
print(array_strings)

#CPF
array_strings = ["12345678912", "37844687305", "18766990855", "55556515398", "12338125685"]
print("Array nao ordenado CPF: ")
print(array_strings)

array_strings.sort()
print("Ordenacao de forma crescente CPF:")
print(array_strings)

array_strings.sort(key=None, reverse = True)
print("Ordenacao de forma decrescente CPF:")
print(array_strings)

#RG
array_strings = ["123456", "37844687", "6990855", "5555398", "12335685"]
print("Array nao ordenado RG: ")
print(array_strings)

array_strings.sort()
print("Ordenacao de forma crescente RG:")
print(array_strings)

array_strings.sort(key=None, reverse = True)
print("Ordenacao de forma decrescente RG:")
print(array_strings)

