def soma_algorismos(numero):
    """
    Esta função recebe um número e retorna a soma de todos seus algorismos.
    :param numero: Número digitado pelo usuário
    :return: Retorna a soma dos seus algorismos.
    """
    if numero > 0:
        soma = 0
        while numero > 0:
            resto = numero % 10
            numero = (numero - resto) / 10
            soma = soma + resto
        return soma
    return 'Número inválido'


numero = int(input('Digite um número: '))
print(soma_algorismos(numero))

