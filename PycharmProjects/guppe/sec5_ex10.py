altura = float(input('Digite o valor da altura em metros: '))
sexo = str(input('Masculino/Feminino? '))
if sexo.lower() == 'masculino':
    peso_ideal = (72.7*altura)-58
    print(f'O peso ideal será de {peso_ideal}')
elif sexo.lower() == 'feminino':
    peso_ideal = (62.1*altura)-44.7
    print(f'O peso ideal será de {peso_ideal}')
else:
    print('Sexo informado está incorreto.')

