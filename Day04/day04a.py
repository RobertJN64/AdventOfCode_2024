import util

def main():
    with open("Day04/day04.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])

    rotated_grid = []
    for line in lines[0]:
        rotated_grid.append('')
    for line in lines:
        for index, c in enumerate(line):
            rotated_grid[index] += c

    util.print_grid(rotated_grid)

    answer = 0
    for line in lines:
        answer += line.count('XMAS')
        answer += line.count('SAMX')

    for line in rotated_grid:
        answer += line.count('XMAS')
        answer += line.count('SAMX')

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            try:
                if lines[y][x] == 'X' and lines[y+1][x+1] == 'M' and lines[y+2][x+2] == 'A' and lines[y+3][x+3] == 'S':
                    answer += 1
            except:
                pass

            try:
                if x - 3 < 0:
                    pass

                else:
                    if lines[y][x] == 'X' and lines[y+1][x-1] == 'M' and lines[y+2][x-2] == 'A' and lines[y+3][x-3] == 'S':
                        answer += 1
            except:
                pass

            try:
                if y - 3 < 0:
                    pass
                else:
                    if lines[y][x] == 'X' and lines[y-1][x+1] == 'M' and lines[y-2][x+2] == 'A' and lines[y-3][x+3] == 'S':
                        answer += 1


            except:
                pass

            try:
                if y - 3 < 0 or x - 3 < 0:
                    pass
                else:

                    if lines[y][x] == 'X' and lines[y-1][x-1] == 'M' and lines[y-2][x-2] == 'A' and lines[y-3][x-3] == 'S':
                        answer += 1

            except:
                pass

    print(answer)