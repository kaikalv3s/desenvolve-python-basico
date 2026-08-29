consumo = float(input("digite o consumo de energia eletrica em kwh:"))
taxa_fixa = 15.00
valor_total = float

if consumo <= 100:
   preço_kwh = 0.50
elif consumo <= 200:
   preço_kwh = 0.70
else:
   preço_kwh=0.90

valor_total = (consumo * preço_kwh) + taxa_fixa
print("seu consumo foi de:", consumo, "\no valor total da conta foi:", valor_total)
if consumo > 300:
     print("atenção:o consumo foi considerado elevado!")