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
            ship.append(tuple(map(int, line.split(','))))

    answer = 0
    for line in ship:
        for rule in orders:
            if rule[0] in line and rule[1] in line:
                if line.index(rule[0]) > line.index(rule[1]):
                    break
        else:
            print(line, 'is correct', line[int(len(line)/2)])
            answer  += line[int(len(line)/2)]
    print(answer)
