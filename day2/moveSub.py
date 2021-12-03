# Move the sub basedon the input
fp = open("input")
lines = fp.readlines()
depth = 0
horizontalPosition = 0
aim = 0
for line in lines:
    command = line.strip().split(" ")
    direction = command[0]
    distance = int(command[1])
    if direction == "forward":
        horizontalPosition += distance
        depth += aim * distance
    elif direction == "up":
        aim -= distance
    elif direction == "down":
        aim += distance

print(depth)
print(horizontalPosition)
print(depth * horizontalPosition)