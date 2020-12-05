import numpy as np
from itertools import combinations


def readData(fName):
    with open(fName, 'r') as reader:
        data = reader.read().replace('\n',',').split(",")
    values = np.array(data).astype(int)
    return values

data = readData('input.txt')

# part1 - Pythonic solution, uses vectorization
candidates = 2020 - data
values = list(set(candidates).intersection(data))
print(np.prod(values))

# part1 - naive solution, uses loops
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

# part2 - Pythonic solution, uses vectorization
print(np.prod([p for p in combinations(data, 3) if sum(p) == 2020]))

combo = [p for p in combinations(data, 3)]
for eachCombo in combo:
    if sum(eachCombo) == 2020:
        break
print(eachCombo, np.prod(eachCombo))





# part2 - naive solution, uses loops
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