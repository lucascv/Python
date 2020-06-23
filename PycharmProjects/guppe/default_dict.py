"""
Módulo Collections - Default Dict

# Recap dicionarios:

dicionario = {'curso': 'Programação em Python'}
print(dicionario)
print(dicionario['curso'])

Default dict -> ao criar um dicionário utilizando essa função nós informamos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre que nao houver um valor definido.
Caso tentemos acessar uma chave que não existe, essa será criada e o valor default será atribuido à mesma.
"""
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python'

print(dicionario)

print(dicionario['outro'])

print(dicionario)
print(type(dicionario))
