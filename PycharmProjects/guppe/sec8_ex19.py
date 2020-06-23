def maior_fator_primo(n):
    i = 2
    lista = []
    while i * i <= n:
        if n % i == 0:
            n = n / i
            lista.append(i)
        else:
            i = i + 1
    print(lista)
    return n


n = int(input('Digite um número: '))
print(maior_fator_primo(n))
