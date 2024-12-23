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

    def expand(group: list):
        # given a group, try to add a connection
        max_size = len(group)
        max_code = ','.join(group)

        last_item = group[-1]
        for conn in connections[last_item]:  # scan the connections attached to the final item
            if conn > last_item:  # if occurs later
                for prev_item in group:
                    if conn not in connections[prev_item]:
                        break
                else:
                    new_group = group.copy()
                    new_group.append(conn)
                    new_size, new_code = expand(new_group)
                    if new_size > max_size:
                        max_size = new_size
                        max_code = new_code

        return max_size, max_code



    best_size = 0
    best_code = ''
    for k in connections:
        n_size, n_code = expand([k])
        if n_size > best_size:
            best_size = n_size
            best_code = n_code

    print(f"Reached max size of {best_size} with code:")
    print(best_code)

