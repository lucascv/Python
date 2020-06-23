"""
Módulo Collections - Counter (contador)

Collections - High-performance container datatypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um
dicionário contendo como chave o elemento da lista (o parâmetro recebido) e como valor a quantidade de ocorrências
deste elemento.

RESUMO: CONTA QUANTAS VEZES CADA ELEMENTO EXISTE DENTRO DA LISTA, TUPLA, ETC.

# Utilizando o Counter

from collections import Counter

# Podemos utilizar qualquer iterável (como exemplo usaremos a lista)

lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

resultado = Counter(lista)
print(type(resultado))
print(resultado)

Exemplo 2:
print(Counter('Geek University')) # Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1,
's': 1, 't': 1, 'y': 1})

# Exemplo 3:

texto = 'A Wikipédia é alojada pela uma uma Wikipédia Foundation, uma organização sem fins lucrativos que também aloja
vários outros projetos.'

palavras = texto.split()
print(palavras)

res = Counter(palavras)
print(res)

print(res.most_common(2))

"""
