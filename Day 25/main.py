def stepRight(data):
    i = 0
    moved = False
    while i < len(data):
        j = 0
        tmp = len(data[0])-1
        if data[i][j] != '.':
            while data[i][tmp] == '>':
                tmp -= 1
           
        while j <= tmp:

            if data[i][j] == '>':
                while data[i][j] == '>':
                    j += 1
                    if j > tmp:
                        if data[i][0] == '.':
                            data[i][j-1], data[i][0] = '.', '>'
                            moved = True
                        break
                    else:
                        if data[i][j] == '.':
                            data[i][j-1], data[i][j] = '.', '>'
                            j += 1
                            moved = True
                    if j > tmp:
                        break
            else:
                j += 1
        i += 1

    return moved

def stepDown(data):
    i = 0
    moved = False
    while i < len(data[0]):
        j = 0
        tmp = len(data)-1
        if data[j][i] != '.':
            while data[tmp][i] == 'v':
                tmp -= 1
           
        while j <= tmp:

            if data[j][i] == 'v':
                while data[j][i] == 'v':
                    j += 1
                    if j > tmp:
                        if data[0][i] == '.':
                            data[j-1][i], data[0][i] = '.', 'v'
                            moved = True
                        break
                    else:
                        if data[j][i] == '.':
                            data[j-1][i], data[j][i] = '.', 'v'
                            j += 1
                            moved = True
                    if j > tmp:
                        break
            else:
                j += 1
        i += 1

    return moved

def part1(data):

    # Sea Cucumber Order
    # East
    # South

    moved = True
    cnt = 0
    while moved:

        moved = stepRight(data)
        moved |= stepDown(data)

        cnt += 1
        

    # for row in data:
    #     print(' '.join(row))

    return cnt

def part2(data):

    return 0 

if __name__ == '__main__':

    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data.append(list(line.strip()))


    print(f'Part 1: {part1(data)}')