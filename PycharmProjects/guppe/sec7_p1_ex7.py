A = []
cont = 0

while cont < 10:
    n = int(input("Digite um número inteiro: "))
    A.append(n)
    cont = cont + 1

print(A)
print(f'O maior elemento do vetor informado é {max(A)}')
print(f'A posição deste elemento no vetor é {A.index(max(A))}')
