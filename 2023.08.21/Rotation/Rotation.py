import numpy as np

def rotate_matrix(matrix, angle):
    if len(matrix) == 0:
        return []

    rows, cols = len(matrix), len(matrix[0])

    rotated_matrix = []

    if angle == 90:
        rotated_matrix = [[0] * rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                rotated_matrix[j][rows - i - 1] = matrix[i][j]

    else:
        print("Invalid angle. Supported angles are 90.")
        return []

    return rotated_matrix

current_matrix = np.random.randint(0, 40, size=(4, 4))

while True:
    print("Matrix:\n", current_matrix)

    current_matrix = rotate_matrix(current_matrix, 90)

    print("Rotated Matrix:")
    for row in current_matrix:
        print(row)

    continue_option = input("Do you want to continue rotating? (yes/no): ")
    if continue_option.lower() != 'yes':
        break

# Print the rotated matrix
for row in rotated_matrix:
    print(row)
