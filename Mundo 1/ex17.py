import math
co = float(input('Comprimento cateto oposto: '))
ca = float(input('Comprimento cateto adjacente: '))
h1 = math.hypot(co,ca)
print('A hipotenusa vai medir: {:.2f}'.format(h1))