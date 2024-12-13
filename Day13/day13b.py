import util

def main():
    with open("Day13/day13.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])

    answer = 0

    for i in range(0, len(lines), 4):
        a_x, a_y = list(map(int, lines[i].split(': X+')[1].split(', Y+')))
        b_x, b_y = list(map(int, lines[i+1].split(': X+')[1].split(', Y+')))
        X, Y = list(map(int, lines[i+2].split(': X=')[1].split(', Y=')))
        X += 10000000000000
        Y += 10000000000000

        a = (Y * b_x - X * b_y) / (a_y * b_x - a_x * b_y)
        b = (Y * a_x - X * a_y) / (b_y * a_x - b_x * a_y)

        if int(a) == a and int(b) == b:
            answer += int(a * 3 + b)

    print(answer)