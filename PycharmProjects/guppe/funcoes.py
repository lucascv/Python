"""
Definindo funções:

- Funções são pequenas partes de código que realizam tarefas específicas;
- Podem ou não receber entradas de dados e retornar uma saída de dados;
- Muito úteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela, é bom fazer uma verificação para que a função
seja simplificada.

Já utilizamos várias funções desde que iniciamos este curso:
- print();
- len();
- max();
- min();
- sum();
- muitas outras.

# Exemplos de utilização de funções:

# cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (built-in) do Python print()

# print(cores)

# curso = 'Programação'

# print(curso)

# Definindo a primeira função


def diz_oi():
    print('oi!')

OBS:

1- Veja que, dentro das nossas funções podemos utilizar outras funções;
2- Veja que, nossa função só executa uma tarefa, ou seja, a única coisa que ela faz é dizer 'oi'
3- Veja que esta função não recebe nenhum parâmetro de entrada;
4- Veja que esta função não retorna nada;

# Utilizando funções

# Chamada de execução
# diz_oi()  # ATENÇÃO: Nunca esquecer de colocar os parênteses ao executar uma função.

# Exemplo 2

def cantar_parabens():
    print('Parabens pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')


# cantar_parabens()

# Em Python, podemos inclusive criar variáveis do tipo de uma função e executar a mesma através da variável.

canta = cantar_parabens

canta()

# FUNÇÕES COM RETORNO

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}.')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')

# Em Python, quando uma função não retorna nenhum valor, o retorno é igual a None.

# Exemplo função


def quadrado_de_sete():
    print(7 * 7)


ret = quadrado_de_sete()

print(f'Retorno de ret: {ret}.')

# Vamos refatorar esta função para que ela retorne o valor

# OBS: funções Python que retornam valores, devem retornar estes com a palavra return


def quadrado_de_seis():
    return 6 * 6


ret = quadrado_de_seis()  # Criamos uma variável para receber o retorno da função.

print(f'Retorno {ret}')

# Refatorando a primeira função

alguem = 'Pedro'


def diz_oi(alguem):
    return 'Oi!'


print(diz_oi())

OBS: Sobre a palavra reservada return

1- Ela finaliza a função, ou seja, ela sai da execução da função;
# Exemplo 1


def diz_oi():
    print('Estou sendo executado antes do return')
    return 'Oi '
    print('Estou sendo executado após o return')


print(diz_oi())
2- Podemos ter em uma função, diferentes returns;
# Exemplo 2


def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    else:
        return 'b'


print(nova_funcao())


3- Podemos em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;
# Exemplo 3


def outra_funcao():
    return 2, 3, 4, 5

# num1, num2, num3, num4 = outra_funcao()

# print(num1, num2, num3, num4)

print(outra_funcao())
print(type(outra_funcao()))

# Vamos criar uma função para jogar a moeda

from random import random


def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    if random() > 0.5:
        return 'Cara!'
    else:
        return 'Coroa!'


print(joga_moeda())

# Erros de codificação desnecessária comuns na utilização do return de uma função

def eh_impar():
    if 5 % 2 != 0:
        return True
    return False


print(eh_impar())

# FUNÇÕES COM PARÂMETROS

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não saída;
- Não possuem entrada mas possui saída;
- Possuem entrada e saída.

# Refatorando uma função


def quadrado(numero):
    return numero ** 2


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

def soma(a, b):
    return a + b


def multiplica(a, b):
    return a * b


def outra(a, b, msg):
    return (a + b) * msg


print(soma(2, 4))
print(multiplica(2, 4))
print(outra(2, 4, 'Geek '))

OBS: Se a gente informar um número errado de parâmetros ou argumentos, teremos TypeError.

# Nomeando parâmetros


def nome_completo(first_name, last_name):
    return f'Seu nome completo é {first_name} {last_name}.'


print(nome_completo('Angelina', 'Jolie'))

print(nome_completo(last_name='Jolie', first_name='Angelina'))

# ENTENDENDO O *args

- o *args é um parâmetro como outro qualquer. Isso significa que vc poderá chamar de qualquer coisa, desde que comece
com asterisco.

Exemplo:

Por convenção da comunidade, utilizamos *args para defini-lo.

Mas o que é o args?

O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla. Então desde
já lembre-se que tuplas são imutáveis.

# Exemplos:


def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(soma_todos_numeros(4, 6, 9))
def soma_todos_numeros(*args):
    return sum(args)


# Desempacotar

numeros = [1, 2, 3, 4, 5, 6, 7]

print(soma_todos_numeros(*numeros))

# OBS: O asterisco serve para que informemos ao Python que estamos passando como argumento uma coleção de dados.
# Com isso, ele irá desempacotar os dados dessa coleção.

# **kwargs:

# Por convenção da comunidade chamamos de **kwargs

# Este é somente mais um parâmetro mas diferente do args que coloca os valores extras em uma tupla, este exige que
# utlizemos parâmetros nomeados, e transforma esses parâmetros extras em um dicionário.

# Exemplo 1


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}.')



cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza de quem é você.'


print(cumprimento_especial())
print(cumprimento_especial(geek='Pyton'))
print(cumprimento_especial(geek='Oi! '))
print(cumprimento_especial(geek='especial'))


# Nas nossas funções podemos ter (NESTA ORDEM):

- Parâmetros obrigatórios;
- *args;
- Parâmetros default (não obrigatórios);
- **kwargs.


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos.')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(0, 'Julia')
minha_funcao(10, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))

# Desempacotar com **kwargs


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(nome='Felicity', sobrenome='Jones'))
print(mostra_nomes(**nomes))

"""


