# Fix the seven-segment displays
fp = open("input3")
lines = fp.readlines()
signalPatterns = []
digitOutputs  = []

# Remove newline character from a string and convert to an integer
def removeNewLine(s):
    return s.replace('\n', '')

lines = list(map(removeNewLine, lines))

# Split at the | character into signal pattern and the digital output
for line in lines:
    splitLine = line.split(' | ')
    signalPatterns.append(splitLine[0])
    digitOutputs.append(splitLine[1])

# Split the signal patterns and the digital outputs in to individual digits
signalPatterns = list(map(lambda s: s.split(' '), signalPatterns))
digitOutputs = list(map(lambda s: s.split(' '), digitOutputs))

# 1, 4, 7, 8 all have unique signal lengths
# 2, 3, 4, 7 corresponds to their respective lengths
def countUniqueNumbers(outputs):
    count = 0
    for o in outputs:
        for digit in o:
            if len(digit) in [2,3,4,7]:
                count += 1
    return count

# Create a dictionary of the unique signal patterns
# 1, 4, 7, 8 all have unique signal lengths
# 2, 3, 4, 7 corresponds to their respective lengths
def createUniqueDictionary(patterns):
    uniqueDict = {}
    for pattern in patterns:
        if len(pattern) == 2:
            uniqueDict[pattern] = 1
        elif len(pattern) == 3:
            uniqueDict[pattern] = 7
        elif len(pattern) == 4:
            uniqueDict[pattern] = 4
        elif len(pattern) == 7:
            uniqueDict[pattern] = 8
    return uniqueDict

# Swap the keys and values in the dictionary
def reverseDictionary(d):
    rd = {}
    for k, v in d.items():
        rd[v] = k
    return rd
        
dictionary = createUniqueDictionary(signalPatterns[0])
rdictionary = reverseDictionary(dictionary)

# Does signal contain every character of the pattern?
def containsPattern(signal, pattern):
    doesContain = True
    for c in pattern:
        if c not in signal:
            doesContain = False
    return doesContain

# Add the digit and pattern to the dictionarys
def addToDictionary(d, rd, digit, pattern):
    d[pattern] = digit
    rd[digit] = pattern

# 9 is the only digit that is 6 in length and contains all the characters of 4
def add9(d, rd, patterns):
    filteredKeys = list(filter(lambda k: len(k) == 6, patterns))
    filteredKeys = list(filter(lambda k: containsPattern(k, rd[4]), filteredKeys))
    addToDictionary(d, rd, 9, filteredKeys[0])

# Only run after add9
# Filter for remaining 6 digit patterns: 6 or 0
# Filter for 5 digit patterns: 5, 2, 3
# Only 6 will contain all the characters of 5
# Remaining 6 digit number is 0
# This allows us to identify 6, 5, 0
def add6and5and0(d, rd, patterns):
    filteredKeys = list(filter(lambda k: len(k) == 6, patterns))
    filteredKeys6or0 = list(filter(lambda k: k != rd[9], filteredKeys))
    filtered5Digits = list(filter(lambda k: len(k) == 5, patterns))
    five = ''
    six = ''
    for k in filteredKeys6or0:
        for j in filtered5Digits:
            if (containsPattern(k, j)):
                five = j
                six = k
                break
    zero = list(filter(lambda k: k != six, filteredKeys6or0))[0]
    addToDictionary(d, rd, 5, five)
    addToDictionary(d, rd, 6, six)
    addToDictionary(d, rd, 0, zero)

# Only run after add6and5and0
# Filter for 5 digit patterns: 2, 3
# Only 3 will contain all the characters of 7
# Remaining 5 digit number is 2
# This allows us to identify 2, 3
def add2and3(d, rd, patterns):
    filteredKeys = list(filter(lambda k: len(k) == 5, patterns))
    filteredKeys2or3 = list(filter(lambda k: k != rd[5], filteredKeys))
    two = ''
    three = ''
    for k in filteredKeys2or3:
        if (containsPattern(k, rd[7])):
            three = k
            break
    two = list(filter(lambda k: k != three, filteredKeys2or3))[0]
    addToDictionary(d, rd, 2, two)
    addToDictionary(d, rd, 3, three)

add9(dictionary, rdictionary, signalPatterns[0])
add6and5and0(dictionary, rdictionary, signalPatterns[0])
add2and3(dictionary, rdictionary, signalPatterns[0])

print(dictionary)
print(rdictionary)
