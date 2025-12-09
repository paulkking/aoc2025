# Solution for https://adventofcode.com/2025/day/2

invalid1 = set()
invalid2 = set()

f = open("aoc2025\\day2.txt")

ranges = f.read().split(",")

for rang in ranges:
    start,end = rang.split("-")
    for i in range(int(start),int(end)+1):
        s = str(i)
        n = len(s)
        for j in range(1,n): 
            if n % j == 0: # Look at all factors of n
                if s == s[0:j] * (n // j): # Check if string matches pattern
                    invalid2.add(i)
                    if j == n // 2: # "Special" case for part 1 where length of repeating segment is 1/2 of total length
                        invalid1.add(i)

print("Part 1 solution: " + str(sum(invalid1)))
print("Part 2 solution: " + str(sum(invalid2)))