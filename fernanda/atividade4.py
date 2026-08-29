sexo = input("digite o sexo (M/F): ")
idade = int(input("digite a idade: "))
tempo_de_contribuicao = int(input("digite o tempo de contribuição: "))

pode_aposentar = False

if sexo == "M":
    if (idade >= 65 and tempo_de_contribuicao >= 10) or (idade >= 63 and tempo_de_contribuicao >= 15):
        pode_aposentar = True

elif sexo == "F":
    if (idade >= 63 and tempo_de_contribuicao >= 10) or (idade >= 61 and tempo_de_contribuicao >= 15):
        pode_aposentar = True

# saída
if pode_aposentar:
    print("aposentável")
else:
    print("não aposentável")

