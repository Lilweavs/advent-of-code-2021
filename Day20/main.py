import copy

algorithm = '..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#'

algorithm = '#.#.#.....###.###..##...##.#.###..##..#.#..#.#..###.#.####.######......#.#..###.#....#.#...########....#.#..#.##.##.#.######..#..#..#.##.##.##..###..##.####.##.##.#.##.##..#.#..#####..##..#.##.#.#......###.#.#..#.#..##.###..###.#####.#...##.##.#.##..####..#.....####..........#...#.#..#..#..##.##....##...#.#..#.....#.##..####.#.##.#.##.#.####.##.#.##..#..##.#.##.###.....##.#.####...#.#.##..#..##...####..#.#.#...###....#..#.#..#..###..#..#..#...#.#.##.##.#...######.##..##.###.#.###.###..#......#..#..#.#...#..'


algorithm = ''.join(['0' if x == '.' else '1' for x in algorithm])

def part1(data, n):

    original = copy.deepcopy(data)

    for m in range(n):
        if m % 2 == 0:
            new = [['1']*(4 + len(original[0])) for i in range(0, len(original)+4)]
        else:
            new = [['0']*(4 + len(original[0])) for i in range(0, len(original)+4)]
        # original = copy.deepcopy(data)
        cnt = 0
        for i in range(1, len(new)-1):
            for j in range(1, len(new[0])-1):
                tmp = getAdjacent(new, original, i, j, m)
                tmp = int(tmp, 2)
                new[i][j] = algorithm[tmp]
                cnt+=1

        original = copy.deepcopy(new)
    
    cnt = 0
    for row in original:
        for col in row:
            if col == '1':
                cnt+=1

    return cnt, original

def getAdjacent(new, old, x, y, m):
    tmp = ''
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            tmpx = x + i; tmpy = y + j
            if tmpx < 2 or tmpx > len(new)-3 or tmpy < 2 or tmpy > len(new[0])-3:
                # tmp += '0'
                if m % 2 == 0:
                    tmp += '0'
                else:
                    tmp += '1'
            else:
                tmp += old[tmpx-2][tmpy-2]

    return tmp


def part2(data):

    board = dict()
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '#':
                board[(i, j)] == 1

    return 0

if __name__ == '__main__':

    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data.append(['0' if x == '.' else '1' for x in line.strip()])


    print(f'Part 1: {part1(data, 2)[0]}')
    print(f'part 2: {part1(data, 50)[0]}')

    # for row in pic:
    #     print(' '.join(['#' if x == '1' else '.' for x in row]))

