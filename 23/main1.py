from collections import defaultdict


def mv_n(ex, ey, elves):
    if all([(ex - 1, ey - 1) not in elves, (ex, ey - 1) not in elves, (ex + 1, ey - 1) not in elves]):
        return ex, ey - 1
    return None


def mv_s(ex, ey, elves):
    if all([(ex - 1, ey + 1) not in elves, (ex, ey + 1) not in elves, (ex + 1, ey + 1) not in elves]):
        return ex, ey + 1
    return None


def mv_w(ex, ey, elves):
    if all([(ex - 1, ey - 1) not in elves, (ex - 1, ey) not in elves, (ex - 1, ey + 1) not in elves]):
        return ex - 1, ey


def mv_e(ex, ey, elves):
    if all([(ex + 1, ey - 1) not in elves, (ex + 1, ey) not in elves, (ex + 1, ey + 1) not in elves]):
        return ex + 1, ey


def proposal_direction(ex, ey, elves, r):
    opts = {
        0: [mv_n(ex, ey, elves), mv_s(ex, ey, elves), mv_w(ex, ey, elves), mv_e(ex, ey, elves), (ex, ey)],
        1: [mv_s(ex, ey, elves), mv_w(ex, ey, elves), mv_e(ex, ey, elves), mv_n(ex, ey, elves), (ex, ey)],
        2: [mv_w(ex, ey, elves), mv_e(ex, ey, elves), mv_n(ex, ey, elves), mv_s(ex, ey, elves), (ex, ey)],
        3: [mv_e(ex, ey, elves), mv_n(ex, ey, elves), mv_s(ex, ey, elves), mv_w(ex, ey, elves), (ex, ey)],
    }[r % 4]
    return [_ for _ in opts if _ is not None][0]


def no_neigh(elves, _x, _y):
    for n in [
        (-1 + _x, -1 + _y),
        (-0 + _x, -1 + _y),
        (+1 + _x, -1 + _y),
        (-1 + _x, -0 + _y),
        (+1 + _x, -0 + _y),
        (-1 + _x, +1 + _y),
        (-0 + _x, +1 + _y),
        (+1 + _x, +1 + _y),
    ]:
        if n in elves:
            return False
    return True


def pr(elves):
    min_x = min([x for x, y in elves])
    max_x = max([x for x, y in elves])
    min_y = min([y for x, y in elves])
    max_y = max([y for x, y in elves])
    for yy in range(min_y, 1 + max_y):
        line = ""
        for xx in range(min_x, 1 + max_x):
            line += '#' if (xx, yy) in elves else '.'
    return ((max_x - min_x + 1) * (max_y - min_y + 1)) - len(elves)


def solve(elves):
    for r in range(10 ** 10):
        proposals = defaultdict(list)

        for ex, ey in elves:
            proposed = proposal_direction(ex, ey, elves, r)

            if no_neigh(elves, ex, ey):
                proposed = (ex, ey)  # no neighbours, must stay put
            proposals[proposed].append((ex, ey))

        new_elves = set()
        moved = False
        for prop, cur_list in proposals.items():
            if len(cur_list) == 1:  # only one so move
                new_elves.add(prop)
                if prop != cur_list[0]:
                    moved = True
            else:  # more than one = can't move
                for cur in cur_list:
                    new_elves.add(cur)
        elves = new_elves

        if r == 9:
            print(pr(elves))
        if not moved:
            print(1 + r)
            break


if __name__ == "__main__":
    with open('case1.in') as fin:
        lines = [list(e.strip()) for e in fin.readlines()]

        elves = set()
        for y in range(len(lines)):
            for x in range(len(lines[0])):
                if lines[y][x] == '#':
                    elves.add((x, y))
        solve(elves)
