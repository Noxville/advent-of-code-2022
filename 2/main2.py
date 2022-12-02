def score(_them, _us):
    shape_score = {'A': 1, 'B': 2, 'C': 3}[_us]
    if _them == _us:
        return 3 + shape_score
    return shape_score + (6 if ((_us, _them) in [('A', 'C'), ('B', 'A'), ('C', 'B')]) else 0)


with open('case1.in') as fin:
    lines = [e.strip().split() for e in fin.readlines()]
    sc_tot = 0
    for them, outcome in lines:
        if outcome == 'Y':
            us = them
        elif outcome == 'X':  # lose
            us = {'A': 'C', 'B': 'A', 'C': 'B'}[them]
        elif outcome == 'Z':  # win
            us = {'A': 'B', 'B': 'C', 'C': 'A'}[them]
        sc_tot += score(them, us)
    print(sc_tot)
