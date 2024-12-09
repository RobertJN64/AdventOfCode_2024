import util

def main():
    with open("Day09/day09.txt") as f:
        line = [line.strip() for line in f.readlines()][0]

    print(line[0:10])
    pairs = []
    free = []
    counter = 0
    for idx, item in enumerate(line):
        if idx % 2 == 0:
            pairs.append([counter, int(idx/2), int(item), int(item)])
        else:
            free.append([counter, int(item), []])
        counter += int(item)

    free.append([counter,0,[]])
    assert len(pairs) == len(free)

    print(pairs)
    print(free)



    for pair_idx, (_, pair_id, pair_len, ____) in enumerate(pairs[::-1]):
        #print('trying to move pair', pair_id)
        for free_idx, (__, free_len, ___) in enumerate(free):
            if pair_len <= free_len:
                #print('put', pair_id, ' in free_idx', free_idx)
                free[free_idx][1] -= pair_len
                free[free_idx][2].append((pair_id, pair_len))
                pairs[-pair_idx-1][2] = 0
                break

    print('done moving')

    checksum = 0
    for pair, free in zip(pairs, free):
        counter_saved, pair_id, pair_len, true_len = pair
        counter = counter_saved
        #print('ticking from', counter, 'with pair', pair_id)
        for __ in range(pair_len):
            checksum += pair_id * counter
            #print('inc checksum by', pair_id, 'at', counter)
            counter += 1
        counter = counter_saved + true_len

        for pair_free in free[2]:
            pair_id, pair_len = pair_free
            for __ in range(pair_len):
                checksum += pair_id * counter
                #print('inc checksum by', pair_id, 'at', counter)
                counter += 1

    print(checksum)
