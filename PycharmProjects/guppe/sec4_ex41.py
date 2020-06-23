valor_hora = float(input('Digite o valor pago por hora de trabalho: '))
horas_trabalhadas = int(input('Digite a quantidade de horas trabalhadas: '))
bonus = 0.10
salario = valor_hora*horas_trabalhadas+(valor_hora*horas_trabalhadas*bonus)
print('O salário esse mês será de R$ {} reais.'.format(salario))
