from math import hypot
o = float(input('Informe o comprimento do cateto oposto: '))
a = float(input('Informe o comprimento do cateto adjacente: '))
hi = hypot(o, a)
print('O comprimento da hipotenusa com cateto oposto {:.2f} e adjacente {:.2f} é igual {:.2f}'.format(o, a, hi))

