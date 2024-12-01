import util

def main():
    with open("Day01/day01.txt") as f:
        lines = [line.strip().split('   ') for line in f.readlines()]
    print(lines[0:10])

    first = []
    second = []
    for a, b in lines:
        a = int(a)
        b = int(b)
        first.append(a)
        second.append(b)

    first = sorted(first)
    second = sorted(second)

    answer = 0
    for a, b in zip(first, second):
        answer += abs(a-b)

    #
    #
    # answer = 0
    # for line in lines:
    #     answer += int(line)

    print(answer)