# Solution for https://adventofcode.com/2025/day/9/input
# Part 1 only

tiles = []

with open('aoc2025\\day9.txt') as f:
    for line in f:
        tiles.append([int(x) for x in line.strip().split(',')])

part1 = 0

for i in range(len(tiles)):
    for j in range(i+1,len(tiles)):
        area = (abs(tiles[i][0] - tiles[j][0]) + 1) * (abs(tiles[i][1] - tiles[j][1]) + 1)
        part1 = max(part1,area)

print("Solution to part 1: " + str(part1))