salario = float(input('Digite o salário: '))
prest = float(input('Digite o valor da prestação: '))
if prest > salario*0.2:
    print('Empréstimo não concedido.')
else:
    print('Empréstimo autorizado.')
