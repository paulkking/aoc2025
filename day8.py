# 2025 Advent of Code Day 8 https://adventofcode.com/2025/day/8

import networkx as nx
import math

# part 1
junc = []

with open("aoc2025\\day8.txt") as f:
    for line in f:        
        junc.append([int(x) for x in line.strip().split(',')])

pairs = [] # Find all pairs
for i in range(len(junc)):
    for j in range(i+1,len(junc)):
        pairs.append((i,j))

def dist(box1,box2): # Euclidean distance
    return math.sqrt((box1[0] - box2[0]) ** 2 + (box1[1] - box2[1]) ** 2 + (box1[2] - box2[2]) ** 2)

pairs.sort(key=lambda pair:dist(junc[pair[0]],junc[pair[1]])) # Sort to find shortest distances between pairs

G = nx.Graph()

for pair in pairs[:1000]: # Add 1st 1000 pairs
    G.add_edge(pair[0],pair[1])
circuits=list(nx.connected_components(G))
circuits.sort(key=lambda x:len(x),reverse=True)
c_len = [len(c) for c in circuits]
part1 = c_len[0] * c_len[1] * c_len[2]

# part 2

for pair in pairs[1000:]: # Add pairs until circuit is same length as all junctions
    memory = (pair[0],pair[1])
    G.add_edge(pair[0],pair[1])
    circuits=list(nx.connected_components(G))
    if len(circuits[0]) == len(junc):
        break

part2 = junc[memory[0]][0] * junc[memory[1]][0] # Multiply x coordinates

print("Part 1 solution: " + str(part1))
print("Part 2 solution: " + str(part2))