def positivo_negativo(numero):
    """Função para verificar se o número é positivo ou negativo
    - Retorna 1 para positivo;
    - Retorna -1 para negativo;
    - Retorna 0 para zero."""
    if numero == 0:
        return 0
    elif numero % 2 == 0:
        return 1
    return -1


numero = int(input('Digite um número: '))
print(positivo_negativo(numero))
