import copy

def part1(data):

    # data = [[1,1,1,1,1],
    #         [1,9,9,9,1],
    #         [1,9,1,9,1],
    #         [1,9,9,9,1],
    #         [1,1,1,1,1]]

    # data= [[5,4,8,3,1,4,3,2,2,3],
    #        [2,7,4,5,8,5,4,7,1,1],
    #        [5,2,6,4,5,5,6,1,7,3],
    #        [6,1,4,1,3,3,6,1,4,6],
    #        [6,3,5,7,3,8,5,4,7,8],
    #        [4,1,6,7,5,2,4,6,4,5],
    #        [2,1,7,6,8,4,1,7,2,1],
    #        [6,8,8,2,8,8,1,1,3,4],
    #        [4,8,4,6,8,4,8,5,5,4],
    #        [5,2,8,3,7,5,1,5,2,6]]

    flashes = 0
    for i in range(100):
        flashes += step(data)
    
    print(data)
   
    return flashes

def step(data):
    flash = 0
    cnt = 0
    cont = True
    while cont:
        cont = False
        for i in range(len(data)):
            for j in range(len(data)):
                if cnt == 0:
                    data[i][j] += 1
                    if data[i][j] > 9:
                        # flash += 1
                        cont = True
                        # data[i][j] = 0
                        # propagate(data, i, j)
                else:
                    if data[i][j] > 9:
                        flash += 1
                        cont = True
                        data[i][j] = 0
                        propagate(data, i, j)
        cnt += 1
    return flash

def propagate(data, i, j):
    adjacent = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for adj in adjacent:            
        x = i + adj[0]
        y = j + adj[1]
        if not (((x == -1) or (x == len(data))) or ((y == -1) or (y == len(data[0])))):
            if data[x][y] == 0:
                continue
            else:
                data[x][y] += 1


def part2(data):

    # data= [[5,4,8,3,1,4,3,2,2,3],
    #     [2,7,4,5,8,5,4,7,1,1],
    #     [5,2,6,4,5,5,6,1,7,3],
    #     [6,1,4,1,3,3,6,1,4,6],
    #     [6,3,5,7,3,8,5,4,7,8],
    #     [4,1,6,7,5,2,4,6,4,5],
    #     [2,1,7,6,8,4,1,7,2,1],
    #     [6,8,8,2,8,8,1,1,3,4],
    #     [4,8,4,6,8,4,8,5,5,4],
    #     [5,2,8,3,7,5,1,5,2,6]]

    cnt = 0
    flashes = 0
    while sum([sum(x) for x in data]) != 0:
        flashes += step(data)
        cnt += 1

    return cnt

if __name__ == '__main__':

    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data.append([int(x) for x in line.strip()])


    print(f'Part 1: {part1(copy.deepcopy(data))}')
    print(f'Part 2: {part2(copy.deepcopy(data))}')