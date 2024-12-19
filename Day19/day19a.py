import util

def main():
    with open("Day19/day19.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    options = lines[0].split(', ')

    count = 0

    for pattern in lines[2:]:
        search = [pattern]
        good = False
        while search:
            t_pat = search.pop()
            if len(t_pat) == 0:
                good = True
                break
            for opt in options:
                if t_pat.startswith(opt):
                    search.append(t_pat.removeprefix(opt))

        if good:
            count += 1

    print(count)