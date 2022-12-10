def evr(cyc, x):
    if cyc > 0 and cyc % 40 == 20:
        return cyc * x
    return 0


if __name__ == "__main__":
    with open('case1.in') as fin:
        ins = [e.strip() for e in fin.readlines()]
        val, cycle, ss = 1, 0, 0
        for cminus, i in enumerate(ins):
            s = i.split(' ')
            if s[0] == 'noop':
                cycle += 1
                ss += evr(cycle, val)
            elif s[0] == 'addx':
                for c in range(2):
                    cycle += 1
                    ss += evr(cycle, val)
                val += int(s[1])
        ss += evr(cycle, val)
    print(ss)
