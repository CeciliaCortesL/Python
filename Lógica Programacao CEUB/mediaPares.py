ct = 0
soma = 0
ctg = 0
print("Digite 0 para sair")
while True:
    numero = int(input("Digite os número:"))
    if numero == 0:
        break
    ctg = ctg + 1
    if numero%2 == 0:
        ct = ct + 1
        soma = soma + numero
if ct != 0:
    media = soma / ct
    print(f"Você digitou {ctg} números e a média dos números é: {media:.4f}")
else:
    print ("Não divide por 0")