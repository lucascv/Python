from random import choice

bingo = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
num = 0

for l in range(0, 5):
    for c in range(0, 5):
        num = choice(range(0, 100))
        if num in bingo:
            num = 0
        else:
            bingo[l][c] = num
            print(f'[{bingo[l][c]:^5}]', end='')
    print()
