# Pesquisei como fazia para converter uma moeda para outra moeda.
dolar = float (5.57)
euro = float (6.17)
real = float(input ("Quanto de dinheiro você tem na carteira? R$"))
print (f"Com R${real}, Você pode comprar US$ {real / dolar:.2f} ou se você for usar EURO, Ficará EUR${real / euro:.2f}")