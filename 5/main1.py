import copy


def load_stacks(ls):
    rs = (len(ls[0]) + 1) // 4
    stx = [[] for _ in range(rs)]

    for y in ls:
        for x in range(rs):
            c = y[1 + 4*x]
            if c != ' ':
                stx[x].append(c)
    return stx


def do_ins(stx, ins, flip):
    for i in ins:
        count, frm, to = map(int, i.replace("move ", "").replace(" from ", ",").replace(" to ", ",").split(","))
        pile = []
        for _ in range(count):
            pile.append(stx[frm-1].pop(0))
        if flip:
            pile = pile[::-1]
        stx[to-1] = pile + stx[to-1]
    return stx


with open('case1.in') as fin:
    lines = [e.replace("\n", "") for e in fin.readlines()]
    spacer = [idx for idx, _ in enumerate(lines) if _ == ''][0] - 1
    stacks = load_stacks(lines[:spacer])
    print("".join([_[0] for _ in do_ins(copy.deepcopy(stacks), lines[2+spacer:], True)]))
    print("".join([_[0] for _ in do_ins(copy.deepcopy(stacks), lines[2+spacer:], False)]))
