import re

def part1(data):
    m = max([max(row) for row in data]) + 1
    board = [[0]*m for i in range(m)]

    for pts in data:
        x1, y1, x2, y2 = pts
        if x1 == x2:
            ypts = [i for i in range(min(y1, y2), max(y1, y2)+1)]
            xpts = [x1 for i in range(len(ypts))]
        elif y1 == y2:
            xpts = [i for i in range(min(x1, x2), max(x1, x2)+1)]
            ypts = [y1 for i in range(len(xpts))]
        else:
            continue

        for i in range(len(xpts)):
            board[xpts[i]][ypts[i]] += 1

    cnt = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] >= 2:
                cnt += 1

    return cnt

def part2(data):
    m = max([max(row) for row in data]) + 1
    board = [[0]*m for i in range(m)]

    for pts in data:
        x1, y1, x2, y2 = pts
        if x1 == x2:
            ypts = [i for i in range(min(y1, y2), max(y1, y2)+1)]
            xpts = [x1 for i in range(len(ypts))]
        elif y1 == y2:
            xpts = [i for i in range(min(x1, x2), max(x1, x2)+1)]
            ypts = [y1 for i in range(len(xpts))]
        else:
            xpts = [i for i in range(min(x1, x2), max(x1, x2)+1)]
            if x1 > x2:
                xpts.reverse()
            ypts = [i for i in range(min(y1, y2), max(y1, y2)+1)]
            if y1 > y2:
                ypts.reverse()
            
        for i in range(len(xpts)):
            board[xpts[i]][ypts[i]] += 1

    cnt = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] >= 2:
                cnt += 1

    return cnt

if __name__ == '__main__':

    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            nums = re.findall(r'\d+', line.strip())
            data.append([int(x) for x in nums])
 
    print(part1(data))
    print(part2(data))

