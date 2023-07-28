from random import randint

def matrix_gen(rows: int, columns: int):
    matrix = []
    for i in range(rows):
        matrix_column = []
        for j in range(columns):
            matrix_column.append(None)
        matrix.append(matrix_column)
    return matrix

def matrix_filling(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = randint(0, 99)

def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
    print("\n")
def matrix_transpones(matrix):
    t_matrix = matrix_gen(len(matrix[0]), len(matrix))

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            t_matrix[len(matrix[0])-j-1][i] = matrix[i][j]
    return t_matrix


rows = 10
columns = 5


matrix = matrix_gen(rows, columns)

matrix_filling(matrix)

print_matrix(matrix)
          
t_matrix = matrix_transpones(matrix)

print_matrix(t_matrix)