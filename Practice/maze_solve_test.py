import util


def main():
    with open("maze.txt") as f:
        lines = f.readlines()

    start_pos = (0,0)
    end_pos = (0,0)
    grid = []

    for index, line in enumerate(lines):
        grid.append(list(map(int, line.strip().replace("S", "0").replace("X", "0").split(','))))
        if "S" in line:
            start_pos = (line.split(',').index("S"), index)
        if "X" in line:
            end_pos = (line.split(',').index("X"), index)

    print(start_pos)
    print(end_pos)

    def c(n_x, n_y, x, y):
        return grid[n_y][n_x] == 0

    maze_costs = util.wavefront(grid, start_pos, end_pos, c)
    util.print_grid_spaced(maze_costs, 3)
    print(maze_costs[start_pos[1]][start_pos[0]] - 1)



if __name__ == '__main__':
    main()