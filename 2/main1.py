def score(_them, _us):
    shape_score = {'A': 1, 'B': 2, 'C': 3}[_us]
    if _them == _us:
        return 3 + shape_score
    return shape_score + (6 if ((_us, _them) in [('A', 'C'), ('B', 'A'), ('C', 'B')]) else 0)


def run(ls, abc):
    lookup = {abc[0]: 'B', abc[1]: 'A', abc[2]: 'C'}
    return sum([score(them, lookup[us]) for them, us in ls])


with open('case1.in') as fin:
    lines = [e.strip().split() for e in fin.readlines()]
    print(run(lines, "YXZ"))  # expected part 2 to be to optimize the strategy
