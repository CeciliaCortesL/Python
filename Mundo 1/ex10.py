real = float(input('Digite a quantidade em real R$ '))
dolar = real / 3.27
print('Com R${:.2f} voce pode comprar U${:.2f}' .format(real,dolar))