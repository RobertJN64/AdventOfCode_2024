import util

def gate_name(xy, num):
    num_str = str(num)
    if num < 10:
        num_str = '0' + num_str
    return xy + num_str

def check_inputs(gate, opa, t, opb):
    return gate[1] == t and (gate[0] == opa and gate[2] == opb or gate[2] == opa and gate[0] == opb)

def search_and_remove(opa, t, opb, gates):
    found = None
    for gate in gates:
        if check_inputs(gate, opa, t, opb):
            found = gate
            break
    else:
        print('No gate', opa, t, opb)
    if found:
        gates.remove(found)
    return found

def main():
    with open("Day24/day24_mod.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])

    gates = []
    max_wire_value = 0
    for line in lines:
        if ':' in line:
            wname = line.split(': ')[0][1:]
            max_wire_value = max(max_wire_value, int(wname))
        if '->' in line:
            gate_data, out = line.split(' -> ')
            opa, t, opb = gate_data.split(' ')
            gates.append((opa, t, opb, out))

    print(gates)
    print(len(gates))
    # start by finding parts of adder 0
    prev_carry_wire = search_and_remove(gate_name('x', 0), 'AND', gate_name('y', 0), gates)

    for num in range(1, max_wire_value):
        print(num)
        partial_sum_wire = search_and_remove(gate_name('x', num), 'XOR', gate_name('y', num), gates)
        partial_carry_wire_a = search_and_remove(gate_name('x', num), 'AND', gate_name('y', num), gates)
        final_sum_wire = search_and_remove(partial_sum_wire[3], 'XOR', prev_carry_wire[3], gates)
        partial_carry_wire_b = search_and_remove(partial_sum_wire[3], 'AND', prev_carry_wire[3], gates)
        final_carry_wire = search_and_remove(partial_carry_wire_a[3], 'OR', partial_carry_wire_b[3], gates)

        assert final_sum_wire[3] == gate_name('z', num), final_sum_wire[3] + ' ' + gate_name('z', num)
        prev_carry_wire = final_carry_wire

    print(len(gates))
