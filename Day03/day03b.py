import util
import re

def main():
    with open("Day03/day03.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])


    answer = 0
    enabled = True
    for line in lines:
        cmds = re.findall(r'(mul)\(([0-9]+),([0-9]+)\)|(do)\(\)|(don\'t)\(\)', line)
        for cmd in cmds:
            if cmd[3] == 'do':
                enabled = True
            if cmd[4] == 'don\'t':
                enabled = False
            if enabled and cmd[0] == 'mul':
                answer += int(cmd[1]) * int(cmd[2])

    print(answer)