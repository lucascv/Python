A = []
B = []
qtd = 5  # quantidade de elementos nos vetores

while len(A) < qtd:
    A.append(int(input('Digite um número inteiro: ')))
print(A)

while len(B) < qtd:
    B.append(int(input('Digite um número inteiro: ')))
print(B)

C = []

C = A + B
C = set(C)
print(C)
