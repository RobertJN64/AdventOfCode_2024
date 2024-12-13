from sympy.solvers import solve
from sympy.abc import x, y
import sympy as sp

import util

def main():
    with open("Day13/day13.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])

    answer = 0

    for i in range(0, len(lines), 4):
        btna = list(map(int, lines[i].split(': X+')[1].split(', Y+')))
        btnb = list(map(int, lines[i+1].split(': X+')[1].split(', Y+')))
        prize = list(map(int, lines[i+2].split(': X=')[1].split(', Y=')))
        prize[0] += 10000000000000
        prize[1] += 10000000000000

        eq1 = sp.Eq(x * btna[0] + y * btnb[0], prize[0])
        eq2 = sp.Eq(x * btna[1] + y * btnb[1], prize[1])
        output = solve([eq1, eq2], dict=True)
        x_val = output[0][x]
        y_val = output[0][y]

        if int(x_val) == x_val and int(y_val) == y_val:
            answer += x_val * 3 + y_val

    print(answer)