A = []
B = []
qtd = 5  # quantidade de elementos nos vetores digitados

while len(A) < qtd:
    A.append(int(input('Digite um número inteiro: ')))
print(A)

while len(B) < qtd:
    B.append(int(input('Digite um número inteiro: ')))
print(B)

A = set(A)
B = set(B)

ambos = A.intersection(B)
print(f'Os números que estão contidos nos dois vetores são {ambos}.')
