import util

def adjacent(pt1, pt2):
    if pt1[0] == pt2[0] and abs(pt1[1] - pt2[1]) == 1:
        return True
    if pt1[1] == pt2[1] and abs(pt1[0] - pt2[0]) == 1:
        return True
    return False


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
            perim_components = [[], [], [], []]

            queue = [(x, y)]
            while len(queue):
                pt_x, pt_y = queue.pop()

                for direction, (dx, dy) in enumerate(util.cardinal):
                    n_x = pt_x + dx
                    n_y = pt_y + dy
                    if util.out_of_bounds(lines, n_x, n_y) or lines[n_y][n_x] != c:
                        current = perim_components[direction]
                        new_component = [(n_x, n_y)]
                        new_list = []
                        for pts in current:
                            for pt in pts:
                                if adjacent(pt, (n_x, n_y)):
                                    new_component.extend(pts)
                                    break
                            else:
                                new_list.append(pts)
                        new_list.append(new_component)
                        perim_components[direction] = new_list


                    elif (n_x, n_y) in visited:
                        continue
                    else:
                        area += 1
                        visited.add((n_x, n_y))
                        queue.append((n_x,n_y))

                #print(pt_x, pt_y, area, perim, queue)

            print("region with ", x, y, c, sum(map(len, perim_components)), area)
            answer += area * sum(map(len, perim_components))
    print(answer)