from print_helpers import print_sudoku, print_graph
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

def build_graph_keys(sudoku_matrix):
    graph = {}

    for i in range(9):
        for j in range(9):
            graph_vertex = GraphVertex(i, j, sudoku_matrix[i][j])
            graph[graph_vertex] = []

    return graph

def find_vertex(graph, coordinate_x, coordinate_y):
    for vertex in graph.keys():
        if vertex.coordinate_x == coordinate_x and vertex.coordinate_y == coordinate_y:
            return vertex

def build_relationships(graph, sudoku_matrix):
    for graph_key in graph.keys():
        graph = build_row_relationships(graph_key, graph, sudoku_matrix)
        # graph = build_colum_relationships(graph_key, graph, sudoku_matrix)
        # graph = build_subset_relationships(graph_key, graph, sudoku_matrix)

    pass

def build_row_relationships(graph_key, graph, sudoku_matrix):
    coordinate_x = graph_key.coordinate_x

    for coordinate_y, row_value in enumerate(sudoku_matrix[coordinate_x]):
        vertex = find_vertex(graph, coordinate_x, coordinate_y)
        graph[graph_key] = graph[graph_key] + [vertex]

    return graph

def build_graph(sudoku_matrix):
    graph = build_graph_keys(sudoku_matrix)
    complete_graph = build_relationships(graph, sudoku_matrix)
    return graph


# print_sudoku(sudoku_template)
graph = build_graph(sudoku_template)
print_graph(graph)
