def simplifica(numerador, denominador):
    """
    Esta função simplifica a fração informada pelo usuário
    :param numerador:
    :param denominador:
    :return: retorna o valor da fração simplificado
    """
    if numerador and denominador > 0:
        i = 2
        while i * i <= numerador and i * i <= denominador:
            if numerador % i == 0 and denominador % i == 0:
                numerador /= i
                denominador /= i
            else:
                i += 1
        return f'{numerador}/{denominador}'
    else:
        return 'Valor inválido'


numerador = int(input('Digite numerador: '))
denominador = int(input('Digite um denominador: '))
print(simplifica(numerador, denominador))
