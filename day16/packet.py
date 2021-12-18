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

binaryString = hexStringToBinary("38006F45291200")

# Convert a binary number to decimal
def binaryToDecimal(binary):
    return int(binary, 2)

# find the packet version
def findPacketVersion(binaryString, index):
    version = binaryToDecimal(binaryString[index:index+3])
    index += 3
    return version, index
    
# find the packet type
def findPacketType(binaryString, index):
    type =  binaryToDecimal(binaryString[index:index+3])
    index += 3
    return type, index

# Keep reading bits of 5 as long as the first bit is 1
def findLiteralValue(binaryString, index):
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
    lengthType =  binaryString[index:index+1]
    index += 1
    return lengthType, index

def findPacketCount(binaryString, index):
    packetCount = binaryToDecimal(binaryString[index:index+11])
    index += 11
    return packetCount, index

# Find the length of the packet 
def findSubPacketLength(binaryString, index):
    length = binaryToDecimal(binaryString[index:index+15])
    index += 15
    return length, index

# Recursively add version of each packet
def addVersions(binaryString, versionSum, index, packetCount, bitCount):
    originalIndex = index
    version, index = findPacketVersion(binaryString, index)
    versionSum += version
    type, index = findPacketType(binaryString, index)
    if type == 4:
        literalValue, index = findLiteralValue(binaryString, index)
    else:
        lengthTypeId, index = findPacketLengthTypeId(binaryString, index)
        if lengthTypeId == "0":
            bitCount, index = findSubPacketLength(binaryString, index)
            versionSum += addVersions(binaryString, versionSum, index, packetCount, bitCount)
            bitCount = 0
        else:
            packetCount, index = findPacketCount(binaryString, index)
            versionSum += addVersions(binaryString, versionSum, index, packetCount, bitCount)
            packetCount = 0

    if bitCount != 0:
        print(bitCount)
        bitCount -= (index - originalIndex)
        return addVersions(binaryString, versionSum, index, packetCount, bitCount)
    elif packetCount != 0:
        return addVersions(binaryString, versionSum, index, packetCount - 1, bitCount)
    else:
        breakpoint()
        return versionSum

print(addVersions(binaryString, 0, 0, 0, 0))
