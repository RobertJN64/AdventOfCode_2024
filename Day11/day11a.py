import util

def main():
    with open("Day11/day11.txt") as f:
        stones = list(map(int, f.readlines()[0].strip().split()))
    print(stones[0:10])

    for blink in range(75):
        print(f"After blink {blink}:")
        idx = 0
        length = len(stones)
        while idx < length:
            stone_str = str(stones[idx])
            if stones[idx] == 0:
                stones[idx] = 1
            elif len(stone_str) % 2 == 0:
                a = stone_str[:int(len(stone_str)/2)]
                b = stone_str[int(len(stone_str)/2):]
                stones[idx] = int(a)
                stones.append(int(b))
            else:
                stones[idx] *= 2024
            idx += 1
        #print(stones)

    print(len(stones))
