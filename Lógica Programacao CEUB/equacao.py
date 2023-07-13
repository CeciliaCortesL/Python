import math
a = float(input("Valor de a: "))
if a == 0:
	print("Não posso dividir por 0.")
else:
	b = float(input("Valor de b:"))
	c = float(input("Valor de c:"))
	delta = pow(b, 2) - 4 *  a * c
	if delta < 0:
		print("A equação não possui raízes no conjunto dos reais.")
	elif delta == 0:
		x = -b / (2*a)
		print("A equação possui duas raízes iguais a", x)
	else:
		x1 = (-b + math.sqrt(delta))/(2*a)
		x2 = (-b - math.sqrt(delta))/(2*a)
		print("A equação possui raízes diferentes: \nx1 =", x1, "e x2 =", x2)

