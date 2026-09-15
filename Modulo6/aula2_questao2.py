import random

num_elementos = random.randint(5, 20)

elementos = []

for i in range(num_elementos):
    numero = random.randint(1, 10)
    elementos.append(numero)

soma = sum(elementos)
media = soma / len(elementos)

print("Lista elementos:", elementos)
print("Soma dos valores:", soma)
print("Média dos valores:", media)