A = []
n = 1
cont = 0

while cont < 6:
    while n % 2 == 1:
        n = int(input('Digite um número inteiro par: '))

    A.append(n)
    n = 1
    cont = cont + 1

A.reverse()
print(A)
