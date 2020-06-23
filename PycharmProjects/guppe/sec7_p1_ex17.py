# Forma 1
A = []
cont = 0

while cont < 10:
    n = int(input('Digite um valor: '))
    if n < 0:
        A.append(0)
    else:
        A.append(n)
    cont = cont + 1

print(A)

# Forma 2
A = []
cont = 0

while cont < 10:
    A.append(int(input('Digite um valor: ')))
    cont = cont + 1

for indice, num in enumerate(A):
    if num < 0:
        A.remove(num)
        A.insert(indice, 0)

print(A)
