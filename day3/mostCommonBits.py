# Figure out the most common and least common bits in a list of numbers.
# The gamma rate is the most common bit at each postion.
# The epsilon rate is the least common bit at each position.
fp = open("input")
lines = fp.readlines()
bitLength = len(lines[0])
gammaRate = []
epsilonRate = []

# Return the most common and least common bits in a list of bits.
def getMostAndLeastCommonBits(bits):
    zeroCount = 0
    oneCount = 0
    for bit in bits:
        if bit == 0:
            zeroCount += 1
        else:
            oneCount += 1
    
    if zeroCount > oneCount:
        return [0,1]
    elif zeroCount < oneCount:
        return [1,0]

# Get the most common bit. In case of a tie, default to 1
def getMostCommonBits(bits):
    zeroCount = 0
    oneCount = 0
    for bit in bits:
        if bit == 0:
            zeroCount += 1
        else:
            oneCount += 1
    
    if zeroCount > oneCount:
        return 0
    elif zeroCount <= oneCount:
        return 1

# Get the least common bit. In case of a tie, default to 0
def getLeastCommonBits(bits):
    zeroCount = 0
    oneCount = 0
    for bit in bits:
        if bit == 0:
            zeroCount += 1
        else:
            oneCount += 1
    
    if zeroCount <= oneCount:
        return 0
    elif zeroCount > oneCount:
        return 1

# Convert a binary list to a decimal number.
def binaryToDecimal(binary):
  number = 0
  for b in binary:
    number = (2 * number) + b
  return number

# Convert a binary list to a decimal number while casting as an int and ignoring \n.
def binaryToDecimalInt(binary):
  number = 0
  for b in binary[:len(binary)-1]:
    number = (2 * number) + int(b)
  return number

# calculate the gammaRate and epsilonRate
for i in range(bitLength-1):
    bits = []
    for line in lines:
        bits.append(int(line[i].strip()))
    gammaAndEpsilonBits = getMostAndLeastCommonBits(bits)
    gammaRate.append(gammaAndEpsilonBits[0])
    epsilonRate.append(gammaAndEpsilonBits[1])

# returns true if the nth value is the bit we are looking for
def bitFilter(line, bit, index):
    if int(line[index]) == bit:
        return True
    else:
        return False

# Grabs the nth place of bits from list of lines.
# Returns as an int list
def linesToBits(lines, index):
    bits = []
    for line in lines:
        bits.append(int(line[index]))
    return bits

# Loops through lines and filters out based on most common bit
def filterOxygenGeneratorRating(lines):
    filteredList = lines
    for index in range(bitLength-1):
        bit = getMostCommonBits(linesToBits(filteredList, index))
        if (len(filteredList) > 1):
            filteredList = list(filter(lambda line: bitFilter(line, bit, index), filteredList))
    return filteredList

# Loops through lines and filters out based on least common bit
def filterCo2ScrubberRating(lines):
    filteredList = lines
    for index in range(bitLength-1):
        bit = getLeastCommonBits(linesToBits(filteredList, index))
        if (len(filteredList) > 1):
            filteredList = list(filter(lambda line: bitFilter(line, bit, index), filteredList))
    return filteredList


oxygenGeneratorRating = binaryToDecimalInt(filterOxygenGeneratorRating(lines)[0])
co2ScrubberRating = binaryToDecimalInt(filterCo2ScrubberRating(lines)[0])

print(oxygenGeneratorRating)
print(co2ScrubberRating)
print(co2ScrubberRating * oxygenGeneratorRating)