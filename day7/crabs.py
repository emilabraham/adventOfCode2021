# Get the crabs to match on the horizontal position by using the least amount of fuel
fp = open("input")
crabs = fp.readline()
crabs = crabs.split(",")
crabs = list(map(int, crabs))
maxPosition = max(crabs)

# Calculate the fuel consumed for a given distance
def fuelConsumedEquation(distance):
    return int((distance * (distance - 1)) / 2)

# Shift the crabs to the position and return the fuel consumed
def shiftToPosition(crabs, position):
    fuelConsumed = 0

    for i in range(len(crabs)):
        distance = abs(crabs[i] - position)
        fuelConsumed += fuelConsumedEquation(distance + 1)
        crabs[i] = position
    
    return fuelConsumed

# Try all positions and return the lowest fuel consumed
def findLeastFuelConsumed(crabs):
    tempCrabs = crabs.copy()
    minFuel = shiftToPosition(tempCrabs, 0)
    for i in range(1, maxPosition):
        tempCrabs = crabs.copy()
        position = i
        fuelConsumed = shiftToPosition(tempCrabs, position)
        if fuelConsumed < minFuel:
            minFuel = fuelConsumed
    return minFuel

print(findLeastFuelConsumed(crabs))