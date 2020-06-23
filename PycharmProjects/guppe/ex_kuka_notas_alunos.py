nota = input('Digite o valor da nota: ')
nota = float(nota)
while nota is float:
    if 0 < nota <= 1:
        print('E-')
    elif 1 < nota <= 2:
        print('E+')
    elif 2 < nota <= 3:
        print('D-')
    elif 3 < nota <= 4:
        print('D+')
    elif 4 < nota <= 5:
        print('C-')
    elif 5 < nota <= 6:
        print('C+')
    elif 6 < nota <= 7:
        print('B-')
    elif 7 < nota <= 8:
        print('B+')
    elif 8 < nota <= 9:
        print('A-')
    elif 9 < nota <= 10:
        print('A+')
    else:
        print('Valor digitado está errado.')
