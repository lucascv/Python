def data_atual (dia, mes, ano):
    meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
             9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}

    return f'{dia} de {meses[mes]} de {ano}.'


dia = int(input('Dia: '))
mes = int(input('Mes: '))
ano = int(input('Ano: '))

print(data_atual(dia, mes, ano))
