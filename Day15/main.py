import heapq
import copy

def part1(data):
    adjacent = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    path = []
    start = (0, 0)
    goal = (len(data)-1, len(data[0])-1)
    openList = [(data[0][0], start)]
    closedList = dict()
    
    while openList:
        cost, currentNode = heapq.heappop(openList)

        if currentNode == goal:

            while start != currentNode:
                currentNode = closedList[currentNode][0]

            return cost - data[0][0]

        for adj in adjacent:
                x = currentNode[0] + adj[0]
                y = currentNode[1] + adj[1]
                if not (((x == -1) or (x == len(data))) or ((y == -1) or (y == len(data[0])))):
                    ncost = cost + data[x][y]
                    if (x, y) not in closedList:
                        heapq.heappush(openList, (ncost, (x, y)))
                        closedList[(x, y)] = (currentNode, ncost)
                    else:
                        if ncost < closedList[(x, y)][1]:
                            closedList[(x,y)]= (currentNode, ncost)
    
    return 0

def part2(data):

    fullMaze = copy.deepcopy(data)
    # print(len(fullMaze), len(fullMaze[0]))
    tmp = copy.deepcopy(data)
    for i in range(4):
        increment(tmp, i+1)
        for i in range(len(fullMaze)):
            fullMaze[i] += copy.deepcopy(tmp[i])

    tmp = copy.deepcopy(fullMaze)
    for i in range(4):
        increment(tmp, i+1)

        for i in range(len(tmp)):
            fullMaze.append(copy.deepcopy(tmp[i]))

    #     print(len(fullMaze), len(fullMaze[0]))

    return part1(fullMaze)

def increment(L, inc):
    for i in range(len(L)):
        for j in range(len(L[0])):
            if L[i][j] + 1 > 9:
                L[i][j] = 1
            else:
                L[i][j] += 1


if __name__ == '__main__':

    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data.append([int(x) for x in line.strip()])

    # print(data)

    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')