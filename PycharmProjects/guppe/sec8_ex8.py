from math import sqrt

def hipotenusa(a, b):
    """
    Função que calcula o valor da hipotenusa a partir dos valores dos catetos
    :param a: valor do primeiro cateto
    :param b: valor do segundo cateto
    :return: Retorna o valor da hipotenusa
    """
    return sqrt((a ** 2) + (b ** 2))


a = float(input('Digite o valor do primeiro cateto: '))
b = float(input('Digite o valor do segundo cateto: '))
print(hipotenusa(a, b))
