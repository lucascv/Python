"""
A = []
cont = 0
num = 0

while cont < 100:
    if num in range(0, 1000):
        if num % 7 != 0:
            lista = list(str(num))
            ultimo_numero = lista[len(lista) - 1]
            if ultimo_numero != '7':
                A.append(num)
                cont = cont + 1
                num = num + 1
            else:
                num = num + 1
        else:
            num = num + 1

print(A)
print(len(A))

"""
A = []
num = 0

while len(A) < 100:
    if num % 7 != 0:
        lista = list(str(num))
        if lista[len(lista) - 1] != '7':
            A.append(num)
            num = num + 1
        else:
            num = num + 1
    else:
        num = num + 1

print(A)
