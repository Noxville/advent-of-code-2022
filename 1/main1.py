with open('case1.in') as fin:
    lines = [e.strip() for e in fin.readlines()]
    elves = []
    cur = 0
    for l in lines:
        if l == '':
            elves.append(cur)
            cur = 0
        else:
            cur += int(l)
    elves.append(cur)

    print(max(elves))
    print(sum(sorted(elves, reverse=True)[:3]))