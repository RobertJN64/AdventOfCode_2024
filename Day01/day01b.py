import util

def main():
    with open("Day01/day01.txt") as f:
        lines = f.readlines()
        col_1 = [int(line.strip().split('   ')[0]) for line in lines]
        col_2 = [int(line.strip().split('   ')[1]) for line in lines]

    print(col_1[0:10])
    print(col_2[0:10])

    answer = 0
    for item in col_1:
        answer += col_2.count(item) * item

    print(answer)