from random import choice

vetor = []


def quantidade_pares(vetor):
    resultado = 0
    for n in vetor:
        if n % 2 == 0:
            resultado += 1
    return resultado


while len(vetor) < 10:
    vetor.append(choice(range(100)))

print(vetor)
print(quantidade_pares(vetor))
