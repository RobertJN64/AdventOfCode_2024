import util

def main():
    with open("Day04/day04.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])

    answer = 0

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if util.out_of_bounds(lines, x-1, y-1) or util.out_of_bounds(lines, x+1, y+1):
                continue

            if lines[y][x] == 'A':
                if lines[y-1][x-1] == 'M' and lines[y+1][x+1] == 'S':
                    if lines[y + 1][x - 1] == 'M' and lines[y - 1][x + 1] == 'S':
                        answer += 1
                    if lines[y + 1][x - 1] == 'S' and lines[y - 1][x + 1] == 'M':
                        answer += 1
                if lines[y-1][x-1] == 'S' and lines[y+1][x+1] == 'M':
                    if lines[y + 1][x - 1] == 'M' and lines[y - 1][x + 1] == 'S':
                        answer += 1
                    if lines[y + 1][x - 1] == 'S' and lines[y - 1][x + 1] == 'M':
                        answer += 1

    print(answer)