from main1 import Line, get_pts

if __name__ == "__main__":
    with open('case1.in') as fin:
        lines = [Line(e.strip()) for e in fin.readlines()]
        rock_sand = set()
        for line in lines:
            for p in line.pts:
                rock_sand.add(p)
        x_min = min([r[0] for r in rock_sand]) - 1
        x_max = max([r[0] for r in rock_sand]) + 1
        y_min = min(0, min([r[1] for r in rock_sand]) - 1)
        y_max = max([r[1] for r in rock_sand]) + 1
        for p in get_pts(x_min - 500, 1 + y_max, x_max + 500, 1 + y_max):
            rock_sand.add(p)  # let's make an abyss

    flag, turn = True, 0
    while True:
        x, y = (500, 0)  # producer
        if (x, y) in rock_sand:
            break
        while True:
            if (x, 1 + y) not in rock_sand:
                y += 1
            elif (x - 1, 1 + y) not in rock_sand:
                (x, y) = (x - 1, 1 + y)
            elif (1 + x, 1 + y) not in rock_sand:
                (x, y) = (1 + x, 1 + y)
            else:
                rock_sand.add((x, y))
                turn += 1
                break
    print(turn)
