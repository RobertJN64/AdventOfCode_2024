import util

class State:
    def __init__(self, x, y, direction, score, history):
        self.x = x
        self.y = y
        self.d = direction
        self.score = score
        self.history = history

    def __repr__(self):
        return f"{(self.x, self.y)} {self.d} {self.score}"

def main():
    with open("Day16/day16.txt") as f:
        grid = [line.strip() for line in f.readlines()]
    print(grid[0:10])

    goal = [0, 0]
    start = [0, 0]
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == 'E':
                goal = [x, y]
            if c == 'S':
                start = [x, y]

    print(goal, start)
    queue = [State(start[0], start[1], 1, 0, [(start[0], start[1])])]
    best_score = float('inf')
    best_path = set()
    visited = {}

    def append_if_useful(ns):
        if ns.score > best_score:
            return
        if grid[ns.y][ns.x] == '#':
            return
        if visited.get((ns.x, ns.y, ns.d), ns.score) < ns.score:
            return
        queue.append(ns)
        visited[(ns.x, ns.y, ns.d)] = ns.score

    while queue:
        state = queue.pop(0)
        if grid[state.y][state.x] == 'E':
            print(f'Reached end in {state.score}')
            if state.score < best_score:
                best_path = set()
                best_score = state.score
            if state.score == best_score:
                for x,y in state.history:
                    best_path.add((x, y))
            continue

        nx = state.x + util.cardinal[state.d][0]
        ny = state.y + util.cardinal[state.d][1]
        hist = state.history.copy() + [(nx, ny)]
        append_if_useful(State(nx, ny, state.d, state.score + 1, hist))
        append_if_useful(State(state.x, state.y, (state.d + 1) % 4, state.score + 1000, state.history))
        append_if_useful(State(state.x, state.y, (state.d - 1) % 4, state.score + 1000, state.history))

    print(best_score)
    print(len(best_path))
