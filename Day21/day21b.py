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
            ok.append(''.join(seq))
    return ok

def layered_numpads(sections, limit):
    length = 0
    for section in sections:
        best = float('inf')
        for option in section:
            option = option + 'A'
            if limit == 1:
                best = min(best, len(option))
            else:
                best = min(best, layered_numpads(get_sections(option, dirpad_layout), limit - 1))
        length += best
    return length

def get_sections(seq, pad):
    last_char = 'A'
    sections = []
    for char in seq:
        sections.append(get_sequence(last_char, char, pad))
        last_char = char
    return sections

def main():
    with open("Day21/day21.txt") as f:
        seqs = [line.strip() for line in f.readlines()]
    print(seqs[0:10])

    total = 0
    for seq_A in seqs:
        best = layered_numpads(get_sections(seq_A, keypad_layout), 3)
        print(best)
        mul = int(seq_A[:-1])
        print(mul)
        print(best * mul)
        total += best * mul
    print(total)