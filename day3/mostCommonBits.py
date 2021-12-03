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
    else:
        return [1,0]

# Convert a binary list to a decimal number.
def binaryToDecimal(binary):
  number = 0
  for b in binary:
    number = (2 * number) + b
  return number

for i in range(bitLength-1):
    bits = []
    for line in lines:
        bits.append(int(line[i].strip()))
    gammaAndEpsilonBits = getMostAndLeastCommonBits(bits)
    gammaRate.append(gammaAndEpsilonBits[0])
    epsilonRate.append(gammaAndEpsilonBits[1])

gamma = binaryToDecimal(gammaRate)
epsilon = binaryToDecimal(epsilonRate)
print(gamma * epsilon)