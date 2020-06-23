from random import choice
from collections import deque

a = []
b = []
qtd = 11  # quantidade de elementos no vetor

# Preenchendo vetor com números aleatórios
while len(a) < qtd:
    a.append(choice(range(1, 100)))
print(a)

# Ordenando o vetor em ordem decrescente
a = sorted(a, reverse=True)
print(a)

# Transformando a lista em DEQUE
b = deque(b)

# Criando o novo vetor na ordem desejada
num = 0

while num < len(a):
    if num % 2 == 0:
        b.append(a[num])
        num = num + 1
    else:
        b.appendleft(a[num])
        num = num + 1

print(b)
