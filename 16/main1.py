import collections
import functools
import sys

sys.setrecursionlimit(10000)

if __name__ == "__main__":
    valves = []
    flows = {}
    dist = collections.defaultdict(lambda: 10 ** 7)

    with open('case1.in') as fin:
        for s in [e.strip() for e in fin.readlines()]:
            sp = s.replace(',', '').split()
            valve, rate = sp[1], int(sp[4][5:-1])
            valves.append(valve)
            flows[valve] = rate
            for other in sp[9:]:
                dist[valve, other] = 1

    for k in valves:
        for i in valves:
            for j in valves:
                dist[i, j] = min(dist[i, j], dist[i, k] + dist[k, j])


    @functools.cache
    def recurse(time_left, start, remaining):
        best = 0
        for node in remaining:
            if dist[start, node] > time_left:  # No time to get here.
                continue
            best = max(best, flows[node] * (time_left - 1 - dist[start, node]) + \
                       recurse(time_left - 1 - dist[start, node], node, frozenset(remaining - {node})))
        return best


    positive_flows = [v for v, rate in flows.items() if rate]  # We don't travel unless we can make it flow!
    print(recurse(30, 'AA', frozenset(positive_flows)))


    @functools.cache
    def recurse_with_elephant(time_left, start, remaining, elephant_available=False):
        best = 0
        for node in remaining:
            if dist[start, node] > time_left:  # No time to get here.
                continue
            this = flows[node] * (time_left - 1 - dist[start, node]) + \
                   recurse_with_elephant(time_left - 1 - dist[start, node],
                                         node,
                                         frozenset(remaining - {node}),
                                         elephant_available)
            if elephant_available:
                this = max(this, recurse_with_elephant(26, 'AA', remaining))
            best = max(this, best)
        return best


    print(recurse_with_elephant(26, 'AA', frozenset(positive_flows), elephant_available=True))
