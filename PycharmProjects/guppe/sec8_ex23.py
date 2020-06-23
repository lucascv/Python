def desenho_triangulo(n):
    i = 1
    while i < n:
        print('*' * i)
        i += 1
    while i > 0:
        print('*' * i)
        i -= 1


n = int(input('Digite um número: '))
desenho_triangulo(n)
