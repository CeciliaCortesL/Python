n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digte o segundo número:"))
op = (input("Digite a operação aritimética desejada dentre as opções(+,-,*,/):"))

if op == "+":
    print("{} + {} = " .format(n1, n2))
    print(n1 + n2)
elif op == "-":
    print("{} - {} =" .formart(n1, n2))
    print(n1 - n2)
elif op == "*":
    print("{} * {} =" .format(n1, n2))
    print(n1 * n2)
elif op == "/":
    print("{} / {} =" .format(n1, n2))
    print(n1 / n2)
else:
    print("Operador ou número(s) não válido(s)")