#Fórmula para calcular porcentagem valor +ou- (valor * 0/100)
salario = float(input("Qual o salário do funcíonario: R$"))
novo = salario + (salario * 15/100)
print (f"Um funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${novo:.2f}")