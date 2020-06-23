from random import choice

matriz1 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
matriz2 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

print(len(matriz1[0]))


def produto_matricial(matriz1, matriz2):
    """
    Esta função recebe duas matrizes quadradas e retorna a matriz que é prduto matricial das mesmas.
    """
    matriz3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    if len(matriz1) == len(matriz1[0]) and len(matriz2) == len(matriz2[0]):
        for l in range(0, 4):
            for c in range(0, 4):
                
    else:
        return 'Matriz não é quadrada.'

