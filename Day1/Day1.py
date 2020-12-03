data = [1721,
979,
366,
299,
675,
1456]

def readData(fName):
    rtn = []
    with open(fName, 'r') as reader:
        for each in reader:
            rtn.append(int(each.strip()))
    return rtn

data = readData('input.txt')

# part1
running = True
while running:
    for i in data:
        for j in data:
            if i == j:
                continue
            else:
                if i + j == 2020:
                    product = i*j
                    running = False

            if not running:
                break
print(product)

# part2
running = True
while running:
    for i in data:
        for j in data:
            for k in data:
                if i == j == k:
                    continue
                else:
                    summation = i + j + k
                if summation == 2020:
                    product = i*j*k
                    running = False

            if not running:
                break
print(product)

# Answers
# Part1: 751776
# Part2: 42275090