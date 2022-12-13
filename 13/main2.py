from main1 import Packet


if __name__ == "__main__":
    divider_2, divider_6 = Packet("[[2]]"), Packet("[[6]]")
    with open('case1.in') as fin:
        packets = [Packet(e.strip()) for e in fin.readlines() if e.strip() != ''] + [divider_2, divider_6]
    std = sorted(packets)
    print((1 + std.index(divider_2)) * (1 + std.index(divider_6)))
