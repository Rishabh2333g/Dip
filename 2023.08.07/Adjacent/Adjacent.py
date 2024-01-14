import random

def gen_matrix(rows, cols):
    return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

def print_matrix(matrix):
    for row in matrix:
        print(*row, sep=" ")

def get_adjacent_coords(matrix, x, y, rows, cols):
    adjacent_coords = [(x-1, y-1), (x-1, y), (x-1, y+1),
                       (x, y-1),             (x, y+1),
                       (x+1, y-1), (x+1, y), (x+1, y+1)]
    valid_adjacent = [c for c in adjacent_coords if 0 <= c[0] < rows and 0 <= c[1] < cols]
    return valid_adjacent

def main():
    rows, cols = map(int, input("Enter the number of rows and columns: ").split())
    matrix = gen_matrix(rows, cols)
    print_matrix(matrix)
    x, y = map(int, input("Enter the row and column indices: ").split())
    value = matrix[x][y]
    print(f"Pixel at ({x}, {y}): {value}")
    choice = int(input("Enter 1 for 4-adjacent, 2 for 8-adjacent, 3 for mixed-adjacent: "))
    adjacent_coords = get_adjacent_coords(matrix, x, y, rows, cols)
    if choice == 1:
        print("4-adjacent coordinates and values:")
        for i, j in adjacent_coords:
            print(f"({i}, {j}): {matrix[i][j]}")

    elif choice == 2:
        print("8-adjacent coordinates and values:")
        for i, j in adjacent_coords:
            print(f"({i}, {j}): {matrix[i][j]}")

    elif choice == 3:
        print("Mixed-adjacent coordinates and values:")
        for i, j in adjacent_coords:
            print(f"({i}, {j}): {matrix[i][j]}")

    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
