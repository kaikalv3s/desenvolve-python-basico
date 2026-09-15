import random

lista = []

for i in range(20):
    numero = random.randint(-100, 100)
    lista.append(numero)

lista_ordenada = sorted(lista)

print("Lista ordenada:", lista_ordenada)
print("Lista original:", lista)

indice_maior = lista.index(max(lista))
indice_menor = lista.index(min(lista))

print("Índice do maior valor:", indice_maior)
print("Índice do menor valor:", indice_menor)