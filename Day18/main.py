from typing import ParamSpec


class Tree:

    def __init__(self, parent=None, data=None, depth=0) -> None:
        # self.data   = data
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

    def insertLeft(self):
        pass
        # if isinstance(self.data, int):
            # return

        # if isinstance(self.data, int):
        #     return
        # elif isinstance(self.data[0], int) and isinstance(self.data[1], int):
        #     self.left = self.data
        # else:
        #     self.left = Tree(self, self.data[0], self.depth+1)
        #     self.left.buildChildren()
        # self.right = Tree(self, self.data[1], self.depth+1)
        # self.right.buildChildren()

        # self.left = self.insertLeft(parent[0])
        # self.right = self.insertRight(parent[1])

    # def findLeftReg(self, left):
    #     if 
    #     self.parent(findLeftReg)
    #     return 0

    def explodeLeft(self):
        self.left = None
        return 0

    def findExplode(self, depth):

        if isinstance(self.left, Tree):
            found, left, right = self.left.findExplode(depth+1)
            if found:
                self.left = 0
                
                self.searchUpLeft(left)
                if isinstance(self.right, int):
                    self.right += right
                else:
                    pass
        else:
            if depth > 3:
                return True, self.left, self.right

        if isinstance(self.right, Tree):
            found, left, right = self.right.findExplode(depth+1)
            if found:
                self.right = 0
                # if isinstance(self.right, int):
                #     self.parent.right += right
                # else:
                self.searchUpRight(right)
                if isinstance(self.left, int):
                    self.left += left
        else:
            if depth > 3:
                return True, self.left, self.right
            
        return False, 0, 0
                # print(self.left, self.right)

        # if not isinstance(self.left, int) and not isinstance(self.right, int):
        #     found = self.left.findExplode()
        # else:


        if not isinstance(self.left, list):
            found = self.left.findExplode()
            if found:
                self.parent.searchLeft(self.left[0], self.left[1])
        else:
            if self.depth > 2:
                return True

                # print(self.data)
            else:
                self.left.findExplode()


        # if self.left:
        #     self.left.findPair()
        # else:
        #     if self.depth > 3:
        #         print(self.data)

        return 0

    def searchDownLeft(self, right):
        if isinstance(self.left, Tree):
            self.left.searchDownLeft(right)
        else:
            if isinstance(self.left, int) and not isinstance(self.right, int):
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

        # elif self.parent.parent == None:
        #     if isinstance(self.parent.)
        # else:
        #     if isinstance(self.right.left, int):
        #         print(self.left + right)

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

    def downSearchRight(self, left):
        if isinstance(self.right, Tree):
            self.left.searchDownRight(left)
        else:
            if self.left == None:
                self.right += left

    def topDownSearch():
        return 0

    # def insertRight(self, child):
    #     if isinstance(child, int):
    #         self.right = child
    #         return child
    #     else: 
    #         self.buildChildren(child)
    #         return Tree(child, self.depth+1)
    #     # self.right = Tree(child, self.depth+1)

    # def insertLeft(self, child):
    #     if isinstance(child, int):
    #         self.left = child
    #         return child
    #     else:
    #         tree = Tree(child, self.depth+1)
    #         tree.buildChildren()
    #         return tree
    #     # self.left = Tree(child, self.depth+1)

def part1(data):


    newList = [data[0], data[1]]

    newList = [[[[4,3],4],4],[7,[[8,4],9]]]

    addition = [1, 1]

    tree = Tree(None, newList)
    
    tmp = Tree()
    tmp.left = tree
    tmp.left.parent = tmp
    tmp.right = Tree(tmp, addition)

    tree = tmp

    tree.findExplode(0)

    return 0

def checkExplode(parentList: list, depth):

    for subList in parentList:
        if depth > 2 and isinstance(subList, list) and len(subList) == 2:
            left, right = subList
            parentList.remove(subList)
            return True, left, right, depth
        if isinstance(subList, list):
            checkExplode(subList, depth+1)

    return None

def part2(data):


    return 0

if __name__ == '__main__':

    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            print(line)
            data.append(eval(line.strip()))

    print(part1(data))