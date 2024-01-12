lar = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = lar * alt
tinta = area / 2
print('Sua parede tem a dimensão de {} e {} e a sua área é de {}m²'.format(lar,alt, area))
print('Você vai usar {}l de tinta para pintar essa parede'.format(tinta))
