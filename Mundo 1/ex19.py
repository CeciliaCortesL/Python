import random
n1 = str(input('Primeiro alno:'))
n2 = str(input('Segundo alno:'))
n3 = str(input('Terceiro alno:'))
n4 = str(input('Quarto alno:'))
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print('O aluno escolhido é: {}'.format(escolhido))