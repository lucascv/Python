def super_fatorial(n):
    """
    Esta função calcula o superfatorial de um número
    :param n: numero digitado pelo usuário
    :return: resultado da operação
    """
    if n > 0:
        fatoriais = []
        i = 1
        while i <= n:
            fatoriais.append(i)
            i += 1
        print(fatoriais)
        i = 1
        resultado = 1
        while n > 0:
            while i <= fatoriais[n - 1]:
                resultado *= i
                i += 1
            i = 1
            n -= 1
        return resultado
    else:
        return 'Numero não é positivo.'


n = int(input('Digite um numero: '))
print(super_fatorial(n))
