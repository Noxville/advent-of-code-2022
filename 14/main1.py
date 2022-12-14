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
        rocks = set()
        for line in lines:
            for p in line.pts:
                rocks.add(p)
        x_min = min([r[0] for r in rocks]) - 1
        x_max = max([r[0] for r in rocks]) + 1
        y_min = min(0, min([r[1] for r in rocks]) - 1)
        y_max = max([r[1] for r in rocks]) + 1
        aby = set(get_pts(x_min, y_max, x_max, y_max))
        sand, sand_producer = set(), (500, 0)

    flag, turn = True, 0
    while flag:
        if sand_producer not in sand:
            sand.add(sand_producer)
        sand_moved = True
        while flag and sand_moved:
            sand_moved = False
            new_sand = set()
            # print(f"Sand: {sand}")
            for s in sorted(list(sand), key=lambda r: (-r[1], -r[0])):
                down, diag_l, diag_r = (s[0], s[1] + 1), (s[0] - 1, s[1] + 1), (s[0] + 1, s[1] + 1)
                # print(f"Cur sand = {s} | new_sand = {new_sand} ;; down = {down} / diag = {diag_l}")
                if down not in rocks and down not in new_sand:
                    new_sand.add(down)
                    sand_moved = True
                    if down in aby:
                        flag = False
                elif diag_l not in rocks and diag_l not in new_sand:
                    new_sand.add(diag_l)
                    sand_moved = True
                    if diag_l in aby:
                        flag = False
                elif diag_r not in rocks and diag_r not in new_sand:
                    new_sand.add(diag_r)
                    sand_moved = True
                    if diag_r in aby:
                        flag = False
                else:
                    new_sand.add(s)  # Stay where you are
            #draw(rocks, new_sand, aby, sand_producer, (x_min, x_max, y_min, y_max))
            sand = new_sand
        if flag:
            turn += 1
    print(turn)
