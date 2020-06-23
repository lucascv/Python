nota1 = float(input('Qual foi a primeira nota? '))
nota2 = float(input('Qual foi a segunda nota? '))
nota3 = float(input('Qual foi a terceira nota? '))
media = (nota1+nota2+(nota3*2))/3
if media >= 60:
    print(f'A média desse aluno foi de {media} e o mesmo está aprovado!')
else:
    print(f'A média desse aluno foi de {media} e o mesmo está reprovado!')
