# Find the lowpoints of heightmap
fp = open("input")
lines = fp.readlines()
heightmap = []

# Remove newline character from a string and convert to an integer
def removeNewLine(s):
    return s.replace('\n', '')

# Create the heightmap from the input
def createHeightmap(heightmap, lines):
    for line in lines:
        line = removeNewLine(line)
        line = [x for x in line]
        heightmap.append(list(map(int, line)))

# Find the lowpoints of the heightmap.
# Need special handling for the edges of the map.
# It looks messy, but idk if there's a great way to clean it up.
def findLowPoints(heightmap):
    lowpoints = []
    for i in range(len(heightmap)):
        for j in range(len(heightmap[i])):
            currentPoint = heightmap[i][j]
            if i == 0: # top row
                if j == 0: # top left
                    if heightmap[i][j+1] > currentPoint and heightmap[i+1][j] > currentPoint:
                        lowpoints.append(currentPoint)
                elif j == len(heightmap[i])-1: # top right
                    if heightmap[i][j-1] > currentPoint and heightmap[i+1][j] > currentPoint:
                        lowpoints.append(currentPoint)
                else:
                    if heightmap[i][j-1] > currentPoint and heightmap[i][j+1] > currentPoint and heightmap[i+1][j] > currentPoint:
                        lowpoints.append(currentPoint)
            elif i == len(heightmap)-1: # bottom row
                if j == 0: # bottom left
                    if heightmap[i][j+1] > currentPoint and heightmap[i-1][j] > currentPoint:
                        lowpoints.append(currentPoint)
                elif j == len(heightmap[i])-1: # bottom right
                    if heightmap[i][j-1] > currentPoint and heightmap[i-1][j] > currentPoint:
                        lowpoints.append(currentPoint)
                else:
                    if heightmap[i][j-1] > currentPoint and heightmap[i][j+1] > currentPoint and heightmap[i-1][j] > currentPoint:
                        lowpoints.append(currentPoint)
            elif j == 0: # left column
                if heightmap[i-1][j] > currentPoint and heightmap[i+1][j] > currentPoint and heightmap[i][j+1] > currentPoint:
                    lowpoints.append(currentPoint)
            elif j == len(heightmap[i])-1: # right column
                if heightmap[i-1][j] > currentPoint and heightmap[i+1][j] > currentPoint and heightmap[i][j-1] > currentPoint:
                    lowpoints.append(currentPoint)
            else:
                if heightmap[i-1][j] > currentPoint and heightmap[i+1][j] > currentPoint and heightmap[i][j-1] > currentPoint and heightmap[i][j+1] > currentPoint:
                    lowpoints.append(currentPoint)

    return lowpoints

# Add one to each lowpoint and return the sum
def calculateRiskLevel(lowpoints):
    lowpoints = list(map((lambda x: x+1), lowpoints))
    return sum(lowpoints)

createHeightmap(heightmap, lines)
lowpoints = findLowPoints(heightmap)
print(calculateRiskLevel(lowpoints))