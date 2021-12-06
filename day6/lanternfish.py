# Population grown of lanternfish
fp = open("input")
line = fp.readline()
line = line.replace('\n', '').split(",")
line = list(map(int, line))

# Decrement fish timers
# Spawn new fish if timer is 0. New fish timer is 8. Reset old fish timer to 6.
def growPopulation(fish):
    newFishCount = 0
    for i in range(len(fish)):
        currentFish = fish[i]
        if currentFish == 0:
            newFishCount += 1
            currentFish = 6
        else:
            currentFish -= 1
        fish[i] = currentFish

    for j in range(newFishCount):
        fish.append(8)

    return fish

# Simulate how the population grows in given number of days
def simulateDays(fish, days):
    for day in range(days):
        fish = growPopulation(fish)
        # print("Simulating day ", str(day + 1))
        print("After " + str(day + 1) + " days: ", fish)

print("Initial state: ", line)
simulateDays(line, 80)
print(len(line))