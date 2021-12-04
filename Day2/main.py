def part1(data):
    x = h = 0
    for cmd, val in data:
        val = int(val)
        if 'f' in cmd:
            x += val
        elif 'u' in cmd:
            h -= val
        else:
            h += val

    print(x*h)

def part2(data):
    x = h = aim = 0
    for cmd, val in data:
        val = int(val)
        if 'f' in cmd:
            x += val
            h += val*aim
        elif 'u' in cmd:
            aim -= val
        else:
            aim += val

    print(x*h)

if __name__ == '__main__':

    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data.append(line.strip().split(' '))

    part1(data)
    part2(data)