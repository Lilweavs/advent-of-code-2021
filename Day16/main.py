nums = {'0': '0000', 
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'}

class LiteralPacket:
    def __init__(self, version, typeID, value) -> None:
        self.version = version
        self.typeID  = typeID
        self.value   = value
        self.packets = []
    
class OperatorPacketZero:
    def __init__(self, version, typeID, length) -> None:
        self.version = version
        self.typeID = typeID
        self.length = length
        self.packets = []

    # if 0 next 15 bits are represents total length of su-packets
    # if 1 next 11 bits are number representing the number of sub-packets immediately contained by this packet

def parseLiteralPacket(data, idx):
    version = int(data[idx:idx+3], 2)
    idx += 3
    typeID = int(data[idx:idx+3], 2)
    idx += 3
    tmp = ''
    while True:
        if data[idx] == '0':
            tmp += data[idx+1:idx+5]
            idx += 5
            return idx, LiteralPacket(version, typeID, int(tmp, 2))
        else:
            tmp += data[idx+1:idx+5]
            idx += 5

def parseOperatorZero(data, idx):
    version = int(data[idx:idx+3], 2)
    idx += 3
    typeID = int(data[idx:idx+3], 2)
    idx += 4
    length = int(data[idx:idx+15], 2)
    idx += 15
    packet = OperatorPacketZero(version, typeID, length)
    tmpIdx = idx
    while tmpIdx - idx < length:
        # print(data[tmpIdx::])
        if data[tmpIdx+3:tmpIdx+6] == '100':
            tmpIdx, newPacket = parseLiteralPacket(data, tmpIdx)
            packet.packets.append(newPacket)
        else:
            if data[tmpIdx+6] == '0':
                tmpIdx, newPacket = parseOperatorZero(data, tmpIdx)
                packet.packets.append(newPacket)
            else:
                tmpIdx, newPacket = parseOperatorOne(data, tmpIdx)
                packet.packets.append(newPacket)
        # tmpIdx, newPacket = parseLiteralPacket(data, tmpIdx)
        # packet.packets.append(newPacket)
    
    return tmpIdx, packet

def parseOperatorOne(data, idx):
    version = int(data[idx:idx+3], 2)
    idx += 3
    typeID = int(data[idx:idx+3], 2)
    idx += 4
    length = int(data[idx:idx+11], 2)
    idx += 11
    packet = OperatorPacketZero(version, typeID, length)
    for i in range(length):
        # print(data[idx::])
        if data[idx+3:idx+6] == '100':
            idx, newPacket = parseLiteralPacket(data, idx)
            packet.packets.append(newPacket)
        else:
            if data[idx+6] == '0':
                idx, newPacket = parseOperatorZero(data, idx)
                packet.packets.append(newPacket)
            else:
                idx, newPacket = parseOperatorOne(data, idx)
                packet.packets.append(newPacket)
    
    return idx, packet


# if typeID == 4:
#     # literalValue
#     pass

def getScore(packet):
    score = 0
    score += packet.version
    for p in packet.packets:
        score += getScore(p)

    return score

def getTotal(packet):
    total = 0
    typeId = packet.typeID
    # if typeId == 0:
    if typeId == 0:
        total = sum([getTotal(p) for p in packet.packets])
    elif typeId == 1:
        total = 1
        for p in packet.packets:
            total *= getTotal(p)
    elif typeId == 2:
        total = min([getTotal(p) for p in packet.packets])
    elif typeId == 3:
        total = max([getTotal(p) for p in packet.packets])
    elif typeId == 4:
        total = packet.value
    elif typeId == 5:
        if getTotal(packet.packets[0]) > getTotal(packet.packets[1]):
            total = 1
        else:
            total = 0
    elif typeId == 6:
        if getTotal(packet.packets[0]) < getTotal(packet.packets[1]):
            total = 1
        else:
            total = 0
    else:
        if getTotal(packet.packets[0]) == getTotal(packet.packets[1]):
            total = 1
        else:
            total = 0

    return total


def part1(data):

    # data = bin(int(data, 16))[2:]
    print(len(data))
    packets = []
    idx = 0
    while len(data) - idx >= 8:
        
        # if data[idx:idx+3] == '000':
        #     break

        # start = idx
        # version = int(data[idx:idx+3], 2)
        # idx += 3
        # typeID = int(data[idx:idx+3], 2)
        # idx += 3
        print(data[idx::])

        if data[idx+3:idx+6] == '100':
            idx, packet = parseLiteralPacket(data, idx)
            packets.append(packet)
        else:
            if data[idx+6] == '0':
                idx, packet = parseOperatorZero(data, idx)
                packets.append(packet)
                # length = int(data[idx:idx+15], 2)
                # idx += 15
                # idx, value = 
            else:
                idx, packet = parseOperatorOne(data, idx)
                packets.append(packet)
            # packets.append((version, typeID))

    # tmp = 0
    # for p in packets:
    #     tmp += getScore(p)

    # for p in packets:
    tmp = 0
    for p in packets:
        tmp += getTotal(p)


    return tmp

def part2(data):

    return 0

if __name__ == '__main__':

    with open('input.txt', 'r') as file:
        for line in file:
            data = line.strip()
    tmp = ''    
    for c in data:
        tmp += nums[c]

    print(f'Part1: {part1(tmp)}')