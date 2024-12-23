import util

def main():
    with open("Day23/day23.txt") as f:
        lines = [line.strip().split('-') for line in f.readlines()]
    print(lines[0:10])

    connections = {}
    for k, v in lines:
        if k not in connections:
            connections[k] = []
        if v not in connections:
            connections[v] = []
        connections[k].append(v)
        connections[v].append(k)

    groups = set()

    for k in connections:
        if k.startswith('t'):
            print('checking computer', k)
        else:
            continue

        for conn in connections[k]:
            for subconn in connections[conn]:
                if k in connections[subconn]:
                    #print(k, conn, subconn, 'valid')
                    groups.add(tuple(sorted((k, conn, subconn))))
    print(len(groups))

