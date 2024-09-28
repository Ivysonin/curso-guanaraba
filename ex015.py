#Carros custa R$60
#km custa R$0.15

dias = int(input ("Quantos dias alugados? "))
km = float(input ("Quanto Km rodados? "))
pago = (dias * 60) + (km * 0.15)
print (f"O total a pagar é de R${pago:.2f}")