A = []
contador = 0

# Lendo vetor com 10 numeros
while contador < 10:
    n1 = float(input('Digite um valor: '))
    A.append(n1)
    contador = contador + 1

contador = 0
contador_pares = 0

while contador < 10:
    if A[contador] % 2 == 0:
        contador_pares = contador_pares + 1
        contador = contador + 1
    else:
        contador = contador + 1

print(f'O vetor informado possui {contador_pares} números pares')
