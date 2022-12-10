class Buffer:
    def __init__(self):
        self.cur_line = ''
        self.lines = list()

    def add_c(self, new_c):
        self.cur_line += new_c
        if len(self.cur_line) == 40:
            self.lines.append(self.cur_line)
            self.cur_line = ''

    def __repr__(self):
        return "\n".join(self.lines)

    def update(self, cyc, x):
        row, col = cyc // 40, cyc % 40
        if col in [x, x + 1, x + 2]:
            self.add_c('#')
        else:
            self.add_c('.')


if __name__ == "__main__":
    with open('case1.in') as fin:
        ins = [e.strip() for e in fin.readlines()]
        val, cycle, buff = 1, 0, Buffer()
        for idx, i in enumerate(ins):
            s = i.split(' ')
            if s[0] == 'noop':
                cycle += 1
                buff.update(cycle, val)
            elif s[0] == 'addx':
                for c in range(2):
                    cycle += 1
                    buff.update(cycle, val)
                val += int(s[1])
        buff.update(cycle, val)
    print(buff)
