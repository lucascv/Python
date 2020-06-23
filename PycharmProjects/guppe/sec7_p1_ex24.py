# Varíaveis iniciais
A = {}
cont = 0

# Adicionando dados dos alunos ao dicionário
while cont < 5:
    indice = int(input(f'Digite a matrícula do {cont + 1}º aluno: '))
    altura = float(input(f'Digite a altura do {cont + 1}º aluno: '))
    A[indice] = altura
    cont = cont + 1

# Calculando as maiores e menores alturas da sala
mais_alto = max(A.values())
mais_baixo = min(A.values())

# Ligando as alturas as suas respectivas chaves/matrículas
chave_mais_baixo = None

for key in A:
    if A[key] == mais_baixo:
        chave_mais_baixo = key
        break

chave_mais_alto = None

for key in A:
    if A[key] == mais_alto:
        chave_mais_alto = key
        break

# Informando resultado ao usuário
print(f'O aluno mais baixo da turma tem {mais_baixo}m e sua matrícula é {chave_mais_baixo}.')
print(f'O aluno mais alto da turma tem {mais_alto}m e sua matrícula é {chave_mais_alto}.')
