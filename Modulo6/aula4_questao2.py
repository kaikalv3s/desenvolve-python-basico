frase = input("Digite uma frase: ")

vogais = sorted([letra.lower() for letra in frase if letra.lower() in "aeiou"])

consoantes = [letra.lower() for letra in frase if letra.lower() not in "aeiou" and letra != " "]

print("Vogais:", vogais)
print("Consoantes:", consoantes)