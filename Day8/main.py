known = {2:1, 3:7, 4:4, 7:8}

letters = 'abcdefg'

def part1(codes, output):
    # data = ['be', 'cfbegad', 'cbdgef', 'fgaecd', 'cgeb', 'fdcge', 'agebfd', 'fecdb', 'fabcd', 'edb']

    data = codes

    freq = dict()
    for letter in letters:
        freq[letter] = sum([x.count(letter) for x in data])

    dataDict = dict()

    for i, key in enumerate(data):
        if len(key) in known:
            dataDict[data[i]] = known[len(key)]

    for key in dataDict:
        data.remove(key)

    for key in freq:
        if freq[key] == 9:
            for i, x in enumerate(data):
                if key not in x:
                    dataDict[data.pop(i)] = 2
                    break

    for key in freq:
        if freq[key] == 4:
            for i, x in enumerate(data):
                if key not in x and len(x) == 6:
                    dataDict[data.pop(i)] = 9
                    break

    for key in freq:
        if freq[key] == 6:
            for i, x in enumerate(data):
                if key not in x and len(x) == 5:
                    dataDict[data.pop(i)] = 3
                    break

    for key in freq:
        if freq[key] == 4:
            for i, x in enumerate(data):
                if key not in x and len(x) == 5:
                    dataDict[data.pop(i)] = 5
                    break

    for key in dataDict:
        if dataDict[key] == 7:
            tmp = key
            break

    for i, x in enumerate(data):
        if set(key) <= set(x):
            dataDict[data.pop(i)] = 0
            dataDict[data.pop(0)] = 6
            break

    # print(data, dataDict, freq)
    tmp = []
    for o in output:
        tmp.append(str(dataDict[o]))
    
    # print(int(''.join(tmp)))

    return int(''.join(tmp))


digits = {2: 1, 3: 7, 4: 4, 7: 8}

digits = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']


if __name__ == '__main__':

    codes = []
    outputs = []
    with open('input.txt', 'r') as file:
        for line in file:

            line = line.strip().split(' ')
            # tmp = line[-4:]
            codes.append([''.join(sorted(x)) for x in line[:10]])
            outputs.append([''.join(sorted(x)) for x in line[-4:]])


    tmp = 0
    for code, output in zip(codes, outputs):
        tmp += part1(code, output)

    print(tmp)
    # print(f'Part 1: {part1(codes[0], outputs[0])}')
    # print(f'Part 2: {part2(data)}')