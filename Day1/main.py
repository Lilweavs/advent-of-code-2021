def part1(data):

    cnt = sum([1 if data[i] > data[i-1] else 0 for i in range(1, len(data))])

    return cnt
    
def part2(data):

    tmp = [data[i] + data[i-1] + data[i-2] for i in range(2, len(data))]

    return part2(tmp)

def part2_2(data):

    cnt = sum([1 if data[i] > data[i-3] else 0 for i in range(3, len(data))])

    return cnt

if __name__ == '__main__':

    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data.append(int(line.strip()))
    part1(data)
    part2(data)
    part2_2(data)