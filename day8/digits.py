# Fix the seven-segment displays
fp = open("input")
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
def countUniqueNumbers(outputs):
    count = 0
    for o in outputs:
        for digit in o:
            if len(digit) in [2,3,4,7]:
                count += 1
    return count

print(countUniqueNumbers(digitOutputs))
