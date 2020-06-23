def desenho_triangulo(n):
    """
    Esta função desenha um triângulo com '!' na quantidade de linhas informada pelo usuário
    """
    i = 1
    while i <= n:
        print('!' * i)
        i += 1


n = int(input('Digite um número: '))
desenho_triangulo(n)
