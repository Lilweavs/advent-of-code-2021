import re
from math import floor, ceil, sqrt

def main(data):

    idx = 0
    validX = []
    while idx <= data[1]:
        idx += 1
        pos = [0, 0]
        vel = [idx, 0]
        while True:
            step(pos, vel)
            if (pos[0] >= data[0]) or (vel[0] == 0 and pos[0] < data[0]):
                break
        if data[0] <= pos[0] <= data[1]:
            validX.append(idx)

    sols = []

    for v in validX:
        idx = data[2]-1
        while idx <= abs(data[2]):
            idx += 1
            pos = [0, 0]
            vel = [v, idx]
            maxH = 0
            while True:
                step(pos, vel)
                maxH = max(maxH, pos[1])

                if data[2] <= pos[1] <= data[3] and data[0] <= pos[0] <= data[1]:
                    break
                if pos[1] <= data[2]:
                    break
            if data[2] <= pos[1] <= data[3] and data[0] <= pos[0] <= data[1]:
                sols.append(maxH)

    return max(sols), len(sols)


def part2(data):

    xvel = ceil(-0.5 + sqrt(1 + 8*data[0])/2)
    validX = []
    while xvel <= data[1]:
        # pos = [0, 0]
        posx = 0
        # vel = [xvel, 0]
        vel = xvel
        while True:
            posx += vel# step(pos, vel)
            vel -= 1
            if (posx >= data[0]) or (vel == 0 and posx < data[0]):
                break
        if data[0] <= posx <= data[1]:
            validX.append(xvel)
        xvel += 1

    # yvel = ceil(-0.5 + sqrt(1 + 8*abs(data[3]))/2)
    
    maxH = 0
    total = 0
    for vx in validX:
        yvel = data[2]
        while yvel <= abs(data[2]):
            posy = 0
            posx = 0
            if yvel > 0:
                vel = -1*(yvel + 1)
                if yvel >= vx:
                    posx = vx*(vx + 1)//2
                    velx = 0
                else:
                    tmp = vx - tmp
                    posx = tmp*(tmp + 1)//2
                    velx = tmp
            else:
                vel = yvel
                velx = vx

            while True:
                # step(pos, vel)
                posx += velx
                posy += vel
                velx  -= 1
                vel -= 1
                if velx == 0: velx = 0
                # maxH = max(maxH, pos[1])
                if (posy <= data[3]):
                    break
            if (data[2] <= posy <= data[3]) and (data[0] <= posx <= data[1]):
                maxH = max(maxH, abs(yvel)*(yvel + 1)//2)
                total += 1
                # validY.append(xvel)
            yvel += 1
                 
    return maxH, total
    
def step(pos, vel):
    pos[0] += vel[0]
    pos[1] += vel[1]
    if vel[0] == 0:
        vel[0] == 0
    else:
        vel[0] -= 1    
    vel[1] -= 1

if __name__ == '__main__':

    with open('input.txt', 'r') as file:
        for line in file:
            data = [int(x) for x in re.findall(r'-?\d+', line.strip())]

    print(part2(data))

    # maxH, L = main(data)

    # print(f'Part 1: {maxH}')
    # print(f'Part 2: {L}')