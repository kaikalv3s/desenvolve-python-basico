import random

def encrypt(nomes):
    chave = random.randint(1, 10)
    nomes_criptografados = []

    for nome in nomes:
        nome_criptografado = ""

        for caractere in nome:
            codigo = ord(caractere)

            novo_codigo = ((codigo - 33 + chave) % 94) + 33

            nome_criptografado += chr(novo_codigo)

        nomes_criptografados.append(nome_criptografado)

    return nomes_criptografados, chave


nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

nomes_cript, chave_aleatoria = encrypt(nomes)

print("Chave:", chave_aleatoria)
print("Nomes criptografados:", nomes_cript)