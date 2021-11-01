import random
from random import sample

def create_sudoku_game():
    base  = 3
    side  = base*base
    rangeBase = range(base)
    rows  = [ g*base + r for g in sample(rangeBase, len(rangeBase)) for r in sample(rangeBase, len(rangeBase)) ]
    cols  = [ g*base + c for g in sample(rangeBase, len(rangeBase)) for c in sample(rangeBase, len(rangeBase)) ]
    values = range(1, base * base + 1)
    nums  = sample(values, len(values))
    board = [ [nums[((base * (r % base) + r//base + c) % side)] for c in cols] for r in rows ]
    return board

def game_with_blank_spaces(board):
    random_temp = []
    coordinates = [[x, y] for x in range(9) for y in range(9)]

    for i in range(30):
        random_row = random.choice(coordinates)
        board[random_row[0]][random_row[1]] = None
        coordinates.remove(random_row)

    return board
