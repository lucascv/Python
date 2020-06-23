from random import choice

A = []
B = []
cont = 0

while cont < 10:
    A.append(choice(range(0, 51)))
    cont = cont + 1

print(A)

for indice, num in enumerate(A):
    if num % 2 == 1:
        B.append(num)

print(B)
