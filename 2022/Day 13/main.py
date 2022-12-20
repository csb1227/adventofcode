from enum import Enum
import functools
import logging
import json


def parse_input_part_1(x):
    raw_input = [packet for packet in open(x).read().split('\n')]

    packet_pairs = [[]]
    for packet in raw_input:
        if packet:
            packet_pairs[-1].append(json.loads(packet))
        else:
            packet_pairs.append([])

    return packet_pairs


def parse_input_part_2(x):
    raw_input = [packet for packet in open(x).read().split('\n')]

    packets = []
    for packet in raw_input:
        if packet:
            packets.append(packet)

    packets.append('[[2]]')
    packets.append('[[6]]')

    return packets


class Status(Enum):
    VALID = 1
    INVALID = 2
    UNDETERMINED = 3


def compare_packets(first, second, indent = 0):
    logging.debug(f'{" " * indent}- Compare {first} vs {second}')
    status = Status.UNDETERMINED

    packets_remain = True
    while packets_remain and status == Status.UNDETERMINED:

        if len(first) == 0 and len(second) == 0:
            status = Status.UNDETERMINED
            packets_remain = False
            continue
        elif len(first) == 0:
            logging.debug(f'{" " * indent}  - Left side ran out of items, so inputs are in the right order')
            status = Status.VALID
            packets_remain = False
            continue
        elif len(second) == 0:
            logging.debug(f'{" " * indent}  - Right side ran out of items, so inputs are not in the right order')
            status = Status.INVALID
            packets_remain = False
            continue

        left = first.pop(0)
        right = second.pop(0)

        try:
            if all(isinstance(x, int) for x in [left, right]):
                logging.debug(f'{" " * indent}  - Compare {left} vs {right}')
                if left < right:
                    logging.debug(f'{" " * indent}    - Left side is smaller, so inputs are in the right order')
                    status = Status.VALID
                elif left > right:
                    logging.debug(f'{" " * indent}    - Right side is smaller, so inputs are not in the right order')
                    status = Status.INVALID
                else:
                    status = Status.UNDETERMINED
            elif all(isinstance(x, list) for x in [left, right]):
                status = compare_packets(left, right, indent+2)
            elif isinstance(left, list):
                status = compare_packets(left, [right], indent+2)
            else:
                status = compare_packets([left], right, indent+2)

        except Exception as ex:
            logging.error(ex)

    return status


def packet_sort(first, second):
    status = compare_packets(json.loads(first), json.loads(second))
    if status == Status.VALID:
        return 1
    else:
        return -1


def part_1(x):
    pair_validation = []
    for ix, packet_pair in enumerate(x):
        logging.debug(f'== Pair {ix+1} ==')
        status = compare_packets(packet_pair[0], packet_pair[1])
        pair_validation.append(status)
        logging.debug(f'== Pair {ix+1} : {status} ==\n')

    return sum([ix+1 for ix, validation in enumerate(pair_validation) if validation == Status.VALID])


def part_2(x):
    sorted_packets = list(reversed(sorted(x, key=functools.cmp_to_key(packet_sort))))
    two = sorted_packets.index('[[2]]') + 1
    six = sorted_packets.index('[[6]]') + 1

    return two * six


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR, format='%(message)s')

    example_input = './input/example.txt'
    puzzle_input = './input/puzzle.txt'

    packet_pairs = parse_input_part_1(puzzle_input)

    print(f'Part 1: {part_1(packet_pairs)}')

    packets = parse_input_part_2(puzzle_input)

    print(f'Part 2: {part_2(packets)}')
