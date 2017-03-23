

A*(start, goal)

closedSet := {}

openSet := {}

cameFrom := the empty map

gScore := map with default value of Infinity

gScore[Start]:= 0

fScore := map with default value of Infinity

fScore[start] := heuristic_cost_estimate(start, goal)

while openSet is not empty:
    current := 