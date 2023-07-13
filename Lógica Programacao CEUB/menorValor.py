print("Digite 0 para sair")
menor_valor = 9999999999
ct = 0
soma = 0

while True:
    numero = int(input("Digite o número: "))
    if numero == 0:
        break
    ct = ct + 1
    soma = soma + numero
    if numero < menor_valor:
      menor_valor = numero

if ct == 0:
    print("Nenhum número foi digitado")

print(f'O menor número é: {menor_valor}, a quantidade de valores digitados foi: {ct} e a soma é {soma}')