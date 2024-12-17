import util

def combo(op, regs):
    d = [0, 1, 2, 3, regs['A'], regs['B'], regs['C']]
    return d[op]

def main():
    with open("Day17/day17.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])

    prog = []
    for line in lines:
        if line.startswith('Program'):
            prog = list(map(int, line.removeprefix('Program: ').split(',')))

    assert prog[-2] == 3 and prog[-1] == 0, "unexpected loop method"
    # these can occur in either order, update accordingly
    assert prog[-4] == 0 and prog[-3] == 3, "unexpected A div method"
    assert prog[-6] == 5 and prog[-5] == 5, "unexpected B out method"

    valid_input = []

    check = list(range(1, 8)) # A can't be zero on the final iteration
    for goal in reversed(prog):
        valid_input = []

        next_check = []
        for A in check:
            pointer = 0
            regs = {'A': A, 'B': 0, 'C': 0} # assume starting value of B and C don't matter

            while pointer < len(prog) - 6:
                instruction = prog[pointer]
                operand = prog[pointer + 1]
                if instruction == 0:  # adv
                    regs['A'] = int(regs['A'] / (2 ** combo(operand, regs)))
                elif instruction == 1:  # bxl
                    regs['B'] = regs['B'] ^ operand
                elif instruction == 2:  # bst
                    regs['B'] = combo(operand, regs) % 8
                elif instruction == 3:  # jnz
                    raise Exception("bad jump loc")
                elif instruction == 4:  # bxc
                    regs['B'] = regs['B'] ^ regs['C']
                elif instruction == 5:  # out
                    raise Exception("bad out loc")
                elif instruction == 6:  # bdv
                    regs['B'] = int(regs['A'] / (2 ** combo(operand, regs)))
                elif instruction == 7:
                    regs['C'] = int(regs['A'] / (2 ** combo(operand, regs)))
                else:
                    raise Exception("invalid instruction")
                pointer += 2

            next_out = regs['B'] % 8 # instruction 5, 5
            if next_out == goal:
                print('achieved', goal, 'with', A)
                valid_input.append(A)
                for d in range(0, 8):
                    next_check.append(A * 8 + d) # instruction 0,3,3,0

        check = next_check
    print(min(valid_input))



