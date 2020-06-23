"""
- Conjuntos são utilizados quando precisamos armazenar elementos mas não nos importamos com a ordenação dos mesmos.
Quando não precisamos preocupar com chaves, valores e itens duplicados.
- Os conjuntos (sets) são referênciados em Python com chaves {}.

Diferença entre conjuntos (sets) e mapas (dicionários) em Python:

    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;

# Definindo um conjunto:

# Forma 1:

s = set({1, 2, 3, 4, 5, 6, 5, 7, 2, 3}) # Repare que temos valores repetidos.
print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar erro e não
# fará parte do conjunto.

# Forma 2: MAIS COMUM

s = {1, 2, 3, 4, 5, 6, 5, 2}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto:

if 3 in s:
    print('Tem o 3')
else:
    print('Nao tem o 3')

# Importante lembrar também que conjuntos não tem ordem.

lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')
print(type(lista))

tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f'Tupla: {lista} com {len(tupla)} elementos')
print(type(tupla))

dicionario = {}.fromkeys(lista, 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')
print(type(dicionario))

conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')
print(type(conjunto))

# Podemos iterar em um set normalmente

s = {1, 'b', True, 34.22, 44}

for valor in s:
    print(valor)

# Adicionando elementos em um conjunto:

s = {1, 3, 4, 5, 4}
s.add(7)
print(s)

# Remover elementos no conjunto:

s = {1, 2, 3}
print(s)

# Forma 1:Caso o valor não seja encontrado será gerado o erro.

s.remove(3) #Informamos o valor a ser removido, pois não existe indice em conjuntos.
print(s)

# Forma 2: Caso o valor nao seja encontrado não será gerado erro.

s.discard(33)

# Copiando um conjunto para outro

s = {1, 2, 3}
print(s)

# Forma 1: Deep Cop

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2: Shallow Copy

novo = s

novo.add(4)

print(novo)
print(s)

# Podemos remover todos os itens de um conjunto

s = {1, 2, 3}
print(s)
s.clear()
print(s)

# Mexendo nos conjuntos

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Tirando os alunos que cursam os dois.

# Forma 1: Utilizando Union

unicos1 = estudantes_java.union(estudantes_python)
print(unicos1)

# Forma 2: Utilizando o caractere pipe (|)

unicos2 = estudantes_java | estudantes_python
print(unicos2)

# Gerar um conjunto de estudantes que estão nos dois cursos

# Forma 1: utilizando intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2: utlizando o &

ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar um conjunto de alunos que não cursam os dois cursos

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)
"""




