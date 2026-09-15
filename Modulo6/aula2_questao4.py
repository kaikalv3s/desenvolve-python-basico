lista1 = []
lista2 = []
lista_intercalada = []

quantidade1 = int(input("Digite a quantidade de elementos da lista 1: "))

print("Digite os", quantidade1, "elementos da lista 1:")

for i in range(quantidade1):
    numero = int(input())
    lista1.append(numero)


quantidade2 = int(input("Digite a quantidade de elementos da lista 2: "))

print("Digite os", quantidade2, "elementos da lista 2:")

for i in range(quantidade2):
    numero = int(input())
    lista2.append(numero)


menor = min(len(lista1), len(lista2))

for i in range(menor):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])


if len(lista1) > menor:
    for i in range(menor, len(lista1)):
        lista_intercalada.append(lista1[i])


if len(lista2) > menor:
    for i in range(menor, len(lista2)):
        lista_intercalada.append(lista2[i])


print("Lista intercalada:", lista_intercalada)