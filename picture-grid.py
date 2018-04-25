import pdb

def list_heart(grid):
    heart_grid = []
    
    for i in range(len(grid[0])):
        dummy_list = []

        for j in range(len(grid)):
            dummy_list.append(grid[j][i])

        heart_grid.append(dummy_list)
        
    return heart_grid

def print_heart(grid):
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            pdb.set_trace()
            print(grid[j][i], end='')
        print()

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

print(list_heart(grid))
print_heart(grid)
