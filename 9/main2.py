from main1 import sign

def pri(ta, he, se):
    min_x, max_x = min([min(_[0] for _ in se), min([_t[0] for _t in tail]), he[0]]), \
                   max([max(_[0] for _ in se), max([_t[0] for _t in tail]), he[0]])
    min_y, max_y = min([min(_[1] for _ in se), min([_t[1] for _t in tail]), he[1]]), \
                   max([max(_[1] for _ in se), max([_t[1] for _t in tail]), he[1]])
    x_len = max(max_x - min_x, 26)
    y_len = max(max_y - min_y, 20)
    print(x_len, y_len, min_x, min_y)
    print(f"Head @ {he}")
    print(f"Tail @ {ta}")

    grid = [['.' for x in range(x_len)] for y in range(y_len)]
    for s in se:
        grid[y_len - (s[1] + min_y) - 1][s[0] + min_x] = '#'
    for idx, tn in enumerate(ta[::-1]):
        grid[y_len - (tn[1] + min_y) - 1][tn[0] + min_x] = str(9 - idx)
    grid[y_len - (he[1] + min_y) - 1][he[0] + min_x] = 'H'
    grid[y_len - min_y - 1][min_x] = 's'
    for _ in grid:
        print("".join(_))


def update_tail(he, ta):
    for idx, t in enumerate(ta):
        if idx == 0:
            ta[0] = update_node(he, t)
        else:
            ta[idx] = update_node(ta[idx-1], t)
    return ta


def update_node(he, ta):
    dx, dy, sx, sy = ta[0] - he[0], ta[1] - he[1], 0, 0
    manh = abs(dx) + abs(dy)
    if manh == 2:
        if abs(dx) == 2:
            sx = -(dx // 2)
        elif abs(dy) == 2:
            sy = -(dy // 2)
    elif manh in [3,4]:
        sx = -sign(dx)
        sy = -sign(dy)
    elif manh in [0, 1]:
        pass
    else:
        print(f"??? {manh} head @ {he}, tail @ {ta}")
    return ta[0] + sx, ta[1] + sy


if __name__ == "__main__":
    with open('case1.in') as fin:
        tail, head, seen = [(0, 0) for _ in range(9)], (0, 0), {(0, 0)}
        for direc, dist_s in [e.strip().split() for e in fin.readlines()]:
            for _ in range(int(dist_s)):
                if direc == 'R':
                    head = (head[0] + 1, head[1])
                elif direc == 'L':
                    head = (head[0] - 1, head[1])
                elif direc == 'U':
                    head = (head[0], head[1] + 1)
                elif direc == 'D':
                    head = (head[0], head[1] - 1)
                tail = update_tail(head, tail)
                seen.add(tail[-1])
            #pri(tail, head, seen)
        print(len(seen))
