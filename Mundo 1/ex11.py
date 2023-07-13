largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2
print('A parede tem a dimensão de {} x {} e sua área é de {}m^2'.format(largura, altura, area) )
print('Para pintar a parede será necessário {}l de tinta' .format(tinta))
