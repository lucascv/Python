from random import choice
from collections import OrderedDict

matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
gabarito = []
respostas = []
alunos = OrderedDict({})

while len(gabarito) < 10:
    gabarito.append(choice(['a', 'b', 'c', 'd', 'e']))
print(f'Gabarito da prova = {gabarito}.')

print('-=' * 15, 'RESPOSTAS', '-=' * 15)
for l in range(0, 3):
    for c in range(0, 10):
        matriz[l][c] = choice(['a', 'b', 'c', 'd', 'e'])
        print(f'[{matriz[l][c]}]', end='')
    print()
print('-=' * 35)

matricula = None
prova = 1

for l in range(0, 3):
    matricula = int(input('Digite a matricula do aluno: '))
    alunos[f'Matrícula {l + 1}º aluno= '] = matricula
    alunos[f'Nota do aluno {matricula}'] = 0
    for c in range(0, 10):
        alunos[f'Matrícula: {matricula}, Prova {prova}'] = matriz[l][c]
        if matriz[l][c] == gabarito[prova - 1]:
            alunos[f'Nota do aluno {matricula}'] = alunos[f'Nota do aluno {matricula}'] + 1
        prova = prova + 1
    prova = 1
print(alunos)

for key in alunos:
    print(alunos[key])

print('-=' * 20, 'PESQUISA DE NOTAS E RESPOSTAS DOS ALUNOS', '-=' * 20)

matricula = int(input('Matricula do aluno: '))
print('-=' * 61)
print('Nota do aluno')
print(alunos[f'Nota do aluno {matricula}'])
print('-=' * 61)
print('Gabarito deste aluno')
while prova < 11:
    print(alunos[f'Matrícula: {matricula}, Prova {prova}'])
    prova += 1
