def operacao_mat(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return  num1 - num2
    elif operacao == '/':
        return num1 / num2
    elif operacao == '*':
        return num1 * num2
    return 'Operação inválida'


num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
operacao = str(input('Digite a operação: Adição(+), Subtração(-), Multiplicação(*), Divisão(/): '))

print(operacao_mat(num1, num2, operacao))
