A = []
contador = 0

while contador < 10:
    n = float(input('Digite um valor: '))
    A.append(n)
    contador = contador + 1

print(f'O maior valor do vetor informado é {max(A)}.')
print(f'O menor valor do vetor informado é {min(A)}.')
