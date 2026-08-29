saldo = float(input("digite o saldo disponivel na conta:R$"))
saque = float(input("digite o valor do saque:R$"))
novo_valor = float

if saque <= 0:
    print("saque não realizado:O valor deve ser maior do que zero.")
elif saque>saldo:
    print("saque não realizado saldo insuficiente.")   
elif saque % 10 != 0:
    print("saque não realizado:o valor do saque deve ser multiplo de R$ 10.")
else:
    novo_valor = saldo - saque
    print("novo saldo: ", novo_valor)