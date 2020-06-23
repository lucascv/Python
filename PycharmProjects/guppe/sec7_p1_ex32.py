x = []
y = []
qtd = 5  # quantidade de elementos nos vetores

while len(x) < qtd:
    num = int(input('Digite um número inteiro: '))
    if num in x:
        print('Número digitado é repetido.')
    else:
        x.append(num)
print(x)

while len(y) < qtd:
    num = int(input('Digite um número inteiro: '))
    if num in y:
        print('Número digitado é repetido.')
    else:
        y.append(num)
print(y)

# Resolução (A):
soma = []
n = 0

while n < qtd:
    soma.append(x[n] + y[n])
    n = n + 1
print(soma)

# Resolução (B):
produto = []
n = 0

while n < qtd:
    produto.append(x[n] * y[n])
    n = n + 1
print(produto)

# Resolução (C):
x1 = set(x)
y1 = set(y)
print(x1 - y1)

# Resolução (D)
ambos = x1.intersection(y1)
print(ambos)

# Resolução (E)
print(x1.union(y1))
