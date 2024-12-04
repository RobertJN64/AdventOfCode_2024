import util

def main():
    with open("Day04/day04.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])

    answer = 0

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            for xd, yd in [(-1,-1),(1,1),(1,-1),(-1,1),(0,1),(1,0),(0,-1),(-1,0)]:
                for d, letter in enumerate('XMAS'):
                    if util.out_of_bounds(lines, x+xd*d, y+yd*d) or lines[y+yd*d][x+xd*d] != letter:
                        break
                else:
                    answer += 1

    print(answer)