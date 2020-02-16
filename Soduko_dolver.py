# this code will solve all soduko Puzzle
# this code was write by Shahriar_panda

import numpy as np

# first we need to define our soduko Puzzle
soduk = [[0, 0, 8, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 8, 0, 0, 5, 2, 7],
         [0, 0, 0, 6, 0, 3, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 7, 0, 5, 0],
         [0, 6, 0, 3, 0, 0, 0, 7, 4],
         [7, 3, 0, 0, 1, 0, 0, 4, 0],
         [1, 0, 0, 0, 5, 2, 0, 9, 0],
         [5, 0, 2, 0, 0, 0, 0, 0, 0]]

print(np.array(soduk))


# This Function Check if the Suggestion n is Suit the given x-y cell or not
def possible(y, x, n):
    global soduk
    for i in range(0, 9):
        if soduk[y][i] == n:
            return False
    for i in range(0, 9):
        if soduk[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if soduk[y0 + i][x0 + j] == n:
                return False
    return True


print(possible(4, 4, 3))
print(possible(4, 4, 5))


# This Function will solve the Puzzle
def solve():
    global soduk
    for y in range(9):
        for x in range(9):
            if soduk[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        soduk[y][x] = n
                        solve()
                        soduk[y][x] = 0
                return
    print(np.array(soduk))
    input('More?')


solve()
