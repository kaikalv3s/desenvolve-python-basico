frase = input("Digite uma frase: ")
objetivo = input("Digite a palavra objetivo: ")

palavras = frase.split()

anagramas = [
    palavra
    for palavra in palavras
    if sorted(palavra.lower()) == sorted(objetivo.lower())
]

print("Anagramas:", anagramas)