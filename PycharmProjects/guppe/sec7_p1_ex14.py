"""
Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais e os escreva na tela.

cont = 0

while cont < 10:
    if A.count(A[cont]) > 1:
        print(A[cont])
        cont = cont +1
    else:
        cont = cont +1

print(A)
"""
# Importando collections
from collections import Counter

# Variáveis
A = []
cont = 0

# Lendo elementos no vetor
while cont < 10:
    A.append(int(input('Digite um valor: ')))
    cont = cont + 1

print(A)

# Verificando e informando quais valores são iguais
resposta = Counter(A)
print(resposta)

for chave, valor in resposta.items():
    if valor > 1:
        print(chave)
