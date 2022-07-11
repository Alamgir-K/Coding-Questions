def zero_matrix(matrix: list) -> str:
    """
    If an element in the MxN matrix is 0, its entire row and column are set to 0

    Time Complexity: O(MxN)
    Space Complexity: O(1)
    """
    def nullify_row(matrix, row):
        for j in range(0, len(matrix[0])):
            matrix[row][j] = 0

    def nullify_column(matrix, column):
        for i in range(0, len(matrix)):
            matrix[i][column] = 0

    row_zero_flag = False
    column_zero_flag = False

    # Check if first row has 0
    for j in range(0, len(matrix[0])):
        if matrix[0][j] == 0:
            row_zero_flag = True
            break

    # Check if first column has 0
    for i in range(0, len(matrix)):
        if matrix[i][0] == 0:
            column_zero_flag = True
            break
    
    # Check for zero in rest of matrix
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    # Nullify row based on first column values
    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            nullify_row(matrix, i)

    # Nullify column based on first row values
    for j in range(1, len(matrix[0])):
        if matrix[0][j] == 0:
            nullify_column(matrix, j)

    # Nullify first row
    if row_zero_flag:
        nullify_row(matrix, 0)

    # Nullify first column
    if column_zero_flag:
        nullify_column(matrix, 0)

    return matrix


def test_zero_matrix():
    m = [
        [1, 3, 5, 6, 8],
        [1, 0, 5, 6, 0],
        [1, 3, 5, 6, 8],
        [1, 3, 0, 6, 8],
    ]

    expected = [
        [1, 0, 0, 6, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 6, 0],
        [0, 0, 0, 0, 0],
    ]

    assert zero_matrix(m) == expected


if __name__ == "__main__":
    test_zero_matrix()
