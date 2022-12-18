def neigh(_x, _y, _z):
    return [
        (+1 + _x, +0 + _y, +0 + _z),
        (+0 + _x, +1 + _y, +0 + _z),
        (+0 + _x, +0 + _y, +1 + _z),
        (-1 + _x, +0 + _y, +0 + _z),
        (+0 + _x, -1 + _y, +0 + _z),
        (+0 + _x, +0 + _y, -1 + _z),
    ]


if __name__ == "__main__":
    with open('case1.in') as fin:
        seen = set()
        for x, y, z in [list(map(int, e.strip().split(','))) for e in fin.readlines()]:
            seen.add((x, y, z))

        surfaces = 0
        for x, y, z in seen:
            for n in neigh(x, y, z):
                surfaces += 0 if n in seen else 1
    print(surfaces)

    # flood a bounding box
    x_range = -1 + min(x for x, y, z in seen), 1 + max(x for x, y, z in seen)
    y_range = -1 + min(y for x, y, z in seen), 1 + max(y for x, y, z in seen)
    z_range = -1 + min(z for x, y, z in seen), 1 + max(z for x, y, z in seen)

    Q = [(z_range[0], y_range[0], z_range[0])]

    flood = set()
    while Q:
        this = Q.pop()
        for n in neigh(*this):
            if x_range[0] <= n[0] <= x_range[1] and \
                    y_range[0] <= n[1] <= y_range[1] and \
                    z_range[0] <= n[2] <= z_range[1] and \
                    n not in seen and \
                    n not in flood:
                Q.append(n)
        flood.add(this)

    outer_surfaces = 0
    for x, y, z in seen:
        for n in neigh(x, y, z):
            outer_surfaces += 1 if n in flood else 0
    print(outer_surfaces)
