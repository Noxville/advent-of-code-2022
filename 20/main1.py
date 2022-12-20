def find(val, offset, ls):
    for i, _ in enumerate(ls):
        if _[offset] == val:
            return i


def solve(raw, dec_key, mix_times):
    li = [(x * dec_key, y) for (x, y) in raw]
    N = len(li)  # store or it changes!
    for mix_count in range(mix_times):
        for fix_idx in range(N):
            old_idx = find(fix_idx, 1, li)
            val, _ = li[old_idx]
            li.pop(old_idx)
            old_idx = (old_idx + val) % (N - 1)
            old_idx = N if old_idx == 0 else old_idx
            li.insert(old_idx, (val, fix_idx))

    zero = find(0, 0, li)
    return sum([li[(zero + num) % N][0] for num in [1000, 2000, 3000]])


if __name__ == "__main__":
    with open('case1.in') as fin:
        lines = [(int(e.strip()), i) for i, e in enumerate(fin.readlines())]

        print(solve(lines, 1, 1))
        print(solve(lines, 811589153, 10))
