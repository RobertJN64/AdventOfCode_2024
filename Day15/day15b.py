import copy

import util

d = {
    '^': (0, -1),
    'v': (0, 1),
    '<': (-1, 0),
    '>': (1, 0)
}

class Status:
    SCAN = 0
    OK_TO_MOVE = 1
    BLOCKED = 2

def main():
    with open("Day15/day15.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])

    grid = []
    cmds = ''

    for line in lines:
        if line.startswith('#'):
            grid.append(list(line
                             .replace('#', '##')
                             .replace('O', '[]')
                             .replace('.', '..')
                             .replace('@', '@.')
                             ))
        else:
            cmds += line

    util.print_grid(grid)
    print(cmds)

    pos = [-1, -1]
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == '@':
                pos = [x, y]
                row[x] = '.'

    print(pos)

    for counter, cmd in enumerate(cmds):
        direction = d[cmd]

        x_vals_to_check = [pos[0]]
        scan_y = pos[1]
        grid[scan_y][pos[0]] = '.'

        pos_to_move = []

        while True:
            scan_y += direction[1]
            if direction[0] != 0:
                x_vals_to_check[0] += direction[0]

            next_to_check = set()
            status = Status.OK_TO_MOVE
            for x_to_check in x_vals_to_check:
                if grid[scan_y][x_to_check] == '#':
                    status = Status.BLOCKED
                    break

                elif grid[scan_y][x_to_check] == '.':
                    pass # status is already OK TO MOVE

                elif cmd in '<>' and grid[scan_y][x_to_check] in '[]':
                    if grid[scan_y][x_to_check] == '[':
                        pos_to_move.append((x_to_check, scan_y))
                        pos_to_move.append((x_to_check + 1, scan_y))
                    if grid[scan_y][x_to_check] == ']':
                        pos_to_move.append((x_to_check, scan_y))
                        pos_to_move.append((x_to_check - 1, scan_y))
                    status = Status.SCAN
                    next_to_check.add(x_to_check + direction[0])

                elif cmd in '^v' and grid[scan_y][x_to_check] in '[]':
                    if grid[scan_y][x_to_check] == '[':
                        pos_to_move.append((x_to_check, scan_y))
                        pos_to_move.append((x_to_check + 1, scan_y))
                        next_to_check.add(x_to_check + 1)
                    if grid[scan_y][x_to_check] == ']':
                        pos_to_move.append((x_to_check, scan_y))
                        pos_to_move.append((x_to_check - 1, scan_y))
                        next_to_check.add(x_to_check - 1)

                    status = Status.SCAN
                    next_to_check.add(x_to_check)

                else:
                    raise Exception("INVALID TILE")

            x_vals_to_check = list(next_to_check)
            if status == Status.OK_TO_MOVE:
                pos[0] += direction[0]
                pos[1] += direction[1]
                break

            if status == Status.BLOCKED:
                break


        if status == Status.OK_TO_MOVE:
            moved = set()
            for (old_x, old_y) in reversed(pos_to_move):
                if (old_x, old_y) in moved:
                    continue
                moved.add((old_x, old_y))
                grid[old_y + direction[1]][old_x + direction[0]] = grid[old_y][old_x]
                grid[old_y][old_x] = '.'

    t_grid = copy.deepcopy(grid)
    t_grid[pos[1]][pos[0]] = '@'
    util.print_grid(t_grid)

    gps = 0
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == '[':
                gps += 100 * y + x
    print(gps)
