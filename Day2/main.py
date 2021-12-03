def part1(data):
    x = h = 0
    for cmd, val in data:
        if 'f' in cmd:
            x += int(val)
        elif 'u' in cmd:
            h -= int(val)
        else:
            h += int(val)

    print(x*h)

def part2(data):
    x = h = aim = 0
    for cmd, val in data:
        if 'f' in cmd:
            tmp = int(val)
            x += tmp
            h += tmp*aim
        elif 'u' in cmd:
            aim -= int(val)
        else:
            aim += int(val)

    print(x*h)

if __name__ == '__main__':

    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data.append(line.strip().split(' '))

    part1(data)
    part2(data)