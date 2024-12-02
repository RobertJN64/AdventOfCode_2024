import util

def main():
    with open("Day02/day02.txt") as f:
        lines = [list(map(int, line.strip().split())) for line in f.readlines()]
    print(lines[0:10])


    count = 0
    for line in lines:
        valid = True
        dec = line[0] < line[1]

        for i in range(len(line) - 1):
            a = line[i]
            b = line[i + 1]

            valid = valid and 0 < abs(a-b) <= 3
            if dec:
                valid = valid and a < b
            else:
                valid = valid and a > b

        count += valid

    print(count)