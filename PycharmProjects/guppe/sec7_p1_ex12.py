A = []
cont = 0

while cont < 5:
    A.append(float(input('Digite um valor: ')))
    cont = cont + 1

print(A)
print(f'O maior valor digitado é {max(A)}.')
print(f'O menor valor digitado é {min(A)}.')
print(f'A média dos valores digitados é {sum(A)/len(A)}.')
