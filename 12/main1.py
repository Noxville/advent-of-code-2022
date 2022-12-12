from queue import PriorityQueue


def h_diff(frm, too):
    return ord(too if too != 'E' else 'z') - ord(frm if frm != 'S' else 'a') <= 1


def dijk(start, cells, neighbours):
    tdist = {c: float('inf') for c in cells}
    seen = set()
    tdist[start] = 0

    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        (dist, vert) = pq.get()
        seen.add(vert)

        for neighbor in neighbours.get(vert, []):
            if neighbor not in seen:
                old_cost = tdist[neighbor]
                new_cost = tdist[vert] + 1
                if new_cost < old_cost:
                    pq.put((new_cost, neighbor))
                    tdist[neighbor] = new_cost
    return tdist


if __name__ == "__main__":
    with open('case1.in') as fin:
        cons, cset, S, E, alist = {}, set(), None, None, []
        grid = [list(e.strip()) for e in fin.readlines()]
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                cset.add((x, y))
                if grid[y][x] == 'S':
                    S = (x, y)
                elif grid[y][x] == 'E':
                    E = (x, y)
                elif grid[y][x] == 'a':
                    alist.append((x, y))
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    sx, sy = x + dx, y + dy
                    if 0 <= sy < len(grid) and 0 <= sx < len(grid[0]) and h_diff(grid[y][x], grid[sy][sx]):
                        neighs = cons.get((sx, sy), list())
                        neighs.append((x, y))
                        cons[(sx, sy)] = neighs
        # Part 1
        dists = dijk(E, list(cset), cons)  # from the end to all cells
        print(dists[S])
        # Part 2
        print(min([dists[a] for a in alist]))