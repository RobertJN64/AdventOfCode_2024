import util

def main():
    with open("Day18/day18.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])

    MAX = 70

    grid = [['.'] * (MAX+1) for _ in range(MAX+1)]

    for row in lines[:1024]:
        x, y = map(int, row.split(','))
        grid[y][x] = '#'

    def constraint(nx, ny, _, __):
        return grid[ny][nx] == '.'

    util.print_grid(grid)
    print(util.wavefront(grid, (0,0), (MAX,MAX), constraint)[0][0] - 1)