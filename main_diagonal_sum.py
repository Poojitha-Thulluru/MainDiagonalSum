def main_diagonal_sum(input_matrix: list, n_rows: int, n_columns: int) -> int:
    diagonal_sum: int = 0
    for row in range(rows):
        diagonal_sum += input_matrix[row][row]
    return diagonal_sum


try:
    given_list = list(map(int, input("Enter number of rows, number of columns and elements that are to be inserted "
                                     "into the matrix : ").split()))
    mat = given_list[2:]
    rows, columns = given_list[0], given_list[1]
    matrix = []
    if rows == columns:
        while mat:
            matrix.append(mat[:rows])
            mat = mat[rows:]
    else:
        print("Please ensure that the number of rows and the number of columns are same")
    print("The Main Diagonal Sum of the given matrix is : ", main_diagonal_sum(matrix, rows, columns))
except ValueError:
    print("Invalid Input. Please enter only integers")
