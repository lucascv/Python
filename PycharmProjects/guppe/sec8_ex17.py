def soma_algorismos(num1, num2):
    soma = 0
    if num1 and num2 > 0:
        while num1 > 0:
            resto = num1 % 10
            num1 = (num1 - resto) / 10
            soma = soma + resto
        while num2 > 0:
            resto = num2 % 10
            num2 = (num2 - resto) / 10
            soma = soma + resto
        return soma
    else:
        return 'Número nulo ou negativo.'


num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print(soma_algorismos(num1, num2))
