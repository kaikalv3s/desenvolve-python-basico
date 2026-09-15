pares = [x for x in range(20, 51) if x % 2 == 0]
print(pares)


quadrados = [x ** 2 for x in range(1, 10)]
print(quadrados)


divisiveis = [x for x in range(1, 101) if x % 7 == 0]
print(divisiveis)


paridade = ["par" if x % 2 == 0 else "ímpar" for x in range(0, 30)]
print(paridade)