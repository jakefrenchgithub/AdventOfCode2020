data = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']

# Part1
def process1(fName):
    with open(fName, 'r') as reader:
        mapLines = reader.read().split()
    for i, ecahLine in enumerate(mapLines):
        mapChar = ecahLine.split()[0]
        print(mapChar)




process1('input.txt')
# Part2
#def process2(fName):
#    validCount = 0
#    with open(fName, 'r') as reader:
#        for eachEntry in reader:
#            minInd, maxInd, ch, pw = eachEntry.strip().replace(':','').replace('-',' ').split(' ')
#            minIndex, maxIndex = int(minInd) - 1, int(maxInd) - 1
#            firstChar, secondChar = pw[minIndex], pw[maxIndex]##
#
#            if (ch in firstChar or ch in secondChar) and (firstChar not in secondChar):
#                validCount += 1
#
#    return validCount
#
#validCount = process2('input.txt')
#print(validCount)
# Answers
# Part1:
# Part2: