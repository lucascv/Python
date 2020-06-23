def soma_do_fatorial(n):
    """
    Esta função recebe um número pelo usuário e calcula a soma dos algorismos do seu fatorial
    :param n:
    :return:
    """
    if n > 0:
        resultado = 1
        i = 1
        while i <= n:
            resultado *= i
            i += 1
        soma = 0
        while resultado > 0:
            resto = resultado % 10
            resultado = (resultado - resto) / 10
            soma = soma + resto
        return soma
    else:
        return 'Número inválido'


n = int(input('Digite um numero: '))
print(soma_do_fatorial(n))
