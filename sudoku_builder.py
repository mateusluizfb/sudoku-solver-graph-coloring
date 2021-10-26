import json

sudoku_template = [
  [5, 3, None, None, 7, None, None, None, None],
  [6, None, None, 1, 9, 5, None, None, None],
  [None, 9, 8, None, None, None, None, 6, None],
  [8, None, None, None, 6, None, None, None, 3],
  [4, None, None, 8, None, 3, None, None, 1],
  [7, None, None, None, 2, None, None, None, 6],
  [None, 6, None, None, None, None, 2, 8, None],
  [None, None, None, 4, 1, 9, None, None, 5],
  [None, None, None, None, 8, None, None, 7, 9]
]

class GraphVertex(object):
    def __init__(self, coordinate_x, coordinate_y, value):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.value = value

# http://www.cs.kent.edu/~dragan/ST-Spring2016/SudokuGC.pdf

def print_sudoku(sudoku_matrix):
    print('---------------------------------------------------------------------------------')
    print(f'{sudoku_matrix[0][0]} {sudoku_matrix[0][1]} {sudoku_matrix[0][2]}   |   {sudoku_matrix[0][3]} {sudoku_matrix[0][4]} {sudoku_matrix[0][5]}   |   {sudoku_matrix[0][6]} {sudoku_matrix[0][7]} {sudoku_matrix[0][8]}')
    print(f'{sudoku_matrix[1][0]} {sudoku_matrix[1][1]} {sudoku_matrix[1][2]}   |   {sudoku_matrix[1][3]} {sudoku_matrix[1][4]} {sudoku_matrix[1][5]}   |   {sudoku_matrix[1][6]} {sudoku_matrix[1][7]} {sudoku_matrix[1][8]}')
    print(f'{sudoku_matrix[2][0]} {sudoku_matrix[2][1]} {sudoku_matrix[2][2]}   |   {sudoku_matrix[2][3]} {sudoku_matrix[2][4]} {sudoku_matrix[2][5]}   |   {sudoku_matrix[2][6]} {sudoku_matrix[2][7]} {sudoku_matrix[2][8]}')
    print('---------------------------------------------------------------------------------')
    print(f'{sudoku_matrix[3][0]} {sudoku_matrix[3][1]} {sudoku_matrix[3][2]}   |   {sudoku_matrix[3][3]} {sudoku_matrix[3][4]} {sudoku_matrix[3][5]}   |   {sudoku_matrix[3][6]} {sudoku_matrix[3][7]} {sudoku_matrix[3][8]}')
    print(f'{sudoku_matrix[4][0]} {sudoku_matrix[4][1]} {sudoku_matrix[4][2]}   |   {sudoku_matrix[4][3]} {sudoku_matrix[4][4]} {sudoku_matrix[4][5]}   |   {sudoku_matrix[4][6]} {sudoku_matrix[4][7]} {sudoku_matrix[4][8]}')
    print(f'{sudoku_matrix[5][0]} {sudoku_matrix[5][1]} {sudoku_matrix[5][2]}   |   {sudoku_matrix[5][3]} {sudoku_matrix[5][4]} {sudoku_matrix[5][5]}   |   {sudoku_matrix[5][6]} {sudoku_matrix[5][7]} {sudoku_matrix[5][8]}')
    print('---------------------------------------------------------------------------------')
    print(f'{sudoku_matrix[6][0]} {sudoku_matrix[6][1]} {sudoku_matrix[6][2]}   |   {sudoku_matrix[6][3]} {sudoku_matrix[6][4]} {sudoku_matrix[6][5]}   |   {sudoku_matrix[6][6]} {sudoku_matrix[6][7]} {sudoku_matrix[6][8]}')
    print(f'{sudoku_matrix[7][0]} {sudoku_matrix[7][1]} {sudoku_matrix[7][2]}   |   {sudoku_matrix[7][3]} {sudoku_matrix[7][4]} {sudoku_matrix[7][5]}   |   {sudoku_matrix[7][6]} {sudoku_matrix[7][7]} {sudoku_matrix[7][8]}')
    print(f'{sudoku_matrix[8][0]} {sudoku_matrix[8][1]} {sudoku_matrix[8][2]}   |   {sudoku_matrix[8][3]} {sudoku_matrix[8][4]} {sudoku_matrix[8][5]}   |   {sudoku_matrix[8][6]} {sudoku_matrix[8][7]} {sudoku_matrix[8][8]}')
    print('---------------------------------------------------------------------------------')


def build_graph_keys(sudoku_matrix):
    graph = {}

    for i in range(8):
        for j in range(8):
            graph_vertex = GraphVertex(i, j, sudoku_matrix[i][j])
            graph[graph_vertex] = []

    return graph

def build_relationships(graph, sudoku_matrix):

    pass

def build_graph(sudoku_matrix):
    graph = build_graph_keys(sudoku_matrix)
    complete_graph = build_relationships(graph, sudoku_matrix)



    return graph
