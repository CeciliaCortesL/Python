ct = 0
soma = 0
v_inicial = int(input("valor inicial"))
v_final = int(input("valor final"))
v_passo = int(input("intervalo"))
if v_inicial <= v_final:
    for i in range (v_inicial, v_final + 1, v_passo):
        print(i)
        ct = ct + 1
        soma = soma + i
        media = soma / ct
elif v_inicial > v_final:
    for i in range (v_inicial, v_final -1, -1):
        print(i)
else:
    print("Os valores são iguais")
print(f'Quantidade de números é {ct} e a media é {media}')