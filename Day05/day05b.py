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

    bad = []
    for line in manuals:
        for rule in rules:
            if rule[0] in line and rule[1] in line and line.index(rule[0]) > line.index(rule[1]):
                bad.append(line)
                break

    answer = 0
    for line in bad:
        redo = True
        while redo:
            redo = False
            for rule in rules:
                if rule[0] in line and rule[1] in line:
                    k = line.index(rule[0])
                    j = line.index(rule[1])
                    if k > j:
                        t = line[j]
                        line[j] = line[k]
                        line[k] = t
                        redo = True

        answer += line[int(len(line) / 2)]

    print(answer)
