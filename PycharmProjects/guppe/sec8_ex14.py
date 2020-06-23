def consumo_carro(distancia, consumo):
    if distancia / consumo < 8:
        return 'Venda o carro!'
    elif distancia / consumo > 12:
        return 'Super econômico!'
    return 'Econômico!'


distancia = float(input('Digite a distância percorrida em KM: '))
consumo = float(input('Digite quantos litros de gasolina foram consumidos: '))
print(consumo_carro(distancia, consumo))
