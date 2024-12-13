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

        best_cost = float('inf')
        found = False

        for a in range(0, 100):
            for b in range(0, 100):
                if prize[0] == btna[0] * a + btnb[0] * b and prize[1] == btna[1] * a + btnb[1] * b:
                    if a * 3 + b < best_cost:
                        best_cost = a * 3 + b
                        found = True
                    print('possible', a, b)

        if found:
            answer += best_cost

    print(answer)