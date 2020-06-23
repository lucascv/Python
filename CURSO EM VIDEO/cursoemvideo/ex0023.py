from random import choice
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
n5 = str(input('Digite o quinto nome: '))
lista = [n1, n2, n3, n4, n5]
s = 1
while s < 2:
    nome = choice(lista)
    print('O nome escolhido é: {}'. format(nome))
    s1 = int(input('Deseja sortear novamente? [Sim - 1/Não - 2]: '))
    if s1 == 2:
        s = s + 1















