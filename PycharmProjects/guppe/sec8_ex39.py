def troque(a, b):
    x = a
    a = b
    b = x
    return f'Valor de a = {a}, valor de b = {b}'


a = float(input('Digite valor de a: '))
b = float(input('Digite valor de b: '))
print(troque(a, b))
