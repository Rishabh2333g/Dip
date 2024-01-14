import numpy as np

# Generate two random matrices
matrix_a, matrix_b = np.random.randint(0, 40, (3, 3)), np.random.randint(0, 40, (3, 3))

# Print the matrices
print("Matrix A:\n", matrix_a)
print("Matrix B:\n", matrix_b)

# Get the user input
operation = input("Select an operation (1: Add, 2: Subtract, 3: Multiply): ")

# Perform the operation
result = {
    "1": matrix_a + matrix_b,
    "2": matrix_a - matrix_b,
    "3": np.dot(matrix_a, matrix_b),
}.get(operation)

# Print the result
print(f"\nResult of {operation}:\n{result}")
