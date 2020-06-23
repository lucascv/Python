A = []
cont = 0
nota = 11

while cont < 5:
    while nota > 10 or nota < 0:
        nota = float(input('Digite a nota do aluno: '))

    A.append(nota)
    nota = 11
    cont = cont + 1

media = sum(A)/len(A)

print(f'A média das notas dos alunos é {media}')
