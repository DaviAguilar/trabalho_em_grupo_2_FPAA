import random

def create_grid(rows, cols):
    return [[1 if random.random() < 0.3 else 0 for _ in range(cols)] for _ in range(rows)]

def print_grid(grid):
    for row in grid:
        print(" ".join(f"{x:2}" for x in row))
    print()

def flood_fill(grid, x, y, color, rows, cols):
    if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] != 0:
        return
    grid[x][y] = color
    flood_fill(grid, x + 1, y, color, rows, cols)
    flood_fill(grid, x - 1, y, color, rows, cols)
    flood_fill(grid, x, y + 1, color, rows, cols)
    flood_fill(grid, x, y - 1, color, rows, cols)

def main():
    while True:
        try:
            rows = int(input("Enter number of rows (1-50): "))
            cols = int(input("Enter number of columns (1-50): "))
            if 1 <= rows <= 50 and 1 <= cols <= 50:
                break
            print("Rows and columns must be between 1 and 50.")
        except ValueError:
            print("Please enter valid integers.")

    grid = create_grid(rows, cols)
    print("\nInitial Grid:")
    print_grid(grid)

    while True:
        try:
            start_row = int(input(f"Enter starting row (0-{rows-1}): "))
            start_col = int(input(f"Enter starting column (0-{cols-1}): "))
            if 0 <= start_row < rows and 0 <= start_col < cols and grid[start_row][start_col] == 0:
                break
            print(f"Starting coordinates must be within grid bounds (0-{rows-1}, 0-{cols-1}) and navigable (value 0).")
        except ValueError:
            print("Please enter valid integers.")

    current_color = 2
    flood_fill(grid, start_row, start_col, current_color, rows, cols)
    current_color += 1

    while True:
        found = False
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    flood_fill(grid, i, j, current_color, rows, cols)
                    current_color += 1
                    found = True
                    break
            if found:
                break
        if not found:
            break

    print("Final Grid:")
    print_grid(grid)

if __name__ == "__main__":
    main()