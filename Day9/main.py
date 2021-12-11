def part1(data):
    adjacent = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    lows = []
    score = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            tmp = []
            for adj in adjacent:            
                x = i + adj[0]
                y = j + adj[1]
                if not (((x == -1) or (x == len(data))) or ((y == -1) or (y == len(data[0])))):
                    tmp.append(data[x][y])

            if all([data[i][j] < x for x in tmp]):
                score += (data[i][j] + 1)
                lows.append((i, j))

    return score, lows


def part2(data, lowPts):
    adjacent = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    top = []
    for pt in lowPts:
        openList = [pt]
        closedList = []

        while openList:

            currentNode = openList.pop()
            if currentNode not in closedList:
                closedList.append(currentNode)
            else:
                continue

            for adj in adjacent:            
                x = currentNode[0] + adj[0]
                y = currentNode[1] + adj[1]
                if not (((x == -1) or (x == len(data))) or ((y == -1) or (y == len(data[0])))):
                    if data[x][y] != 9 and (x, y) not in closedList:
                        openList.append((x, y))

        top.append(len(closedList))

    top.sort()

    score = top[-1]*top[-2]*top[-3]

    return score

if __name__ == '__main__':

    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data.append([int(x) for x in line.strip()])

    score, lowPts = part1(data)

    print(f'Part 1: {score}')
    print(f'Part 1: {part2(data, lowPts)}')