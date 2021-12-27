# Doing some hexadecimal packet manipulation
import numpy as np
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

binaryString = hexStringToBinary("9C0141080250320F1802104A08")
print(binaryString)

# Convert a binary number to decimal
def binaryToDecimal(binary):
    return int(binary, 2)

def breakOutEarly(binaryString, index, increment, accumulator):
    if index + increment > len(binaryString):
        breakpoint()
        return True
    return False

# find the packet version
def findPacketVersion(binaryString, index, accumulator):
    if breakOutEarly(binaryString, index, 3, accumulator):
        return 0, -1
    version = binaryToDecimal(binaryString[index:index+3])
    index += 3
    return version, index
    
# find the packet type
def findPacketType(binaryString, index, accumulator):
    if breakOutEarly(binaryString, index, 3, accumulator):
        return 0, -1
    type =  binaryToDecimal(binaryString[index:index+3])
    index += 3
    return type, index

# Keep reading bits of 5 as long as the first bit is 1
def findLiteralValue(binaryString, index, accumulator):
    if breakOutEarly(binaryString, index, 5, accumulator):
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
def findPacketLengthTypeId(binaryString, index, accumulator):
    if breakOutEarly(binaryString, index, 1, accumulator):
        return 0, -1
    lengthType =  binaryString[index:index+1]
    index += 1
    return lengthType, index

def findPacketCount(binaryString, index, accumulator):
    if breakOutEarly(binaryString, index, 11, accumulator):
        return 0, -1
    packetCount = binaryToDecimal(binaryString[index:index+11])
    index += 11
    return packetCount, index

# Find the length of the packet 
def findSubPacketLength(binaryString, index, accumulator):
    if breakOutEarly(binaryString, index, 15, accumulator):
        return None, -1
    length = binaryToDecimal(binaryString[index:index+15])
    index += 15
    return length, index



# Recursively add version of each packet
# I think I'm having trouble properly breaking out of this.
# If I  put a breakpoint inside the breakOutEarly function, it ends up correct without looping.
def addVersions(binaryString, accumulator, index, packetCount, bitCount, currentType, isSecond):
    breakpoint()
    originalIndex = index
    version, index = findPacketVersion(binaryString, index, accumulator)
    type, index = findPacketType(binaryString, index, accumulator)
    latestType = -1
    if type == 4:
        latestType = -1 if len(currentType) == 0 else currentType.pop()
        literalValue, index = findLiteralValue(binaryString, index, accumulator)
        if latestType == -1 or latestType == 4:
            accumulator = literalValue
        elif latestType == 0:
            accumulator += literalValue
        elif latestType == 1:
            if accumulator == 0:
                accumulator = 1
            accumulator *= literalValue
        elif latestType == 2:
            if accumulator == 0 or literalValue <= accumulator:
                accumulator = literalValue
        elif latestType == 3:
            if accumulator == 0 or literalValue >= accumulator:
                accumulator = literalValue
        elif latestType == 5:
            if isSecond:
                accumulator = (1 if accumulator > literalValue else 0)
                isSecond = False
            else:
                accumulator = literalValue
                isSecond = True
        elif latestType == 6:
            if isSecond:
                accumulator = (1 if accumulator < literalValue else 0)
                isSecond = False
            else:
                accumulator = literalValue
                isSecond = True
        elif latestType == 7:
            if isSecond:
                accumulator = (1 if accumulator == literalValue else 0)
                isSecond = False
            else:
                accumulator = literalValue
                isSecond = True
    else:
        currentType.append(type)
        lengthTypeId, index = findPacketLengthTypeId(binaryString, index, accumulator)
        if lengthTypeId == "0":
            newBitCount, index = findSubPacketLength(binaryString, index, accumulator)
            bitCount += newBitCount
            packetCount -= 0 if packetCount == 0 else 1
            return addVersions(binaryString, accumulator, index, packetCount, bitCount, currentType, isSecond)
        else:
            newPacketCount, index = findPacketCount(binaryString, index, accumulator)
            packetCount += newPacketCount
            bitCount -= 0 if bitCount == 0 else (index - originalIndex)
            return addVersions(binaryString, accumulator, index, packetCount, bitCount, currentType, isSecond)

    if packetCount > 0:
        packetCount -= 1
        bitCount -= 0 if bitCount == 0 else (index - originalIndex)
        if (packetCount != 0 and latestType != -1):
            currentType.append(latestType)
        return addVersions(binaryString, accumulator, index, packetCount, bitCount, currentType, isSecond)
    if bitCount > 0:
        bitCount -= (index - originalIndex)
        packetCount -= 0 if packetCount == 0 else 1
        if (bitCount != 0 and latestType != -1):
            currentType.append(latestType)
        return addVersions(binaryString, accumulator, index, packetCount, bitCount, currentType, isSecond)

    return accumulator

def incrementPacketAndBitCount(packetCount, bitCount, index, originalIndex):
    bitCount -= 0 if bitCount == 0 else (index - originalIndex)
    packetCount -= 0 if packetCount == 0 else 1
    return packetCount, bitCount

def reduceAccumulator(accumulator, type):
    if type == 0:
        return sum(accumulator)
    elif type == 1:
        return np.product(accumulator)
    elif type == 2:
        return min(accumulator)
    elif type == 3:
        return max(accumulator)
    elif type == 4:
        return accumulator
    elif type == 5:
        return 1 if accumulator[0] > accumulator[1] else 0
    elif type == 6:
        return 1 if accumulator[0] < accumulator[1] else 0
    elif type == 7:
        return 1 if accumulator[0] == accumulator[1] else 0

def calculatePacket(binaryString, accumulator, index, packetCount, bitCount):
    breakpoint()
    originalIndex = index
    version, index = findPacketVersion(binaryString, index, accumulator)
    type, index = findPacketType(binaryString, index, accumulator)
    if type == 4:
        literalValue, index = findLiteralValue(binaryString, index, accumulator)
        packetCount, bitCount = incrementPacketAndBitCount(packetCount, bitCount, index, originalIndex)
        accumulator.append(literalValue)
        return accumulator
    else:
        lengthTypeId, index = findPacketLengthTypeId(binaryString, index, accumulator)
        if lengthTypeId == "0":
            newBitCount, index = findSubPacketLength(binaryString, index, accumulator)
            bitCount += newBitCount
            packetCount -= 0 if packetCount == 0 else 1
            newAccumulator = calculatePacket(binaryString, [], index, packetCount, bitCount)
            reduced = reduceAccumulator(newAccumulator, type)
            accumulator.append(reduced)
            return accumulator
        else:
            newPacketCount, index = findPacketCount(binaryString, index, accumulator)
            packetCount += newPacketCount
            bitCount -= 0 if bitCount == 0 else (index - originalIndex)
            newAccumulator = calculatePacket(binaryString, [], index, packetCount, bitCount)
            reduced = reduceAccumulator(newAccumulator, type)
            accumulator.append(reduced)
            return accumulator

# print(addVersions(binaryString, 0, 0, 0, 0, [], False))
print(calculatePacket(binaryString, [], 0, 0, 0))