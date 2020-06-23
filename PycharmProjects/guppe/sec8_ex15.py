def triangulo(lado1, lado2, lado3):
    """
    Esta função recebe três valores e verifica se é possivel formar um triângulo com os mesmos. Além disso, informa
    também o tipo do triângulo que será criado.
    """
    tr = False
    if lado1 and lado2 and lado3 > 0:
        while tr is False:
            if lado1 < lado2 + lado3:
                if lado2 < lado1 + lado3:
                    if lado3 < lado1 + lado2:
                        tr = True
                    else:
                        return 'Não é possível formar triângulo.'
                else:
                    return 'Não é possivel formar triângulo.'
            else:
                return 'Não é possivel formar triângulo.'
        if lado1 == lado2 == lado3:
            return 'Triângulo Equilátero'
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return 'Triângulo Isósceles'
        return 'Triângulo Escaleno'
    else:
        return 'Um ou mais lados é(são) nulos ou negativos.'


lado1 = float(input('Digite o valor do primeiro lado: '))
lado2 = float(input('Digite o valor do segundo lado: '))
lado3 = float(input('Digite o valor do terceiro lado: '))
print(triangulo(lado1, lado2, lado3))



