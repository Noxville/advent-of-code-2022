import sys


class Line:
    def __init__(self, s):
        pts = []
        verts = s.split(' -> ')
        for st, en in zip(verts, verts[1:]):
            sx, sy = list(map(int, st.split(',')))
            ex, ey = list(map(int, en.split(',')))
            pts.extend(get_pts(sx, sy, ex, ey))
        self.pts = pts


def get_pts(ax, ay, bx, by):
    ret = []
    if ax == bx:
        for _ in range(min(ay, by), 1 + max(ay, by)):
            ret.append((ax, _))
    else:
        for _ in range(min(ax, bx), 1 + max(ax, bx)):
            ret.append((_, ay))
    return ret


def draw(rock, sand, abyss, producer, bounding_box):
    print(f"top left is x={bounding_box[0]},{bounding_box[2]}")
    for y in range(bounding_box[2], bounding_box[3] + 1):
        line = ''
        for x in range(bounding_box[0], bounding_box[1] + 1):
            if (x, y) in rock:
                line += '#'
            elif (x, y) in abyss:
                line += 'a'
            elif (x, y) == producer:
                line += '+'
            elif (x, y) in sand:
                line += 'o'

            else:
                line += '.'
        print(line)


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

    flag, turn = True, 0
    while True:
        x, y = (500, 0)  # producer
        if (x, y) in rock_sand:
            break
        while True:
            if y > y_max:
                print(turn)
                sys.exit(0)
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
