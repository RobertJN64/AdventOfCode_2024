import util

def main():
    with open("Day25/day25.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])

    items = []
    last_item = []
    for row in lines:
        if row == "":
            items.append(last_item)
            last_item = []
        else:
            last_item.append(row)
    items.append(last_item)

    keys = []
    locks = []

    for item in items:
        cols = []
        for cindex in range(0, 5):
            count = 0
            for row in item:
                if row[cindex] == '#':
                    count += 1
            cols.append(count - 1)
        if item[0] == '#####':
            locks.append(cols)
        else:
            keys.append(cols)

    print(locks)
    print(keys)

    answer = 0

    for lock in locks:
        for key in keys:
            for cindex in range(0, 5):
                if lock[cindex] + key[cindex] > 5:
                    break
            else:
                answer += 1

    print(answer)

