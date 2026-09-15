lista = []

print("Digite números inteiros.")
print("Digite 0 para finalizar.")

while True:
    numero = int(input("Número: "))

    if numero == 0:
        if len(lista) >= 4:
            break
        else:
            print("Digite pelo menos 4 valores.")

    else:
        lista.append(numero)


print("Lista original:", lista)

print("Os 3 primeiros elementos:", lista[:3])

print("Os 2 últimos elementos:", lista[-2:])

print("Lista invertida:", lista[::-1])

print("Elementos de índice par:", lista[0::2])

print("Elementos de índice ímpar:", lista[1::2])