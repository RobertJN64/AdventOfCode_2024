import util

def safe_int(x):
    if x == '.':
        return -1
    else:
        return int(x)

def main():
    with open("Day10/day10.txt") as f:
        lines = [list(map(safe_int, line.strip())) for line in f.readlines()]
    print(lines[0:10])

    trailheads = []
    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if c == 0:
                trailheads.append((x,y))

    answer = 0

    for trailhead in trailheads:
        visited = set()
        to_check = [trailhead]
        score = 0

        while len(to_check):
            x, y = to_check.pop()
            if (x, y) in visited:
                continue

            if lines[y][x] == 9:
                score += 1
                #print("Found 9 at ", x, y)

            visited.add((x, y))

            for dx, dy in util.cardinal:
                n_x = x + dx
                n_y = y + dy
                if not util.out_of_bounds(lines, n_x, n_y) and lines[y][x] + 1 == lines[n_y][n_x]:
                    to_check.append((n_x, n_y))


        print(score)
        answer += score

    print(answer)
