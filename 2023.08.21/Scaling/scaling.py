import numpy as np

# Initialize the input matrix
input_matrix = np.zeros((8, 8))

# Set the 4 coordinates with a value of 1
coordinates = [(2, 2), (2, 4), (4, 2), (4, 4)]
for coord in coordinates:
    input_matrix[coord] = 1

# Initialize the output matrix for scaling
output_matrix_scaling = np.zeros((8, 8))

# Scaling parameters
scale_x = 2
scale_y = 2

# Apply scaling transformation using loops
for i in range(8):
    for j in range(8):
        new_i = int(i * scale_y)
        new_j = int(j * scale_x)
        output_matrix_scaling[new_i:new_i+scale_y, new_j:new_j+scale_x] = input_matrix[i, j]

# Print the input and output matrices for scaling
print("Input Matrix:")
print(input_matrix)
print("\nOutput Matrix (Scaling):")
print(output_matrix_scaling)
