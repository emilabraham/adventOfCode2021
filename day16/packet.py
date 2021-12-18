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
def findPacketVersion(binaryString):
    return binaryToDecimal(binaryString[:3])
    
# find the packet type
def findPacketType(binaryString):
    return binaryToDecimal(binaryString[3:6])

# Keep reading bits of 5 as long as the first bit is 1
def findLiteralValue(binaryString):
    literalValue = ""
    index = 6
    keepReading = True
    while keepReading:
        chunk = binaryString[index:index+5]
        if chunk[0] == "0":
            keepReading = False
        index += 5
        literalValue += chunk[1:5]
    return binaryToDecimal(literalValue)

print(findLiteralValue(binaryString))
