def fatorial(n):
    """
    Função para calcular o fatorial de um número.
    :param n: Número digitado pelo usuário
    :return: Retorna o resultado do fatorial do número 'n'
    """
    if n > 0:
        resultado = 1
        while n > 0:
            resultado = resultado * n
            n -= 1
        return resultado
    else:
        return 'Número inválido.'


n = int(input('Digite um número: '))
print(fatorial(n))
