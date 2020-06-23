def volume_cilindro(altura, raio):
    """
    Função que calcula o volume de um cilindro circular.
    :param altura: altura do cilindro circular.
    :param raio: raio do cilindro circular.
    :return: Retorna o volume deste cilindro
    """
    return 3.141592 * (raio ** 2) * altura


altura = float(input('Digite o valor da altura do cilindro: '))
raio = float(input('Digite o valor do raio do cilindro: '))
print(volume_cilindro(altura, raio))
