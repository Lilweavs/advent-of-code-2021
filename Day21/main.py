from itertools import product
from collections import defaultdict
import re

class Dice:
    dice = [i for i in range(1, 101)]
    idx = 0
    cnt = 0

    def roll(self):
        roll = self.dice[self.idx]
        self.idx += 1
        self.cnt += 1
        if self.idx == 100:
            self.idx = 0
        return roll


def part1(data):

    players = [data[0], data[1]]
    scores  = [0, 0]

    dice = Dice()

    rollCnt = 0
    while scores[0] < 1000 and scores[1] < 1000:

        for i in range(len(players)):
            roll = 0
            for j in range(3):
                roll += dice.roll()

            tmp = (players[i] + roll) % 10
            if tmp == 0:
                tmp = 10
            players[i] = tmp
            scores[i] += players[i]
            if scores[i] >= 1000:
                break

    return dice.cnt*min(scores)


def part2(data):

    freq = defaultdict(int)
    sums = [sum(x) for x in list(product((1, 2, 3), repeat=3))]
    for item in sums:
        freq[item] += 1

    wins = [0, 0]
    states = [{(0, data[0]): 1}, {(0, data[1]): 1}]

    r, cnt, wins = 0, 1, [0, 0]

    while cnt != 0:
        for i in range(2):
            newState = defaultdict(int) # will initialize (int, int): 0 if (int, int) does not exist
            for (score, pos), num in states[i].items():
                for die, qty in freq.items():
                    tmp = (pos + die - 1) % 10 + 1
                    newScore = score + tmp
                    if newScore < 21:
                        newState[(newScore, tmp)] += qty*num
                    else:
                        wins[i] += qty*cnt*num
            states[i] = newState
            cnt = sum(states[i].values())

    return max(wins)

if __name__ == '__main__':

    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data.append(int(re.findall(r'\d+', line.strip())[1]))

    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


