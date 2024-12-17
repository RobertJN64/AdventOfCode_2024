work_backwards = []
prog = [2,4,1,2,7,5,4,7,1,3,5,5,0,3,3,0]
check = list(range(0, 8))

for goal in reversed(prog):
    next_check = []
    for A in check:
        B = (A % 8) ^ 2
        next_out = (B ^ int(A / (2 ** B)) ^ 3) % 8
        if next_out == goal:
            print('achieved', goal, 'with', A)
            for d in range(0, 8):
                next_check.append(A * 8 + d)

    check = next_check