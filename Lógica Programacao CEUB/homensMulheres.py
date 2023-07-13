ct_masc = 0
ct_fem = 0
maior = 0
menor = 3

print("Digite 0 para sair.")

while True:
    altura = float(input("Altura:"))
    if altura == 0:
        break
    genero = input("[m] para masculino \n [f] para feminino")
    if genero == "m":
        ct_masc += 1
    else:
        ct_fem += 1
    if altura < menor:
        menor = altura
    if altura > maior:
        maior = altura

if ct_masc == 0:
    print("Inválido")
if ct_fem == 0:
    print("Inválido ")

print(f' A menor pessoa: {menor} e a maior pessoa {maior} \n Quantidade de mulheres: {ct_fem}, quantidade de homens: {ct_masc}')