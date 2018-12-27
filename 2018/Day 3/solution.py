fabric = [[0] * 1000 for _ in range(1000)]
overlap = 0
ids = set()
overlapping = set()

for line in open('input.txt'):
    splt = line.split(" ")
    num = int((splt[0])[1:])
    offset_x = int(str(splt[2]).split(",")[0])
    offset_y = int(str(str(splt[2]).split(",")[1])[:-1])
    width = int(str(splt[3]).split("x")[0])
    height = int(str(splt[3]).split("x")[1])
    ids.add(num)
    for x in range(0, width):
        for y in range(0, height):
            if fabric[x + offset_x][y + offset_y] == 0:
                fabric[x + offset_x][y + offset_y] = num
            elif fabric[x + offset_x][y + offset_y] > 0:
                overlapping.add(fabric[x + offset_x][y + offset_y])
                overlapping.add(num)
                overlap += 1
                fabric[x + offset_x][y + offset_y] = -1
            elif fabric[x + offset_x][y + offset_y] == -1:
                overlapping.add(num)

print(overlap)
print(list(ids - overlapping)[0])
