km = int(input('Quantos KM foram percorridos com o veículo? '))
dias = int(input('Por quantas diárias o veículo foi alugado? '))
preco = (60*dias) + (0.15*km)
print('O valor total a pagar com {}km rodados e {} diárias é de R$ {:.2f}'.format(km, dias, preco))

