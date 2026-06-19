experimentos = int(input("Quantos experimentos foram registrados? "))
tipo1 = int(input("Desses experimentos quantas cobaias ultilizadas eram tipo 'S'"))
tipo2 = int(input("Desses experimentos quantas cobaias ultilizadas eram tipo 'R'"))
tipo3 = int(input("Desses experimentos quantas cobaias ultilizadas eram tipo 'C'"))

percentual1 = tipo1 / experimentos * 100
percentual2 = tipo2 / experimentos * 100
percentual3 = tipo3 / experimentos * 100

print(f"Total de cobaias: {experimentos}")
print(f"Total de coelhos: {tipo3}")
print(f"Total de ratos: {tipo2}")
print(f"Total de sapos: {tipo1}")
print(f"Percentual de sapos: {percentual1:.2f}%")
print(f"Percentual de ratos: {percentual2:.2f}%")
print(f"Percentual de coelhos: {percentual3:.2f}%")