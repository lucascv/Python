terça = 's'
while terça == 's':
    terça = str(input('Trabalhou terça? [S/N] '))
    if terça.lower() == 's':
        terça = True
    elif terça.lower() == 'n':
        terça = False
    else:
        terça = 's'
        print('Digite um valor válido.')
quinta = 's'
while quinta == 's':
    quinta = str(input('Trabalhou quinta? [S/N] '))
    if quinta.lower() == 's':
        quinta = True
    elif quinta.lower() == 'n':
        quinta = False
    else:
        quinta = 's'
        print('Digite um valor válido.')
if terça == True and quinta == True:
    print("Comprar TV50' e tomar sorvete.")
elif terça or quinta == True:
    print("Comprar TV32' e tomar sorvete.")
else:
    print('Ficar em casa')
