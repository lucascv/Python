"""
indice = 0
cont = len(A) + len(B)
a = 0
b = 0

while cont > 0:
    if indice % 2 == 0:
        C.insert(indice, A[a])
        indice = indice + 1
        a = a + 1
    else:
        C.insert(indice, B[b])
        indice = indice + 1
        b = b + 1

print(A)
print(B)
print(C)

------

cont = 0
n = 0

while cont < quantidade:
    C.append(A[n])
    C.append(B[n])
    cont = cont + 1
    n = n + 1

print(C)


"""
A = []
B = []
C = []
cont = 0
quantidade = 5

while cont < quantidade:
    A.append(int(input('Digite um valor: ')))
    cont = cont + 1

cont = 0

while cont < quantidade:
    B.append(int(input('Digite um valor: ')))
    cont = cont + 1

print(A)
print(B)

cont = 0
quantidade = len(A) + len(B)
a = 0
b = 0

while cont < quantidade:
    if cont % 2 == 0:
        C.insert(cont, A[a])
        cont = cont + 1
        a = a + 1
    else:
        C.insert(cont, B[b])
        cont = cont + 1
        b = b + 1

print(C)
