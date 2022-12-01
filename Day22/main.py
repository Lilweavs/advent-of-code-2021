from itertools import product
from collections import defaultdict
import re

def part1(data):

    d = defaultdict(int)
    for flip, step in data:

        x = [_ for _ in range(step[0], step[1]+1)]
        y = [_ for _ in range(step[2], step[3]+1)]
        z = [_ for _ in range(step[4], step[5]+1)]

        on = list(product(x, y, z))

        if flip == 'on':
            for points in on:
                d[points] = 1
        else:
            for points in on:
                d[points] = 0
        
    # print(d)

    return sum(d.values())

def part2(data):

    return 0

if __name__ == '__main__':

    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            if 'on' in line:
                data.append(('on', [int(x) for x in re.findall(r'-?\d+', line)]))
            else:
                data.append(('off', [int(x) for x in re.findall(r'-?\d+', line)]))

    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


