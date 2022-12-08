with open('case1.in') as fin:
    grid = [[int(_) for _ in e.strip()] for e in fin.readlines()]
    mx, my = len(grid), len(grid[0])

    best = 0
    for y in range(1, my - 1):
        for x in range(1, mx - 1):
            val = grid[y][x]
            running = 1

            # -/= 
            direction = 1
            for _ in range(y - 1, 0, -1):
                if grid[_][x] < val:
                    direction += 1
                else:
                    break
            running *= direction

            # +/= 
            direction = 1
            for _ in range(y + 1, my - 1, +1):
                if grid[_][x] < val:
                    direction += 1
                else:
                    break
            running *= direction

            # =/- 
            direction = 1
            for _ in range(x - 1, 0, -1):
                if grid[y][_] < val:
                    direction += 1
                else:
                    break
            running *= direction

            # +/= 
            direction = 1
            for _ in range(x + 1, mx - 1, +1):
                if grid[y][_] < val:
                    direction += 1
                else:
                    break
            running *= direction

            if running > best:
                best = running

    print(best)
