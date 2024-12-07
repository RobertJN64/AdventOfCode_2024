import util

operations = [
    lambda a, b: a + b,
    lambda a, b: a * b,
    lambda a, b: int(str(a) + str(b)),
]

def get_possible(nums):
    resp = []
    for op in operations:
        if len(nums) == 2:
            resp.append(op(nums[0], nums[1]))
        else:
            resp.extend([op(x, nums[-1]) for x in get_possible(nums[:-1])])
    return resp

def main():
    with open("Day07/day07.txt") as f:
        lines = [line.strip().split(': ') for line in f.readlines()]
    print(lines[0:10])

    count = 0
    for line in lines:
        answer = int(line[0])
        nums = list(map(int, line[1].split()))
        print(answer)
        if answer in get_possible(nums):
            count += answer
    print(count)