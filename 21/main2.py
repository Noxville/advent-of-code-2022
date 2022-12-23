from copy import deepcopy
from main1 import Op


def search(lower, upper, roots, operations):
    orig = deepcopy(operations)
    done, mid = {'humn'}, (lower + upper) // 2
    exec(f"humn = {mid}")

    while len(operations):
        todo = []
        for o in operations:
            if o.val is not None or all([d in done for d in o.depends]):
                exec(f"{o.left} = {o.right}")
                done.add(o.left)
            else:
                todo.append(o)
        operations = todo

    if eval(roots[0]) == eval(roots[1]):
        return mid
    return search(mid, upper, roots, orig) if eval(roots[0]) > eval(roots[1]) else search(lower, mid, roots, orig)


if __name__ == "__main__":
    with open('case1.in') as fin:
        ops = [Op(e.strip()) for e in fin.readlines()]

        root = ops.pop([i for i, v in enumerate(ops) if v.left == 'root'][0])
        humn = ops.pop([i for i, v in enumerate(ops) if v.left == 'humn'][0])

        N = 10 ** 20
        print(search(-N, N, root.depends, deepcopy(ops)))
       