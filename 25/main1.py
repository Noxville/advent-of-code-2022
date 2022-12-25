def decode(s) -> int:
    if not s:
        return 0
    return (5 * decode(s[:-1])) + {
        '=': -2,
        '-': -1,
        '0': 0,
        '1': 1,
        '2': 2
    }[s[-1]]


def encode(n) -> str:
    if not n:
        return ''
    return encode((n + 2) // 5) + {  # offset by 2
        0: '=',
        1: '-',
        2: '0',
        3: '1',
        4: '2'
    }[(n + 2) % 5]


def test():
    for k, v in {
        1: '1',
        2: '2',
        3: '1=',
        4: '1-',
        5: '10',
        6: '11',
        7: '12',
        8: '2=',
        9: '2-',
        10: '20',
        15: '1=0',
        20: '1-0',
        2022: '1=11-2',
        12345: '1-0---0',
        314159265: '1121-1110-1=0',
    }.items():
        assert encode(k) == v

    for k, v in {
        '1=-0-2': 1747,
        '12111': 906,
        '2=0=': 198,
        '21': 11,
        '2=01': 201,
        '111': 31,
        '20012': 1257,
        '112': 32,
        '1=-1=': 353,
        '1-12': 107,
        '12': 7,
        '1=': 3,
        '122': 37,
    }.items():
        assert decode(k) == v


if __name__ == "__main__":
    # test()
    with open('case1.in') as fin:
        lines = [e.strip() for e in fin.readlines()]

        print(encode(sum([decode(l) for l in lines])))
