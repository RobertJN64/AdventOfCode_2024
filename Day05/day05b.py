import util

def main():
    with open("Day05/day05.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])

    orders = []
    ship = []
    puz = False
    for line in lines:
        if line == '':
            puz = True
            continue

        if not puz:
            orders.append(tuple(map(int, line.split('|'))))
        else:
            ship.append(list(map(int, line.split(','))))

    answer = 0
    bad = []
    for line in ship:
        valid = True
        for rule in orders:
            if rule[0] in line and rule[1] in line:
                if line.index(rule[0]) > line.index(rule[1]):
                    valid = False
        if not valid:
            bad.append(line)

    print(bad)
    answer = 0
    for line in bad:
        redo = True
        while redo:
            redo = False
            for rule in orders:
                if rule[0] in line and rule[1] in line:
                    k = line.index(rule[0])
                    j = line.index(rule[1])
                    if k > j:
                        t = line[j]
                        line[j] = line[k]
                        line[k] = t
                        redo = True
        print(line)
        answer += line[int(len(line) / 2)]

    print(answer)
