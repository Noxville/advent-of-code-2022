def over(a, b):
    for c in a:
        if c in b:
            return c
    return ''


def score(c):
    c2 = c.upper()
    return ord(c2) - ord('A') + 1 + (26 if c == c2 else 0)


with open('case1.in') as fin:
    lines = [e.strip() for e in fin.readlines()]
    tot_score = 0
    for l in lines:
        mid = len(l) // 2
        s1, s2 = l[:mid], l[mid:]
        lap = over(s1, s2)
        tot_score += score(lap)
    print(tot_score)