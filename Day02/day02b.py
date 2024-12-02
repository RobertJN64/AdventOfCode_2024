import util

def main():
    with open("Day02/day02.txt") as f:
        lines = [line.strip().split() for line in f.readlines()]
    print(lines[0:10])


    count = 0
    for t_line in lines:
        line_ok = False

        for index in range(len(t_line)):
            line = t_line[:index] + t_line[index+1:]

            valid = True
            dec = 0

            for i in range(len(line) - 1):
                a = int(line[i])
                b = int(line[i + 1])
                if abs(a-b) > 3:
                    valid = False
                if abs(a-b) == 0:
                    valid = False
                if a > b and dec == 1:
                    valid = False
                if a > b:
                    dec = 2
                if a < b and dec == 2:
                    valid = False
                if a < b:
                    dec = 1

            if valid:
                line_ok = True

        count += line_ok

    print(count)