def solve(string, x):
    for i in range(len(string)-x):
        if len(set([_ for _ in string[i:i+x]])) == x:
            return i + x


with open('case1.in') as fin:
    lines = [e.strip() for e in fin.readlines()]
    for li in lines:
        print(solve(li, 4))
        print(solve(li, 14))
