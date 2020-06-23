def quantidade_primos(n):
    """
    Esta função calcula quantos números primos existem abaixo do número digitado pelo usuário.
    :param n: número digitado pelo usuário
    :return: quantidade de números primos abaixo do 'n'
    """
    i = 1
    n2 = 1
    primos = 0
    primos2 = 0
    while n2 < n:
        while i <= n2:
            if n2 % i == 0:
                primos2 += 1
                i += 1
            else:
                i += 1
        if primos2 == 2:
            primos += 1
            primos2 = 0
            n2 += 1
            i = 1
        else:
            primos2 = 0
            n2 += 1
            i = 1
    return primos


n = int(input('Digite um número: '))
print(quantidade_primos(n))
