def ovl(rngs):
    seen, does_overlap = set(), False
    for (x, y) in rngs:
        for i in range(x, 1 + y):
            if i in seen:
                return 1
            seen.add(i)
    return 0


with open('case1.in') as fin:
    lines = [e.strip() for e in fin.readlines()]

    overlap_count = 0
    for l in lines:
        f, s = l.split(',')
        a, b = map(int, f.split('-'))
        c, d = map(int, s.split('-'))
        overlap_count += ovl([(a, b), (c, d)])

    print(overlap_count)
