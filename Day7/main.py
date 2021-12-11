

def part2_while(data):
    m = sum(data)//len(data)
        
    tmp = [1e99, 1e99]
    cnt = 0
    while tmp[1] <= tmp[0]:
        tmp[0] = tmp[1]
        tmp[1] = sum([abs(d - cnt)*(abs(d - cnt) + 1)//2 for d in data])
        cnt += 1

    return tmp[0]

def part1_while(data):
    m = sum(data)//len(data)
        
    tmp = [1e99, 1e99]
    cnt = 0
    while tmp[1] <= tmp[0]:
        tmp[0] = tmp[1]
        tmp[1] = sum([abs(d - cnt) for d in data])
        cnt += 1

    return tmp[0]

# def part1_for(data):

#     for i in range(0, m):
#         tmp[0] = tmp[1]
#         tmp[1] = sum([abs(d - i) for d in data])
#         if tmp[1] > tmp[0]:
#             return i, min(tmp)


#         # tmp.append(sum([abs(d - i) for d in data]))
#         # if i > 2:
#         #     if tmp[-1] > tmp[-2]:
#         #         print(i, m)
#         #         return min(tmp)

#     return min(tmp)

# def part2(data):
#     m = sum(data)//len(data)

#     tmp = []
#     for i in range(0, m):
#         tmp.append(sum([abs(d - i)*(abs(d - i) + 1)//2 for d in data]))

#     return min(tmp)

# def part2(data):
#     m = max(data)//2

#     prev = curr = cnt = 1
#     while prev - curr > 0:
#         for d in range()
#         tmp = abs( - cnt)
#     for i in range(0, m):
#         tmp.append(sum([abs(d - i)*(abs(d - i) + 1)//2 for d in data]))

#     return min(tmp)


if __name__ == '__main__':

    data = []
    with open('input.txt', 'r') as file:
        line = file.readline()
        data = [int(x) for x in line.strip().split(',')]

    print(f'Part 1: {part1_while(data)}')
    print(f'Part 2: {part2_while(data)}')