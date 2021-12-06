# Population growth of lanternfish
fp = open("input")
line = fp.readline()
line = line.replace('\n', '').split(",")
line = list(map(int, line))
buckets = []

# Initialize buckets
for index in range(9):
    buckets.append(0)

# Put the fish in buckets basedo on their internal timer
def bucketize(fish, buckets):
    for f in fish:
        buckets[f] += 1
    return buckets

# Decrement fish timers
# Spawn new fish if timer is 0. New fish timer is 8. Reset old fish timer to 6.
def growPopulation(buckets):
    breedingFish = buckets[0]
    for i in range(1, 9):
        buckets[i-1] = buckets[i]
    buckets[8] = breedingFish
    buckets[6] += breedingFish

    return buckets

# Simulate how the population grows in given number of days
def simulateDays(fish, days):
    for day in range(days):
        fish = growPopulation(fish)
        print("Simulating day ", str(day + 1))

# Sum the quantity of fish in each bucket
def populationCount(fish):
    return sum(fish)

print("Initial state: ", line)
buckets = bucketize(line, buckets)
simulateDays(buckets, 256)
print(buckets)
print(populationCount(buckets))
