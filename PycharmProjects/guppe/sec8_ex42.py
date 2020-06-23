vetor = []


def media_vetor(vetor):
    """
    Esta função recebe um vetor e retorna a média dos seus elementos.
    """
    return sum(vetor) / len(vetor)


while len(vetor) < 3:
    vetor.append(float(input('Digite um número: ')))

print(vetor)
print(media_vetor(vetor))
