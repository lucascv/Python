nota1 = float(input('Digite a primeira nota do aluno: '))
if 0 <= nota1 <= 10:
    nota2 = float(input('Digite a segunda nota do aluno: '))
    if 0 <= nota2 <= 10:
        media = (nota1+nota2)/2
        print('A média das notas do aluno é : {}'.format(media))
    else:
        print('Valor da segunda nota inválido.')
else:
    print('Valor da primeira nota inválido.')
