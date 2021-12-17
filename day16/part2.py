import sys
from lib import timed_run
from dataclasses import dataclass
from functools import reduce


@dataclass
class Literal:
    version: int
    id: int
    value: int = 0

    def parse(self, stream, idx):
        binary = ''
        while True:
            prefix, idx = read_int(stream, idx, 1)
            block, idx = read_stream(stream, idx, 4)
            binary += block
            if prefix == 0:
                break
        self.value = int(binary, base=2)
        return idx

    def calculate(self):
        return self.value


def get_operator(func):
    @dataclass
    class Operator:
        version: int
        id: int
        length_type: int = 0
        length: int = 0
        sub_packets: list = None

        def parse(self, stream, idx):
            self.sub_packets = list()
            self.length_type, idx = read_int(stream, idx, 1)
            if self.length_type == 0:
                self.length, idx = read_int(stream, idx, 15)
                goal_idx = idx + self.length
                while idx < goal_idx:
                    packet, idx = parse_packet(stream, idx)
                    self.sub_packets.append(packet)
            else:
                self.length, idx = read_int(stream, idx, 11)
                for _ in range(self.length):
                    packet, idx = parse_packet(stream, idx)
                    self.sub_packets.append(packet)
            return idx

        def calculate(self):
            return func(tuple(pkt.calculate() for pkt in self.sub_packets))
    return Operator


id_to_type = {
    0: get_operator(sum),
    1: get_operator(lambda values: reduce(lambda x, y: x * y, values)),
    2: get_operator(min),
    3: get_operator(max),
    4: Literal,
    5: get_operator(lambda values: int(values[0] > values[1])),
    6: get_operator(lambda values: int(values[0] < values[1])),
    7: get_operator(lambda values: int(values[0] == values[1])),
}


def read_stream(stream, idx, n):
    return stream[idx:idx + n], idx + n


def read_int(stream, idx, n):
    binary, idx = read_stream(stream, idx, n)
    return int(binary, base=2), idx


def parse_packet(stream, idx):
    version, idx = read_int(stream, idx, 3)
    id, idx = read_int(stream, idx, 3)
    packet = id_to_type[id](version, id)
    idx = packet.parse(stream, idx)
    return packet, idx


@timed_run
def read_input():
    binary = ''
    for char in sys.stdin.read().strip():
        binary += f'{int(char, 16):0>{4}b}'
    return binary


@timed_run
def solve(raw):
    packet, idx = parse_packet(raw, 0)
    return packet.calculate()


if __name__ == '__main__':
    print(solve(read_input()))
