data = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']

# Part1
def process1(fName):
    validCount = 0
    with open(fName, 'r') as reader:
        for eachEntry in reader:
            minCnt, maxCnt, ch, pw = eachEntry.strip().replace(':','').replace('-',' ').split(' ')
            minCount, maxCount = int(minCnt), int(maxCnt)
            occurances = pw.count(ch)
            if minCount <= occurances <= maxCount:
                validCount += 1
    return validCount

# Part2
def process2(fName):
    validCount = 0
    with open(fName, 'r') as reader:
        for eachEntry in reader:
            minInd, maxInd, ch, pw = eachEntry.strip().replace(':','').replace('-',' ').split(' ')
            minIndex, maxIndex = int(minInd) - 1, int(maxInd) - 1
            firstChar, secondChar = pw[minIndex], pw[maxIndex]

            if (ch in firstChar or ch in secondChar) and (firstChar not in secondChar):
                validCount += 1

    return validCount

validCount = process2('input.txt')
print(validCount)

# Answers
# Part1: 445
# Part2: 491