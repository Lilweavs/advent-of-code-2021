

from os import PathLike


def part1(data, rules, unique_chars):

    polymer = dict(data)
    

    # unique_vals = set(polymer)

    # freq = {'N':2, 'C':1, 'H':0, 'B':1}
    # start = 'NNCB'
    # OHFNNCKCVOBHSSHONBNF
    start = 'OHFNNCKCVOBHSSHONBNF'

    s = set(start)

    freq = {x : start.count(x) for x in set(unique_chars)}


    for i in range(len(start)-1):
        tmp = start[i:i+2]
        polymer[start[i:i+2]] += 1

    polymer_copy = data

    for j in range(40):
        for key in polymer:
            if polymer[key] > 0:
                polymer_copy[key] -= polymer[key]
                tmp1, tmp2 = rules[key]
                polymer_copy[tmp1] += polymer[key]
                polymer_copy[tmp2] += polymer[key]
                
                freq[tmp1[1]] += polymer[key]
                
                # for c in tmp1:
                #     freq[c] += key[1]
                # for c in tmp2:
                #     freq[c] += key[1]

        for key in polymer:
            polymer[key] += polymer_copy[key]
            polymer_copy[key] = 0

        print(sum([polymer[key] for key in polymer]) + 1 )
        # polymer_copy = dict(data)


    # freq = {'N':0, 'C':0, 'H':0, 'B':0}
    # for key in polymer:
    #     # c1 = key[0]
    #     # c2 = key[1]
    #     c1, c2 = key
    #     freq[c1] += polymer[key]
    #     freq[c2] += polymer[key]

    # for key in freq:
    #     if key == start[0]:
    #         freq[key] + 1

    tmp = list(freq.values())
    print(tmp)

    return max(tmp) - min(tmp)

    # print(len(rules))

    # polymer = list(polymer)

    # for j in range(5):
    #     i = 0
    #     while i != len(polymer):
    #         tmp = ''.join(polymer[i:i+2])
    #         if tmp in rules:
    #             polymer.insert(i+1, rules[tmp])
    #             i = i + 2
    #         else:
    #             i = i + 1

    # freq = [polymer.count(x) for x in unique_vals]

    # print(freq)

    # # print(''.join(polymer))
    # return max(freq) - min(freq)

if __name__ == '__main__':

    rules = dict()
    data = dict()
    letters = []
    with open('input.txt', 'r') as file:
        for line in file:
            tmp = line.strip().split(' -> ')
            rules[tmp[0]] = (tmp[0][0] + tmp[1], tmp[1] + tmp[0][1] )
            data[tmp[0]] = 0
            letters.append(''.join(tmp))
    # data = 'NNCB'

    unique_chars = set(''.join(letters))

    print(f'Part 1: {part1(data, rules, unique_chars)}')
