import random

lista = []

for i in range(20):
    lista.append(random.randint(-10, 10))

print("Original:", lista)


maior_inicio = 0
maior_fim = 0
maior_quantidade = 0

inicio = 0
quantidade = 0

for i in range(len(lista)):

    if lista[i] < 0:
        if quantidade == 0:
            inicio = i

        quantidade = quantidade + 1

    else:
        if quantidade > maior_quantidade:
            maior_quantidade = quantidade
            maior_inicio = inicio
            maior_fim = i

        quantidade = 0


if quantidade > maior_quantidade:
    maior_quantidade = quantidade
    maior_inicio = inicio
    maior_fim = len(lista)


del lista[maior_inicio:maior_fim]

print("Editada:", lista)