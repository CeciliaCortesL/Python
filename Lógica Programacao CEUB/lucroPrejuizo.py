compra = float(input("Preço de compra:"))
venda = float(input("Preço da venda:"))
total = venda - compra
if total > 0:
	print("Lucro=", total)
elif total == 0:
	print("Os valores são iguais")
else:
	print("Seu prejuizo foi de:", total)