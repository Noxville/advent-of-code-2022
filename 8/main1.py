with open('case1.in') as fin:
    grid = [[int(_) for _ in e.strip()] for e in fin.readlines()]
    mx, my = len(grid[0]), len(grid)
    good = set()

    for r in range(my):
        for (sx, ex, dx) in [(0, mx, 1), (mx - 1, -1, -1)]:
            cur, bad = [-1], False
            for c in range(sx, ex, dx):
                val = grid[r][c]
                if val > max(cur):
                    good.add((r, c))
                    cur.append(val)

    for c in range(mx):
        for (sy, ey, dy) in [(0, my, 1), (my - 1, -1, -1)]:
            cur, bad = [-1], False
            for r in range(sy, ey, dy):
                val = grid[r][c]
                if val > max(cur):
                    good.add((r, c))
                    cur.append(val)
    print(len(good))
