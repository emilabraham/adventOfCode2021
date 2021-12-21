# Doing some hexadecimal packet manipulation
fp = open("input")
line = fp.readline()

# Converts a single hexadecimal digit to binary representation
def hexToBinary(hex):
    return bin(int(hex, 16))[2:].zfill(4) # lol thanks github copilot

# Converts a whole hex string to binary representation
def hexStringToBinary(hexString):
    binary = ""
    for i in range(len(hexString)):
        binary += hexToBinary(hexString[i])
    return binary

binaryString = hexStringToBinary("C200B40A82")

# Convert a binary number to decimal
def binaryToDecimal(binary):
    return int(binary, 2)

def breakOutEarly(binaryString, index, increment):
    if index + increment >= len(binaryString):
        breakpoint()
        return True
    return False

# find the packet version
def findPacketVersion(binaryString, index):
    if breakOutEarly(binaryString, index, 3):
        return 0, -1
    version = binaryToDecimal(binaryString[index:index+3])
    index += 3
    return version, index
    
# find the packet type
def findPacketType(binaryString, index):
    if breakOutEarly(binaryString, index, 3):
        return 0, -1
    type =  binaryToDecimal(binaryString[index:index+3])
    index += 3
    return type, index

# Keep reading bits of 5 as long as the first bit is 1
def findLiteralValue(binaryString, index):
    if breakOutEarly(binaryString, index, 5):
        return 0, -1
    literalValue = ""
    keepReading = True
    while keepReading:
        chunk = binaryString[index:index+5]
        if chunk[0] == "0":
            keepReading = False
        index += 5
        literalValue += chunk[1:5]
    return binaryToDecimal(literalValue), index

# Find the length type Id
def findPacketLengthTypeId(binaryString, index):
    if breakOutEarly(binaryString, index, 1):
        return 0, -1
    lengthType =  binaryString[index:index+1]
    index += 1
    return lengthType, index

def findPacketCount(binaryString, index):
    if breakOutEarly(binaryString, index, 11):
        return 0, -1
    packetCount = binaryToDecimal(binaryString[index:index+11])
    index += 11
    return packetCount, index

# Find the length of the packet 
def findSubPacketLength(binaryString, index):
    if breakOutEarly(binaryString, index, 15):
        return None, -1
    length = binaryToDecimal(binaryString[index:index+15])
    index += 15
    return length, index



# Recursively add version of each packet
# I think I'm having trouble properly breaking out of this.
# If I  put a breakpoint inside the breakOutEarly function, it ends up correct without looping.
def addVersions(binaryString, accumulator, index, packetCount, bitCount, currentType, isSecond):
    originalIndex = index
    version, index = findPacketVersion(binaryString, index)
    type, index = findPacketType(binaryString, index)
    if type == 4:
        literalValue, index = findLiteralValue(binaryString, index)
        if currentType == -1 or currentType == 4:
            return accumulator
        elif currentType == 0:
                accumulator += literalValue
        elif currentType == 1:
                accumulator *= literalValue
        elif currentType == 2:
            if accumulator == 0 or literalValue <= accumulator:
                accumulator = literalValue
        elif currentType == 3:
            if accumulator == 0 or literalValue >= accumulator:
                accumulator = literalValue
        elif currentType == 5:
            if isSecond:
                accumulator = (1 if accumulator > literalValue else 0)
                isSecond = False
            else:
                accumulator = literalValue
                isSecond = True
        elif currentType == 6:
            if isSecond:
                accumulator = (1 if accumulator < literalValue else 0)
                isSecond = False
            else:
                accumulator = literalValue
                isSecond = True
        elif currentType == 7:
            if isSecond:
                accumulator = (1 if accumulator == literalValue else 0)
                isSecond = False
            else:
                accumulator = literalValue
                isSecond = True
    else:
        lengthTypeId, index = findPacketLengthTypeId(binaryString, index)
        if lengthTypeId == "0":
            newBitCount, index = findSubPacketLength(binaryString, index)
            bitCount += newBitCount
            addVersions(binaryString, accumulator, index, packetCount, bitCount, type, isSecond)
            bitCount = 0
        else:
            newPacketCount, index = findPacketCount(binaryString, index)
            packetCount += newPacketCount
            addVersions(binaryString, accumulator, index, packetCount, bitCount, type, isSecond)
            packetCount = 0

    if packetCount > 0:
        packetCount -= 1
        return addVersions(binaryString, accumulator, index, packetCount, bitCount, type, isSecond)
    if bitCount > 0:
        bitCount -= (index - originalIndex)
        return addVersions(binaryString, accumulator, index, packetCount, bitCount, type, isSecond)

    return accumulator

print(addVersions(binaryString, 0, 0, 0, 0, -1, False))