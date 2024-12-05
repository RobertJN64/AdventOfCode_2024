import util

def main():
    with open("Day05/day05.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])

    rules = []
    manuals = []
    scan_rules = True

    for line in lines:
        if line == '':
            scan_rules = False
            continue

        if scan_rules:
            rules.append(tuple(map(int, line.split('|'))))
        else:
            manuals.append(list(map(int, line.split(','))))

    answer = 0
    for line in manuals:
        for rule in rules:
            if rule[0] in line and rule[1] in line:
                if line.index(rule[0]) > line.index(rule[1]):
                    break
        else:
            answer += line[int(len(line)/2)]
    print(answer)
