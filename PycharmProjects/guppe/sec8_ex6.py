def calculo_segundos(horas, minutos, segundos):
    return horas*3600 + minutos*60 + segundos


horas = int(input('Digite quantidade de horas: '))
minutos = int(input('Digite quantidade de minutos: '))
segundos = int(input('Digite quantidade de segundos: '))
print(calculo_segundos(horas, minutos, segundos))
