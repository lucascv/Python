def numero_maior(num1, num2):
    """
    Função que recebe dois números e retorna qual é o maior.
    :param num1: primeiro número
    :param num2: segundo número
    :return: Retorna o maior. Se forem iguais a função irá informar
    """
    if num1 == num2:
        return 'Os números são iguais.'
    elif num1 > num2:
        return f'O número {num1} é maior que {num2}.'
    return f'O número {num2} é maior que {num1}.'


num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
print(numero_maior(num1, num2))
