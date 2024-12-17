import util

def combo(op, regs):
    d = [0, 1, 2, 3, regs['A'], regs['B'], regs['C']]
    return d[op]

def main():
    with open("Day17/day17.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])

    regs = {}
    prog = []
    pointer = 0
    for line in lines:
        if line.startswith('Register'):
            k, v = line.removeprefix('Register ').split(': ')
            regs[k] = int(v)
        if line.startswith('Program'):
            prog = list(map(int, line.removeprefix('Program: ').split(',')))


    while pointer < len(prog):
        instruction = prog[pointer]
        operand = prog[pointer + 1]
        if instruction == 0: # adv
            regs['A'] = int(regs['A'] / (2 ** combo(operand, regs)))
        elif instruction == 1: # bxl
            regs['B'] = regs['B'] ^ operand
        elif instruction == 2: #bst
            regs['B'] = combo(operand, regs) % 8
        elif instruction == 3: #jnz
            if regs['A'] != 0:
                pointer = operand - 2
        elif instruction == 4: #bxc
            regs['B'] = regs['B'] ^ regs['C']
        elif instruction == 5: #out
            print(combo(operand, regs) % 8, ',', end='', sep='')
        elif instruction == 6: #bdv
            regs['B'] = int(regs['A'] / (2 ** combo(operand, regs)))
        elif instruction == 7:
            regs['C'] = int(regs['A'] / (2 ** combo(operand, regs)))
        else:
            raise Exception("invalid instruction")

        pointer += 2

    print()
    print(regs)





