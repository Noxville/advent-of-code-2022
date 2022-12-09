def sign(n):
    if n == 0:
        return 0
    return 1 if n > 0 else -1


def update_tail(he, ta):
    dx, dy, sx, sy = ta[0] - he[0], ta[1] - he[1], 0, 0
    manh = abs(dx) + abs(dy)
    if manh == 2:
        if abs(dx) == 2:
            sx = -(dx // 2)
        elif abs(dy) == 2:
            sy = -(dy // 2)
    elif manh == 3:
        sx = -sign(dx)
        sy = -sign(dy)
    return ta[0] + sx, ta[1] + sy


if __name__ == "__main__":
    with open('case1.in') as fin:
        tail, head, seen = (0, 0), (0, 0), {(0, 0)}
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
                seen.add(tail)
        print(len(seen))
