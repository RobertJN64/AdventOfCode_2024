import util
import re

def main():
    with open("Day03/day03.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])


    answer = 0
    for line in lines:
        cmds = re.findall(r'mul\(([0-9]+),([0-9]+)\)', line)
        print(cmds)
        for cmd in cmds:
            answer += int(cmd[0]) * int(cmd[1])

    print(answer)