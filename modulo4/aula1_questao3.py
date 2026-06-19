n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite terceira nota: "))

m = (n1 + n2 + n3) / 3

if m >= 60:
    print("Aprovado")

elif m >= 40:
    print("Reculperação")

else:
    print("Reprovado")