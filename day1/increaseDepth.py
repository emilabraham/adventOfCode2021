# Figure out how many inputs are larger than the previous input
fp = open("input")
lines = fp.readlines()
previousDepth = 0
increasingCount = 0
maxWindow = len(lines) - 3
for index, line in enumerate(lines):
    if (index <= maxWindow):
        line1 = lines[index]
        line2 = lines[index + 1]
        line3 = lines[index + 2]
        sum = int(line1.strip()) + int(line2.strip()) + int(line3.strip())
        if (sum > previousDepth):
            increasingCount += 1
        previousDepth = sum
    

# Exclude the first depth
increasingCount -= 1
print(increasingCount)