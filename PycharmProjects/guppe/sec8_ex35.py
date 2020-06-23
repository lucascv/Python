def fatorial_quadruplo(n):
    """
    Esta função calcula fatorial quadruplo de um numero
    :param n: número digitado pelo usuário
    :return: resultado do fatorial quadruplo do número 'n'
    """
    if n > 0:
        resultado = 1
        i = 1
        while i <= n * 2:
            resultado *= i
            i += 1
        i = 1
        resultado1 = 1
        while i <= n:
            resultado1 *= i
            i += 1
        print(resultado1)
        print(resultado)
        return resultado / resultado1
    else:
        return 'Número nulo ou negativo.'


n = int(input('Digite um numero: '))
print(fatorial_quadruplo(n))
