class board:
    def __init__(self) -> None:
        self.board = []
        self.marked = [[0]*5 for i in range(5)]
        
    def add(self, l):
        self.board.append(l)

    def check(self):
        markedT = list(map(list, zip(*self.marked)))
        for i in range(5):
            if sum(self.marked[i]) == 5:
                return True
            if sum(markedT[i]) == 5:
                return True

    def find(self, num):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == num:
                    self.marked[i][j] = 1

    def getScore(self):
        tmp = 0
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.marked[i][j] == 0:
                    tmp += self.board[i][j]
        return tmp

order = [76,69,38,62,33,48,81,2,64,21,80,90,29,99,37,15,93,46,75,0,89,56,58,40,92,47,8,6,54,96,12,66,83,4,70,19,17,5,50,52,45,51,18,27,49,71,28,86,74,77,11,20,84,72,23,31,16,78,91,65,87,79,73,94,24,68,63,9,88,82,30,42,60,13,67,85,44,59,7,53,22,1,26,41,61,55,43,39,3,35,25,34,57,10,14,32,97,95,36,98]

def part1(boards):
    for nxtNum in order:
        for b in boards:
            b.find(nxtNum)
            if b.check():
                return b.getScore()*nxtNum

def part2(boards):
    for nxtNum in order:
        tmp = []
        for b in boards:
            b.find(nxtNum)

            if len(boards) == 1 and b.check():
                return b.getScore()*nxtNum

            if not b.check():
                tmp.append(b)
        
        boards = tmp


if __name__ == '__main__':

    boards = []
    with open('input.txt', 'r') as file:
        lines = file.readlines()

        numBoards = (len(lines) + 1) // 6

        cnt = 0
        for i in range(numBoards):
            boards.append(board())
            for j in range(5):
                line = lines[cnt].replace('  ', ' ')
                boards[i].add([int(x) for x in line.strip().split(' ')])
                cnt += 1
            cnt += 1

    print(part1(boards))
    print(part2(boards))