import re

def main(data, instructions, width, height):
    
    paper = [[0]*width for i in range(height)]

    for x, y in data:
        paper[y][x] = 1
    
    cnt = 0
    for dir, num in instructions:

        if dir == 'y':
            tmp = paper[:num][:]
            paper = paper[(2*num+1):num:-1][:]

            for y in range(len(paper)):
                for x in range(len(paper[0])):
                    paper[y][x] = paper[y][x] | tmp[y][x]
        
        else:
            tmp = [paper[i][:num] for i in range(len(paper))]
            paper = [paper[i][(2*num+1):num:-1] for i in range(len(paper))]

            for y in range(len(paper)):
                for x in range(len(paper[0])):
                    paper[y][x] = paper[y][x] | tmp[y][x]
        
        if cnt == 0:
            cnt = sum([sum(x) for x in paper])

    for p in paper:
        print(' '.join(['#' if c == 1 else '.' for c in p]))

    return cnt

if __name__ == '__main__':

    data = []
    width = 0
    height = 0
    with open('input.txt', 'r') as file:
        for line in file:
            tmp = [int(x) for x in line.strip().split(',')]
            data.append(tmp)
            
    instructions = []
    with open('instructions.txt', 'r') as file:
        for line in file:
            num = int(re.findall(r'\d+', line)[0])
            if 'x' in line:
                instructions.append(('x', num))
                width  = max(width, num)
            else:
                instructions.append(('y', num))
                height = max(height, num)
            
    print(f'Part 1: {main(data, instructions, 2*width+1, 2*height+1)}')
