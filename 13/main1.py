def lt(lef, rig):
    if type(rig) == int and type(lef) == int:
        if rig == lef:
            return None
        return rig > lef
    if type(rig) == int:
        rig = [rig]
    if type(lef) == int:
        lef = [lef]
    for xx, yy in zip(lef, rig):
        recurse = lt(xx, yy)
        if recurse is not None:
            return recurse
    if len(lef) == len(rig):
        return None
    return len(lef) < len(rig)


class Packet:
    def __init__(self, s):
        self.v = eval(s)

    def __gt__(self, other):
        return not lt(self.v, other.v)

    def __lt__(self, other):
        return lt(self.v, other.v)

    def __eq__(self, other):
        return other.v == self.v

    def __repr__(self):
        return str(self.v)


def make_packet_pairs(idx, raw_packet_pair):
    l, r = Packet(raw_packet_pair[0]), Packet(raw_packet_pair[1])
    return idx if l < r else 0


if __name__ == "__main__":
    with open('case1.in') as fin:
        ls = [e.strip() for e in fin.readlines()]
    print(sum([make_packet_pairs(1 + i, ls[3 * i:3 * i + 2]) for i in range((len(ls) + 1) // 3)]))
