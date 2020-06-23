def volume_esfera(raio):
    return 4/3 * 3.14 * (raio ** 3)


raio = float(input('Digite o raio da esfera: '))
print(f'O volume de esfera com raio {raio} é {volume_esfera(raio)}')
