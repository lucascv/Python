from random import choice
a = []
qtd = 15  # quantidade de elementos no vetor

while len(a) < qtd:
    a.append(int(input('Digite um número inteiro: ')))
print(a)

for num in a:
    if num == 0:
        a.remove(num)

print(a)
