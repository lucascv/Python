def quadrado_perfeito(numero):
    """
    Função para verificar se o número é um quadrado perfeito.
    :param numero: número inteiro posivito.
    :return: retorna se o número é quadrado perfeito ou nao.
    """
    raiz = int(numero ** (1/2))
    if (raiz ** 2) == numero:
        return f'O número {numero} é um quadrado perfeito!'
    return f'O número {numero} NÃO é um quadrado perfeito.'


numero = int(input('Digite um número: '))
print(quadrado_perfeito(numero))
