numero = float(input('Digite um número: '))
if numero > 0:
    raiz = numero**0.5
    print('A raiz quadrada do número informado é {}'.format(raiz))
elif numero == 0:
    print('O núméro é nulo.')
else:
    n2 = numero*numero
    print('O número ao quadrado é: {}'.format(n2))
