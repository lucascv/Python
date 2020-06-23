distancia = float(input('Digite a distância em metros: '))
print('A medida de {:.2f}m corresponde a {:.3f}km, {:.2f}hm, {:.1f} dam, {:.0f}dm, {:.0f}cm, {:.0f}mm'.format(distancia, (distancia*0.001), (distancia*0.01), (distancia*0.1), (distancia*10), (distancia*100), (distancia*1000)))
