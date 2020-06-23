"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python.

The Zen of Python

import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica.

[1] - Utilize Canel Case para nomes de classes;


class Calculadora:
    pass


class CalculadoraCientifica:
    pass


[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis;

def soma():
    pass


def soma_dois():
    pass


numero = 4


numero_impar = 5

[3] - Utilize 4 espaços para identação! (NÃO use TAB)

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
- Separar funções e definições de classes com 2 linhas em branco;
- Métodos dentro de uma classe devem ser separados oom uma única linha em branco;

[5] - Imports

- Imports de pacotes completos devem ser sempre feitos em linhas separadas;
# Import Errado

import sys, os

# Import Certo

import_sys
import_os

# Caso tenham vários imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e
# antes de constantes ou variáveis globais.

[6] - Espaços em expressões e instruções

[7] - Termine sempre uma instrução com uma nova linha
"""
import this












