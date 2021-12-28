from itertools import combinations
def part1(data):

    out = list(combinations(data, 12))

    return 0

def part2(data):

    return 0

if __name__ == '__main__':

    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data.append([int(x) for x in line.strip().split(',')])

    print(len(data))

    # print(f'Part 1: {part1(data)}')
    # print(f'Part 2: {part2(data)}')