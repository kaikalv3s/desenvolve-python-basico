valor_da_compra = float(input("digite o valor total da compra: R$ "))
tem_cartao = input("o cliente possui cartão da loja (s/n)? ")

if valor_da_compra <= 100:
    percentual_desconto = 0.0
elif valor_da_compra <= 500:
    percentual_desconto = 0.10
else:
    percentual_desconto = 0.20

if tem_cartao == "s":
    percentual_desconto += 0.05

novo_valor = valor_da_compra * (1 - percentual_desconto)
print("o valor final da compra foi: R$", novo_valor)

if valor_da_compra > 1000.00: 
    print("compra de alto valor1")