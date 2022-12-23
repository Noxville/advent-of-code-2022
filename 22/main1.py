def split_ins(ins):
    ret, cur = [], ""
    for c in ins:
        if (len(cur) == 0) or cur[-1].isalpha() == c.isalpha():
            cur += c
        else:
            ret.append(cur)
            cur = c
    ret.append(cur)
    return [int(_) if _.isdigit() else _ for _ in ret]


def update_dir(cur_dir, rot):
    cardinal = 'NESW'
    return cardinal[(cardinal.index(cur_dir) + (1 if rot == 'R' else -1)) % 4]


class Node:
    def __init__(self, x, y, item):
        self.x = x
        self.y = y
        self.item = item
        self.neighbours = dict()

    def add_neighbour(self, nx, ny, direction, new_dir, grid):
        if direction in self.neighbours:
            # print(f"for cell {self.x, self.y}; direction {direction} already in {self.neighbours}")
            assert direction not in self.neighbours
        assert (nx, ny) in grid
        self.neighbours[direction] = (nx, ny, new_dir)


def prt(grid, xx, yy):
    for _y in range(len(grid)):
        line = ""
        for _x in range(len(grid[0])):
            if (_x, _y) == (xx, yy):
                line += "X"
            else:
                line += grid[yy][xx]
        print(line)


def create_graph(p1=True):
    G = {}

    overall_mx_x, overall_mx_y = 0, 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] in '#.':
                overall_mx_x = max(overall_mx_x, x)
                overall_mx_y = max(overall_mx_y, y)
                G[x, y] = Node(x, y, grid[y][x])

    for (x, y) in G:
        for direct, dx, dy in [
            ('N', +0, -1),
            ('S', +0, +1),
            ('E', +1, +0),
            ('W', -1, +0)
        ]:
            if (x + dx, y + dy) in G:
                G[x, y].add_neighbour(x + dx, y + dy, direct, direct, G)

    if p1:
        min_x = {i: min([x for x, y in G if y == i]) for i in range(overall_mx_y)}
        max_x = {i: max([x for x, y in G if y == i]) for i in range(overall_mx_y)}
        min_y = {i: min([y for x, y in G if x == i]) for i in range(overall_mx_x)}
        max_y = {i: max([y for x, y in G if x == i]) for i in range(overall_mx_x)}

        for y in range(overall_mx_y):
            G[min_x[y], y].add_neighbour(max_x[y], y, 'W', 'W', G)
            G[max_x[y], y].add_neighbour(min_x[y], y, 'E', 'E', G)

        for x in range(overall_mx_x):
            G[x, min_y[x]].add_neighbour(x, max_y[x], 'N', 'N', G)
            G[x, max_y[x]].add_neighbour(x, min_y[x], 'S', 'S', G)

    else:
        for _ in range(50):
            G[_, 100].add_neighbour(50, 50 + _, 'N', 'E', G)
            G[50, 50 + _].add_neighbour(_, 100, 'W', 'S', G)

            G[100 + _, 49].add_neighbour(99, 50 + _, 'S', 'W', G)
            G[99, 50 + _].add_neighbour(100 + _, 49, 'E', 'N', G)

            G[49, 150 + _].add_neighbour(50 + _, 149, 'E', 'N', G)
            G[50 + _, 149].add_neighbour(49, 150 + _, 'S', 'W', G)

            G[_, 199].add_neighbour(100 + _, 0, 'S', 'S', G)
            G[100 + _, 0].add_neighbour(_, 199, 'N', 'N', G)

            G[0, 150 + _].add_neighbour(50 + _, 0, 'W', 'S', G)
            G[50 + _, 0].add_neighbour(0, 150 + _, 'N', 'E', G)

            G[0, 100 + _].add_neighbour(50, _, 'W', 'E', G)
            G[50, _].add_neighbour(0, 100 + _, 'W', 'W', G)

            G[149, _].add_neighbour(99, 100 + _, 'E', 'W', G)
            G[99, 100 + _].add_neighbour(149, _, 'E', 'W', G)

    return G


def solve(grid, instructs, p1=True):
    G = create_graph(p1)

    x, y, direction = grid[0].index('.'), 0, 'E'

    for idx, instruct in enumerate(instructs):
        if idx % 2 == 1:
            direction = update_dir(direction, instruct)
        else:
            for _ in range(instruct):
                px, py, pd = G[x, y].neighbours[direction]
                if G[px, py].item != '#':
                    x, y, direction = px, py, pd

    print(1 + y, 1 + x, direction)
    print((1000 * (1 + y)) + (4 * (1 + x)) + {'N': 3, 'S': 1, 'E': 0, 'W': 2}[direction])


if __name__ == "__main__":
    with open('case1.in') as fin:
        lines = [e.replace('\n', '') for e in fin.readlines()]
        grid = [list(l) for l in lines[:-2]]
        ins = split_ins(lines[-1])
        solve(grid, ins, p1=True)
        solve(grid, ins, p1=False)
