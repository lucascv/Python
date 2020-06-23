"""
Módulo Collections - Ordered Dict

# Em um dicionário, a ordem de inserção dos elementos não é garantida.
dicionario = {'a': 1, 'b': 2 , 'd': 4, 'e': 5}

Ordereddict -> é um dicionário que nos garante a ordem de inserção dos elementos.

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave: {chave} : valor: {valor}')

# Entendendo a diferença entre Dict e Ordered Dict

# Dicionários comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)  # Retornará True pois para o dicionário comum a ordem nao importa. Apenas chave e valor.

# Ordered Dict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})
print(odict1 == odict2)  # Retornará False pois para o Ordered Dict a ordem importa.
"""



