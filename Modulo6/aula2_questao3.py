import random

lista1 = []
lista2 = []

for i in range(20):
    lista1.append(random.randint(0, 50))
    lista2.append(random.randint(0, 50))

interseccao = []

for numero in lista1:
    if numero in lista2 and numero not in interseccao:
        interseccao.append(numero)

interseccao.sort()

print("Lista1 =", lista1)
print("Lista2 =", lista2)
print("Intersecção =", interseccao)

print("Contagem")

for numero in interseccao:
    quantidade_lista1 = lista1.count(numero)
    quantidade_lista2 = lista2.count(numero)

    print(numero, ":(lista1=", quantidade_lista1, ", lista2=", quantidade_lista2, ")")