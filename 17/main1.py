# No need today
class Block:
    def __init__(self, shape, x, y):
        self.x = x
        self.y = y  # x, y are reference cells for the shape (min(x), min(y))
        self.shape = shape

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.shape == other.shape

    def move_lr(self, direction, grid):
        if direction == '<':
            return self._move(-1, 0, grid)
        return self._move(+1, 0, grid)

    def fall(self, grid):
        return self._move(0, -1, grid)

    def _move(self, dx, dy, grid):
        nw = Block(self.shape, self.x + dx, self.y + dy)
        xs = [x for x, y in nw.cells()]
        ys = [y for x, y in nw.cells()]
        if min(xs) <= 0 or max(xs) > 7 or min(ys) < 0 or (grid & set(nw.cells())):
            return Block(self.shape, self.x, self.y)  # can't move here sorry
        return nw  # can move

    def cells(self):
        s = self
        return {
            'SQUARE': [(s.x, s.y), (s.x + 1, s.y), (s.x, s.y + 1), (s.x + 1, s.y + 1)],
            'LINE_FLAT': [(s.x, s.y), (s.x + 1, s.y), (s.x + 2, s.y), (s.x + 3, s.y)],
            'LINE_TALL': [(s.x, s.y), (s.x, s.y + 1), (s.x, s.y + 2), (s.x, s.y + 3)],
            'STAR': [(s.x + 1, s.y), (s.x, s.y + 1), (s.x + 1, s.y + 1), (s.x + 2, s.y + 1), (s.x + 1, s.y + 2)],
            'ELL': [(s.x, s.y), (s.x + 1, s.y), (s.x + 2, s.y), (s.x + 2, s.y + 1), (s.x + 2, s.y + 2)]
        }[self.shape]


def heightmap(cells):
    # heightmap relative to the top cell
    ys = [0 for _ in range(1, 7 + 1)]
    for x, y in cells:
        ys[x - 1] = max(ys[x - 1], y)
    return [_ - max(ys) for _ in ys]


if __name__ == "__main__":
    with open('case1.in') as fin:
        jets = [list(e.strip()) for e in fin.readlines()][0]
        shapes = ['LINE_FLAT', 'STAR', 'ELL', 'LINE_TALL', 'SQUARE']

        highest_y, jet_idx, shape_idx = 0, -1, 0
        block_fall_count = 0
        block = None
        resting = set()
        lookup = {}
        skipped = 0
        while block_fall_count < 1000000000000:
            block = Block(shapes[shape_idx % len(shapes)], 3, highest_y + 3)
            shape_idx += 1

            while True:
                jet_idx += 1
                dir_string = jets[jet_idx % len(jets)]
                block = block.move_lr(dir_string, resting)
                fall = block.fall(resting)
                if block == fall:
                    for cell in fall.cells():
                        resting.add(cell)
                        highest_y = max(highest_y, 1 + cell[1])
                    block_fall_count += 1
                    break
                else:
                    block = fall

            key = tuple(heightmap(resting)), shape_idx % len(shapes), jet_idx % len(jets)
            # We're about to place a shape onto some (relative) heightmap, starting at modulo instruction jet_idx
            # Have we seen this state before?
            if key in lookup and block_fall_count > 2022:
                previous_block_fall_count, previous_highest_y = lookup[key]
                togo = 1000000000000 - block_fall_count
                skip_length = block_fall_count - previous_block_fall_count
                skips = togo // skip_length
                skipped += skips * (highest_y - previous_highest_y)
                block_fall_count += skips * skip_length
                # print(f"Skipped {skips} skips this time")
                lookup = {}  # wormholes collapse after take one
            lookup[key] = (block_fall_count, highest_y)

            if block_fall_count == 2022:
                print(highest_y)
        print(skipped + highest_y)
