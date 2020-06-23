def dobro_numero(numero):
    """Retorna o dobro do número informado"""
    return f'O dobro do {numero} é {numero * 2}'


numero = int(input('Digite um número: '))
print(dobro_numero(numero))
