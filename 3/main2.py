def f_badge(gr):
    counts = {}
    for g in gr:
        for c in set([_ for _ in g]):
            counts[c] = 1 + counts.get(c, 0)
    for c, count in counts.items():
        if count == 3:
            return c


def score(c):
    c2 = c.upper()
    return ord(c2) - ord('A') + 1 + (26 if c == c2 else 0)


with open('case1.in') as fin:
    lines = [e.strip() for e in fin.readlines()]
    score_tot = 0
    for i in range(len(lines)//3):
        x, y, z = lines[3*i], lines[3*i+1], lines[3*i+2]
        score_tot += score(f_badge([x, y, z]))
    print(score_tot)
