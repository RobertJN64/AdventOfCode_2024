import util

def main():
    with open("Day08/day08.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    freqs_to_check = set()
    for line in lines:
        for char in line:
            if char != '.' and char != '#':
                freqs_to_check.add(char)

    antenna_locs = set()

    for freq in freqs_to_check:
        locations = []

        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == freq:
                    locations.append((x,y))

        for s_index, loc_a in enumerate(locations):
            for loc_b in locations[s_index+1:]:
                x_delta = loc_a[0] - loc_b[0]
                y_delta = loc_a[1] - loc_b[1]

                i = 0
                while True:
                    new_loc_a = (loc_a[0] + x_delta * i, loc_a[1] + y_delta * i)
                    i += 1
                    if not util.out_of_bounds(lines, new_loc_a[0], new_loc_a[1]):
                        antenna_locs.add(new_loc_a)
                    else:
                        break

                i = 0
                while True:
                    new_loc_b = (loc_b[0] - x_delta * i, loc_b[1] - y_delta * i)
                    i += 1
                    if not util.out_of_bounds(lines, new_loc_b[0], new_loc_b[1]):
                        antenna_locs.add(new_loc_b)
                    else:
                        break

    print(len(antenna_locs))


