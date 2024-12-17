prog = [2,4,1,2,7,5,4,7,1,3,5,5,0,3,3,0]
print(len(prog))
A = 35200350

start = 0
while True:
    A = start
    start += 1

    prog_counter = 0
    while A != 0:
        B = (A % 8) ^ 2
        next_out = (B ^ int(A / (2 ** B)) ^ 3) % 8
        if prog_counter == len(prog):
            break
        if prog[prog_counter] != next_out:
            break
        prog_counter += 1
        A = int(A / (2 ** 3))
