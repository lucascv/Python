def notas(nota1, nota2, nota3, letra):
    """
    Esta função recebe as notas do aluno e uma letra para informar o que o usuário deseja.
    :param nota1: Primeira nota do aluno
    :param nota2: Segunda nota do aluno
    :param nota3: Terceira nota do aluno
    :param letra: Se receber A, calcula a média aritmética das notas. Se P, média ponderada, com pesos 5, 3 e 2.
    :return: Retorna a média desejada.
    """
    if letra == 'A':
        return (nota1 + nota2 + nota3) / 3
    elif letra == 'P':
        return ((nota1 * 5) + (nota2 * 3) + (nota3 * 2)) / 3
    return 'Parâmetro digitado inválido.'


nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
nota3 = float(input('Digite a 3ª nota: '))
letra = str(input('Digite A para média aritimética ou P para média ponderada: '))
print(notas(nota1, nota2, nota3, letra.upper()))
