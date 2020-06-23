a = []
qtd = 10  # quantidade de números no vetor
pos = 0

while len(a) < qtd:
    n = int(input('Digite um número inteiro: '))
    if n in a:
        print('Número digitado já se encontra no vetor. Gentileza informar outro número.')
    else:
        a.insert(pos, n)
        pos = pos + 1
print(a)
