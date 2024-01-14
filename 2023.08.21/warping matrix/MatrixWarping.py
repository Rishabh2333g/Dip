import numpy as np

def matrix_warping(matrix, transformation_matrix, warping_choice):
    if warping_choice == "forward":
        warped_matrix = np.dot(transformation_matrix, matrix)
    elif warping_choice == "backward":
        warped_matrix = np.dot(np.linalg.inv(transformation_matrix), matrix)
    else:
        print("Invalid choice")
    return warped_matrix

# Generate a random input matrix
input_matrix = np.array([[1, 2],
                        [3, 4]])

# Generate a random transformation matrix
transformation_matrix = np.array([[2, 0],
                                  [0, 2]])

print("Input Matrix:\n", input_matrix)
print("Transformation Matrix:\n", transformation_matrix)

warped_matrix = matrix_warping(input_matrix, transformation_matrix, input("Enter 'forward' or 'backward' matrix warping: "))
print("Warped Matrix:\n", warped_matrix)
