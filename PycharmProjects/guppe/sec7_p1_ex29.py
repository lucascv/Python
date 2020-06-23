A = []

while len(A) < 6:
    A.append(int(input('Digite um número inteiro: ')))
print(A)

a = 0
pares = []
impares = []

while a < len(A):
    if A[a] % 2 == 0:
        pares.append(A[a])
        a = a + 1
    else:
        impares.append(A[a])
        a = a + 1

print(f'Os números pares digitados são {pares} e a soma entre eles é {sum(pares)}.')
print(f'O total de números impares digitados é {len(impares)} e os números são {impares}.')
