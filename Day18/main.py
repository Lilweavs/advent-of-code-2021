from math import floor, ceil

class Tree:

    def __init__(self, parent=None, data=None, depth=0) -> None:
        self.parent = parent
        self.depth  = depth
        self.left   = None
        self.right  = None
        self.buildChildren(data)

    def buildChildren(self, data):

        if not data:
            return

        if isinstance(data[0], int) and isinstance(data[1], int):
            self.left = data[0]
            self.right = data[1]
            return

        if isinstance(data[0], list):
            self.left = Tree(self, data[0], self.depth+1)
        else:
            self.left = data[0]

        if isinstance(data[1], list):
            self.right = Tree(self, data[1], self.depth+1)
        else:
            self.right = data[1]

    def findSplit(self, depth):

        if isinstance(self.left, Tree):
            tmp = self.left.findSplit(depth+1)
            if tmp:
                return True
        else:
            if isinstance(self.left, int):
                if self.left > 9:
                    self.left = Tree(self, [floor(self.left/2), ceil(self.left/2)], depth+1)
                    return True
            if isinstance(self.right, int):
                if self.right > 9:
                    self.right = Tree(self, [floor(self.right/2), ceil(self.right/2)], depth+1)
                    return True

        if isinstance(self.right, Tree):
            tmp = self.right.findSplit(depth+1)
            if tmp:
                return True
        else:
            if isinstance(self.left, int):
                if self.left > 9:
                    self.left = Tree(self, [floor(self.left/2), ceil(self.left/2)], depth+1)
                    return True
            if isinstance(self.right, int):
                if self.right > 9:
                    self.right = Tree(self, [floor(self.right/2), ceil(self.right/2)], depth+1)
                    return True

        return False

    def findExplode(self, depth, tmp):
        if isinstance(self.left, Tree):
            found, left, right, tmp = self.left.findExplode(depth+1, tmp)
            if found:
                tmp = True
                self.left = 0
                
                self.searchUpLeft(left)
                if isinstance(self.right, int):
                    self.right += right
                else:
                    self.right.searchDownLeft(right)
        else:
            if depth > 3:
                return True, self.left, self.right, tmp

        if isinstance(self.right, Tree):
            found, left, right, tmp = self.right.findExplode(depth+1, tmp)
            if found:
                tmp = True
                self.right = 0
                # if isinstance(self.right, int):
                #     self.parent.right += right
                # else:
                self.searchUpRight(right)
                if isinstance(self.left, int):
                    self.left += left
                elif isinstance(self.left, Tree):
                    self.left.searchDownRight(left)
        else:
            if depth > 3:
                return True, self.left, self.right, tmp
            
        return False, 0, 0, tmp

    def searchDownLeft(self, right):
        if isinstance(self.left, Tree):
            self.left.searchDownLeft(right)
        else:
            if isinstance(self.left, int):
                self.left += right

        return

    def searchUpRight(self, right):
        if self.parent == None:
            return None
        if self == self.parent.right:
            self.parent.searchUpRight(right)
        else:
            if isinstance(self.parent.right, int):
                self.parent.right += right
            else:
                self.parent.right.searchDownLeft(right)

    def searchUpLeft(self, left):
        if self.parent == None:
            return
        elif self == self.parent.left:
            self.parent.searchUpLeft(left)
        else:
            if isinstance(self.parent.left, int):
                self.parent.left += left
            else:
                self.parent.left.searchDownRight(left)

    def searchDownRight(self, left):
        if isinstance(self.right, Tree):
            self.right.searchDownRight(left)
        else:
            if isinstance(self.right, int):
                self.right += left

    def magnitude(self):
        
        if isinstance(self.left, Tree):
            leftMag = self.left.magnitude()
        else:
            leftMag = self.left
        if isinstance(self.right, Tree):
            rightMag = self.right.magnitude()
        else:
            rightMag = self.right

        return 3*leftMag + 2*rightMag

    def simplify(self):
        tmp = True
        while tmp:
            _, _, _, tmp = self.findExplode(0, False)
            tmp = self.findSplit(0)   


def part1(data):

    tree = Tree(None, data.pop(0))

    for addition in data:
        tmpTree = Tree()
        tmpTree.left = tree
        tmpTree.left.parent = tmpTree
        tmpTree.right = Tree(tmpTree, addition)

        tree = tmpTree

        tree.simplify()

    return tree.magnitude()

def part2(data):

    m = 0
    for leftFish in data:
        for rightFish in data:
            
            tree = Tree(None, [leftFish, rightFish])
            tree.simplify()
            m = max(m, tree.magnitude())

    return m

if __name__ == '__main__':

    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data.append(eval(line.strip()))

    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')