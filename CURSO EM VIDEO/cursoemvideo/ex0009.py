altura = float(input('Digite quantos metros de altura tem a parede: '))
largura = float(input('Digite quantos metros de largura tem a parede: '))
area = altura * largura
tinta = area / 2
print('A quantidade de tinta para pintar a parede com área {:.2f} m² seria de {:.2f} litros de tinta'.format(area, tinta))


