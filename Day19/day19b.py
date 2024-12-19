import util

def main():
    with open("Day19/day19.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    options = lines[0].split(', ')

    count = 0

    for index, pattern in enumerate(lines[2:]):
        print(index)
        search = [[pattern, 1]]
        while search:
            t_pat, qty = search.pop(0)
            if len(t_pat) == 0:
                count += qty
                continue
            for opt in options:
                if t_pat.startswith(opt):
                    n_pat = t_pat.removeprefix(opt)
                    for k in search:
                        if k[0] == n_pat:
                            k[1] += qty
                            break
                    else:
                        search.append([n_pat, qty])

    print(count)