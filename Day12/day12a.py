import util

def main():
    with open("Day12/day12.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])

    visited = set()

    answer = 0

    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            if (x,y) in visited:
                continue
            visited.add((x,y))

            area = 1
            perim = 0

            queue = [(x, y)]
            while len(queue):
                pt_x, pt_y = queue.pop()

                for dx, dy in util.cardinal:
                    n_x = pt_x + dx
                    n_y = pt_y + dy
                    if util.out_of_bounds(lines, n_x, n_y) or lines[n_y][n_x] != c:
                        perim += 1
                    elif (n_x, n_y) in visited:
                        continue
                    else:
                        area += 1
                        visited.add((n_x, n_y))
                        queue.append((n_x,n_y))

                #print(pt_x, pt_y, area, perim, queue)

            print("region with ", x, y, c, perim, area)
            answer += area * perim
    print(answer)