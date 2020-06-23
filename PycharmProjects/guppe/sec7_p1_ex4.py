# Variáveis
A = []
contador = 0

# Lendo vetor com 8 posições
while contador < 8:
    n1 = float(input('Digite um valor: '))
    A.append(n1)
    contador = contador + 1

# Lendo X e Y
X = int(input('Digite posição do primeiro elemento: '))
Y = int(input('Digite posição do segundo elemento: '))

print(A)
print(f'A soma dos valores encontrados nas posições {X} e {Y} é {A[X] + A[Y]}')
