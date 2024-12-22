import util

def step(x):
    x = ((x * 64) ^ x) % 16777216
    x = ((x // 32) ^ x) % 16777216
    x = ((x * 2048) ^ x) % 16777216
    return x

def multi_step(x, n):
    for _ in range(n):
        x = step(x)
    return x

def main():
    with open("Day22/day22.txt") as f:
        lines = [int(line.strip()) for line in f.readlines()]
    print(lines[0:10])


    answer = 0
    for line in lines:
        answer += (multi_step(line, 2000))

    print(answer)