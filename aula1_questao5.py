frase = input("Digite uma frase: ")

indices = []

for i in range(len(frase)):
    if frase[i].lower() in "aeiou":
        indices.append(i)

print(len(indices), "vogais")
print("Índices:", indices)