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

binaryString = hexStringToBinary("EE00D40C823060")

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

# Find the length of the packet 
def findSubPacketLength(binaryString):
    return binaryToDecimal(binaryString[8:8+14])

def addVersions(binaryString, versionSum, index):
    version, index = findPacketVersion(binaryString, index)
    versionSum += version
    type, index = findPacketType(binaryString, index)
    if type == 4:
        literalValue, index = findLiteralValue(binaryString, index)
        print(literalValue)
        print(index)
    else:
        lengthTypeId, index = findPacketLengthTypeId(binaryString, index)
        if lengthTypeId == "0":
            length = findSubPacketLength(binaryString)
            index += length


addVersions(binaryString, 0, 0)
