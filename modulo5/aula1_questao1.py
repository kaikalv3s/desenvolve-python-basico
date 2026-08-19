print("Digite 2 números decimais")

n1 = float(input("1º número: "))
n2 = float(input("2º número: "))

diferença = n1 - n2

resultado = round(abs(diferença), 2)

print(f"\nA diferença absoluta entre os números é: {resultado}")