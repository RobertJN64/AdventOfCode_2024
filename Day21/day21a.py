from sympy.utilities.iterables import multiset_permutations
import util

#TODO - can't cross blank

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
    return multiset_permutations(actions)

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

def main():
    with open("Day21/day21.txt") as f:
        seqs = [line.strip() for line in f.readlines()]
    print(seqs[0:10])


    for seq_A in seqs:
        for seq_B in get_options(seq_A, keypad_layout):
            print(get_options(seq_B, dirpad_layout))
        break