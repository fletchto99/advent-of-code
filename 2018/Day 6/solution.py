dist = 10000
points = []

for line in open('input.txt'):
    x, y = [int(i) for i in line.split(", ")]
    points.append((x, y))

min_x = min([z for z, _ in points])
min_y = min([z for _, z in points])
max_x = max([z for z, _ in points])
max_y = max([z for _, z in points])
grid = [[-1] * (max_y + 1) for _ in range(max_x + 1)]

# Part 1
for x in range(0, max_x + 1):
    for y in range(0, max_y + 1):
        best = -1
        distance = max_x * max_y
        tie = False

        for idx, point in enumerate(points):
            dst = abs(point[0] - x) + abs(point[1] - y)
            if dst < distance:
                best = idx
                tie = False
                distance = dst
            elif distance == dst:
                best = -1

        grid[x][y] = best

results = {}
infinites = {-1: True}
reigon = 0
for x in range(0, max_x + 1):
    for y in range(0, max_y + 1):
        tile = grid[x][y]
        if x <= min_x or y <= min_y or x >= max_x or y >= max_y:
            if tile in results:
                results[tile] = 0
            infinites[tile] = True

        if tile not in infinites:
            if tile in results:
                results[tile] += 1
            else:
                results[tile] = 1

        # Part 2.... literally just this <.<
        distance = 0
        for point in points:
            distance += abs(point[0] - x) + abs(point[1] - y)
        if distance < dist:
            reigon += 1

print(results[max(results, key=results.get)])
print(reigon)
