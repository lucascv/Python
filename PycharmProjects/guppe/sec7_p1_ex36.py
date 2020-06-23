a = []
qtd = 10

while len(a) < qtd:
    a.append(float(input('Digite um número: ')))
print(a)

a = sorted(a)
print(a)
