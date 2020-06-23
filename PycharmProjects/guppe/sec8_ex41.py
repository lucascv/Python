from random import choice

vetor = []

def maior_vetor(vetor):
    """
    Esta função retorna o maior valor de determinado vetor
    :param vetor:
    :return:
    """
    maior = 0
    for n in vetor:
        if n > maior:
            maior = n
    return maior


while len(vetor) < 10:
    vetor.append(choice(range(100)))

print(vetor)
print(maior_vetor(vetor))
