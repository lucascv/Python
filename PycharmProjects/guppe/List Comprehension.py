"""
List Comprehension

Nós podemos adicionar estruturas condicionais lógicas às nossas list comprehension.

# Exemplos

# 1

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Refatorar

# Qualquer numero por modulo de 2 = 0. 0 em Python é False. Ou seja, not False = True

pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)


"""




