# Find the lowpoints of heightmap
fp = open("input")
lines = fp.readlines()
heightmap = []

# Represents a point with an x and y coordinate.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printMe(self):
        return (str(self.x) + "," + str(self.y))

# Remove newline character from a string
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
                        lowpoints.append(Point(j,i))
                elif j == len(heightmap[i])-1: # top right
                    if heightmap[i][j-1] > currentPoint and heightmap[i+1][j] > currentPoint:
                        lowpoints.append(Point(j,i))
                else:
                    if heightmap[i][j-1] > currentPoint and heightmap[i][j+1] > currentPoint and heightmap[i+1][j] > currentPoint:
                        lowpoints.append(Point(j,i))
            elif i == len(heightmap)-1: # bottom row
                if j == 0: # bottom left
                    if heightmap[i][j+1] > currentPoint and heightmap[i-1][j] > currentPoint:
                        lowpoints.append(Point(j,i))
                elif j == len(heightmap[i])-1: # bottom right
                    if heightmap[i][j-1] > currentPoint and heightmap[i-1][j] > currentPoint:
                        lowpoints.append(Point(j,i))
                else:
                    if heightmap[i][j-1] > currentPoint and heightmap[i][j+1] > currentPoint and heightmap[i-1][j] > currentPoint:
                        lowpoints.append(Point(j,i))
            elif j == 0: # left column
                if heightmap[i-1][j] > currentPoint and heightmap[i+1][j] > currentPoint and heightmap[i][j+1] > currentPoint:
                    lowpoints.append(Point(j,i))
            elif j == len(heightmap[i])-1: # right column
                if heightmap[i-1][j] > currentPoint and heightmap[i+1][j] > currentPoint and heightmap[i][j-1] > currentPoint:
                    lowpoints.append(Point(j,i))
            else:
                if heightmap[i-1][j] > currentPoint and heightmap[i+1][j] > currentPoint and heightmap[i][j-1] > currentPoint and heightmap[i][j+1] > currentPoint:
                    lowpoints.append(Point(j,i))

    return lowpoints

# Return true if the point is not in the list
def notInList(point, points):
    for p in points:
        if p.x == point.x and p.y == point.y:
            return False
    return True

# Recursively find the basins
# First, find the adjacents of the current point.
# Then filter out the visited points
def findBasin(heightmap, point, visited):
    x = point.x
    y = point.y

    if heightmap[y][x] != 9 and notInList(point, visited):
        visited.append(point)

    adjacents = findAdjacent(heightmap, point)
    adjacents = list(filter((lambda p: notInList(p, visited)), adjacents))
    for adjacent in adjacents:
        newVisited = findBasin(heightmap, adjacent, visited)
        newVisited = list(filter((lambda p: notInList(p, visited)), newVisited))
        visited = visited + newVisited

    return visited

# Find the points adjacent to the given point
# Don't add 9's to adjacents
def findAdjacent(heightmap, point):
    adjacents = []
    x = point.x
    y = point.y
    if y == 0: # top row
        if x == 0: # top left
            temp = [Point(x,y+1), Point(x+1,y)]
            temp = list(filter((lambda p: heightmap[p.y][p.x] != 9), temp))
            adjacents = adjacents + temp
        elif x == len(heightmap[y])-1: # top right
            temp = [Point(x-1,y), Point(x,y+1)]
            temp = list(filter((lambda p: heightmap[p.y][p.x] != 9), temp))
            adjacents = adjacents + temp
        else:
            temp = [Point(x-1,y), Point(x,y+1), Point(x+1,y)]
            temp = list(filter((lambda p: heightmap[p.y][p.x] != 9), temp))
            adjacents = adjacents + temp
    elif y == len(heightmap)-1: # bottom row
        if x == 0: # bottom left
            temp = [Point(x,y-1), Point(x+1,y)]
            temp = list(filter((lambda p: heightmap[p.y][p.x] != 9), temp))
            adjacents = adjacents + temp
        elif x == len(heightmap[y])-1: # bottom right
            temp = [Point(x-1,y), Point(x,y-1)]
            temp = list(filter((lambda p: heightmap[p.y][p.x] != 9), temp))
            adjacents = adjacents + temp
        else:
            temp = [Point(x-1,y), Point(x,y-1), Point(x+1,y)]
            temp = list(filter((lambda p: heightmap[p.y][p.x] != 9), temp))
            adjacents = adjacents + temp
    elif x == 0: # left column
        temp = [Point(x,y-1), Point(x+1,y), Point(x,y+1)]
        temp = list(filter((lambda p: heightmap[p.y][p.x] != 9), temp))
        adjacents = adjacents + temp
    elif x == len(heightmap[y])-1: # right column
        temp = [Point(x,y-1), Point(x-1,y), Point(x,y+1)]
        temp = list(filter((lambda p: heightmap[p.y][p.x] != 9), temp))
        adjacents = adjacents + temp
    else:
        temp = [Point(x,y-1), Point(x-1,y), Point(x,y+1), Point(x+1,y)]
        temp = list(filter((lambda p: heightmap[p.y][p.x] != 9), temp))
        adjacents = adjacents + temp

    return adjacents

# Add one to each lowpoint and return the sum
def calculateRiskLevel(lowpoints):
    lowpoints = list(map((lambda x: x+1), lowpoints))
    return sum(lowpoints)

# Find the product of a list of numbers
def product(list):
    product = 1
    for i in list:
        product *= i
    return product

# Find and return the product of the 3 largest basins in a heatmap
def calculate3LargestBasins(heightmap):
    lowpoints = findLowPoints(heightmap)
    basins = list(map((lambda p: len(findBasin(heightmap, p, []))), lowpoints))
    basins.sort()
    return product(basins[-3:])

createHeightmap(heightmap, lines)
print(calculate3LargestBasins(heightmap))
