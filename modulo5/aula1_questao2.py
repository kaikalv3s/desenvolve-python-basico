import math
import random

n = int(input("Digite a quantidade de números: "))

numero = []

for _ in range(n):
    numero_aleatorio = random.randint(0, 100)
    numero.append(numero_aleatorio)

soma = sum(numero)
raiz_quadrada = math.sqrt(soma)

print(f"\nNúmeros gerados: {numero}")
print(f"Soma dos valores: {soma}")
print(f"Raiz quadrada da soma: {round(raiz_quadrada, 2)}")