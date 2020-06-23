def conversao_temperatura(celsius):
    """
    Função para converter temperatura de Celsius para Fahrenheit.
    :param celsius: temperatura em graus Celsius
    :return: Retorna a temperatura convertida em Fahrenheit
    """
    return celsius * (9/5) + 32


celsius = float(input('Digite a temperatura em Celsius: '))
print(conversao_temperatura(celsius))
