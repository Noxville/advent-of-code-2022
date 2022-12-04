with open('case1.in') as fin:
    lines = [e.strip() for e in fin.readlines()]

    overlap_count = 0
    for l in lines:
        f, s = l.split(',')
        a, b = map(int, f.split('-'))
        c, d = map(int, s.split('-'))

        if (a <= c and b >= d) or (c <= a and d >= b):
            overlap_count += 1
    print(overlap_count)
