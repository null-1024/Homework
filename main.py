"""
布尔矩阵运算
join
meet
boolean_product
"""
import random
import time


def get_size(matrix):
    """
    get the row and column of matrix
    :param matrix:
    :return: tuple
    """
    # 1. row
    row = len(matrix)
    if row == 0:  # 空矩阵
        return 0, 0

    # 2. column
    column = len(matrix[0])
    for _ in matrix:  # 检查每行列数是否相等
        if len(_) != column:
            raise ValueError

    return row, column


def is_legal(matrix_a, matrix_b):
    """
    检查矩阵是否合法
    :return: True or False
    """
    try:
        if get_size(matrix_a) != get_size(matrix_b):
            print('different size')
            return False
    except ValueError:
        print('illegal value')
        return False

    return True


def join(matrix_a, matrix_b):
    if not is_legal(matrix_a, matrix_b):
        return

    # operation
    row, column = get_size(matrix_a)
    matrix_c = [[-1] * column for _ in range(row)]  # matrix_c init
    for r in range(row):
        for c in range(column):
            matrix_c[r][c] = 1 if (matrix_a[r][c] == 1 or matrix_b[r][c] == 1) else 0
    return matrix_c


def meet(matrix_a, matrix_b):
    if not is_legal(matrix_a, matrix_b):
        return

    # operation
    row, column = get_size(matrix_a)
    matrix_c = [[-1] * column for _ in range(row)]
    for r in range(row):
        for c in range(column):
            matrix_c[r][c] = 1 if (matrix_a[r][c] == 1 and matrix_b[r][c] == 1) else 0
    return matrix_c


def boolean_product(matrix_a, matrix_b):
    try:
        a_r, a_c = get_size(matrix_a)
        b_r, b_c = get_size(matrix_b)
        if a_c != b_r:
            print('the column of matrix_a != the row of matrix_b')
            return
    except ValueError:
        print('illegal value')
        return

    # operation
    matrix_c = [[0] * b_c for _ in range(a_r)]
    for r in range(a_r):
        for c in range(b_c):
            matrix_c[r][c] = 0 if (sum([matrix_a[r][i] * matrix_b[i][c] for i in range(a_c)]) == 0) else 1
    return matrix_c


def print_matrix(matrix):
    if matrix is None:
        return
    i = 1
    for _ in matrix:
        print(f'r{i}: ', _)
        i += 1


def main():
    """
    测试用例
    matrix_a = [[1, 1, 0], [0, 1, 0], [1, 1, 0], [0, 0, 1]]
    matrix_b = [[1, 0, 0, 0], [0, 1, 1, 0], [1, 0, 1, 1]]
    print_matrix(join(matrix_a, matrix_b))
    print_matrix(meet(matrix_a, matrix_b))
    print_matrix(boolean_product(matrix_a, matrix_b))
    """

    while True:
        # 随机生成矩阵
        dimension = range(random.randint(1, 3))
        matrix_a = [[random.randint(0, 1) for j in dimension] for i in dimension]
        matrix_b = [[random.randint(0, 1) for j in dimension] for i in dimension]
        # 显示运算
        print_matrix(matrix_a)
        print('join')
        print_matrix(matrix_b)
        print('=')
        print_matrix(join(matrix_a, matrix_b))
        if input('enter exit to stop: ') == 'exit':
            break


if __name__ == '__main__':
    main()
