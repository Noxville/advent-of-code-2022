dirs = {
    '>': (+1, +0),
    '<': (-1, +0),
    '^': (+0, -1),
    'v': (+0, +1)
}


def update_blizs(bliz_set, raw_grid):
    locs = set()
    for bx, by, bdir in bliz_set:
        _dx, _dy = dirs[bdir]
        locs.add((
            1 + ((-1 + bx + _dx) % (len(raw_grid[0]) - 2)),
            1 + ((-1 + by + _dy) % (len(raw_grid) - 2)),
            bdir
        ))
    return locs


def solve(grid, start, end, blizs):
    seen = set()
    cur_turn = -1
    Q = [(start, 0)]
    while True:
        (x, y), t = Q.pop(0)
        if (x, y) == end:
            return blizs, t
        if t > cur_turn:
            cur_turn = t
            blizs = update_blizs(blizs, grid)
            blizxy = [(bx, by) for (bx, by, bd) in blizs]

        for dx, dy in [(+0, +0)] + list(dirs.values()):
            nx, ny = x + dx, y + dy
            if ((nx, ny) in [start, end]) or \
                    (1 <= nx < (len(grid[0]) - 1) and 1 <= ny < (len(grid) - 1) and (nx, ny) not in blizxy):
                if ((nx, ny), t) in seen:  # already seen this location at this time
                    continue
                seen.add(((nx, ny), t))
                Q.append(((nx, ny), 1 + t))


if __name__ == "__main__":
    with open('case1.in') as fin:
        G = [list(e.strip()) for e in fin.readlines()]
        S, E = (G[0].index('.'), 0), (G[-1].index('.'), len(G) - 1)
        B = [
            [x, y, G[y][x]]
            for y in range(len(G))
            for x in range(len(G[0]))
            if G[y][x] in '<>v^'
        ]

        B, t1 = solve(G, S, E, B)  # there
        print(t1)
        B, t2 = solve(G, E, S, B)  # back
        B, t3 = solve(G, S, E, B)  # there again
        print(t1 + t2 + t3 + 2)  # add 2 because -1 initialization x2
