class Sensor:
    def __init__(self, s):
        self.s = s
        filt = "".join([c for c in s if c in "1234567890,:"])
        sen, bea = [_.split(',') for _ in filt.split(":")]
        self.x = int(sen[0])
        self.y = int(sen[1])

        bx, by = int(bea[0]), int(bea[1])
        self.range = abs(self.x - bx) + abs(self.y - by)

    def valid_by_row(self, y):
        vert_dist = abs(y - self.y)
        remaining_power = self.range - vert_dist
        if remaining_power < 0:
            return []
        return list(range(self.x - (remaining_power), self.x + (remaining_power)))

    def out_of_range(self, x, y):  # Is this point out of range of this sensor?
        return (abs(self.x - x) + abs(self.y - y)) > self.range

    def generate_ring(self, max_xy):  # make a circle with radius 1 + self.range, with center (self.x, self.y)
        for arc_x in range(0, 1 + self.range):
            arc_y = 1 + self.range - arc_x
            for sign_x in (-1, +1):  # one quarter * 4
                for sign_y in (-1, +1):
                    x, y = sign_x * (arc_x + self.x), sign_y * (arc_y + self.y)
                    if 0 <= x <= max_xy and 0 <= y <= max_xy:
                        yield x, y


if __name__ == "__main__":
    with open('case1.in') as fin:
        sensors = [Sensor(e.strip()) for e in fin.readlines()]
        for sidx, s in enumerate(sensors):
            other_sensors = [_ for _ in sensors if s.s != _.s]
            for ringx, ringy in s.generate_ring(4000000):
                flag = True
                for ots in other_sensors:
                    if not ots.out_of_range(ringx, ringy):
                        flag = False
                        break
                if flag:
                    print(ringx, ringy, ringx * 4000000 + ringy)
