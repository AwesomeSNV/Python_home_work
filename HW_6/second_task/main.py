def check_queens(positions):
    result = True
    for i in range(len(positions)):
        row_1, col_1 = positions[i]
        for j in range(i + 1, len(positions)):
            row_2, col_2 = positions[j]
            if row_1 == row_2 or col_1 == col_2 or abs(row_1 - row_2) == abs(col_1 - col_2):
                result = False
                break
    return result


if __name__ == "__main__":
    positions = [(4,1), (8,2), (1,3), (3,4), (6,5), (2,6), (7,7), (5,8)]
    print(check_queens(positions))