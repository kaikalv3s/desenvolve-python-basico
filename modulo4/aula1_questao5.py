quantidade = int(input("Quantas pessoas são? "))

soma = 0
contador = 1

while contador <= quantidade:
    idade = int(input(f"Digite a idade da pessoa {contador}: "))
    soma += idade
    contador += 1

media = soma / quantidade

print("Média:", media)