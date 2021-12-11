def main(data, day):
    fish = []
    for i in range(9):
        fish.append(data.count(i))

    for i in range(day):
        tmp_old  = fish.pop(0)

        fish.append(tmp_old)
        fish[6] += tmp_old

    return sum(fish)

if __name__ == '__main__':

    data = []
    with open('input.txt', 'r') as file:
        line = file.readline()
        data = [int(x) for x in line.strip().split(',')]

    print(f'Part1: {main(data, 80)}')
    print(f'Part2: {main(data, 256)}')