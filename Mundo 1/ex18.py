import math
an = float(input('Digite o angulo que voce deseja: '))
seno = math.sin(math.radians(an))
print('O angulo {} tem o seno de {:.2f}'.format(an,seno))
coseno = math.cos(math.radians(an))
print('O angulo {} tem o coseno de {:.2f}'.format(an,coseno))
tangente = math.tan(math.radians(an))
print('O angulo {} tem a tangente de {:.2f}'.format(an,tangente))