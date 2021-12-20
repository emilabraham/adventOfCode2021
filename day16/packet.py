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

binaryString = hexStringToBinary(line)

# Convert a binary number to decimal
def binaryToDecimal(binary):
    return int(binary, 2)

def breakOutEarly(binaryString, index, increment):
    if index + increment >= len(binaryString):
        return True
    return False

# find the packet version
def findPacketVersion(binaryString, index, versionSum):
    if breakOutEarly(binaryString, index, 3):
        return versionSum, -1
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
def addVersions(binaryString, versionSum, index, packetCount, bitCount):
    print(index)
    originalIndex = index
    version, index = findPacketVersion(binaryString, index, versionSum)
    if index < 0:
        return version + versionSum
    versionSum += version
    type, index = findPacketType(binaryString, index)
    if index < 0:
        return versionSum
    if type == 4:
        literalValue, index = findLiteralValue(binaryString, index)
        if index < 0:
            return versionSum
    else:
        lengthTypeId, index = findPacketLengthTypeId(binaryString, index)
        if index < 0:
            return versionSum
        if lengthTypeId == "0":
            newBitCount, index = findSubPacketLength(binaryString, index)
            bitCount += newBitCount
            if index < 0:
                return versionSum
            addVersions(binaryString, versionSum, index, packetCount, bitCount)
        else:
            newPacketCount, index = findPacketCount(binaryString, index)
            packetCount += newPacketCount
            if index < 0:
                return versionSum
            addVersions(binaryString, versionSum, index, packetCount, bitCount)

    if packetCount > 0:
        packetCount -= 1
        return addVersions(binaryString, versionSum, index, packetCount, bitCount)
    if bitCount > 0:
        bitCount -= (index - originalIndex)
        return addVersions(binaryString, versionSum, index, packetCount, bitCount)

    return versionSum

print(addVersions(binaryString, 0, 0, 0, 0))