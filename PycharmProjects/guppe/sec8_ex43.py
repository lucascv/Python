from random import choice



def preenche_vetor_sem_repetidos():
    vetor = []
    while len(vetor) < 10:
        a = choice(range(100))
        if a in vetor:
            a = 0
        else:
            vetor.append(a)
    return vetor


print(preenche_vetor_sem_repetidos())
