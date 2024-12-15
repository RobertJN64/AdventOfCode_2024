import copy

import util

d = {
    '^': (0, -1),
    'v': (0, 1),
    '<': (-1, 0),
    '>': (1, 0)
}

def main():
    with open("Day15/day15.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])

    grid = []
    cmds = ''

    for line in lines:
        if line.startswith('#'):
            grid.append(list(line))
        else:
            cmds += line

    util.print_grid(grid)
    print('.')
    print(cmds)

    pos = [-1, -1]
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == '@':
                pos = [x, y]
                row[x] = '.'
    print(pos)

    for cmd in cmds:
        print("MOVE", cmd)
        direction = d[cmd]
        scan_x = pos[0]
        scan_y = pos[1]
        grid[scan_y][scan_x] = '.'

        block_stack = 0
        while True:
            scan_x += direction[0]
            scan_y += direction[1]
            if grid[scan_y][scan_x] == '#':
                #print('blocked')
                block_stack = 0
                break
            elif grid[scan_y][scan_x] == '.':
                #print('valid')
                pos[0] += direction[0]
                pos[1] += direction[1]
                break
            elif grid[scan_y][scan_x] == 'O':
                #print('block stack')
                block_stack += 1
            else:
                raise Exception("INVALID TILE")

        #print("need to move blocks", block_stack)
        for i in range(0, block_stack):
            grid[scan_y][scan_x] = 'O'
            scan_x -= direction[0]
            scan_y -= direction[1]

        # t_grid = copy.deepcopy(grid)
        # t_grid[pos[1]][pos[0]] = '@'
        # util.print_grid(t_grid)

    gps = 0
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == 'O':
                gps += 100 * y + x
    print(gps)

