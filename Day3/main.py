def getMostCommonBit(data: list[int], idx: int):
    tmp = 0
    for num in data:
        tmp += (num >> idx) & 1
    if 2*tmp >= len(data):
        return 1
    else:
        return 0

def getRates(data: list[int]):
    gamma_rate = []
    for i in range(SIZE):
        gamma_rate.append(getMostCommonBit(data, i))

    out = 0
    for bit in gamma_rate[::-1]:
        out = (out << 1) | bit

    return [out, ~out & 0b111111111111]

def part1(data):

    rates = getRates(data)

    print(f'Gamma Rate: {rates[0]}')
    print(f'Epislon Rate: {rates[1]}')
    print(f'Power Consumption: {rates[0]*rates[1]}')

def part2(data):
    out = []
    for j in range(2):
        tmp = []
        prev_nums = data
        for i in range(SIZE):
            rates = getRates(prev_nums)
            shift = SIZE - 1 - i
            for num in prev_nums:
                    if ((num >> shift) & 1) == ((rates[j] >> shift) & 1):
                        tmp.append(num)

            prev_nums = tmp
            if len(prev_nums) == 1:
                out.append(prev_nums[0])
                break
            else:
                tmp = []

    print(f'Oxygen Generator Rating: {out[0]}')
    print(f'C02 Scrubber Rating: {out[1]}')
    print(f'Life Suuport Rating: {out[0]*out[1]}')

if __name__ == '__main__':

    SIZE = 12

    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data.append(int(line.strip(), 2))

    part1(data)
    part2(data)