import util

def combo(op, regs):
    d = [0, 1, 2, 3, regs['A'], regs['B'], regs['C']]
    return d[op]

def main():
    with open("Day17/day17.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])

    start_regs = {}
    prog = []
    for line in lines:
        if line.startswith('Register'):
            k, v = line.removeprefix('Register ').split(': ')
            start_regs[k] = int(v)
        if line.startswith('Program'):
            prog = list(map(int, line.removeprefix('Program: ').split(',')))

    start_value = 0
    while True:
        if start_value % 100000 == 0:
            print(start_value)

        regs = start_regs.copy()
        pointer = 0
        regs['A'] = start_value
        start_value += 1
        out = []
        out_count = 0
        valid = True

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
                if out_count == len(prog):
                    valid = False
                    break
                if prog[out_count] != combo(operand, regs) % 8:
                    valid = False
                    break
                out.append(combo(operand, regs) % 8)
                out_count += 1
            elif instruction == 6: #bdv
                regs['B'] = int(regs['A'] / (2 ** combo(operand, regs)))
            elif instruction == 7:
                regs['C'] = int(regs['A'] / (2 ** combo(operand, regs)))
            else:
                raise Exception("invalid instruction")

            pointer += 2

        if len(out) == len(prog) and valid:
            break

    print(start_value - 1)





