cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")

cpf = cpf.replace(".", "").replace("-", "")

if len(cpf) != 11 or not cpf.isdigit():
    print("Inválido")
else:
    soma = 0
    multiplicador = 10

    for i in range(9):
        soma += int(cpf[i]) * multiplicador
        multiplicador -= 1

    resto = soma % 11

    if resto < 2:
        primeiro_digito = 0
    else:
        primeiro_digito = 11 - resto

    soma = 0
    multiplicador = 11

    for i in range(10):
        soma += int(cpf[i]) * multiplicador
        multiplicador -= 1

    resto = soma % 11

    if resto < 2:
        segundo_digito = 0
    else:
        segundo_digito = 11 - resto

    if int(cpf[9]) == primeiro_digito and int(cpf[10]) == segundo_digito:
        print("Válido")
    else:
        print("Inválido")