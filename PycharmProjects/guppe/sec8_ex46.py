from random import choice

vetor = []

while len(vetor) < 10:
    vetor.append(choice(range(100)))
print(vetor)


def impressao_normal(vetor):
    return vetor


def impressao_inversa(vetor):
    vetor.reverse()
    return vetor


def media_aritmetica(vetor):
    return sum(vetor) / len(vetor)


print(impressao_normal(vetor))
print(impressao_inversa(vetor))
print(media_aritmetica(vetor))
