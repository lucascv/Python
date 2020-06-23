from random import choice

matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

v = []
aluno = 1

for l in range(0, 5):
    for c in range(0, 10):
        matriz[l][c] = choice(['a', 'b', 'c', 'd'])
        print(f'[{matriz[l][c]:^2}]', end='')
    print()
print('-=' * 25)

while len(v) < 10:
    v.append(choice(['a', 'b', 'c', 'd']))
print(v)

respostas_certas = 0
aluno = 0
resultado = []

for l in range(0, 5):
    for c in range(0, 10):
        if matriz[l][c] == v[c]:
            respostas_certas = respostas_certas + 1
    print(f'O {aluno + 1}º aluno acertou {respostas_certas} questões.')
    resultado.insert(c, respostas_certas)
    aluno = aluno + 1
    respostas_certas = 0

print(resultado)
