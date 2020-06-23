from random import choice

a = choice(range(1, 10000))
b = choice(range(1, 10000))

print(a)
print(b)

# Resolvendo letra (A)
A = []
B = []

a = list(str(a))
b = list(str(b))

print(a)
print(b)

for num in a:
    A.append(num)
print(A)

for num in b:
    A.append(num)
print(A)

pos = 0

for num in A:
    if len(B) == 0:
        B.append(num)
    elif len(B) == 1:
        if num > B[pos]:
            B.insert(pos + 1, num)
        else:
            B.insert(pos, num)
    else:
        if num > B[len(B) - 1]:
            B.insert(len(B), num)
        else:
            while num > B[pos]:
                pos = pos + 1
            B.insert(pos, num)
            pos = 0
print(B)
