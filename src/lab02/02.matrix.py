from ..lib import testing

def rect(mat: list[list[int | float]]): # функция для проверки прямоугольности матрицы
    if len(mat) == 0:
            return []
         
    row_len = len(mat[0])
    for row in mat:
        if len(row) != row_len:
            raise ValueError('Рваная матрица')

def transpose(mat: list[list[int | float]]) -> list[list]:
    rect(mat)
    # Транспонируем с помощью zip(*mat).
    # Функция zip возвращает кортежы, преобразуем listом.
    return [list(x) for x in zip(*mat)]

def row_sums(mat: list[list[float | int]]):

    rect(mat)

    return [sum(x) for x in mat]

def col_sums(mat: list[list[float | int]]):
    rect(mat)

    return [sum(x) for x in transpose(mat)]

test_transpose=[
    [[1, 2, 3]],
    [[1], [2], [3]],
    [[1, 2], [3, 4]],
    [],
    [[1, 2], [3]]
]

test_row_sums=[
    [[1, 2, 3], [4, 5, 6]],
    [[-1, 1], [10, -10]],
    [[0, 0], [0, 0]],
    [[1, 2], [3]]
]

test_col_sums=[
    [[1, 2, 3], [4, 5, 6]],
    [[-1, 1], [10, -10]], 
    [[0, 0], [0, 0]],
    [[1, 2], [3]]
]
print("TRANSPOSE")
testing(transpose,test_transpose)
print()
print("ROW_SUMS")
testing(row_sums,test_row_sums)
print()
print("COL_SUMS")
testing(col_sums,test_col_sums)
