from random import choice

vetor = []
while len(vetor) < 30:
    vetor.append(choice(range(100)))
print(vetor)


def separar_vetor_par_impar(vetor):
    """
    Esta função recebe um vetor e o separa em dois outros vetores. Um contendo os valores pares e outro os ímpares.
    """
    A = []
    B = []
    for n in vetor:
        if n % 2 == 0:
            A.append(n)
        else:
            B.append(n)
    return A, B


print(separar_vetor_par_impar(vetor))



