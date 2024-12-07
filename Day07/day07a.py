import util

def get_possible(nums):
    if len(nums) == 2:
        return [nums[0] + nums[1], nums[0] * nums[1]]
    else:
        return [nums[-1] + x for x in get_possible(nums[:-1])] + [nums[-1] * x for x in get_possible(nums[:-1])]


def main():
    with open("Day07/day07.txt") as f:
        lines = [line.strip().split(': ') for line in f.readlines()]
    print(lines[0:10])

    count = 0
    for line in lines:
        answer = int(line[0])
        nums = list(map(int, line[1].split()))

        print(get_possible(nums))

        if answer in get_possible(nums):

            count += answer

    print(count)