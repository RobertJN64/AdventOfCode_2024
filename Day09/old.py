import util

def main():
    with open("Day09/day09.txt") as f:
        line = [line.strip() for line in f.readlines()][0]

    print(line[0:10])
    pairs = []
    free = []
    for idx, item in enumerate(line):
        if idx % 2 == 0:
            pairs.append([int(idx/2), int(item)])
        else:
            free.append(int(item))
    free.append(0)
    assert len(pairs) == len(free)

    print(pairs)
    print(free)
    out_str = ''
    for idx, (pair_id, pair_len) in enumerate(pairs):
        out_str += str(pair_id) * pair_len
        pairs[idx][1] = 0
        free_len = free[idx]

        for neg_idx, (neg_pair_id, neg_pair_len) in enumerate(pairs[::-1]):
            if neg_pair_len > free_len:
                out_str += str(neg_pair_id) * free_len
                pairs[-neg_idx-1][1] -= free_len
                free_len = 0
                break
            else:
                out_str += str(neg_pair_id) * neg_pair_len
                pairs[-neg_idx-1][1] = 0
                free_len -= neg_pair_len
        out_str += '.' * free_len

        #print(out_str)
        #print(pairs)

    check_sum = 0
    for idx, item in enumerate(out_str):
        if item != '.':
            check_sum += idx * int(item)


    print(check_sum)
