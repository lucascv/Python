n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n1 == n2:
    print('Os dois números digitados são iguais.')
else:
    print(f'{n2} é maior que {n1}')
