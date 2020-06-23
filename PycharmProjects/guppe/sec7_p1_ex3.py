A = []
contador = 0

while contador < 10:
    n1 = float(input('Digite um valor: '))
    A.append(n1)
    contador = contador + 1

B = []
a = 0
contador = 0
while contador < 10:
    B.append(A[a]**2)
    a = a + 1
    contador = contador + 1

print(A)
print(B)
