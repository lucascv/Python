A = []
cont = 0

while cont < 5:
    A.append(float(input('Digite um valor: ')))
    cont = cont + 1

print(A)
print(f'O maior valor está na posição {A.index(max(A))}.')
print(f'O menor valor está na posição {A.index(min(A))}.')
