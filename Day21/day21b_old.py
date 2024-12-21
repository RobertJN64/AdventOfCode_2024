from sympy.utilities.iterables import multiset_permutations
import functools
import util

keypad_layout = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [' ', '0', 'A']
]

dirpad_layout = [
    [' ', '^', 'A'],
    ['<', 'v', '>']
]

def get_sequence(start, end, pad):
    start_coord = (-1, -1)
    end_coord = (-1, -1)
    for y, row in enumerate(pad):
        for x, c in enumerate(row):
            if c == start:
                start_coord = (x, y)
            if c == end:
                end_coord = (x, y)

    x_delta = end_coord[0] - start_coord[0]
    y_delta = end_coord[1] - start_coord[1]
    actions = '^' * -y_delta + 'v' * y_delta + '>' * x_delta + '<' * -x_delta

    d = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}
    ok = []
    for seq in multiset_permutations(actions):
        c_pos = [start_coord[0], start_coord[1]]
        for c in seq:
            c_pos[0] += d[c][0]
            c_pos[1] += d[c][1]
            if pad[c_pos[1]][c_pos[0]] == ' ':
                break
        else:
            ok.append(seq)
    return ok

@functools.cache
def get_dirpad_sequence(start, end):
    start_coord = (-1, -1)
    end_coord = (-1, -1)
    for y, row in enumerate(dirpad_layout):
        for x, c in enumerate(row):
            if c == start:
                start_coord = (x, y)
            if c == end:
                end_coord = (x, y)

    x_delta = end_coord[0] - start_coord[0]
    y_delta = end_coord[1] - start_coord[1]
    actions = '^' * -y_delta + 'v' * y_delta + '>' * x_delta + '<' * -x_delta

    d = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}
    ok = []
    for seq in multiset_permutations(actions):
        c_pos = [start_coord[0], start_coord[1]]
        for c in seq:
            c_pos[0] += d[c][0]
            c_pos[1] += d[c][1]
            if dirpad_layout[c_pos[1]][c_pos[0]] == ' ':
                break
        else:
            ok.append(seq)
    return ok


def get_options(seq, pad):
    last_char = 'A'
    nested_seqs = ['']
    for char in seq:
        new_nested = []
        for new_seq in get_sequence(last_char, char, pad):
            for old_seq in nested_seqs:
                new_nested.append(old_seq + ''.join(new_seq) + 'A')
        nested_seqs = new_nested
        last_char = char

    return nested_seqs


@functools.cache
def get_dirpad_options(seq):
    last_char = 'A'
    nested_seqs = ['']
    for char in seq:
        new_nested = []
        for new_seq in get_dirpad_sequence(last_char, char):
            for old_seq in nested_seqs:
                new_nested.append(old_seq + ''.join(new_seq) + 'A')
        nested_seqs = new_nested
        last_char = char

    return nested_seqs

@functools.cache
def recursive_lim(seq, limit):
    best = float('inf')
    for subseq in get_dirpad_options(seq):
        if limit == 1:
            best = min(best, len(subseq))
        else:
            best = min(best, recursive_lim(subseq, limit - 1))
    return best

def main():
    with open("Day21/day21.txt") as f:
        seqs = [line.strip() for line in f.readlines()]
    print(seqs[0:10])

    nested = 2

    total = 0
    for seq_A in seqs:
        best = float('inf')
        for seq_B in get_options(seq_A, keypad_layout):
            best = min(best, recursive_lim(seq_B, nested))

        print(best)
        mul = int(seq_A[:-1])
        print(mul)
        print(best * mul)
        total += best * mul
    print(total)