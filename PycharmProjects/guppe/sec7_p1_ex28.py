v = []

while len(v) < 5:
    v.append(int(input('Digite um valor: ')))
print(v)

v1 = []
v2 = []
a = 0

while a < len(v):
    if v[a] % 2 == 0:
        v2.append((v[a]))
        a = a + 1
    else:
        v1.append(v[a])
        a = a + 1

print(f'Os números ímpares são {v1}.')
print(f'Os números pares são {v2}.')
