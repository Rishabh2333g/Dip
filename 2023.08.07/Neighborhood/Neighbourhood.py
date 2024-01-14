import numpy as np

def get_neighborhood(matrix, row, col, neighbors):
    directions = {'N4': [(1, 0), (0, 1), (-1, 0), (0, -1)],
                  'Nd': [(1, 1), (-1, -1), (-1, 1), (1, -1)],
                  'N8': [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]}
    return [matrix[row + dr, col + dc] for direction in neighbors for dr, dc in directions[direction] if (0 <= row + dr < matrix.shape[0]) and (0 <= col + dc < matrix.shape[1]) and ('N4' in direction and abs(dr) + abs(dc) == 1 or 'N4' not in direction)]

matrix = np.random.randint(0, 50, size=(4, 4))
print("Generated Matrix:\n", matrix)

selected_row = int(input("Enter the row of the selected pixel: "))
selected_col = int(input("Enter the column of the selected pixel: "))
neighbors_option = input("Choose neighbors (N4, N8, Nd): ").split()

neighborhood = get_neighborhood(matrix, selected_row, selected_col, neighbors_option)
selected_pixel = matrix[selected_row, selected_col]

print(f"Selected Pixel: {selected_pixel}")
print(f"Selected Neighbors: {neighborhood}")
