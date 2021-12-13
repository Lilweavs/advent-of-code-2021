class Tree:
    def __init__(self, parent, visited) -> None:
        self.parent = parent
        self.children = []
        self.visited = dict(visited)

    def add_child(self, node):
        self.children.append(node)

def main(graph, small, depthLimit):

    root = Tree('start', dict())

    buildTree(root, graph['start'], graph, small, depthLimit)

    return paths(root, 0)
            
def paths(tree, cnt):
    for children in tree.children:
        if children.parent == 'end':
            cnt += 1
        else:
            cnt += paths(children, 0)
    return cnt
    
def buildTree(tree, branches, graph, small, depthLimit):

    for branch in branches:
        if branch == 'end':
            tree.add_child(Tree(branch, dict()))
        elif branch in small:

            if branch in tree.visited:
                if any([tree.visited[x] == depthLimit for x in tree.visited]):
                    continue
                else:
                    child = Tree(branch, tree.visited)
                    child.visited[branch] += 1
                    tree.add_child(child)
                    buildTree(child, graph[branch], graph, small, depthLimit)
            else:
                child = Tree(branch, tree.visited)
                child.visited[branch] = 1
                tree.add_child(child)
                buildTree(child, graph[branch], graph, small, depthLimit)
        else:
            child = Tree(branch, tree.visited)
            tree.add_child(child)
            buildTree(child, graph[branch], graph , small, depthLimit)
    
    return tree

if __name__ == '__main__':

    data = dict()
    small = []
    with open('input.txt', 'r') as file:
        for line in file:
            line = line.strip().split('-')

            if line[0] not in data:
                data[line[0]] = []
            if line[1] not in data:
                data[line[1]] = []

            if line[1] not in data[line[0]] and not line[1] == 'start':
                data[line[0]].append(line[1])
            if line[0] not in data[line[1]] and not line[0] == 'start':
                data[line[1]].append(line[0])

            for l in line:
                if not l in small and l.islower() and not l == 'start' and not l == 'end':
                    small.append(l)

    print(f'Part 1: {main(data, small, 1)}')
    print(f'Part 1: {main(data, small, 2)}')    