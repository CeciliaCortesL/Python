#Fornece o peso dos bois. Qual boi mais pesado, quantos bois foram analisados e a soma dos pesos

ct = 0
peso_total = 0
maior_peso = 0
print("Digite 0 para sair")

while True:
    peso = float(input("Digite o peso:"))
    if peso == 0:
        break
    ct = ct + 1
    peso_total = peso_total + peso
    if peso > maior_peso:
        maior_peso = peso

print(f'O número de bois analisados foi: {ct}, a soma dos pesos dos bois é: {peso_total} e o maior peso é {maior_peso}')