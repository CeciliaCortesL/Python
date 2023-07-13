salario = float(input('Qual é o salário? R$'))
novo = salario + (salario * 15 /100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento passa a ganhar{:.2f}'.format(salario, novo))