class Sensor:
    def __init__(self, s):
        filt = "".join([c for c in s if c in "1234567890,:"])
        sen, bea = [_.split(',') for _ in filt.split(":")]
        self.x = int(sen[0])
        self.y = int(sen[1])
        
        bx, by = int(bea[0]), int(bea[1])
        self.range = abs(self.x - bx) + abs(self.y - by)
                                            
    def valid_by_row(self, y):
        vert_dist = abs(y - self.y)
        remaining_power = self.range - vert_dist
        #print(f"remaining power: {remaining_power}")
        if remaining_power < 0:
            return []
        return list(range(self.x - (remaining_power), self.x + (remaining_power)))

def solve(sensors, y):
    possible = set()
    for s in sensors:
        for v in s.valid_by_row(y):
            possible.add(v)
    return len(possible)

if __name__ == "__main__":
    with open('case1.in') as fin:
        sensors = [Sensor(e.strip()) for e in fin.readlines()]
        print(solve(sensors, 2000000))
