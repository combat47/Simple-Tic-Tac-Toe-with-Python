grid = list(input().replace('_', ' '))

print(f'''---------
| {grid[0]} {grid[1]} {grid[2]} |
| {grid[3]} {grid[4]} {grid[5]} |
| {grid[6]} {grid[7]} {grid[8]} |
---------''')

while True:
    try:
        x, y = (int(cell) for cell in input().split())
    except ValueError:
        print('You should enter numbers!')
        continue

    if x not in range(1, 4) or y not in range(1, 4):
        print('Coordinates should be from 1 to 3!')
        continue

    value = {1: y - x, 2: x + y, 3: x + y + 2}.get(x)
    if grid[value] != ' ':
        print('This cell is occupied! Choose another one!')
        continue

    grid[value] = 'X'
    break

print(f'''---------
| {grid[0]} {grid[1]} {grid[2]} |
| {grid[3]} {grid[4]} {grid[5]} |
| {grid[6]} {grid[7]} {grid[8]} |
---------''')
