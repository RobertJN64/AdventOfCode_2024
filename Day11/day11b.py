import functools
import util

@functools.lru_cache(maxsize=10000)
def get_ct_after_iter(value, remaining_iters):
    bonus_ct = 0
    for i in range(remaining_iters):
        stone_str = str(value)
        if value == 0:
            value = 1
        elif len(stone_str) % 2 == 0:
            a = stone_str[:int(len(stone_str) / 2)]
            b = stone_str[int(len(stone_str) / 2):]
            value = int(a)
            bonus_ct += get_ct_after_iter(int(b), remaining_iters - i - 1)
        else:
            value *= 2024
    return bonus_ct + 1

def main():
    with open("Day11/day11.txt") as f:
        stones = list(map(int, f.readlines()[0].strip().split()))
    print(stones[0:10])

    answer = 0
    for stone in stones:
        print('stone ->', stone)
        answer += get_ct_after_iter(stone, 75)
    print('done')
    print(answer)