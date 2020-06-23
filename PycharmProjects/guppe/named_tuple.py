"""
Módulo Collections - Named Tuple

Named Tuple -> cria chave de acesso para os elementos. São Tuplas diferenciadas onde especificamos um nome para a mesma
e também parâmetros.

from collections import namedtuple

# Precisamos definir o nome e parâmetros.

# Forma 1:

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2:

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3:

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='PitBull', nome='ray')
print(ray)
print(type(ray))

# Acessando elementos

# FOrma 1

print(ray[0])

# Forma 2

print(ray.idade)
print(ray.raca)
print(ray.nome)

print(ray.index('PitBull'))
print(ray.count('PitBull'))

"""
