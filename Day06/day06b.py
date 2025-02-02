import util
import line_profiler

# optimized with faster bounds checking + removing copies
# could be further optimized by only checking the path after the obstacle is added, or by being smarter about where obstacles go

@line_profiler.profile
def main():
    with open("Day06/day06.txt") as f:
        lines = [list(line.strip()) for line in f.readlines()]
    print(lines[0:10])

    x = 0
    y = 0
    c_dir = 'U'
    for y_index, line in enumerate(lines):
        if '^' in line:
            x = line.index('^')
            y = y_index
    start_pos = (x, y)

    MAX_X = len(lines[0])
    MAX_Y = len(lines)

    visited = set()

    while True:
        visited.add((x, y))
        last_pos = (x, y)
        if c_dir == 'U': #check forward
            y -= 1
        if c_dir == 'R':
            x += 1
        if c_dir == 'D':
            y += 1
        if c_dir == 'L':
            x -= 1

        if util.out_of_bounds(lines, x, y): #if outside maze then done
            break

        if lines[y][x] == '#': #if blocker turn right and revert position
            if c_dir == 'U':
                c_dir = 'R'
            elif c_dir == 'R':
                c_dir = 'D'
            elif c_dir == 'D':
                c_dir = 'L'
            elif c_dir == 'L':
                c_dir = 'U'

            x, y = last_pos

    answer = 0
    # each pos of visited could be a valid blocker
    for index, pos in enumerate(visited):
        if index%100 == 0:
            print(f"Progress: {round(index * 100 / len(visited))}%")

        #print("trying to put a blocker here", pos)
        x, y = start_pos
        c_dir = 'U'
        lines[pos[1]][pos[0]] = '#'
        t_visited = set()

        looped = False
        while True:
            t_visited.add((x, y, c_dir))
            last_pos = (x, y)
            if c_dir == 'U':  # check forward
                y -= 1
                if y < 0:
                    break
            if c_dir == 'R':
                x += 1
                if x >= MAX_X:
                    break
            if c_dir == 'D':
                y += 1
                if y >= MAX_Y:
                    break
            if c_dir == 'L':
                x -= 1
                if x < 0:
                    break


            if lines[y][x] == '#':
                if c_dir == 'U':
                    c_dir = 'R'
                elif c_dir == 'R':
                    c_dir = 'D'
                elif c_dir == 'D':
                    c_dir = 'L'
                elif c_dir == 'L':
                    c_dir = 'U'
                x, y = last_pos

            if (x, y, c_dir) in t_visited:
                looped = True
                break

        lines[pos[1]][pos[0]] = '.'
        if looped:
            answer += 1
    print(answer)


