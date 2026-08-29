idade = int(input("informe sua idade: "))
salario = float(input("informe seu salário mensal: R$ "))
valor_emprestimo = float(input("informe o valor do empréstimo: R$ "))
restricao_cpf = input("possui restrição no CPF? (sim/não): ")

motivo = ""

if idade < 18:
    motivo += "o cliente tem menos de 18 anos.\n"

if salario < 2000:
    motivo += "o salário mensal é menor que R$ 2.000,00.\n"

if valor_emprestimo > salario * 5:
    motivo += "o valor solicitado é superior a 5 vezes o salário mensal.\n"

if restricao_cpf == "sim":
    motivo += "o cliente possui restrição no CPF.\n"

print("\nresultado da análise:")

if motivo == "":
    print("empréstimo aprovado!")
else:
    print("empréstimo negado.")
    print("motivos:")
    print(motivo)