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

    checksum = 0
    check_idx = 0
    for idx, (pair_id, pair_len) in enumerate(pairs):
        for i in range(0, pair_len):
            checksum += pair_id * check_idx
            check_idx += 1

        pairs[idx][1] = 0
        free_len = free[idx]

        for neg_idx, (neg_pair_id, neg_pair_len) in enumerate(pairs[::-1]):
            if neg_pair_len > free_len:
                for i in range(0, free_len):
                    checksum += neg_pair_id * check_idx
                    check_idx += 1

                pairs[-neg_idx-1][1] -= free_len
                free_len = 0
                break
            else:
                for i in range(0, neg_pair_len):
                    checksum += neg_pair_id * check_idx
                    check_idx += 1

                pairs[-neg_idx-1][1] = 0
                free_len -= neg_pair_len
        check_idx += free_len

        #print(out_str)
        #print(pairs)

    print(checksum)
