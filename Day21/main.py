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

    players = [5, 9]
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

    return 0

if __name__ == '__main__':

    print(f'Part 1: {part1(0)}')