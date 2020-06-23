def somatorio_n(n):
    """
    Esta função soma os algorismos de 1 até o 'n' informado pelo usuário
    :param n: valor informado pelo usuário
    :return: soma de 1 até 'n'
    """
    if n > 0:
        i = 1
        soma = 0
        while i <= n:
            soma = soma + i
            i += 1
        return soma
    else:
        return 'Número inválido'


n = int(input('Digite um número: '))
print(somatorio_n(n))
