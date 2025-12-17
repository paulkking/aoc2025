# AOC Day 4 Solution https://adventofcode.com/2025/day/4

grid = []
with open("aoc2025\\day4.txt") as f:
    for line in f:
        row = []
        for char in line:
            if char == "@":
                row.append(1)
            elif char == ".":
                row.append(0)
        row.append(0)
        grid.append(row)

m = len(grid[0])
n = len(grid)

grid.append([0] * m)

part1 = 0
part2 = 0
diff = True

for i in range(m): # Part 1
        for j in range(n):
            if grid[i][j] == 1:
                neighbours = grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] + grid[i][j-1] + grid[i][j+1] + grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
                if neighbours < 4:                    
                    part1 += 1


while diff == True: # Part 2
    diff = False
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                neighbours = grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] + grid[i][j-1] + grid[i][j+1] + grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
                if neighbours < 4:
                    grid[i][j] = 0
                    part2 += 1
                    diff = True

print("Part 1 solution: " + str(part1))
print("Part 2 solution: " + str(part2))