from print_helpers import print_sudoku, print_graph
import json

# http://www.cs.kent.edu/~dragan/ST-Spring2016/SudokuGC.pdf

# sudoku_template = [
#   [5, 3, None, None, 7, None, None, None, None],
#   [6, None, None, 1, 9, 5, None, None, None],
#   [None, 9, 8, None, None, None, None, 6, None],
#   [8, None, None, None, 6, None, None, None, 3],
#   [4, None, None, 8, None, 3, None, None, 1],
#   [7, None, None, None, 2, None, None, None, 6],
#   [None, 6, None, None, None, None, 2, 8, None],
#   [None, None, None, 4, 1, 9, None, None, 5],
#   [None, None, None, None, 8, None, None, 7, 9]
# ]

sudoku_template = [
  [1, 12,  13,  14, 15, 16, 17, 18, 19],
  [2, 100, 102, None, None, None, None, None, None],
  [3, 103, 104, None, None, None, None, None, None],
  [4, None, None, None, None, None, None, None, None],
  [5, None, None, None, None, None, None, None, None],
  [6, None, None, None, None, None, None, None, None],
  [7, None, None, None, None, None, None, None, None],
  [8, None, None, None, None, None, None, None, None],
  [9, None, None, None, None, None, None, None, None]
]

class GraphVertex(object):
    def __init__(self, coordinate_x, coordinate_y, value):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.value = value

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
        graph = build_column_relationships(graph_key, graph, sudoku_matrix)

    graph = build_subset_relationships(graph, sudoku_matrix)

    return graph

def build_row_relationships(graph_key, graph, sudoku_matrix):
    coordinate_x = graph_key.coordinate_x

    for coordinate_y, row_value in enumerate(sudoku_matrix[coordinate_x]):
        vertex = find_vertex(graph, coordinate_x, coordinate_y)

        if vertex == graph_key:
            continue

        graph[graph_key] = list(dict.fromkeys(graph[graph_key] + [vertex]))

    return graph

def build_column_relationships(graph_key, graph, sudoku_matrix):
    coordinate_y = graph_key.coordinate_y

    for coordinate_x, row_value in enumerate(sudoku_matrix[coordinate_y]):
        vertex = find_vertex(graph, coordinate_x, coordinate_y)

        if vertex == graph_key:
            continue

        graph[graph_key] = list(dict.fromkeys(graph[graph_key] + [vertex]))

    return graph

def build_subset_relationships(graph, sudoku_matrix):
    subsets = []

    for index in [0, 3, 6]:
        subsets.append([
            [index,     index], [index,     index + 1], [index,     index + 2],
            [index + 1, index], [index + 1, index + 1], [index + 1, index + 2],
            [index + 2, index], [index + 2, index + 1], [index + 2, index + 2]
        ])

    # iterate over subsets
    for index in [0, 1, 2]:
        coordinates = subsets[index]

        # iterate over a given subset cooridates
        for coordinate in coordinates:
            vertex = find_vertex(graph, coordinate[0], coordinate[1])

            # for each coordinate, check it's neighbors and create a relation
            for coordinates_to_relate in coordinates:
                # print(coordinates_to_relate)
                vertex_to_relate = find_vertex(graph, coordinates_to_relate[0], coordinates_to_relate[1])

                if vertex == vertex_to_relate:
                    continue

                graph[vertex] = list(dict.fromkeys(graph[vertex] + [vertex_to_relate]))

    return graph

def build_graph(sudoku_matrix):
    graph = build_graph_keys(sudoku_matrix)
    complete_graph = build_relationships(graph, sudoku_matrix)
    return complete_graph


# print_sudoku(sudoku_template)
graph = build_graph(sudoku_template)
print_graph(graph)
