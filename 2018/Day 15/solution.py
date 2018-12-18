map = []
elves = []
goblins = []

for y, line in enumerate(open("input.txt")):
  row = list(line.rstrip())
  for x in len(row):
    if row[i] == "G":
      row[i] = "."
      goblins.append({
        'alive': True,
        'x': x,
        'y': y
      })
    elif row[i] == "E":
      row[i] = "."
      elves.append({
        'alive': True,
        'x': x,
        'y': y
      })
  map.append(row)
