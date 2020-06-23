A = []
B = []
C = []
cont = 0

while cont < 10:
    A.append(int(input('Digite um valor: ')))
    cont = cont + 1

cont = 0

while cont < 10:
    B.append(int(input('Digite um valor: ')))
    cont = cont +1

C = A - B
print(C)
