def fatorial_duplo(n):
    """
    Esta função calcula fatorial duplo de um número impar informado pelo usuário
    :param n: número informado pelo usuário
    :return: retorna o resultado do fatorial duplo de 'n'
    """
    if n > 0:
        if n % 2 != 0:
            resultado = 1
            i = 1
            while i <= n:
                if i % 2 != 0:
                    resultado *= i
                    i += 1
                else:
                    i += 1
            return resultado
        else:
            return 'Número digitado é PAR.'
    else:
        return 'Número nulo ou negativo.'


n = int(input('Digite um número: '))
print(fatorial_duplo(n))
