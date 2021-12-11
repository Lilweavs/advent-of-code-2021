import re
from typing import ParamSpec

pairs = ['()', '{}', '<>', '[]']

# end = [')', '}', '>', ']']

start = {'(':')', '{':'}', '<':'>', '[':']'}


def part1(data):
    end   = {')':3, ']':57, '}':1197, '>':25137}
    score = 0
    tmp = []
    for j, string in enumerate(data):

        found = True
        while found:
            found = False
            for pair in pairs:
                if pair in string:
                    string = string.replace(pair, '')
                    found = True

        tmp.append(string)
        for i, l in enumerate(string[:-1]):
            if string[i+1] in start:
                continue
            else:
                # print(string[i+1])
                score += end[string[i+1]]
                tmp.pop(-1)
                break
        

    return score, tmp

def part2(data):
    end   = {'(':1, '[':2, '{':3, '<':4}
    scores = []
    for string in data:
        tmp = 0
        for c in string[::-1]:
            tmp = 5*tmp + end[c]

        scores.append(tmp)

    scores.sort()
    
    return scores[len(scores)//2]

if __name__ == '__main__':

    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data.append(line.strip())

    score, tmp = part1(data)
    
    print(tmp)

    print(f'Part 1: {score}')

    


    print(f'Part 1: {part2(tmp)}')