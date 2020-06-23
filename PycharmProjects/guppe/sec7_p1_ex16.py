A = []
cont = 0

while cont < 5:
    A.append(float(input('Digite um valor: ')))
    cont = cont + 1

codigo = int(input('Digite o código: '))
if codigo == 1:
    print(A)
elif codigo == 2:
    A.reverse()
    print(A)
elif codigo == 0:
    print('Fim.')
else:
    print('Codigo inválido.')
