A = []
cont = 0

while cont < 10:
    A.append(int(input('Digite um valor: ')))
    cont = cont + 1

print(A)

x = int(input("Digite o valor de 'x': "))
multiplos_x = 0

for num in A:
    if num % x == 0:
        print(num)
        multiplos_x = multiplos_x + 1

print(f'O número {x} possui {multiplos_x} múltiplos no vetor {A}')
