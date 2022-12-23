import json


def words_val(s):
    sp = s
    for r in [" +", " -", " *", " //"]:
        sp = sp.replace(r, "")
    sp = sp.split(" ")
    if len(sp) == 1 and sp[0].isdigit():
        return [], int(sp[0])
    return sp, None


class Op:
    def __init__(self, s):
        sp = s.replace("/", "//").split(":")
        self.left = sp[0]
        self.right = sp[1].strip()
        self.depends, self.val = words_val(self.right)

    def __repr__(self) -> str:
        return json.dumps(self.__dict__)


if __name__ == "__main__":
    with open('case1.in') as fin:
        ops = [Op(e.strip()) for e in fin.readlines()]
        done = set()

        while len(ops):
            todo = []
            for o in ops:
                if o.val is not None or all([d in done for d in o.depends]):
                    exec(f"{o.left} = {o.right}")
                    done.add(o.left)
                else:
                    todo.append(o)
            ops = todo
        print(eval("root"))
