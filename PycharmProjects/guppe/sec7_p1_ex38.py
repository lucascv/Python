a = []
qtd = 10  # quantidade de elementos no vetor
pos = 0

while len(a) < qtd:
    n = int(input('Digite um número: '))
    if len(a) == 0:
        a.append(n)
    elif len(a) == 1:
        if n > a[pos]:
            a.insert(pos + 1, n)
        else:
            a.insert(pos, n)
    else:
        if n > a[len(a) - 1]:
            a.insert(len(a), n)
        else:
            while n > a[pos]:
                pos = pos + 1
            a.insert(pos, n)
            pos = 0
print(a)
