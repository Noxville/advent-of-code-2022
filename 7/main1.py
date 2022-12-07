class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = dict()  # filename -> size
        self.dirs = dict()  # filename -> Dir()
        self.size = None

    def add_file(self, file, size):
        self.files[file] = size

    def add_dir(self, dir):
        self.dirs[dir] = Dir(dir, self)  # point at parent

    def descend(self, dir):
        return self.dirs[dir]

    def update_size(self):
        self.size = sum(self.files.values()) + sum([_.size for _ in self.dirs.values()])


root, cur, mode = Dir("/", None), None, ""
root.parent = root  # solves `cd ..` on root

with open('case1.in') as fin:
    lines = [e.strip() for e in fin.readlines()]
    for li in lines:
        if li.startswith('$'):
            if li == '$ cd /':
                cur = root
            elif li == '$ cd ..':
                cur = cur.parent
            elif li == '$ ls':
                mode = 'ls'
            elif li.startswith('$ cd '):
                subdir = li.split()[-1]
                cur = cur.descend(subdir)
        else:
            sp = li.split()
            if li.startswith('dir '):
                cur.add_dir(sp[1])  # It's a dir
            else:
                cur.add_file(sp[1], int(sp[0]))  # It's a file

# Just BFS first rather than memoizing
todo, calc = [root], []
while todo:
    this = todo.pop(0)
    calc.append(this)
    for _ in this.dirs.values():
        todo.append(_)

running_total = 0
for d in calc[::-1]:
    d.update_size()
    running_total += d.size if d.size <= 100000 else 0
print(running_total)

#  Part 2
std_sizes = sorted([d.size for d in calc[::-1]])
print([s for s in std_sizes if root.size - s < 40000000][0])
