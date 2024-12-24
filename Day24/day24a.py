import util

class Gate:
    def __init__(self, t, opa, opb, out):
        self.opa = opa
        self.opb = opb
        self.t = t
        self.out = out

    def eval(self, wires):
        if self.out in wires:
            return False
        if self.opa not in wires or self.opb not in wires:
            return False
        if self.t == 'AND':
            wires[self.out] = wires[self.opa] and wires[self.opb]
        if self.t == 'OR':
            wires[self.out] = wires[self.opa] or wires[self.opb]
        if self.t == 'XOR':
            wires[self.out] = wires[self.opa] ^ wires[self.opb]
        return True

def main():
    with open("Day24/day24.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    print(lines[0:10])

    wires = {}
    gates = []
    for line in lines:
        if ':' in line:
            wname, value = line.split(': ')
            wires[wname] = int(value)
        if '->' in line:
            gate_data, out = line.split(' -> ')
            opa, t, opb = gate_data.split(' ')
            gates.append(Gate(t, opa, opb, out))

    changed = True
    while changed:
        changed = False
        for gate in gates:
            changed = changed or gate.eval(wires)
        print(wires)

    print(wires)
    value = 0
    for k, v in wires.items():
        if k.startswith('z'):
            value += 2 ** int(k.removeprefix('z')) * v
    print(value)
