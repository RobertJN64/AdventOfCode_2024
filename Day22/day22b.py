import util

def step(x):
    x = ((x * 64) ^ x) % 16777216
    x = ((x // 32) ^ x) % 16777216
    x = ((x * 2048) ^ x) % 16777216
    return x

def create_table(x, n):
    table = {}
    last = x % 10
    seq = []
    for i in range(n):
        x = step(x)
        s_val = x % 10
        seq.append(s_val - last)
        last = s_val

        if len(seq) == 4:
            sub_seq = tuple(seq[0:4])
            if sub_seq not in table:
                table[sub_seq] = last
            seq.pop(0)

    #print(table)
    return table

def main():
    with open("Day22/day22.txt") as f:
        lines = [int(line.strip()) for line in f.readlines()]
    print(lines[0:10])



    monk_tables = []
    for line in lines:
        monk_tables.append(create_table(line, 2000))

    print('starting checks')

    best = 0

    for a in range(-9, 10):
        print(a)
        for b in range(-9, 10):
            for c in range(-9, 10):
                for d in range(-9, 10):
                    answer = 0

                    k = (a, b, c, d)
                    for table in monk_tables:
                        if k in table:
                            answer += table[k]

                    best = max(answer, best)

    print(best)