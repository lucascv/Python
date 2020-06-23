def desenho_triangulo(n):
    i = 1
    space = n
    while i <= n * 2:
        print(' ' * space, '*' * i, ' ' * space)
        i += 2
        space -= 1


n = int(input('Digite um número: '))
desenho_triangulo(n)
