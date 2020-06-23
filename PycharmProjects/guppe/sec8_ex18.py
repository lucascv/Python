def potencia(x, z):
    """
    Esta função recebe dois valores e retorna o resultado do primeiro sobre a potencia do segundo.
    :param x: base
    :param z: potência
    :return: Resultado da operação
    """
    return x ** z


x = int(input('Digite um valor: '))
z = int(input('Digite outro valor: '))
print(potencia(x, z))
